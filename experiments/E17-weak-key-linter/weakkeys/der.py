# SPDX-License-Identifier: Apache-2.0
"""A tiny DER/PEM reader for public keys and X.509 certificates.

Only what E17 needs: extract the SubjectPublicKeyInfo of EC and Ed25519 keys.
Research prototype; it parses PUBLIC data only.
"""

from __future__ import annotations

import base64
import re

from .curves import CURVES, KeyFormatError

OID_EC_PUBLIC_KEY = "1.2.840.10045.2.1"
OID_ED25519 = "1.3.101.112"
OID_RSA = "1.2.840.113549.1.1.1"
CURVE_OIDS = {
    "1.2.840.10045.3.1.7": "p256",
    "1.3.132.0.34": "p384",
    "1.3.132.0.10": "secp256k1",
}
OID_BY_CURVE = {v: k for k, v in CURVE_OIDS.items()}

_PEM_RE = re.compile(
    r"-----BEGIN (?P<label>[A-Z0-9 ]+)-----(?P<body>.*?)-----END (?P=label)-----", re.S
)


def _read_tlv(data: bytes, pos: int = 0):
    """Return (tag, value, next_pos)."""
    if pos + 2 > len(data):
        raise KeyFormatError("bad-der", "truncated DER")
    tag = data[pos]
    length = data[pos + 1]
    pos += 2
    if length & 0x80:
        n = length & 0x7F
        if n == 0 or n > 4 or pos + n > len(data):
            raise KeyFormatError("bad-der", "unsupported or truncated DER length")
        length = int.from_bytes(data[pos : pos + n], "big")
        pos += n
    if pos + length > len(data):
        raise KeyFormatError("bad-der", "DER value runs past the end of the data")
    return tag, data[pos : pos + length], pos + length


def _decode_oid(value: bytes) -> str:
    if not value:
        raise KeyFormatError("bad-der", "empty OID")
    first = value[0]
    arcs = [first // 40, first % 40]
    acc = 0
    for byte in value[1:]:
        acc = (acc << 7) | (byte & 0x7F)
        if not byte & 0x80:
            arcs.append(acc)
            acc = 0
    return ".".join(str(a) for a in arcs)


def _encode_len(n: int) -> bytes:
    if n < 0x80:
        return bytes([n])
    b = n.to_bytes((n.bit_length() + 7) // 8, "big")
    return bytes([0x80 | len(b)]) + b


def _tlv(tag: int, value: bytes) -> bytes:
    return bytes([tag]) + _encode_len(len(value)) + value


def _encode_oid(oid: str) -> bytes:
    arcs = [int(x) for x in oid.split(".")]
    out = bytes([arcs[0] * 40 + arcs[1]])
    for arc in arcs[2:]:
        chunk = [arc & 0x7F]
        arc >>= 7
        while arc:
            chunk.append(0x80 | (arc & 0x7F))
            arc >>= 7
        out += bytes(reversed(chunk))
    return out


def to_spki_der(curve_name: str, point_bytes: bytes) -> bytes:
    """Build a SubjectPublicKeyInfo (used by tests and the demo command)."""
    if curve_name == "ed25519":
        alg = _tlv(0x30, _tlv(0x06, _encode_oid(OID_ED25519)))
    else:
        alg = _tlv(
            0x30,
            _tlv(0x06, _encode_oid(OID_EC_PUBLIC_KEY))
            + _tlv(0x06, _encode_oid(OID_BY_CURVE[curve_name])),
        )
    return _tlv(0x30, alg + _tlv(0x03, b"\x00" + point_bytes))


def parse_spki(der: bytes):
    """Return (curve_name, point_bytes) from a SubjectPublicKeyInfo."""
    tag, body, end = _read_tlv(der)
    if tag != 0x30 or end != len(der):
        raise KeyFormatError("bad-der", "SubjectPublicKeyInfo must be a single SEQUENCE")
    tag, alg, pos = _read_tlv(body)
    if tag != 0x30:
        raise KeyFormatError("bad-der", "missing AlgorithmIdentifier")
    tag, bitstring, _ = _read_tlv(body, pos)
    if tag != 0x03 or not bitstring or bitstring[0] != 0:
        raise KeyFormatError("bad-der", "subjectPublicKey must be a BIT STRING with no unused bits")
    key_bytes = bitstring[1:]
    tag, oid_bytes, pos = _read_tlv(alg)
    if tag != 0x06:
        raise KeyFormatError("bad-der", "missing algorithm OID")
    oid = _decode_oid(oid_bytes)
    if oid == OID_ED25519:
        return "ed25519", key_bytes
    if oid == OID_EC_PUBLIC_KEY:
        tag, param, _ = _read_tlv(alg, pos)
        if tag != 0x06:
            raise KeyFormatError("unsupported", "EC key without named-curve parameters is not supported")
        curve_oid = _decode_oid(param)
        if curve_oid not in CURVE_OIDS:
            raise KeyFormatError("unsupported", f"EC curve OID {curve_oid} is not supported by this prototype")
        return CURVE_OIDS[curve_oid], key_bytes
    if oid == OID_RSA:
        raise KeyFormatError(
            "unsupported",
            "RSA keys are not supported by this prototype (USI would not allow RSA; batch-GCD checks are future work)",
        )
    raise KeyFormatError("unsupported", f"algorithm OID {oid} is not supported")


def spki_from_certificate(der: bytes) -> bytes:
    """Extract the SubjectPublicKeyInfo (raw DER) from an X.509 certificate."""
    tag, cert, end = _read_tlv(der)
    if tag != 0x30:
        raise KeyFormatError("bad-der", "certificate must be a SEQUENCE")
    tag, tbs, _ = _read_tlv(cert)
    if tag != 0x30:
        raise KeyFormatError("bad-der", "missing tbsCertificate")
    pos = 0
    tag, _, nxt = _read_tlv(tbs, pos)
    if tag == 0xA0:  # explicit version
        pos = nxt
    # serial, signature algorithm, issuer, validity, subject
    for _ in range(5):
        _, _, pos = _read_tlv(tbs, pos)
    start = pos
    tag, _, pos = _read_tlv(tbs, start)
    if tag != 0x30:
        raise KeyFormatError("bad-der", "could not locate subjectPublicKeyInfo")
    return tbs[start:pos]


def pem_blocks(text: str):
    """Yield (label, der_bytes) for each PEM block in a text."""
    for m in _PEM_RE.finditer(text):
        body = re.sub(r"\s+", "", m.group("body"))
        try:
            yield m.group("label"), base64.b64decode(body, validate=True)
        except ValueError as exc:
            raise KeyFormatError("bad-pem", f"invalid base64 in PEM block: {exc}") from exc


def keys_from_pem(text: str):
    """Yield (label, curve_name, point_bytes) for public keys and certificates."""
    found = False
    for label, der in pem_blocks(text):
        if label == "PUBLIC KEY":
            curve, pt = parse_spki(der)
        elif label == "CERTIFICATE":
            curve, pt = parse_spki(spki_from_certificate(der))
        else:
            continue
        found = True
        yield label, curve, pt
    if not found:
        raise KeyFormatError("no-keys", "no PUBLIC KEY or CERTIFICATE PEM block found")


def curve_by_name(name: str):
    try:
        return CURVES[name.lower()]
    except KeyError as exc:
        raise KeyFormatError("unsupported", f"unknown curve '{name}'; supported: {', '.join(CURVES)}") from exc
