# GETHUB Epoch 380008 — review audit receipt (2026-10-10)

## Provenance
- Project owner / original research attribution: Richard Stein.
- Root contract: `REIK_ROOT.md` (left unchanged).
- Comparison baseline: `eternalimit/clarity` branch `vent` commit `bd22bee71acd52098b0f6d1c05347952e85abd4f`.
- Code and README review commit: `94228788d4a927cf6da5708d6a6d1959a6a3fe59`.
- Review branch: `review/gethub-epoch380008-validator-20261010`.
- User-supplied sequence was a proposed record; the named root code/workflow files were absent from the inspected `vent` tree.

## Original-byte local hash structure (review files only)

| File | SHA-256 | Git blob |
| --- | --- | --- |
| `gethub_pipeline.py` | `1f90e1a26a5506ceffda7081ccf14a70b0ac1b5b4ada1ff834a52ece55cfffc4` | `b2b92826300ec14e053af4300acc2d2c043c4bc3` |
| `test_gethub_pipeline.py` | `a48daf3a131cf331d91bcb69f2c653a0f13203fa05f8c1910e188f59a2830376` | `d238b2ecd225d6bd85b1ac787216f58df16f5b50` |
| `README.md` | `d93af667c23fe666d41a673d3ca6278e5ad62631e65ada7619b919f8ca5831e5` | `f5dca51493b805f20b7bd667897d2bba69a348fe` |

These were calculated on the local files and the Git blobs were read back from the review branch. The historical original REIK/TCGE kernel SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` is preserved here as a reference only; its original bytes were NOT rehashed in this task.

## Execution receipt and falsification
- `python -m pytest -q test_gethub_pipeline.py`: **26 passed in 0.04s** after fixing an escaped-regex error identified by the first test run.
- Negative controls include matching-prefix wrong wallet, bad epoch, missing/short secret, missing allowlist, invalid coordinate input and mutated coordinate bytes.
- No real keys or wallet-custody signatures were used. No GitHub Actions workflow, protected environment, GPG signing or chain transaction was started.

## Evidence classification
- R: test output plus the GitHub `vent` and review branch read-back.
- I: exact-match allowlisting, fail-closed exceptions and HMAC provide stronger bounded local validation than prefix-only matching plus unkeyed SHA-256.
- E: synthetic local controls; no independent external Echo.
- K: **0 · HOLD** on custody, independent attestation, CI deployment and production authorization.

## Next gated action
Review the new implementation and add separately verified custody/signature challenge, trust root, external second implementation, attested receipt and a protected manual workflow only after human approval. Do not merge or deploy as a security control on the strength of these tests alone.
