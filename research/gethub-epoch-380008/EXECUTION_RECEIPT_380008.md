# Epoch 380008 — Local execution receipt / review-only

Date: 2026-10-10 (session calendar); branch under review:
`review/gethub-epoch380008-validator-20261010`.

## Exact verified original four-file baseline

| File | SHA-256 freshly calculated | Git blob reported by GitHub; locally recomputed |
| --- | --- | --- |
| `gethub_pipeline.py` | `1f90e1a26a5506ceffda7081ccf14a70b0ac1b5b4ada1ff834a52ece55cfffc4` | `b2b92826300ec14e053af4300acc2d2c043c4bc3` |
| `test_gethub_pipeline.py` | `a48daf3a131cf331d91bcb69f2c653a0f13203fa05f8c1910e188f59a2830376` | `d238b2ecd225d6bd85b1ac787216f58df16f5b50` |
| `README.md` | `d93af667c23fe666d41a673d3ca6278e5ad62631e65ada7619b919f8ca5831e5` | `f5dca51493b805f20b7bd667897d2bba69a348fe` |
| `AUDIT_RECEIPT.md` | `a9dc49a2004ff2469cde1abab5ba98eaaa01406ffbe93beaa58871ba5b3c06d4` | `754ff559b16932090354402eb1d8a3d4df3c7174` |

Review branch HEAD at input: `1f87b593b4a8a6c32648950d7dff91773d71ef05`.
These original four files are unchanged by this continuation.
Historical original kernel recorded SHA-256
`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`
**is a historical reference only**, not a fresh original-byte audit.

## Execution results

- Fresh baseline command: `PYTHONDONTWRITEBYTECODE=1 python -B -m pytest -q -p no:cacheprovider test_gethub_pipeline.py`: **26 passed, 0.04s**.
- New combined command: `PYTHONDONTWRITEBYTECODE=1 python -B -m pytest -q -p no:cacheprovider test_gethub_pipeline.py test_attestation_review.py`: **72 passed, 0.10s**.
- An intermediate second-backend test failed because PyNaCl was absent. That
  failed attempt is preserved in the session audit history. The distinct
  verifier was replaced with the installed system `libsodium` backend;
  72/72 passed after the change. This does **not** imply external Echo.
- No signing performed (even test fixture signing). Two verifiers checked
  published RFC 8032 test vector bytes.

## Byte provenance for newly proposed review-only files

New file hashes are provided in the next append-only continuation commit's
commit message/read-back report and must be recalculated on downloaded bytes.
This receipt carries no assertion of a completed remote commit until an
actual commit and read-back occur.

## Evidence and authorization boundaries

R: GitHub original four-file fetch and local tests.
I: deterministic fail-closed draft gates against replay, time, revocation,
forks and identity mismatch.
E: independent external wallet and witness attestations absent.
K: `0 HOLD`; no protected authorization or chain claim.

No changes to `vent`, `main`, `.github/workflows`, REIK/TCGE kernel or
historical experiment lineages were requested or performed in this local step.
