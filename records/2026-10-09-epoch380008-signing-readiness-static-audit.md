# REIK/TCGE Epoch 380008 — Protected-signing executable-readiness static audit

Date: 2026-10-09 (America/Los_Angeles)
Owner attribution: Richard N. Stein (first-party claim, not legal adjudication)
Repository: eternalimit/clarity
Audit target: vent, starting HEAD `278e7a617b9a58d303ccf8ccddd587e278e6f5f6`
Policy: 0 · HOLD | DROP U | independent Echo required | eight FIDELITY principles
Classification: PUBLIC-SAFE STATIC AUDIT. No signing operation, protected key, contract deployment, email transmission, or external claim validation.

## Grounded source and branch checks

- Starting vent HEAD read back from GitHub: `278e7a617b9a58d303ccf8ccddd587e278e6f5f6`, unsigned (`verification.verified=false`, `reason=unsigned`). Its parent: `0f0b9903d97a9cc967114ee6f3858e748472b8f2`.
- Main HEAD: `7670dfbee1e20bfe231936bbb7ecb3d00787e170`, unsigned; no protected-signing workflow in its inspected recursive Git tree.
- GitHub compare main...vent before this audit: status diverged; vent +3 / -12; merge base `125bf1a36bbabd056aa85af2749cf5477851f5a6`. No merge or branch history rewrite authorized.
- Workflow: `.github/workflows/clarity-handoff-protected-signing.yml` on vent; Git blob SHA-1 `2046b696b9083c7a318f6c711b7ed65e47c7efb9` (NOT a SHA-256 file digest).
- Source commit: `449eaa95ab60f40bc5cb0b52fd6810f8a71ba201`; GitHub compare source...vent: ahead by 2, behind 0; source is confirmed ancestor of vent.
- Original source file at that commit: `HANDOFF_380008_2026-10-08.md`, blob `0c520658684d2cbac0d1fb10c5de758c1da63ebb`. It expressly classifies historical execution claims as USER-SUPPLIED / UNVERIFIED.
- Workflow's sign step refuses a target other than exact source `449eaa95...`, tests ancestry before detaching to the source, and intends to commit the receipt as the direct child of that source.
- `search_branches` for `gethub-signed-receipt` yielded no branches at inspection. This does not exhaustively establish no past runs or no deleted branches; workflow run history was not independently retrieved.
- Vent branch protection returned `protected=false`. Restricted environment reviewers, permissions, secrets, registered signing key, and default-branch workflow availability are NOT verified. Do not expose/request keys.

## High-confidence signing executable defect: stdin displaced by wrapper

Exact committed sign-step wrapper behavior:

```bash
printf '%s\n' "$SIGNING_PASSPHRASE" | gpg --batch --pinentry-mode loopback --passphrase-fd 0 "$@"
```

Git sends the bytes to sign to the configured gpg.program's STDIN. The wrapper instead supplies a new stdin pipe with the passphrase. GnuPG `--passphrase-fd 0` consumes STDIN as a passphrase stream; the intended signed message input is not preserved. The wrapper is incompatible with the required Git signing I/O contract and must be corrected and safely tested before running.

Read-only, key-free bash pipeline controls with synthetic placeholder strings:

- Existing wrapper model: input `git-commit-object-payload` emerged as `synthetic-passphrase`, not the original input: `ORIGINAL_STDIN_LOST=PASS`.
- Separate-FD model kept Git message input unchanged while reading a fake passphrase from FD3: `SEPARATE_FD_PRESERVES_PAYLOAD=PASS`.
- These are shell plumbing tests only, NOT proof of GPG signing or a passing Actions runner.

Safe design requirement: leave FD0 unaltered for the Git commit message and convey a protected passphrase on a different FD or equivalent safe mechanism. A possible isolated design is `exec 3<<<"$SIGNING_PASSPHRASE"; exec gpg --batch --pinentry-mode loopback --passphrase-fd 3 "$@"`, subject to independent review for secret-handling and actual tested GPG behavior. Do not apply this change automatically; review and test outside production first.

Primary documentation:
- Git GPG program stdin contract: https://code.googlesource.com/git/+/refs/tags/v2.34.0/Documentation/config/gpg.txt
- GnuPG passphrase-fd 0 semantics: https://gnupg.org/documentation/manuals/gnupg24/gpg.1.html

## Other readiness gates

