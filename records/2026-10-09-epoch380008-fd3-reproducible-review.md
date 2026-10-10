# REIK/TCGE Epoch 380008 — Reproducible FD3 Review-Only Patch and Synthetic Receipt

Date: 2026-10-09 (America/Los_Angeles)
Owner attribution: Richard N. Stein (first-party claim only)
Repository: `eternalimit/clarity`; branch: `vent`; exact inspected parent commit: `7932ed0d86c827f0d52f69ac0ffd5217a345603f`.
**State: 0 · HOLD. DROP U. Independent Echo required.** No production signing, private keys, workflow dispatch, main branch changes or original kernel edits.

## New public-safe reproducible artifacts

- `research/epoch380008/test_fd3_mock_signing.py`: Python standard-library only, Git/Bash required; **actual `git commit -S` invocation** with an instrumented *fake* `gpg` executable, no cryptographic signature.
- `research/epoch380008/review-only-gpg-wrapper-fd3.patch`: minimal unified diff for code review; the original `.github/workflows/clarity-handoff-protected-signing.yml` is **UNCHANGED**.
- `research/epoch380008/test-results.json`: locally produced deterministic-structure results with 18 passing synthetic assertions. Test timestamp is deliberately excluded; Git signing dates are fixed for reference byte equality.

Run locally from an isolated environment: `python3 research/epoch380008/test_fd3_mock_signing.py`. The harness creates a disposable **unconnected** Git repository and deletes it on completion. It uses the fake passphrase `SYNTHETIC_PASS_PHRASE_FOR_FD3_ONLY` only. Never supply owner keys.

### Object identity (SHA-256 of exact newly authored local files)

- Harness: `a7dee50beb844ca0e8c0dabec94c9449352beb9adc2e5f4155dc28a979797130`.
- Review-only patch: `395c827e52851e60ef17ac0b4dedafb200de68a861394147da1d0c3e555fd8b9`.
- Test result JSON: `e54f4586dfdeef518c84fa98c2f1cfbc9906c7c97f23aba52578e0a34449670b`.
- Git blobs (SHA-1 identifiers, **not** the same hash function): harness `47ea06f51319604da504ee71dc678411a680ef4a`, patch `abce2175157416ef15ac0d5df1fa92f5be0a5ea5`, JSON `264027ea02798d16cab6376a99edda48f7c5b387`.

### Finite test results

**18/18 assertions passed** using Git `2.47.3` and Bash `5.2.37` in this isolated runtime. Both original and corrected wrapper tests deliberately invoked a mock that exited nonzero, so no new Git signed commit was produced.

- Original wrapper: mock `gpg` FD0 received dummy passphrase, not Git commit bytes; reproduced documented defect.
- FD3 review candidate: mock FD0 received exactly the same bytes as a third independent `exec gpg "$@"` reference wrapper, comparing **complete bytes**, not merely a substring.
- Git input SHA-256, both reference and corrected: `8f1259683fc93bcf8f7ab7fc32c5b1c6779737cf77c47c1b3196952c597f3645`.
- Dummy FD3 channel SHA-256: `e4b8bd402239803635a6f0450dc21f3110b94f6c92af11f1823e4c1a6528e52d`.
- Dummy passphrase was absent from FD0, mock command-line arguments and mock child's environment; it remained separately available on FD3.
- Empty passphrase was rejected before the mock `gpg` executable ran; `HEAD` remained the original unsigned seed; disposable repository had no remote.
- Review-only patch was checked/applied in a **synthetic fixture matching the exact affected original workflow lines**, not against a downloaded full workflow file. Full workflow untouched.

**Limits:** This proves a finite mocked interface contract, not real GPG cryptography, secret security under hostile runners, successful GitHub Actions, or independent third-party testing. The here-string adds a newline, and GnuPG reads the first passphrase line; prohibit embedded newlines in real passphrases or specify secure behavior. Seek independent review before production.

## GitHub readiness read-back

