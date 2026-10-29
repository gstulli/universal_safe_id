# SPDX-License-Identifier: Apache-2.0
"""Command line interface for weakkeys. Research prototype (experiment E17)."""

from __future__ import annotations

import argparse
import hashlib
import sys

from . import __version__
from .checks import (
    DEFAULT_MAX_SCALAR,
    check_batch,
    format_json,
    format_text,
    load_blocklist,
)
from .curves import CURVES, P384, KeyFormatError
from .der import curve_by_name, keys_from_pem, parse_spki, spki_from_certificate, to_spki_der

BANNER = (
    "weakkeys %s: RESEARCH PROTOTYPE. Inspects PUBLIC keys only. Never paste private keys.\n"
    "A key that passes is only 'not obviously bad'; it is NOT proof of quality." % __version__
)

# Private scalars reported for the eight intermediate-CA certificates in the
# October 2026 incident (see whitepaper section 23.1). The demo builds SYNTHETIC
# keys from these values; they are not the real certificate keys.
REPORTED_SCALARS = (4, 56, 66, 115, 155, 156, 230, 237)


def _collect(args):
    items = []
    for path in args.pem or []:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for i, (label, curve_name, pt) in enumerate(keys_from_pem(text), 1):
            items.append((f"{path}#{i} ({label.lower()})", curve_by_name(curve_name), pt))
    for path in args.der or []:
        with open(path, "rb") as fh:
            der = fh.read()
        try:
            curve_name, pt = parse_spki(der)
        except KeyFormatError:
            curve_name, pt = parse_spki(spki_from_certificate(der))
        items.append((path, curve_by_name(curve_name), pt))
    for i, spec in enumerate(args.point or [], 1):
        name, _, hexpt = spec.partition(":")
        if not hexpt:
            raise KeyFormatError("usage", f"--point expects CURVE:HEX, got '{spec}'")
        try:
            raw = bytes.fromhex(hexpt.strip())
        except ValueError as exc:
            raise KeyFormatError("usage", f"invalid hex in --point {i}: {exc}") from exc
        items.append((f"point[{i}]", curve_by_name(name), raw))
    if args.list:
        with open(args.list, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                name, _, hexpt = line.partition(":")
                try:
                    raw = bytes.fromhex(hexpt.strip())
                except ValueError as exc:
                    raise KeyFormatError("usage", f"{args.list}:{ln}: invalid hex: {exc}") from exc
                items.append((f"{args.list}:{ln}", curve_by_name(name), raw))
    if not items:
        raise KeyFormatError("usage", "no keys given: use --pem, --der, --point or --list")
    return items


def _cmd_check(args) -> int:
    items = _collect(args)
    blocklist = load_blocklist(args.blocklist) if args.blocklist else None
    reports = check_batch(items, max_scalar=args.max_scalar, deep=args.deep, blocklist=blocklist)
    print(format_json(reports) if args.json else format_text(reports))
    return 1 if any(r.failed for r in reports) else 0


def _cmd_fingerprint(args) -> int:
    from .checks import fingerprint

    for label, curve, raw in _collect(args):
        print(f"{fingerprint(curve, curve.decode_point(raw))}  {label}")
    return 0


def _cmd_demo(args) -> int:
    print(BANNER)
    print()
    print("Synthetic keys on NIST P-384 built from the private scalars reported for the")
    print("October 2026 incident, plus one control key. Table limited to 1024 multiples for speed.\n")
    items = []
    for d in REPORTED_SCALARS:
        items.append((f"synthetic d={d}", P384, P384.encode_point(P384.mul(d, P384.generator))))
    control = int.from_bytes(hashlib.sha256(b"usi-e17-demo-control-not-a-secret").digest(), "big") % P384.n
    items.append(("control (hash-derived toy scalar)", P384, P384.encode_point(P384.mul(control, P384.generator))))
    reports = check_batch(items, max_scalar=1024)
    print(format_text(reports))
    return 0 if any(r.failed for r in reports) else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="weakkeys", description=BANNER, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def inputs(sp):
        sp.add_argument("--pem", action="append", metavar="FILE", help="PEM file with PUBLIC KEY and/or CERTIFICATE blocks")
        sp.add_argument("--der", action="append", metavar="FILE", help="DER file (public key or certificate)")
        sp.add_argument("--point", action="append", metavar="CURVE:HEX", help="raw public key, e.g. p384:04ab...")
        sp.add_argument("--list", metavar="FILE", help="file with one CURVE:HEX per line")

    c = sub.add_parser("check", help="check public keys for known weaknesses")
    inputs(c)
    c.add_argument("--max-scalar", type=int, default=DEFAULT_MAX_SCALAR, help="test private scalars 1..N (default %(default)s)")
    c.add_argument("--deep", action="store_true", help="also test structured scalars and trivial Ed25519 seeds (slower)")
    c.add_argument("--blocklist", metavar="FILE", help="file of SHA-256 fingerprints of known weak/compromised keys")
    c.add_argument("--json", action="store_true", help="machine-readable output")
    c.set_defaults(func=_cmd_check)

    f = sub.add_parser("fingerprint", help="print the SHA-256 fingerprint of public keys")
    inputs(f)
    f.set_defaults(func=_cmd_fingerprint)

    d = sub.add_parser("demo", help="replay the reported-incident scalars on synthetic keys")
    d.set_defaults(func=_cmd_demo)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except KeyFormatError as exc:
        print(f"error [{exc.code}]: {exc.message}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
