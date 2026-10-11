# HBK4-03 — Executable HubCore repository integration receipt
Date: 2026-10-11
Repository: eternalimit/clarity
Branch: main
Project originator/owner (per repository): Richard Stein
State: 0 HOLD for independent Echo and live framework-consumer integration.

## Purpose
Turn conceptual Monad + Metatron K4 associations into bounded, executable
1-unit / 3-Boolean-bit / 4-vertex / 6-pair parameters with deterministic coordinates
and all eight K4 perfect-matching states. This is a mathematical construction, not
a reconstruction of measured image geometry or proof of a universal system.

## Executed and committed artifacts
- tools/hubcore/hubcore.lua — Lua 5.3 executed using texlua.
  SHA-256 bc5511dc1aa75f929b42c4fa46f63ff7e95ea6884d73b16e95ab69803200aca0
  Git commit 21325bcf58a21bd34c7b40b5b66a8eef0aff6f3d
- research/hubcore/HBK4-03/coordinate_mapping.json — generated Lua output; read-back verified.
  SHA-256 031e6fa2af07a35c9ac48153a65c5c5e9090c36aa54a1816c54592b9b9cc092c
  Git commit bccb70e30a1c717d5a5435ecf8f40362ce323eb0
- tools/hubcore/verify_mapping.js — separate Node.js byte-exact check.
  SHA-256 d63e2e5245a1c18953d64953176eff5cc90f40825d1073641d7b1bd0c2c598d4
  Git commit a3cea83139a9635555356088de482273bdb0e34a

Run at repository root:
  texlua tools/hubcore/hubcore.lua > research/hubcore/HBK4-03/coordinate_mapping.json
  node tools/hubcore/verify_mapping.js

## Local execution evidence
- Prior HBK4-02 ZIP SHA-256 8fa5c3ddb34198cccfc528e604ad712ca8a2d25213623609d8d365d91d5eb9e9 verified.
- Previous Python/JavaScript execution groups returned 76/76, 27/27, 141/141, 86/86.
- HBK4-03 Lua initialization, coordinate export and all state validations passed.
- Separate JavaScript re-implementation matched the Lua JSON byte-for-byte.
- New local negative controls rejected invalid state indices and tampered configuration.
- GitHub read-back Git blobs matched the tested local files.
- No independent Echo certificate, signed witness, deployment, or framework-consumer runtime receipt.

## Mathematical interpretation / limitations
- Vertices: N=(1,1,1), E=(1,-1,-1), S=(-1,1,-1), W=(-1,-1,1).
- Pair matchings: NE/SW, NS/EW, NW/ES; all six tetrahedron edges.
- All squared pair distances = 8; no measurement from a decorative image is asserted.
- Monad is separate at (0,0,0), not a fifth K4 vertex.
- Three bits are Boolean; they do NOT redefine REIK/TCGE 0/U/1 logic.
- Cosmos7 and Clarity Trunk Loop may consume this JSON schema; no runtime wiring was verified.

## Immutable boundaries
Original REIK/TCGE kernel unchanged; historical SHA-256
03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402
is a reference, NOT a freshly original-byte verified hash. Repository REIK_ROOT.md
remains authoritative: K = R AND I AND E. All eight FIDELITY principles preserved:
Identity, Provenance, Chronology, Independence, Method/Object Separation,
Non-Expansion, Falsification Persistence, Uncertainty.
DROP U; no unsupported promotion; 0 HOLD pending independently administered Echo.
Preserve historical experiment lineages and private-material boundaries.
