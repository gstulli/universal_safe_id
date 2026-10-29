# SPDX-License-Identifier: Apache-2.0
import hashlib
import unittest

from weakkeys.checks import ed25519_public_from_seed
from weakkeys.curves import ED25519, P256, P384, SECP256K1, KeyFormatError

try:  # optional cross-check against an independent implementation
    from cryptography.hazmat.primitives.asymmetric import ec, ed25519
    from cryptography.hazmat.primitives import serialization

    HAVE_CRYPTOGRAPHY = True
except Exception:  # pragma: no cover
    HAVE_CRYPTOGRAPHY = False


def pseudo_scalar(tag: bytes, n: int) -> int:
    return int.from_bytes(hashlib.sha512(tag).digest(), "big") % (n - 1) + 1


class CurveParameters(unittest.TestCase):
    def test_generator_on_curve_and_order(self):
        for c in (P256, P384, SECP256K1):
            with self.subTest(curve=c.name):
                self.assertTrue(c.is_on_curve(c.generator))
                self.assertIsNone(c.mul(c.n, c.generator))
        self.assertTrue(ED25519.is_on_curve(ED25519.generator))
        self.assertEqual(ED25519.mul(ED25519.n, ED25519.generator), ED25519.identity)

    def test_known_double_p256(self):
        x = 0x7CF27B188D034F7E8A52380304B51AC3C08969E277F21B35A60B48FC47669978
        y = 0x07775510DB8ED040293D9AC69F7430DBBA7DADE63CE982299E04B79D227873D1
        self.assertEqual(P256.mul(2, P256.generator), (x, y))

    def test_known_double_secp256k1(self):
        x = 0xC6047F9441ED7D6D3045406E95C07CD85C778E4B8CEF3CA7ABAC09B95C709EE5
        y = 0x1AE168FEA63DC339A3C58419466CEAEEF7F632653266D0E1236431A950CFE52A
        self.assertEqual(SECP256K1.mul(2, SECP256K1.generator), (x, y))

    def test_ed25519_rfc8032_vector_1(self):
        seed = bytes.fromhex("9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")
        expected = "d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a"
        self.assertEqual(ED25519.encode_point(ed25519_public_from_seed(seed)).hex(), expected)


class Encoding(unittest.TestCase):
    def test_roundtrip_and_compressed(self):
        for c in (P256, P384, SECP256K1):
            with self.subTest(curve=c.name):
                pt = c.mul(pseudo_scalar(b"rt" + c.name.encode(), c.n), c.generator)
                self.assertEqual(c.decode_point(c.encode_point(pt)), pt)
                tag = 2 + (pt[1] & 1)
                comp = bytes([tag]) + pt[0].to_bytes(c.size, "big")
                self.assertEqual(c.decode_point(comp), pt)

    def test_off_curve_rejected(self):
        gx, gy = P256.generator
        bad = b"\x04" + gx.to_bytes(32, "big") + (gy + 1).to_bytes(32, "big")
        with self.assertRaises(KeyFormatError) as cm:
            P256.decode_point(bad)
        self.assertEqual(cm.exception.code, "off-curve")

    def test_unreduced_coordinate_rejected(self):
        bad = b"\x04" + P256.p.to_bytes(32, "big") + (0).to_bytes(32, "big")
        with self.assertRaises(KeyFormatError) as cm:
            P256.decode_point(bad)
        self.assertEqual(cm.exception.code, "not-reduced")

    def test_bad_lengths_and_tags(self):
        for data in (b"", b"\x04" + b"\x00" * 10, b"\x05" + b"\x00" * 64, b"\x02" + b"\x00" * 5):
            with self.assertRaises(KeyFormatError):
                P256.decode_point(data)


@unittest.skipUnless(HAVE_CRYPTOGRAPHY, "optional cross-check needs the 'cryptography' package")
class CrossCheck(unittest.TestCase):
    CURVES = {"p256": ec.SECP256R1, "p384": ec.SECP384R1, "secp256k1": ec.SECP256K1} if HAVE_CRYPTOGRAPHY else {}

    def test_public_key_derivation_matches(self):
        for c in (P256, P384, SECP256K1):
            for i in range(5):
                with self.subTest(curve=c.name, i=i):
                    d = pseudo_scalar(b"x" + c.name.encode() + bytes([i]), c.n)
                    theirs = ec.derive_private_key(d, self.CURVES[c.name]()).public_key().public_bytes(
                        serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint
                    )
                    self.assertEqual(c.encode_point(c.mul(d, c.generator)), theirs)

    def test_ed25519_derivation_matches(self):
        for i in range(5):
            seed = hashlib.sha256(b"seed%d" % i).digest()
            theirs = ed25519.Ed25519PrivateKey.from_private_bytes(seed).public_key().public_bytes_raw()
            self.assertEqual(ED25519.encode_point(ed25519_public_from_seed(seed)), theirs)


if __name__ == "__main__":
    unittest.main()
