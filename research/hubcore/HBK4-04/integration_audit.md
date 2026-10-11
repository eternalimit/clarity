# HBK4-04 — local HubCore consumer audit
Date: 2026-10-11
Repo: eternalimit/clarity
Base commit: dbfaf93f4fd3cb6fdce32badddad29042160e337
Scope: opt-in executable JSON consumer; not a Cosmos7 or Clarity Trunk Loop deployment.
Owner attribution: Richard Stein per repository records.

## Source verification
At the base commit, matching original-byte SHA-256 and Git blob checks:
- `tools/hubcore/hubcore.lua`: SHA-256 `bc5511dc1aa75f929b42c4fa46f63ff7e95ea6884d73b16e95ab69803200aca0`; Git blob `3e826cb10be934a0c6747876c3656103d8bec2f5`.
- `tools/hubcore/verify_mapping.js`: SHA-256 `d63e2e5245a1c18953d64953176eff5cc90f40825d1073641d7b1bd0c2c598d4`; blob `d15ec36de3a55b47273f08e82165d5a18c555a3d`.
- `research/hubcore/HBK4-03/coordinate_mapping.json`: SHA-256 `031e6fa2af07a35c9ac48153a65c5c5e9090c36aa54a1816c54592b9b9cc092c`; blob `4f766e4a6b16425ef26abf7e4b3d7f30c8c06e6a`.
- HBK4-03 original ZIP: SHA-256 `a795ad30fe2d310c33664430d9f30d4d23e840e422c57f66379fb4d73f72975e`.
- `REIK_ROOT.md` Git blob remained `f6cf9d97ab2be5322336857b7624978acec75f51`.

Reproduced HBK4-03: Lua regenerate/cmp PASS; Node verifier PASS; Lua negative controls PASS.

## Consumer search boundary
Default-branch GitHub content search for `Cosmos7`, `FLORA`, `Clarity Trunk`, `trunk`, `consumer`, and `package.json` found only retrospective research mentions or the previous HubCore receipt, not a callable Cosmos7/Trunk Loop runtime entry point. This is a bounded search result, NOT proof that no such system exists elsewhere. No deployed integration or live runtime import was verified.

## New implementation / execution
- `tools/hubcore/coordinate_adapter.js`: SHA-256 `a9aca29e9327cbf7bdaa04880897addf8d29d962d17a3845daa5263c8ef61c84`.
- `tools/hubcore/test_coordinate_adapter.js`: SHA-256 `d62db097af38009e80d417fa812aa4541db724637da76665105d4b0b5e328171`.
- `node tools/hubcore/test_coordinate_adapter.js` => `{"status":"PASS","assertions":58,"independent_echo":false,"deployed":false}`.
- `node tools/hubcore/coordinate_adapter.js 011` => four K4 edges, degree two, Monad separate, `reik_status: 0 HOLD`.
- `node tools/hubcore/coordinate_adapter.js 01U` => nonzero exit and fail-closed error.
- Negative controls cover invalid bits, 17 structural mutations, pin mismatch, and malformed source.
- This is local execution; GitHub read-back proves storage, not CI/CD deployment.

Run from the repository root (Node.js, built-in modules only):
```sh
node tools/hubcore/test_coordinate_adapter.js
node tools/hubcore/coordinate_adapter.js 011
```
Opt-in module import: `require('./tools/hubcore/coordinate_adapter').consume('011')`.

## Mathematical and evidence boundaries
The mapping is a chosen exact tetrahedral K4 embedding, not reconstructed from the decorative generated image. One Monad at (0,0,0) is not a fifth graph vertex. Three bits denote Boolean selectors, NOT the REIK/TCGE 0/U/1 evidence vocabulary. Independent externally administered Echo is absent. K=R AND I AND E remains authoritative; DROP U and 0 HOLD for unsupported claims.
All eight FIDELITY principles retained: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. Original REIK/TCGE kernel and distinct historical lineages remain untouched; historical kernel SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` is only a reference, not newly rehashed.

## Next
HBK4-05: recover a real, separately verifiable Cosmos7 or Clarity Trunk Loop consumer contract before creating a named runtime adapter. Require direct import execution, negative tests, externally independent Echo before increasing knowledge state.
