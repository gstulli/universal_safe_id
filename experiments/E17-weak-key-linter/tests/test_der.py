# SPDX-License-Identifier: Apache-2.0
import base64
import datetime
import unittest

from weakkeys.checks import check_batch
from weakkeys.curves import CURVES, P256, P384, SECP256K1, ED25519, KeyFormatError
from weakkeys.der import keys_from_pem, parse_spki, spki_from_certificate, to_spki_der
from tests.test_curves import HAVE_CRYPTOGRAPHY, pseudo_scalar

if HAVE_CRYPTOGRAPHY:
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec, rsa
    from cryptography.x509.oid import NameOID


def pem(label, der):
    b64 = base64.b64encode(der).decode()
    lines = "\n".join(b64[i : i + 64] for i in range(0, len(b64), 64))
    return f"-----BEGIN {label}-----\n{lines}\n-----END {label}-----\n"


class Spki(unittest.TestCase):
    def test_roundtrip_all_curves(self):
        for c in (P256, P384, SECP256K1):
            with self.subTest(curve=c.name):
                pt = c.encode_point(c.mul(pseudo_scalar(b"d" + c.name.encode(), c.n), c.generator))
                self.assertEqual(parse_spki(to_spki_der(c.name, pt)), (c.name, pt))
        ed = ED25519.encode_point(ED25519.mul(12345678901234567890, ED25519.generator))
        self.assertEqual(parse_spki(to_spki_der("ed25519", ed)), ("ed25519", ed))

    def test_pem_extraction(self):
        pt = P256.encode_point(P256.mul(pseudo_scalar(b"p", P256.n), P256.generator))
        text = pem("PUBLIC KEY", to_spki_der("p256", pt)) + pem("PRIVATE KEY", b"ignored")
        self.assertEqual([(l, c, p) for l, c, p in keys_from_pem(text)], [("PUBLIC KEY", "p256", pt)])

    def test_garbage_is_rejected(self):
        for data in (b"", b"\x30", b"\x30\x03\x01\x02\x03", b"\x31\x00"):
            with self.assertRaises(KeyFormatError):
                parse_spki(data)
        with self.assertRaises(KeyFormatError):
            list(keys_from_pem("nothing here"))


@unittest.skipUnless(HAVE_CRYPTOGRAPHY, "optional cross-check needs the 'cryptography' package")
class WithCryptography(unittest.TestCase):
    def test_spki_matches_cryptography_encoding(self):
        key = ec.generate_private_key(ec.SECP384R1()).public_key()
        der = key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        curve, pt = parse_spki(der)
        self.assertEqual(curve, "p384")
        self.assertEqual(to_spki_der(curve, pt), der)

    def _certificate(self, private_key, name="test"):
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, name)])
        now = datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
        builder = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(subject)
            .public_key(private_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now)
            .not_valid_after(now + datetime.timedelta(days=30))
        )
        # Sign with an unrelated, ordinary key so that the subject key can be arbitrary.
        signer = ec.generate_private_key(ec.SECP256R1())
        return builder.sign(signer, hashes.SHA256())

    def test_certificate_with_tiny_private_key_is_rejected(self):
        # Test-only: a P-384 key with private scalar 4, like the pattern reported in the incident.
        weak = ec.derive_private_key(4, ec.SECP384R1())
        good = ec.generate_private_key(ec.SECP384R1())
        text = ""
        for k, n in ((weak, "weak"), (good, "good")):
            cert = self._certificate(k, n)
            text += cert.public_bytes(serialization.Encoding.PEM).decode()
        items = [(f"cert{i}", CURVES[c], p) for i, (_, c, p) in enumerate(keys_from_pem(text), 1)]
        reports = check_batch(items, max_scalar=256)
        self.assertTrue(reports[0].failed)
        self.assertEqual(reports[0].findings[0].scalar, 4)
        self.assertFalse(reports[1].failed)

    def test_certificate_spki_extraction_matches(self):
        key = ec.generate_private_key(ec.SECP256R1())
        cert = self._certificate(key)
        der = cert.public_bytes(serialization.Encoding.DER)
        expected = key.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        self.assertEqual(spki_from_certificate(der), expected)

    def test_rsa_is_reported_as_unsupported(self):
        rsa_pub = rsa.generate_private_key(65537, 2048).public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()
        with self.assertRaises(KeyFormatError) as cm:
            list(keys_from_pem(rsa_pub))
        self.assertEqual(cm.exception.code, "unsupported")


if __name__ == "__main__":
    unittest.main()
