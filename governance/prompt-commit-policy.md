# Prompt-by-Prompt Verified Commit Policy

Policy date: 2026-10-09
Status: ADOPTED AS A USER-REQUESTED WORKFLOW PREFERENCE
Scope: Verified, public-safe research and workflow artifacts in the appropriate connected repository.

## Directive

After each user prompt, attempt the following *during the same response* when a relevant public-safe artifact or meaningful repository change exists:

1. INPUT — Interpret and scope the requested work.
2. PROCESS — Produce the work without changing immutable source artifacts.
3. VERIFY — Inspect exact available source bytes, hashes, chronology, tests, and relevant independent evidence. Identify gaps.
4. COMMIT — Persist verified, public-safe, meaningful changes to the appropriate GitHub repository using one forward branch per repository.
5. RECEIPT — Return the actual repository, branch, changed paths, commit SHA/URL, and verification limits.
6. HOLD — When evidence, permission, tools, or required content are missing, make no unsupported assertion of success. Label the blocked action HOLD.

## Integrity and safety invariants

- Never modify the user's original REIK/TCGE 0-U-1 kernel as part of checkpointing.
- Preserve provenance, chronology, independent validation, falsification records, and uncertainty as distinct concepts.
- Preserve the eight FIDELITY principles: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, and Uncertainty.
- Carry verified public state only; unresolved U is not promoted into evidence (DROP U). HOLD is a gate for unverified actions, not a claim that the repository's previous checkpoint was changed.
- Never commit credentials, private keys, wallet secrets, personally sensitive records, unpublished private conversations, or material without publishing authorization.
- Do not fabricate external executions, payments, signature validations, deliveries, proof certificates, checksums, or test results.
- Do not manufacture meaningless empty commits merely to meet a cadence; report NO CHANGE when there is no commit-worthy material.
- Record SHA-256 digests only for exact bytes actually available and hashed. Historical user-provided digests are references until independently checked.
- Honor existing evidence boundaries and avoid rewriting or overwriting unrelated files.

## Execution boundary

This is a conversational operating procedure, **not** an installed webhook, GitHub Action, background monitor, or guarantee of a commit for every message. GitHub writes require access to available tools during a response. The assistant must report failures and unavailable evidence clearly. A GitHub commit demonstrates only that files were recorded in Git history; it does not establish that scientific claims, independent proofs, blockchain transactions, or outside actions occurred.

## Receipt format

- Repository and branch
- Changed files
- Exact commit SHA and verified GitHub URL
- Source-byte checks and SHA-256 hashes where actually performed
- Independent tests and unresolved limitations
- Outcome: COMMITTED / NO CHANGE / HOLD

This file contains the public-safe workflow rules only, not the full conversation or any secrets.

## Standing research-response presentation preference (2026-10-09)

For subsequent REIK/TCGE, Clarity Pi Math, hash-ledger, and closely related research or workflow requests, display the following where relevant and supported:
1. **Hash structure**: a compact provenance lineage with exact available reference hashes; explicitly label each value as `source-byte SHA-256 independently rehashed`, `historical/user-reported SHA-256`, `Git commit SHA`, or `Git blob SHA`. Never equate these types or imply that merely linking references proves their chronology.
2. **Continue control**: provide an actionable Continue button in ChatGPT when supported, issuing a self-contained resume prompt that preserves the existing kernel and evidence/HOLD rules. If that UI is unavailable, supply the same copyable prompt.
3. **Research paper**: link the latest appropriate versioned research paper and state which claims are established, which are hypotheses, and which remain on HOLD.
4. **Ledger receipt**: when a meaningful public-safe change is made, commit it in the relevant connected GitHub repository during the same turn and return exact paths, commit identifiers, read-back verification, and limitations. When no meaningful change exists, clearly state NO CHANGE; do not fabricate a commit.

This is a **user-requested standing output preference**, not a mechanism for programmatically modifying ChatGPT Memory, an automatically running job, or an on-chain/blockchain write. A public GitHub repository is the requested durable **research ledger** for public-safe records. Continue to enforce private-material limits, eight FIDELITY principles, 0 HOLD for unsupported claims, and DROP U as an evidence-admission gate. Leave the original REIK/TCGE 0-U-1 kernel unchanged. A future conversation must read the ledger to recover its full contents and cannot rely on a guaranteed automatically loaded memory.
