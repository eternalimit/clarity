# REIK/TCGE Epoch 380008 — FD3 synthetic validation and dispatch evidence audit

**Date:** 2026-10-09 (America/Los_Angeles)  
**First-party owner attribution:** Richard N. Stein  
**Classification:** public-safe finite executable-interface testing and GitHub read-back. No production signing.  
**Target:** `eternalimit/clarity`, branch `vent`  
**Baseline commit:** `c3302b00fcb46ee63933caa7019615f022493e9e`  
**Admission state:** **0 · HOLD**; **DROP U**, independent Echo required.

## What was actually verified

GitHub branch and file read-back:
- `vent` HEAD at start: `c3302b00fcb46ee63933caa7019615f022493e9e`; GitHub signature verification `false` / `unsigned`.
- `main` HEAD at start: `7670dfbee1e20bfe231936bbb7ecb3d00787e170`.
- The original signing workflow on `vent` is unchanged: `.github/workflows/clarity-handoff-protected-signing.yml`, Git blob SHA-1 `2046b696b9083c7a318f6c711b7ed65e47c7efb9`.
- No corresponding workflow file was found in the inspected recursive tree of `main`, which is the repository's default branch. GitHub's documented `workflow_dispatch` event requires the workflow file on the default branch. Source: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch .
- The pinned source `449eaa95ab60f40bc5cb0b52fd6810f8a71ba201` is an ancestor of `vent`; GitHub reported source...vent ahead=3 and behind=0 at inspection.
- `main` and `vent` remain separate. No merge, history rewrite or main-branch edit took place.

### New: actual Git invocation with a mock GPG executable

A temporary **local-only Git repository** was created, with an unsigned seed commit, a mock GPG executable that captured input bytes and synthetic FD3, and two distinct wrappers: (a) the currently committed pipe-to-FD0 wrapper; (b) a proposed separate-FD3 wrapper.

Test versions: Git `2.47.3`, Bash `5.2.37`, Python `3.13.5`, GnuPG installed `2.4.7` but **not used to sign**.

The test invoked `git -c gpg.program=<wrapper> commit -S --allow-empty -m 'synthetic git commit message'` against both wrappers. A fake key ID and the dummy string `SYNTHETIC_PASS_PHRASE` were used; neither actual private key nor real GPG signature was involved. The mock always exited `1`, causing Git to exit `128` without creating a signed commit.

| Assertion | Outcome |
| --- | --- |
| Original wrapper loses Git-supplied commit payload | PASS (defect reproduced) |
| Original wrapper substitutes the synthetic passphrase on FD0 | PASS (defect reproduced) |
| FD3 wrapper preserves Git-supplied commit payload on FD0 | PASS |
| FD3 wrapper sends synthetic passphrase to FD3 only | PASS |
| FD3 wrapper keeps passphrase out of captured CLI arguments | PASS |
| Both mock signing attempts intentionally failed | PASS |
| No signed or additional local Git commit was created | PASS |
| Temporary test Git repository has no remote | PASS |

**Result: 8/8 finite synthetic assertions PASS.**

Observed original-wrapper mock stdin: **22 bytes**, SHA-256 `eba879acfbf9dd0633223e4c533900b22a944825742c330fab93514f6866e5ce`, contained the synthetic passphrase instead of the Git commit message.

Observed FD3-wrapper mock stdin: **265 bytes**, SHA-256 `3b9185cc9aad2d66fc68eb92fbbe7ef0bfc292c27e43a131798f413401d74a08`, contained the Git commit message and no passphrase. Separate FD3 carried the dummy passphrase.

Local independently authored test script SHA-256: `7ef86b57e0614933efc5c7cdf3c44d9958048c76609a854c2efa44db3ea3e8ce`. Printed synthetic result JSON SHA-256: `699e8eedd2db8c00468740fc2e76f8328377fef6ad811716e88a4d8788f5e4bf`. These *local* test artifacts were not published; a digest is not a substitute for publicly reproducible test code or external reproduction.

### Proposed review-only wrapper

```bash
#!/bin/bash
set -euo pipefail
exec 3<<<"$SIGNING_PASSPHRASE"
exec gpg --batch --pinentry-mode loopback --passphrase-fd 3 "$@"
```

This preserves standard input to the signing program and directs the passphrase to descriptor 3. Tested using a mock executable only, not real GPG. It remains subject to secure secret-handling review, testing with disposable controlled test material, GitHub environment readiness and separate execution authorization. **The workflow file was not modified or dispatched.**

Git's `gpg.program` contract requires standard input containing the data to be signed; GnuPG's `--passphrase-fd n` reads a separate file descriptor (0 means standard input). See:
- https://git-scm.com/docs/git-config/2.35.4.html
- https://gnupg.org/documentation/manuals/gnupg24/gpg.1.html

### Synthetic verification-output negative controls

The committed verify job uses `awk` to accept GPG `VALIDSIG` records with the expected fingerprint. Additional **synthetic text-only** `awk` checks gave:
- Matching synthetic `VALIDSIG`: accepted.
- Different fingerprint: rejected.
- No `VALIDSIG` record: rejected.

These are parser tests, not verification of actual GPG signatures or actual GitHub trust.

## New: repository Actions run inventory

The connected GitHub public read interface returned `total_count=47` workflow runs, with all 47 retrieved using `per_page=100`. Counts:
- `pages build and deployment`: 37
- `Bitcoin Miner Control Check`: 9
- `Signed archive receipt verification`: 1, a **different** workflow (`.github/workflows/signed-archive-receipt.yml`), completed `failure` on an older `main.pub` run.

