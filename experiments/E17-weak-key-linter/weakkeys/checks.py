# SPDX-License-Identifier: Apache-2.0
"""Weak-key checks on PUBLIC keys. Research prototype (experiment E17).

What these checks can and cannot do
-----------------------------------
They detect KNOWN BAD PATTERNS: tiny private scalars (the kind reported in the
October 2026 intermediate-CA incident), structured scalars, invalid or
small-order points, duplicates, and keys on a blocklist.

They CANNOT prove that a key is random or good. A key that passes is merely
"not obviously bad". See whitepaper section 23.10.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Iterable, Optional

from .curves import ED25519, Ed25519Curve, KeyFormatError, WeierstrassCurve

FAIL, WARN, INFO = "FAIL", "WARN", "INFO"

DEFAULT_MAX_SCALAR = 1 << 16


@dataclass
class Finding:
    severity: str
    code: str
    message: str
    scalar: Optional[int] = None

    def as_dict(self):
        d = {"severity": self.severity, "code": self.code, "message": self.message}
        if self.scalar is not None:
            d["scalar"] = self.scalar
        return d


@dataclass
class KeyReport:
    label: str
    curve: str
    fingerprint: Optional[str]
    findings: list = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return any(f.severity == FAIL for f in self.findings)

    def as_dict(self):
        return {
            "label": self.label,
            "curve": self.curve,
            "fingerprint": self.fingerprint,
            "verdict": "FAIL" if self.failed else ("WARN" if any(f.severity == WARN for f in self.findings) else "PASS"),
            "findings": [f.as_dict() for f in self.findings],
        }


def fingerprint(curve, point) -> str:
    """SHA-256 of the canonical encoding (uncompressed SEC1, or the 32-byte Ed25519 encoding)."""
    return hashlib.sha256(curve.encode_point(point)).hexdigest()


def _table_key(curve, point) -> int:
    # Weierstrass: +/-P share x. Edwards: +/-P share y.
    return point[1] if isinstance(curve, Ed25519Curve) else point[0]


_CACHE: dict = {}


def small_scalar_table(curve, limit: int = DEFAULT_MAX_SCALAR) -> dict:
    """Map table_key -> d for d*G, d = 1..limit (the +/- pair shares a key)."""
    ck = ("small", curve.name, limit)
    if ck in _CACHE:
        return _CACHE[ck]
    table = {}
    point = curve.generator
    for d in range(1, limit + 1):
        table.setdefault(_table_key(curve, point), d)
        point = curve.add(point, curve.generator)
    _CACHE[ck] = table
    return table


def structured_scalar_table(curve) -> dict:
    """Map table_key -> (description, scalar) for structured scalars (deep mode).

    Covers 2^k, 2^k-1, 2^k+1 and a full-length repeated byte (0x0101..01, ..., 0xFFFF..FF).
    """
    ck = ("structured", curve.name)
    if ck in _CACHE:
        return _CACHE[ck]
    n = curve.n
    table = {}

    def add(desc, scalar, point):
        if point is not None:
            table.setdefault(_table_key(curve, point), (desc, scalar))

    G = curve.generator
    power = G  # 2^0 * G
    for k in range(0, n.bit_length()):
        add(f"2^{k}", 1 << k, power)
        add(f"2^{k}+1", (1 << k) + 1, curve.add(power, G))
        add(f"2^{k}-1", (1 << k) - 1, curve.add(power, curve.neg(G)) if k > 0 else None)
        power = curve.add(power, power)
    length = (n.bit_length() + 7) // 8
    for b in range(1, 256):
        scalar = int.from_bytes(bytes([b]) * length, "big")
        if scalar < n:
            add(f"repeated byte 0x{b:02x} x {length}", scalar, curve.mul(scalar, G))
    _CACHE[ck] = table
    return table


def ed25519_public_from_seed(seed: bytes):
    """RFC 8032 key derivation, for PUBLIC analysis of trivial seeds only."""
    c = ED25519
    h = bytearray(hashlib.sha512(seed).digest()[:32])
    h[0] &= 248
    h[31] &= 127
    h[31] |= 64
    return c.mul(int.from_bytes(h, "little"), c.generator)


def trivial_ed25519_seed_table() -> dict:
    """Map y -> description for public keys derived from trivial 32-byte seeds (deep mode)."""
    ck = ("ed-seeds",)
    if ck in _CACHE:
        return _CACHE[ck]
    c = ED25519
    seeds = {}
    for b in range(256):
        seeds[f"seed = byte 0x{b:02x} repeated 32 times"] = bytes([b]) * 32
    for i in range(64):
        seeds[f"seed = integer {i} (big-endian, 32 bytes)"] = i.to_bytes(32, "big")
        seeds[f"seed = integer {i} (little-endian, 32 bytes)"] = i.to_bytes(32, "little")
    table = {}
    for desc, seed in seeds.items():
        table.setdefault(ed25519_public_from_seed(seed)[1], desc)
    _CACHE[ck] = table
    return table


def load_blocklist(path) -> set:
    """One lowercase hex SHA-256 fingerprint per line; '#' starts a comment."""
    out = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip().lower()
            if line:
                out.add(line)
    return out


def check_key(
    curve,
    encoded: bytes,
    label: str = "key",
    *,
    max_scalar: int = DEFAULT_MAX_SCALAR,
    deep: bool = False,
    blocklist: Optional[set] = None,
) -> KeyReport:
    """Run every check on one encoded public key."""
    try:
        point = curve.decode_point(encoded)
    except KeyFormatError as exc:
        return KeyReport(label, curve.name, None, [Finding(FAIL, exc.code, exc.message)])

    report = KeyReport(label, curve.name, fingerprint(curve, point))
    add = report.findings.append

    if isinstance(curve, Ed25519Curve):
        if point == curve.identity:
            add(Finding(FAIL, "identity-point", "the key is the identity point"))
        elif curve.mul(curve.cofactor, point) == curve.identity:
            add(Finding(FAIL, "small-order", "the key is a small-order point (order divides 8)"))
        elif curve.mul(curve.n, point) != curve.identity:
            add(Finding(WARN, "mixed-order", "the key has a torsion component (not in the prime-order subgroup)"))

    if not any(f.severity == FAIL for f in report.findings):
        table = small_scalar_table(curve, max_scalar)
        d = table.get(_table_key(curve, point))
        if d is not None:
            actual = curve.mul(d, curve.generator)
            sign = "" if actual == point else "-"
            add(Finding(FAIL, "small-scalar", f"the private scalar is {sign}{d}, found among the first {max_scalar} multiples of the generator", d))
        if deep:
            hit = structured_scalar_table(curve).get(_table_key(curve, point))
            if hit:
                add(Finding(FAIL, "structured-scalar", f"the private scalar looks structured: {hit[0]}", hit[1]))
            if isinstance(curve, Ed25519Curve):
                desc = trivial_ed25519_seed_table().get(point[1])
                if desc:
                    add(Finding(FAIL, "trivial-seed", f"the public key matches a trivial Ed25519 {desc}"))

    if blocklist and report.fingerprint in blocklist:
        add(Finding(FAIL, "blocklisted", "the key fingerprint is on the supplied blocklist (known weak or compromised)"))

    if not report.findings:
        add(Finding(INFO, "no-known-weakness", "no known weakness found (this does NOT prove the key is good)"))
    return report


def check_batch(items: Iterable, **options) -> list:
    """items: iterable of (label, curve, encoded_bytes). Adds cross-key checks."""
    reports = []
    decoded = []
    for label, curve, encoded in items:
        report = check_key(curve, encoded, label, **options)
        reports.append(report)
        if report.fingerprint:
            try:
                decoded.append((report, curve, curve.decode_point(encoded)))
            except KeyFormatError:
                pass

    by_fp: dict = {}
    for report, _, _ in decoded:
        by_fp.setdefault((report.curve, report.fingerprint), []).append(report)
    for group in by_fp.values():
        if len(group) > 1:
            names = ", ".join(r.label for r in group)
            for r in group:
                r.findings.insert(0, Finding(FAIL, "duplicate", f"the same public key appears more than once: {names}"))

    by_coord: dict = {}
    for report, curve, point in decoded:
        by_coord.setdefault((report.curve, _table_key(curve, point)), []).append((report, point))
    for group in by_coord.values():
        points = {p for _, p in group}
        if len(points) > 1:
            names = ", ".join(r.label for r, _ in group)
            for r, _ in group:
                r.findings.insert(0, Finding(WARN, "related-keys", f"keys are negations of each other (private scalars d and -d): {names}"))

    for r in reports:
        if len(r.findings) > 1:
            r.findings = [f for f in r.findings if f.code != "no-known-weakness"]
    return reports


def format_text(reports: list) -> str:
    lines = []
    for r in reports:
        verdict = r.as_dict()["verdict"]
        fp = (r.fingerprint or "-")[:16]
        lines.append(f"[{verdict}] {r.label}  curve={r.curve}  fingerprint={fp}")
        for f in r.findings:
            lines.append(f"    {f.severity:4} {f.code}: {f.message}")
    failed = sum(1 for r in reports if r.failed)
    lines.append(f"{len(reports)} key(s) checked, {failed} rejected.")
    lines.append("Reminder: a key that passes is only 'not obviously bad'. Research prototype.")
    return "\n".join(lines)


def format_json(reports: list) -> str:
    return json.dumps(
        {"tool": "weakkeys", "research_prototype": True, "keys": [r.as_dict() for r in reports]},
        indent=2,
    )