- Baseline `vent` HEAD: `7932ed0d86c827f0d52f69ac0ffd5217a345603f`, unsigned. `main` HEAD: `7670dfbee1e20bfe231936bbb7ecb3d00787e170`, unsigned.
- Pinned source handoff commit: `449eaa95ab60f40bc5cb0b52fd6810f8a71ba201`, verified ancestor of baseline `vent` (source...vent = ahead 4 / behind 0).
- Unchanged workflow on `vent`: `.github/workflows/clarity-handoff-protected-signing.yml`, Git blob SHA-1 `2046b696b9083c7a318f6c711b7ed65e47c7efb9`. Default `main` recursive tree lacked this workflow. GitHub requires `workflow_dispatch` workflow file on the default branch. Source: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch .
- Full GitHub Actions history query returned 47 runs, 0 matching the epoch protected-signing workflow. Absence from this run list is not proof that no deleted/private historical evidence ever existed.
- Protected environments `gethub-signing` and `gethub-signing-public` are **named in source**, but their reviewer rules, self-review blocks, deployment branch restrictions and configured public/private variables could not be independently inspected through the available connector. Source: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments .
- Public signing-key identity, expected GPG fingerprint, GitHub verified committer email, GitHub `verification.verified=true` and `reason=valid`, and receipt commit URL are **UNVERIFIED**. Source: https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification .
- GnuPG FD handling: https://gnupg.org/documentation/manuals/gnupg24/gpg.1.html . FD0 and FD3 must remain distinct.
- Receipt JSON in currently committed design explicitly writes `signature_verification:PENDING` and `claim_validation:HOLD`; eventual independent public signature evidence is a separate object, never inferred from the original pending receipt.

## Inherited original hash lineage — recorded, not rehashed in this task

Original unmodified `kernel001.py` SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
Block −1: historical provenance boundary unauthenticated. 029 is common parent; 030-A and 030-B are siblings. 031-A and 031-B are separate 030-A descendants; 031-C descends from 030-B. 032 derives only from 031-B.

| Archive | Events | Original ZIP SHA-256 | Manifest SHA-256 | Tip SHA-256 |
| --- | ---: | --- | --- | --- |
| 029 common | 270 | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` | `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd` |
| 030-A from 029 | 282 | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` |
| 030-B from 029 | 280 | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` |
| 031-A from 030-A | 294 | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384` |
| 031-B from 030-A | 294 | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f` |
| 031-C from 030-B | 290 | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768` |
| 032 from 031-B ONLY | 306 | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` | `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f` | `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8` |

- A033 independently published original-source 256-variable monotone 2-CNF SAT file, recorded SHA-256: `5f4be6d6d859422e6a1b837f965a2db10d9e64e580f77ecfef2d9930301d072c`, 20,864 clauses satisfied by all TRUE witness in previous finite check; **not retested here**.
- Debian CaDiCaL 2.1.3-3 AMD64 publisher expected package SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`, actual package and binary not locally acquired/executed in this task.
- Missing external fully-active original-byte 256-variable UNSAT with independent certificate, authenticated Block −1, formal Clarity Pi-to-REIK semantic adapter and independent scientific Echo remain HOLD. No P-versus-NP result established.

## Research paper update

**Title:** *Exact Git Message Preservation Under File-Descriptor Separation: A Reproducible REIK/TCGE Epoch 380008 Signing-Gate Test*

**Abstract.** This experiment introduces a fully public-safe, independently rerunnable test harness for the signing-input preservation defect identified in the REIK/TCGE Epoch 380008 workflow. Standard Git commit signing was directed to a synthetic mock GPG process in an isolated repository. An unchanged original passphrase-pipeline wrapper and a review-only FD3 design were compared against a direct pass-through reference. Eighteen assertions passed, including full bytewise identity of the corrected Git signed-message input and its independent reference, separation of the passphrase channel, negative controls for empty passphrases, and absence of any successfully signed or remote commit. The original workflow remains unchanged. The result supports a narrow finite software-input correctness hypothesis but establishes no real GPG signing, independent external execution, wallet transaction, or mathematical theorem. The upstream source-parent link and explicit 0 HOLD gate persist under all eight FIDELITY principles.

**Method/object boundary:** Correct Git-to-GPG I/O is not proof of signature validity; a verified Git signature is not proof of external scientific truth. REIK's `K = R AND I AND E` admission gate requires independently attributable Echo. Exact `sqrt(pi)/sqrt(pi)=1` self-normalization supplies no external attestation.

**FIDELITY 8/8:** Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.

## Next authorized research gate

1. Independent party reruns the committed harness (no keys) and checks its hashes/output. Real GPG end-to-end test using **disposable** keys may be designed separately, but not executed against owner credentials here.
2. Review the standalone minimal diff for newline behavior, fd inheritance, env exposure, runner security, and compatibility with GnuPG/Git; keep it **unapplied** until authorized.
3. Obtain authorized, reviewed default-branch workflow placement without merging divergent research histories; verify environment protection settings out of band using account UI without sharing credentials.
4. Before any future run, require explicit owner authorization and then verify immutable signed commit, correct parent, source SHA-256, public signing fingerprint, GitHub verification status, Actions run URL and external independent Echo.
5. Continue fully active independent original-byte 256-variable SAT/UNSAT and CaDiCaL research separately; never infer proof, wallet control, economic value or deployment.

**NO EVIDENCE → NO ADVANCE. STATE = 0 · HOLD.**
