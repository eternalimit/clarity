# REIK/TCGE — Epoch 380008 cross-repository dependency verification

Date: 2026-10-09 (America/Los_Angeles)
Owner attribution: Richard N. Stein (first-party claim; not an adjudication)
Scope: GitHub public-safe read-only dependency verification, with this append-only audit record
State: **0 · HOLD**; **DROP U**; independent Echo still required

## Frozen kernel and scientific evidence boundary

Original kernel file: `kernel001.py`
Recorded kernel SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.

The source kernel file was not present in the inspected public tree of either `clarity/main` or `clarity/vent`; therefore this audit did not freshly recalculate its digest. Earlier finite archive checks and the 256-variable SAT specimen are preserved as reported research evidence, not re-executed by this GitHub dependency audit. No claim of P-vs-NP resolution.

FIDELITY preserved: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.

## Exact verified GitHub positions

- Repository: `eternalimit/clarity` (public), default branch `main`.
- Target branch `vent` HEAD **before this append-only receipt**: `0f0b9903d97a9cc967114ee6f3858e748472b8f2`, https://github.com/eternalimit/clarity/commit/0f0b9903d97a9cc967114ee6f3858e748472b8f2 .
- `main` HEAD at check: `7670dfbee1e20bfe231936bbb7ecb3d00787e170`, https://github.com/eternalimit/clarity/commit/7670dfbee1e20bfe231936bbb7ecb3d00787e170 .
- GitHub comparison before this receipt: `vent` and `main` diverged at `125bf1a36bbabd056aa85af2749cf5477851f5a6`; `vent` was 2 commits ahead and 12 behind `main`.
- `vent` previous HEAD commit's GitHub signature status was `unsigned`; `vent` branch protection was disabled.
- Exact protected-signing source commit in `clarity`: `449eaa95ab60f40bc5cb0b52fd6810f8a71ba201`. It is the immediate parent of the previous `vent` HEAD and adds `HANDOFF_380008_2026-10-08.md`: https://github.com/eternalimit/clarity/commit/449eaa95ab60f40bc5cb0b52fd6810f8a71ba201 .
- The handoff labels historical operations and ledger claims `USER-SUPPLIED / UNVERIFIED`, not authenticated delivery or execution.
- The handoff's claimed `3653b3062eeb0d20d52d82a42719fd071fad7a8b` is an existing **`eternalimit/chatgpt`** commit (ANCOIN Block 011 public evidence receipt), NOT a `clarity/vent` HEAD: https://github.com/eternalimit/chatgpt/commit/3653b3062eeb0d20d52d82a42719fd071fad7a8b .
- Its `3efc20829642b7f34304fe06c20cc0b1528b4f3d` anchor is also an existing **`eternalimit/chatgpt`** commit (Clarity Root reference), NOT a commit in `clarity`: https://github.com/eternalimit/chatgpt/commit/3efc20829642b7f34304fe06c20cc0b1528b4f3d .

## Signing and deployment gates

- `.github/workflows/clarity-handoff-protected-signing.yml` and `SIGNING_BINDING_380008.md` exist on `clarity/vent` and were added by previous HEAD `0f0b9903...`. The binding explicitly states `PREPARED; signing and deployment NOT EXECUTED`.
- The inspected `clarity/main` recursive tree did not include that workflow. Do not infer it is dispatchable, run, or configured.
- The workflow pins `target_sha` to `449eaa95ab60f40bc5cb0b52fd6810f8a71ba201`, requires an approved private signing environment, creates a receipt branch from the exact target and has a separate public-key verification runner.
- This audit did not inspect protected environment variables or private secrets, did not execute GitHub Actions, did not create any GPG signature, and did not verify a signed receipt or GitHub `valid` verdict.
- An Ethereum-style address, epoch identifier and GitHub App identifier in a user-supplied handoff are references only, not proof of control, funds, contract deployment, wallet signing, chain anchoring or external execution. No email was sent.

## Research-paper update — bounded interpretation

**Title:** Cross-Repository Provenance Reconciliation and Execution-Gate Preservation for REIK/TCGE Epoch 380008

**Abstract:** A read-only GitHub audit reconciled two historical handoff identifiers originally labeled as clarity HEAD/anchor with their actual source repository, eternalimit/chatgpt. The clarity/vent branch instead points to a prepared, unsigned signing workflow whose fixed parent commit preserves a user-supplied historical handoff with explicit verification limitations. The audit confirmed branch divergence from main and absence of the signing workflow from main's inspected tree. These outcomes improve provenance classification and expose unmet execution dependencies; they do not establish historical execution, wallet ownership, cryptographic signing, external adoption, or new scientific results. The unchanged REIK/TCGE kernel reference and eight FIDELITY rules remain preserved with 0 HOLD.

## Falsifiable next gate

1. Independently verify signing public-key identity, authorized reviewer and environment configuration without exposing secret material.
2. Independently review workflow security and obtain required default-branch availability under approved change control before dispatch.
3. Only after permitted execution, collect actual Actions run ID, signed receipt commit SHA, parent SHA, signed fingerprint, GitHub signature verification and independent check, each by read-back.
4. Keep `main` finite research lineage and `vent` epoch-signing lineage separate; no forced reconciliation.
5. Do not promote any unrelated kernel/Clarity Pi, third-party 256-variable UNSAT, dedicated CaDiCaL execution, or P-vs-NP claim from this dependency audit.

**No evidence -> no advance. State: 0 · HOLD.**