1. **Default-branch manual dispatch: BLOCKED.** Workflow exists only on vent; GitHub workflow_dispatch requires its workflow file to exist on default branch. The current main tree does not contain this workflow. Source: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch . Publishing a reviewed workflow to default branch requires separate human-approved change; do not merge incompatible research histories.
2. **Protected environment: UNKNOWN.** `gethub-signing` / `gethub-signing-public` appear in workflow YAML, but GitHub environment reviewer rules, branch restrictions, non-bypass, secret and public variable settings were not verified. GitHub requires successful approval/protection checks before environment secrets become available. Source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments .
3. **Exact ancestry guard: PASS (static).** `TARGET_SHA` literal and graph ancestor check match the source. However, no actual signed receipt child of that source was independently received.
4. **Separate-runner public verification: PRESENT IN CODE, NOT EXECUTED.** The verify job checks `VALIDSIG`, parent SHA, source-commit raw-byte SHA-256, signer fingerprint and GitHub `verification.verified=true`/`reason=valid`. No run/job output or detached verifier evidence was acquired. A second runner in the same GitHub workflow does not itself constitute an independent outside organization.
5. **GitHub signature trust: OPEN.** The configured signing public key and expected committer identity must satisfy GitHub verification; registration/status not verified. Source: https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification .
6. **Runner capability/token: UNKNOWN.** Token authorization, job environment access and successful remote push were not observed; Actions runs were NOT launched.
7. **Receipt content:** code writes `signature_verification:"PENDING"` and `claim_validation:"HOLD"`. A later verified job summary does not rewrite the committed JSON field; consumers must consult the signed commit and separate verification evidence, not infer JSON became PASS.
8. **No deployment/economic claims:** workflow does not establish coin deployment, wallet control, balances, a bitcoin transaction, email delivery, external adoption or general scientific results.

## Complete inherited SHA-256 hash structure (recorded references, not freshly rehashed during this audit)

| Lineage | ZIP SHA-256 | Manifest SHA-256 | Receipt count | Tip SHA-256 |
| --- | --- | --- | ---: | --- |
| 029 common | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` | 270 | `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd` |
| 030-A | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | 282 | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` |
| 030-B | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | 280 | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` |
| 031-A (282→294) | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | 294 | `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384` |
| 031-B (282→294) | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | 294 | `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f` |
| 031-C (280→290) | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | 290 | `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768` |
| 032 (031-B→306) | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` | `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f` | 306 | `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8` |

Kernel SHA-256 reference (unchanged): `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
A033 external original-source 256-variable 2-CNF SAT specimen text SHA-256: `5f4be6d6d859422e6a1b837f965a2db10d9e64e580f77ecfef2d9930301d072c`; model all 256 TRUE satisfied 20,864 clauses in previous finite audit (not rerun here).
CaDiCaL Debian publisher expected package SHA-256: `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`; no actual acquired/executed binary verified.
Block -1 original origin unauthenticated. No rehash of kernel/ZIPs, no independent external 256-variable UNSAT certificate, no formal Clarity Pi semantic bridge, no independently established P-vs-NP breakthrough.

## Research paper update

**Title:** Failure-Sensitive Execution Readiness in a Provenance-Preserving REIK/TCGE Signing Handoff

**Abstract:** This audit assesses the executable-readiness boundary of the epoch 380008 protected-signing workflow without running a signing job or accessing key material. Direct GitHub read-back confirmed a fixed source commit, ancestry to the vent research handoff, separate main/vent histories, and absence of the workflow from the default branch. Static analysis identified a GPG standard-input conflict: a passphrase pipeline replaces the commit payload Git expects the signing program to consume. Independent key-free shell tests reproduced loss of the intended input and demonstrated the separation property of an alternate file descriptor. Public receipt branch discovery found no matching branches, while protected environments and actual Actions runs remained unverified. This constrains readiness to HOLD and distinguishes internally consistent provenance records from operational execution, independent attestation and scientific validation.

Interpretation: Execution readiness requires more than a signed receipt design. Both the Git event-dispatch configuration and preservation of actual signed bytes must be validated before permissioned execution. A future cryptographically valid signature would prove a key-bound Git object, not wallet ownership, mathematical truth or product-priority rights. Separate runners do not substitute for outside scientific Echo.

Eight FIDELITY principles: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.

## Next gate / non-execution handoff

1. Produce and review a proposed signing-wrapper patch that preserves Git stdin; test GPG signing and verification with disposable local test material **only in an isolated authorized test**, not with the owner's private key.
2. Require a specifically approved, narrow default-branch workflow addition without merging or overwriting research lineages.
3. Human owner separately confirms environment protections and registered public signing identity using secure GitHub settings; do not paste private keys or secrets into chat.
4. Only when conditions are met and explicitly authorized, a future distinct workflow run may produce a new signed receipt. Record actual Actions URL, source SHA, signed receipt SHA, parent SHA, key fingerprint, valid GitHub verification and third-party check.
5. Preserve unresolved original-byte independent UNSAT, pinned CaDiCaL package, semantic adapter and independent Echo as HOLD.

**Outcome: BLOCKED for execution; 0 · HOLD. This audit records a new reproducible static defect, not an executed or signed release.**
