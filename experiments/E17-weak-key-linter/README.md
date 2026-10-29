# E17: weak-key checker (first prototype)

🌐 **English** · [Português (Brasil)](README.pt-BR.md)

> ⚠️ **Research prototype.** It inspects **public** keys only. **Never** paste private keys, and never use real keys or personal data here. A key that passes is only "not obviously bad": **it is not proof of quality** (whitepaper section 23.10).

- **Whitepaper:** sections 23.4 to 23.6 (rejecting weak secrets, publish before use, continuous monitoring) · section 16, experiment E17
- **Issue:** [#17](https://github.com/gstulli/universal_safe_id/issues/17)
- **Status:** **in progress.** Only the first part (the checker) is prototyped. "Publish before use" and the proof of compromise are not implemented yet.

## Hypothesis

Rejection by construction, monitors and "publish before use" detect weak keys and block their activation (whitepaper section 16, E17).

## What this prototype does

It checks public keys on NIST P-256, NIST P-384, secp256k1 and Ed25519, read from PEM public keys, PEM certificates, DER files or raw hex points.

| Check | Severity | Notes |
|---|---|---|
| Invalid encoding, point not on the curve, coordinate not reduced | FAIL | Invalid-curve risk |
| **Tiny private scalar** (the kind reported in the October 2026 intermediate-CA incident) | FAIL | Tests private scalars ±1 to ±N by lookup (N = 65,536 by default) |
| Structured scalar (`2^k`, `2^k±1`, repeated bytes) | FAIL | `--deep` |
| Trivial Ed25519 seed (all-zero, repeated byte, small integers) | FAIL | `--deep` |
| Ed25519 identity or small-order point; non-canonical encoding | FAIL | |
| Ed25519 point with a torsion component | WARN | Not in the prime-order subgroup |
| Same key more than once in a batch | FAIL | |
| Keys that are negations of each other (scalars d and −d) | WARN | |
| Fingerprint on a blocklist | FAIL | SHA-256 of the canonical encoding |

It has **no dependencies** beyond the Python standard library (Python 3.9+). The tests use the optional `cryptography` package as an independent cross-check.

## How to use

From this folder:

```bash
python3 -m weakkeys demo                                   # replays the reported scalar values on synthetic keys
python3 -m weakkeys check --pem chain.pem                  # PEM public keys and/or certificates
python3 -m weakkeys check --point p384:04<hex...>          # a raw public key
python3 -m weakkeys check --list keys.txt --deep --json    # one CURVE:HEX per line; deeper search; JSON output
python3 -m weakkeys fingerprint --pem chain.pem            # SHA-256 fingerprints
```

Exit code: `0` no key rejected, `1` at least one key rejected, `2` usage or parse error.

## Method and success criterion

Defined in the whitepaper (section 16, E17). For this first prototype we set a narrower criterion **before running**: *every key built from the scalar values reported for the incident is rejected, with the scalar recovered; ordinary keys pass; results agree with an independent implementation on curve arithmetic.*

## Result (first run, 29 October 2026)

- **Tests:** 32 pass (`python3 -m unittest discover -v`, about 16 s). They include known vectors (NIST P-256 and secp256k1 doubled generator, RFC 8032 Ed25519 test vector 1), a cross-check of public-key derivation against the independent `cryptography` library, and parsing of real X.509 certificates.
- **Incident replay (synthetic):** all eight scalar values reported in the press (4, 56, 66, 115, 155, 156, 230, 237) on P-384 are rejected, with the scalar recovered. An X.509 certificate whose key has private scalar 4 is rejected end to end. An ordinary P-384 key passes. The real certificate keys were **not** used (we do not have them): the keys are synthetic, built from the reported values.
- **Cost (pure Python, one core, development machine):** building the table of 65,536 multiples takes about 2 s (P-256, secp256k1), 3 s (P-384) and 4 s (Ed25519), once per run. After that each key is an O(1) lookup. `--deep` adds about 3 to 7 s per curve for structured scalars and about 8 s for Ed25519 trivial seeds.
- **Against the success criterion:** met for the narrower criterion above. The broader E17 criterion ("all known weak keys rejected; detection in minutes; no activation without independent verification") is **not yet** met: only the checker exists, there is no activation flow or proof-of-compromise protocol.

## Limitations (what this does not show)

- **It detects known patterns, not randomness.** A subtly weak generator passes. This is an open question (whitepaper question 36).
- **Search depth is small by default.** Scalars above N (default 65,536) are not found unless they are structured. A baby-step giant-step search could cover far larger ranges with modest memory; not implemented.
- Pure Python and not constant-time. A real monitor scanning public certificate logs would need an optimized implementation.
- No RSA (USI would not allow RSA; batch-GCD checks are future work), no P-521, no signature or certificate-chain validation, and a deliberately minimal DER parser.
- The `demo` and tests use synthetic keys derived from scalar values reported in the press. The press reports differ in details and the cause of the weak generation was not clarified (whitepaper section 23.1).

## Next steps

1. Independent cryptographic review of this code and of the checks.
2. Extend the search with baby-step giant-step; add P-521 and RSA batch-GCD.
3. Prototype "publish before use" (pending state, independent monitors, activation delay) and the proof-of-compromise protocol.
4. Measure detection and blocking time end to end, as the whitepaper's E17 requires.
