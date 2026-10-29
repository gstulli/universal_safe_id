# SPDX-License-Identifier: Apache-2.0
import unittest

from weakkeys.checks import (
    FAIL,
    INFO,
    WARN,
    check_batch,
    check_key,
    ed25519_public_from_seed,
    fingerprint,
)
from weakkeys.curves import ED25519, P256, P384, SECP256K1
from tests.test_curves import pseudo_scalar

SMALL = 1024


def key_for(curve, d):
    return curve.encode_point(curve.mul(d, curve.generator))


def codes(report):
    return {f.code for f in report.findings}


class SmallScalars(unittest.TestCase):
    def test_small_scalars_rejected_on_every_curve(self):
        for c in (P256, P384, SECP256K1, ED25519):
            for d in (1, 2, 3, 255, 1000):
                with self.subTest(curve=c.name, d=d):
                    r = check_key(c, key_for(c, d), max_scalar=SMALL)
                    self.assertTrue(r.failed)
                    self.assertIn("small-scalar", codes(r))
                    self.assertEqual(r.findings[0].scalar, d)

    def test_negative_small_scalar_rejected(self):
        for c in (P256, P384):
            with self.subTest(curve=c.name):
                r = check_key(c, key_for(c, c.n - 7), max_scalar=SMALL)
                self.assertIn("small-scalar", codes(r))
                self.assertIn("-7", r.findings[0].message)

    def test_boundary_of_search_limit(self):
        r_in = check_key(P256, key_for(P256, SMALL), max_scalar=SMALL)
        r_out = check_key(P256, key_for(P256, SMALL + 1), max_scalar=SMALL)
        self.assertIn("small-scalar", codes(r_in))
        self.assertNotIn("small-scalar", codes(r_out))

    def test_default_limit_is_65536(self):
        self.assertIn("small-scalar", codes(check_key(P256, key_for(P256, 65536))))
        self.assertNotIn("small-scalar", codes(check_key(P256, key_for(P256, 65537))))

    def test_ordinary_keys_pass(self):
        for c in (P256, P384, SECP256K1):
            with self.subTest(curve=c.name):
                r = check_key(c, key_for(c, pseudo_scalar(b"ok" + c.name.encode(), c.n)), max_scalar=SMALL)
                self.assertFalse(r.failed)
                self.assertEqual([f.severity for f in r.findings], [INFO])


class IncidentReproduction(unittest.TestCase):
    """Synthetic keys from the scalar values reported for the October 2026 incident."""

    REPORTED = (4, 56, 66, 115, 155, 156, 230, 237)

    def test_all_reported_scalars_detected_with_recovered_value(self):
        reports = check_batch([(f"d={d}", P384, key_for(P384, d)) for d in self.REPORTED], max_scalar=256)
        self.assertEqual(len(reports), 8)
        for d, r in zip(self.REPORTED, reports):
            with self.subTest(d=d):
                self.assertTrue(r.failed)
                self.assertEqual(r.findings[0].scalar, d)


class Structured(unittest.TestCase):
    def test_structured_scalars_need_deep_mode(self):
        pattern = int.from_bytes(bytes([0x42]) * 32, "big")
        cases = {"2^100": 1 << 100, "2^200-1": (1 << 200) - 1, "2^64+1": (1 << 64) + 1, "0x42 repeated": pattern}
        for name, d in cases.items():
            with self.subTest(case=name):
                key = key_for(P256, d)
                self.assertFalse(check_key(P256, key, max_scalar=SMALL).failed, "not caught without --deep")
                r = check_key(P256, key, max_scalar=SMALL, deep=True)
                self.assertIn("structured-scalar", codes(r))
                self.assertEqual(r.findings[0].scalar, d)

    def test_deep_mode_passes_ordinary_key(self):
        r = check_key(P256, key_for(P256, pseudo_scalar(b"deep-ok", P256.n)), max_scalar=SMALL, deep=True)
        self.assertFalse(r.failed)


class PointValidity(unittest.TestCase):
    def test_off_curve_is_a_failure(self):
        gx, gy = P384.generator
        bad = b"\x04" + gx.to_bytes(48, "big") + (gy ^ 1).to_bytes(48, "big")
        r = check_key(P384, bad)
        self.assertTrue(r.failed)
        self.assertEqual(r.findings[0].code, "off-curve")

    def test_ed25519_identity_small_order_and_noncanonical(self):
        p = ED25519.p
        identity = (1).to_bytes(32, "little")
        order2 = (p - 1).to_bytes(32, "little")
        noncanonical = (p + 1).to_bytes(32, "little")
        self.assertIn("identity-point", codes(check_key(ED25519, identity)))
        self.assertIn("small-order", codes(check_key(ED25519, order2)))
        self.assertIn("non-canonical", codes(check_key(ED25519, noncanonical)))

    def test_ed25519_mixed_order_warns(self):
        # Most points picked at random have a torsion component; find one and check the warning.
        found = None
        for y in range(2, 200):
            try:
                pt = ED25519.decode_point(y.to_bytes(32, "little"))
            except Exception:
                continue
            if ED25519.mul(ED25519.n, pt) != ED25519.identity and ED25519.mul(8, pt) != ED25519.identity:
                found = pt
                break
        self.assertIsNotNone(found)
        r = check_key(ED25519, ED25519.encode_point(found), max_scalar=SMALL)
        self.assertIn("mixed-order", codes(r))
        self.assertFalse(r.failed)

    def test_trivial_ed25519_seed_needs_deep_mode(self):
        key = ED25519.encode_point(ed25519_public_from_seed(bytes(32)))
        self.assertFalse(check_key(ED25519, key, max_scalar=SMALL).failed)
        self.assertIn("trivial-seed", codes(check_key(ED25519, key, max_scalar=SMALL, deep=True)))


class CrossKey(unittest.TestCase):
    def test_duplicates_and_related_keys(self):
        a = key_for(P256, pseudo_scalar(b"a", P256.n))
        b = key_for(P256, pseudo_scalar(b"b", P256.n))
        a_neg = P256.encode_point(P256.neg(P256.decode_point(a)))
        reports = check_batch([("a1", P256, a), ("b", P256, b), ("a2", P256, a), ("a-neg", P256, a_neg)], max_scalar=SMALL)
        by = {r.label: r for r in reports}
        self.assertIn("duplicate", codes(by["a1"]))
        self.assertIn("duplicate", codes(by["a2"]))
        self.assertNotIn("duplicate", codes(by["b"]))
        self.assertIn("related-keys", codes(by["a-neg"]))
        self.assertEqual([f.severity for f in by["b"].findings], [INFO])

    def test_blocklist(self):
        k = key_for(P256, pseudo_scalar(b"blk", P256.n))
        fp = fingerprint(P256, P256.decode_point(k))
        self.assertIn("blocklisted", codes(check_key(P256, k, max_scalar=SMALL, blocklist={fp})))
        self.assertNotIn("blocklisted", codes(check_key(P256, k, max_scalar=SMALL, blocklist={"00" * 32})))

    def test_severities_are_known(self):
        r = check_key(P256, key_for(P256, 5), max_scalar=SMALL)
        self.assertTrue(all(f.severity in (FAIL, WARN, INFO) for f in r.findings))


if __name__ == "__main__":
    unittest.main()