**No run matching `Clarity Handoff Protected Signing` or the epoch workflow path was present among those 47 visible runs.** This does not prove no deleted/unlisted historical run ever existed. A `gethub-signed-receipt` branch search also returned zero current matching branches. It is incorrect to claim a signing receipt was generated or verified.

## Outstanding operational gates

1. **Dispatch: BLOCKED.** Workflow absent from default `main`. A narrowly reviewed default-branch workflow addition must be approved separately; do not force-merge the separate research histories.
2. **Production signing I/O: BLOCKED.** The original committed wrapper still consumes FD0 for passphrase. Mock-validated FD3 design is not deployed and has not been end-to-end tested using real disposable signing credentials.
3. **Protected environments: UNKNOWN.** Code names `gethub-signing` and `gethub-signing-public` but environment reviewer identity, self-review prevention, branch restrictions, and configured public/private variables could not be inspected via the connected GitHub interface. Request no keys or secret values. Environment policies must pass before secrets become available. See https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments .
4. **Signer identity: UNKNOWN.** Public GPG key registration and account/email verification have not been independently confirmed. A verified signature requires GitHub to validate a signed commit against a registered public key. See https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification .
5. **Receipt verification: NOT EXECUTED.** A future successful run must supply immutable signed commit SHA, actual Actions run URL, signed commit's immediate parent/source commit, exact SHA-256 of raw source Git commit bytes, GPG fingerprint with independent public-key check, and GitHub commit verification `verified=true` / `reason=valid`.
6. **Receipt JSON status: remains `PENDING` by design.** The proposed signing workflow writes `signature_verification:PENDING` in the receipt payload; no later step updates that value. Evidence must instead include separately verifiable signed object and public verification result.
7. **Claim scope: HOLD.** Even a verified receipt does not validate wallet ownership, Bitcoin anchor, coin deployment, funds, email delivery, external scientific adoption, or mathematical conjectures. A separate-runner verification is not external independent scientific replication.

## Inherited hash structure (recorded SHA-256; not rehashed in this signing audit)

**Frozen original `kernel001.py` SHA-256:** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.

| Artifact | ZIP SHA-256 | Manifest SHA-256 | Receipt count | Receipt-tip SHA-256 |
| --- | --- | --- | ---: | --- |
| 029 shared | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` | 270 | `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd` |
| 030-A | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | 282 | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` |
| 030-B | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | 280 | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` |
| 031-A from 030-A | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | 294 | `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384` |
| 031-B from 030-A | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | 294 | `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f` |
| 031-C from 030-B | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | 290 | `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768` |
| 032 from 031-B only | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` | `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f` | 306 | `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8` |

**A033 third-party fixed-source 256-variable monotone 2-CNF SHA-256:** `5f4be6d6d859422e6a1b837f965a2db10d9e64e580f77ecfef2d9930301d072c`. Historical finite model: all 256 variables TRUE, 20,864 of 20,864 clauses satisfied. Not rerun here. Independently sourced original-byte 256-variable UNSAT proof remains HOLD.

**Expected publisher hash for Debian CaDiCaL 2.1.3-3 AMD64 package:** `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`. Actual package acquisition/executable-run remains HOLD. Block -1 origin remains unauthenticated.

All **eight FIDELITY** principles preserved: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.

## Research paper update

**Title:** *Input-Channel Separation as a Falsifiable Signing Precondition in the REIK/TCGE Epoch 380008 Evidence Chain*

**Abstract.** This study extends the static readiness audit of a GitHub-based cryptographic receipt workflow through finite, synthetic execution tests. A new mock GPG harness was invoked by Git's actual commit-signing interface against an existing shell wrapper and a proposed separate-file-descriptor variant. The original wrapper reproducibly replaced Git's signed-data input with passphrase bytes, whereas the FD3 variant preserved the expected payload and separated the passphrase in eight passing assertions. Independent inspection of GitHub's 47 publicly listed Actions runs found no execution of the target epoch signing workflow. The source commit ancestry was confirmed; default-branch dispatch availability and protected-environment prerequisites were not. The evidence establishes a bounded input-interface repair candidate, **not** a real cryptographic signature, completed workflow, financial state, or scientific breakthrough. Cryptographic provenance and scientific validation remain distinct admission gates under REIK/TCGE.

**Interpretation.** The preservation of `U` at the evidence gate and the `0 · HOLD` state prevents a plausible design or a mock success from being promoted into a true external execution claim. Signed commit bytes, independent public verification, and documented authorized execution are required before release conclusions. REIK's proposed `K = R AND I AND E` gate and original ternary kernel correspondence remain separate unless formally proved.

## Next continuation

- Produce a minimal, review-only workflow diff replacing the passphrase FD0 pipe with a separately reviewed safe FD3 mechanism; do not apply it to the protected workflow without explicit review.
- Make the mock test harness reproducible as a public-safe standalone artifact if separately requested; its local SHA-256 alone does not enable outside reproduction.
- Obtain human-approved environment and default-branch configuration evidence, without copying secrets or merging histories.
- Require actual future signed receipt proof only after explicit execution authorization.
- Independently seek original-byte UNSAT evidence, pinned CaDiCaL verification, semantic correspondence proof and third-party Echo as separate research streams.

**Final admission state: 0 · HOLD. No evidence → no advance. No signing run was triggered.**
