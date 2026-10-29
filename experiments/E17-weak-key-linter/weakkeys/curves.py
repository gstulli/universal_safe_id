# SPDX-License-Identifier: Apache-2.0
"""Curve parameters and minimal elliptic-curve arithmetic.

RESEARCH PROTOTYPE. Not constant-time, not for production, never for real
private keys. It only handles PUBLIC keys and public data.
"""

from __future__ import annotations

from dataclasses import dataclass


class KeyFormatError(ValueError):
    """A public key could not be decoded or is structurally invalid."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class WeierstrassCurve:
    """y^2 = x^3 + a*x + b over GF(p), with prime order n and cofactor 1."""

    name: str
    p: int
    a: int
    b: int
    gx: int
    gy: int
    n: int

    @property
    def size(self) -> int:
        return (self.p.bit_length() + 7) // 8

    @property
    def generator(self):
        return (self.gx, self.gy)

    def is_on_curve(self, point) -> bool:
        if point is None:
            return True
        x, y = point
        if not (0 <= x < self.p and 0 <= y < self.p):
            return False
        return (y * y - (x * x * x + self.a * x + self.b)) % self.p == 0

    def neg(self, point):
        if point is None:
            return None
        return (point[0], (-point[1]) % self.p)

    def add(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q
        p = self.p
        if x1 == x2:
            if (y1 + y2) % p == 0:
                return None
            lam = (3 * x1 * x1 + self.a) * pow(2 * y1, -1, p) % p
        else:
            lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
        x3 = (lam * lam - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return (x3, y3)

    def mul(self, k: int, P):
        """Double-and-add. NOT constant-time."""
        if P is None:
            return None
        k %= self.n
        result = None
        addend = P
        while k:
            if k & 1:
                result = self.add(result, addend)
            addend = self.add(addend, addend)
            k >>= 1
        return result

    def encode_point(self, point) -> bytes:
        """Uncompressed SEC1 encoding (04 || X || Y)."""
        x, y = point
        s = self.size
        return b"\x04" + x.to_bytes(s, "big") + y.to_bytes(s, "big")

    def decode_point(self, data: bytes):
        """Decode a SEC1 point (compressed or uncompressed) and validate it."""
        s = self.size
        if len(data) == 0:
            raise KeyFormatError("bad-encoding", "empty point encoding")
        tag = data[0]
        if tag == 0x04:
            if len(data) != 1 + 2 * s:
                raise KeyFormatError("bad-encoding", f"uncompressed point must be {1 + 2 * s} bytes, got {len(data)}")
            x = int.from_bytes(data[1 : 1 + s], "big")
            y = int.from_bytes(data[1 + s :], "big")
            if x >= self.p or y >= self.p:
                raise KeyFormatError("not-reduced", "coordinate is not reduced modulo p")
            point = (x, y)
            if not self.is_on_curve(point):
                raise KeyFormatError("off-curve", "point is not on the curve (invalid-curve risk)")
            return point
        if tag in (0x02, 0x03):
            if len(data) != 1 + s:
                raise KeyFormatError("bad-encoding", f"compressed point must be {1 + s} bytes, got {len(data)}")
            x = int.from_bytes(data[1:], "big")
            if x >= self.p:
                raise KeyFormatError("not-reduced", "coordinate is not reduced modulo p")
            rhs = (x * x * x + self.a * x + self.b) % self.p
            # All supported curves have p = 3 (mod 4), so sqrt = rhs^((p+1)/4).
            y = pow(rhs, (self.p + 1) // 4, self.p)
            if (y * y - rhs) % self.p != 0:
                raise KeyFormatError("off-curve", "x has no matching y: point is not on the curve")
            if (y & 1) != (tag & 1):
                y = (-y) % self.p
            return (x, y)
        raise KeyFormatError("bad-encoding", f"unknown point encoding tag 0x{tag:02x}")


@dataclass(frozen=True)
class Ed25519Curve:
    """Twisted Edwards -x^2 + y^2 = 1 + d*x^2*y^2 over GF(2^255 - 19)."""

    name: str = "ed25519"
    p: int = 2**255 - 19
    d: int = (-121665 * pow(121666, -1, 2**255 - 19)) % (2**255 - 19)
    n: int = 2**252 + 27742317777372353535851937790883648493
    cofactor: int = 8
    gx: int = 15112221349535400772501151409588531511454012693041857206046113283949847762202
    gy: int = 46316835694926478169428394003475163141307993866256225615783033603165251855960

    @property
    def size(self) -> int:
        return 32

    @property
    def generator(self):
        return (self.gx, self.gy)

    @property
    def identity(self):
        return (0, 1)

    def is_on_curve(self, point) -> bool:
        x, y = point
        p = self.p
        if not (0 <= x < p and 0 <= y < p):
            return False
        return (-x * x + y * y - 1 - self.d * x * x * y * y) % p == 0

    def neg(self, point):
        return ((-point[0]) % self.p, point[1])

    def add(self, P, Q):
        x1, y1 = P
        x2, y2 = Q
        p = self.p
        t = self.d * x1 * x2 * y1 * y2 % p
        x3 = (x1 * y2 + x2 * y1) * pow(1 + t, -1, p) % p
        y3 = (y1 * y2 + x1 * x2) * pow(1 - t, -1, p) % p
        return (x3, y3)

    def mul(self, k: int, P):
        """Double-and-add on the whole group (no reduction mod n). NOT constant-time."""
        result = self.identity
        addend = P
        while k:
            if k & 1:
                result = self.add(result, addend)
            addend = self.add(addend, addend)
            k >>= 1
        return result

    def encode_point(self, point) -> bytes:
        x, y = point
        return (y | ((x & 1) << 255)).to_bytes(32, "little")

    def decode_point(self, data: bytes):
        """RFC 8032 section 5.1.3 decoding, rejecting non-canonical encodings."""
        if len(data) != 32:
            raise KeyFormatError("bad-encoding", f"Ed25519 public key must be 32 bytes, got {len(data)}")
        v = int.from_bytes(data, "little")
        sign = v >> 255
        y = v & ((1 << 255) - 1)
        p = self.p
        if y >= p:
            raise KeyFormatError("non-canonical", "y coordinate is not reduced modulo p (non-canonical encoding)")
        x2 = (y * y - 1) * pow(self.d * y * y + 1, -1, p) % p
        x = pow(x2, (p + 3) // 8, p)
        if (x * x - x2) % p != 0:
            x = x * pow(2, (p - 1) // 4, p) % p
        if (x * x - x2) % p != 0:
            raise KeyFormatError("off-curve", "no square root: point is not on the curve")
        if x == 0 and sign == 1:
            raise KeyFormatError("non-canonical", "x = 0 with sign bit set (non-canonical encoding)")
        if (x & 1) != sign:
            x = (-x) % p
        return (x, y)


def _p384_p() -> int:
    return 2**384 - 2**128 - 2**96 + 2**32 - 1


P256 = WeierstrassCurve(
    name="p256",
    p=0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF,
    a=0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF - 3,
    b=0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B,
    gx=0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
    gy=0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5,
    n=0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551,
)

P384 = WeierstrassCurve(
    name="p384",
    p=_p384_p(),
    a=_p384_p() - 3,
    b=0xB3312FA7E23EE7E4988E056BE3F82D19181D9C6EFE8141120314088F5013875AC656398D8A2ED19D2A85C8EDD3EC2AEF,
    gx=0xAA87CA22BE8B05378EB1C71EF320AD746E1D3B628BA79B9859F741E082542A385502F25DBF55296C3A545E3872760AB7,
    gy=0x3617DE4A96262C6F5D9E98BF9292DC29F8F41DBD289A147CE9DA3113B5F0B8C00A60B1CE1D7E819D7A431D7C90EA0E5F,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC7634D81F4372DDF581A0DB248B0A77AECEC196ACCC52973,
)

SECP256K1 = WeierstrassCurve(
    name="secp256k1",
    p=2**256 - 2**32 - 977,
    a=0,
    b=7,
    gx=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    gy=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
)

ED25519 = Ed25519Curve()

CURVES = {c.name: c for c in (P256, P384, SECP256K1, ED25519)}
