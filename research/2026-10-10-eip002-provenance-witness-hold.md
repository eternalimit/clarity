# EIP-002 — A Falsification Test of Self-Contained Provenance

**REIK/TCGE significance research; Richard Stein (first-party research attribution).**  
**Date:** 2026-10-10. **Classification:** bounded, synthetic negative-control study; not independent external witnessing.  
**Handoff:** [`eternalimit/clarity` commit `6774cdc00b8244bc0f76297b7dfcda742372c636`](https://github.com/eternalimit/clarity/commit/6774cdc00b8244bc0f76297b7dfcda742372c636).  
**Canonical state:** **0 · HOLD**; **DROP U**. **Gemini content:** unverified, not evidence.

## Abstract

Experiment EIP-002 tests whether a locally self-consistent SHA-256 receipt chain is sufficient to establish an authentic original history. The 256-case challenge preregistered in the prior public handoff separates four groups of 64: synthetic baselines, stale-hash edits, fully recomputed forgeries, and same-height fork histories. Using a reproducible Python standard-library harness, the naive rule `local chain passes -> admit` accepted **128/128** synthetic internally consistent attack chains (64 forgeries and 64 forks). An intentionally conservative admission gate detected 64 stale-hash edits and held all 192 locally consistent chains because no independently authenticated witness was available. Thus, the strong pre-registered external-witness goal is **NOT TESTABLE** here: 0/64 properly externally witnessed positive cases were supplied. The gate's zero false admissions is achieved by abstention, not proof of security, usefulness, or external scientific validity. This result establishes an elementary counterexample to *hash-chain-only provenance admission*, not a new cryptographic primitive, natural law or general complexity theorem.

## 1. Question, hypotheses and scope

**Question:** Can REIK/TCGE avoid promoting plausible but unauthenticated histories into verified knowledge when both an authentic-looking candidate and a deliberately rewritten candidate pass local integrity checks?

- **H0 (unsafe shortcut):** a valid self-contained receipt chain alone suffices to authenticate its purported history.
- **Falsifier:** produce even one rewritten history satisfying all local chain checks without any independent trusted historical anchor.
- **Restricted local hypothesis:** a gate that requires authenticated independent Echo will not mistake a bare self-asserted witness count or a self-recomputed receipt for external attestation.

The original REIK root contract remains `R = Reality`, `I = Inference`, `E = independent Echo`, and `K = R AND I AND E`; missing required evidence implies **HOLD**. Failure to establish K is not necessarily falsification of the underlying assertion. The original `0/U/1` CNF computational kernel is a separate immutable artifact; this synthetic test is **not** an implementation or redefinition of it.

## 2. Method and exact replication scope

Before this run, the public significance handoff specified **256 blinded trials, 64 in each of four groups**. This implementation realizes those deterministic group counts, but cases are **not genuinely blinded by an independent custodian**; the harness creates, labels and evaluates them itself. The independent blinded/witnessed portion of the preregistered experiment is **unfulfilled**.

Generate four events per case, SHA-256 link each to the prior event, and replay from a fixed synthetic genesis. All event bodies use JSON with sorted keys, ASCII encoding, and compact separators. For each case index 0..63:

1. **Synthetic baseline:** original four-event chain; should pass local checks, but cannot be independently authenticated.
2. **Stale-hash mutation:** mutate event 3 source digest without updating its old event digest; should fail local replay.
3. **Recomputed forgery:** use different source contents, then recompute all event digests and predecessors; should pass local replay and fool hash-only admission.
4. **Same-height fork:** preserve the first two events, change the last two, and recompute digest links; should pass local replay, demonstrating that genesis and chain length do not force one history.

The fabricated forged/fork records include optional textual claims to multiple witnesses or a trusted anchor; such text contains no authenticated outside witness signatures and is **never** treated as Echo. The strict demonstrator returns `INVALID_LOCAL` if replay fails and otherwise `HOLD_NO_INDEPENDENT_ECHO`; it does **not** implement actual signature verification, roster authentication, independently sourced timestamping or Merkle consistency proofs. These functions are security *requirements for future work*, not completed work in this harness.

Reproduce with `python3 eip002_provenance_gate.py > eip002_results.json` using Python standard library, without network access. Inspect both source and output. The script generates 256 synthetic fixture rows; it does not publish or claim independent raw historical witness observations.

## 3. Results and explicit falsification

| Case type | Count | Local chain passes | Unsafe hash-only admissions | Strict gate result |
|---|---:|---:|---:|---|
| Synthetic baseline | 64 | 64 | 64 | 64 HOLD |
| Stale-hash mutation | 64 | 0 | 0 | 64 INVALID_LOCAL |
| Recomputed forgery | 64 | 64 | 64 | 64 HOLD |
| Same-height fork | 64 | 64 | 64 | 64 HOLD |
| **Total** | **256** | **192** | **192** | **192 HOLD, 64 INVALID** |

**Falsification:** Hash-only admission passes **128/128** deliberately forged/forked internally consistent synthetic cases. Therefore local cryptographic self-consistency, even with a pinned synthetic genesis and equal height, does **not** authenticate which history actually happened. This is a statement about the modeled evidence, not proof of cryptographic hash failure.

**Gate non-result:** The restrictive gate did not falsely verify any of the synthetic cases because it held every locally consistent case. This is an **abstain-all policy in the absence of Echo**, and does **not** meet the intended 64/64 witnessed-positive acceptance goal. No external witness was accessed, authenticated, or asked to check this work. The claimed 192/192 attack rejection-or-HOLD performance would be trivial if all inputs were held, so it is not presented as a scientific success.

**Independent Echo status:** `NOT OBTAINED`; claimed factual authenticity: `0 · HOLD`. The earlier Experiment 048 38/38 synthetic controls and its Ed25519 key roster are separate from this EIP-002 negative-control harness. Experiment 049's external roster and rotation studies are not claimed completed or subsumed.

## 4. Evidence architecture required for a genuine EIP-002 independent test

Each challenge must reference a frozen exact-byte candidate, publisher/version digest, source-capture provenance, independent-checker digest, and an **externally acquired** signed or independently archived checkpoint with a trust root pinned *before* viewing challenge outcomes. At least two independent organizations/operators, separated in key custody and administration, should attest as scoped external witnesses, with identity and timestamp verifiability. Witness count must not be supplied merely by candidate-controlled metadata.

A genuine test should specify certificate/signature formats, key rotation/revocation and discovery, signed checkpoints bound to protocol+ledger+epoch+height+tip, and proof of historical prefix consistency. Witnesses must receive challenges without the hidden answer labels and report their own decisions and timestamps. Report every rejected, held, admitted, timed-out, unavailable or conflicting case; record precommitment and observed error rates and stratification separately. Negative controls must include legitimate but unattested records, withheld witness data, compromised/revoked keys, fully recomputed forks, conflicting signed views and delayed dissemination. If the test relies on a transparency log, inspect signed checkpoints, inclusion/consistency proofs and cross-client consistency; merely listing an artifact in a log does not validate the scientific claim it contains.

**External reference baseline:** [RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html) defines Certificate Transparency mechanisms for signed tree heads, Merkle inclusion/consistency proofs, monitors and auditing. Sigstore's [security model](https://docs.sigstore.dev/about/security/) explicitly distinguishes append-only logging and its trust roots from long-term independent monitoring. This study cites these **published mechanisms as background**, not evidence that EIP-002 performed their validation.

### Locked acceptance plan for an actual independent-witness run

- **64/64** genuine, properly witnessed candidates must be admitted under a prepublished policy and threat model.
- **192/192** attacks must be either rejected or held, stratified by exact attack and missing-data class, with zero false VERIFY decisions; no blanket HOLD policy can be called a successful positive-evidence test.
- Any authenticated false admission falsifies the strong bounded target; an unavailable or unreliable positive witness may produce an indeterminate result rather than prove a substantive claim false.
- Maintain separate independent checker implementation, witnessed test dataset and falsification archive. Report sample limitations; finite pass would not prove universal consensus or asymptotic complexity claims.

## 5. Full preserved hash structure and verification classes

SHA-256 values below are **exact 64-character references** from the connected public papers unless labelled **new local file SHA-256**. **Git commit and blob values are SHA-1 identifiers, not SHA-256**, and public Git retrieval does not independently recover unpublished original ZIP bytes.

### Immutable kernel and earlier ledger

| Artifact / exact identifier | Digest | Evidence class |
|---|---|---|
| Original `kernel001.py` | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` | Prior reported exact archived-byte rehash in 032/048; **NOT rehashed here** |
| EC-025 manifest | `c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835` | Historical reference, not rehashed here |
| EC-026 manifest | `bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e` | Historical reference, not rehashed here |
| Experiment 029 common ZIP | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | Earlier 032 audit, not independently acquired again |
| Experiment 030 / 282-event ZIP | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | Earlier 032 audit; distinct 030 history |
| Experiment 030 / 282-event manifest | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | Earlier public reference |
| Experiment 030 / 282-event tip | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` | Earlier public reference |
| Experiment 030 / 280-event ZIP | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | Earlier 032 audit; distinct 030 history |
| Experiment 030 / 280-event manifest | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | Earlier public reference |
| Experiment 030 / 280-event tip | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` | Earlier public reference |

### Distinct 031 successors and 032 branch

| Artifact | Digest | Evidence class |
|---|---|---|
| 031 A / 294, from 030/282, ZIP | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | Earlier 032 audit |
| 031 A manifest | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | Historical public reference |
| 031 A tip | `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384` | Historical public reference |
| 031 B / 294, from 030/282, ZIP | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | Earlier 032 audit |
| 031 B manifest | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | Historical public reference |
| 031 B tip | `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f` | Historical public reference |
| 031 C / 290, from 030/280, ZIP | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | Earlier 032 audit |
| 031 C manifest | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | Historical public reference |
| 031 C tip | `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768` | Historical public reference |
| 032 ZIP, child of **031 B only** | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` | Earlier 032 exact-byte audit |
| 032 manifest | `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f` | Earlier 032 exact-byte audit |
| 032 306-event tip | `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8` | Earlier 032 exact-byte audit |

### Later and EIP-002 study identifiers

| Artifact | Digest | Evidence class |
|---|---|---|
| 035 ZIP | `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` | Previously reported archived-byte rehash in 048; not rehashed here |
| 036 ZIP | `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce` | Prior historical reference, not independently replayed here |
| 036 manifest | `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749` | Prior historical reference |
| 036 354-event tip | `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0` | Prior historical reference |
| EIP-001 prior Python source | `eef6955e9ee5fc41c5808110b41cc4f6c2edba18d92a870065b37c0fd79d4130` | **Locally rehashed here**, source available in supplied archive |
| EIP-001 prior JSON results | `dd4270ddec1090672257c507ffa9b933ddbd0ed6e80699f41ae59b5dbd94f871` | **Locally rehashed here** |
| EIP-002 Python source | `2621826fc20192c688d53b99f9fd3f8e4e577f464ea11d1b837b6b27decc5518` | **New local SHA-256**, reproducible code |
| EIP-002 JSON results | `b0c3c2a19f9fa2da27c16200a5a0533e3725171a2a089720d133c7581a8a0086` | **New local SHA-256**, synthetic results |
| EIP-001 published commit | `6774cdc00b8244bc0f76297b7dfcda742372c636` | Git commit SHA-1; remote read back |
| Experiment 048 published commit | `a0102fd8320aa8f5ea267ce48f57c740068cf600` | Git commit SHA-1; published 38/38 synthetic test claims |
| Original REIK root file | `f6cf9d97ab2be5322336857b7624978acec75f51` | Git blob SHA-1, re-read this session |

### Chain map (branches intentionally separate)

```text
historical EC-025 -> EC-026                 (reported links; not replayed here)
common 029
  |--> 030 / 282 --> 031 A / 294            (distinct)
  |                `-> 031 B / 294 --> 032  (this one child)
  `--> 030 / 280 --> 031 C / 290            (distinct)

033 / 034 / 035 / 036--048                  (separate referenced later work)
EIP-001 (6774cdc...) --> EIP-002            (research-note handoff, NOT inherited original ZIP branch)
```

The full original 033–048 chain was **not** independently rehashed/replayed here. Do not treat an EIP research-note handoff as a merge of canonical experiment archive histories.

## 6. FIDELITY and preservation

Eight unchanged FIDELITY principles: **Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty**. Keep independent Echo as an evidence gate; historical negative findings and unavailable-source HOLD decisions persist. Never silently upgrade a claimed source, self-signature, synthetic witness, citation, public commit or compatible implementation into scientific knowledge. **DROP U** forbids promotion of unresolved evidence, not deletion of unresolved records. Public-safe notes only; no original kernel writes, private archives, signing keys, wallets or personal secrets included.

**Remaining HOLD:** authentic independent EIP-002 witness material, verified roster origin/rotation and third-party checker, distinct 048/049 integration, Gemini share contents, general complexity results, scientific adoption, real-world ledger history, and claims of universe-level information inheritance.

## Sources

1. `eternalimit/clarity`, [EIP-001 handoff](https://github.com/eternalimit/clarity/blob/6774cdc00b8244bc0f76297b7dfcda742372c636/research/2026-10-10-reik-tcge-identity-retention-significance.md).
2. `eternalimit/clarity`, [REIK_ROOT.md](https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md).
3. `eternalimit/clarity`, [Experiment 031 variant map](https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-reik-tcge-refresh-exp031-variant-map.md), and [032 original-byte audit](https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-exp032-original-byte-independent-audit.md).
4. `eternalimit/chatgpt`, [Experiment 048 public paper](https://github.com/eternalimit/chatgpt/blob/main/research/reik-tcge/experiment-048/REIK_TCGE_RESEARCH_PAPER_048.md).
5. RFC 9162, [Certificate Transparency Version 2.0](https://www.rfc-editor.org/rfc/rfc9162.html).
6. Sigstore, [Security Model](https://docs.sigstore.dev/about/security/).

## Audit receipt and next continuation

Local reproducible script and JSON results are generated above. **This paper's future Git commit SHA, Git blob SHA and exact read-back state must be supplied only after actual GitHub write and read-back**, not inferred from a filename. Next: independently acquire a real signed, historically pinned checkpoint and a distinct-admin witness audit, preserving 048/049 boundaries; until that happens remain **0 · HOLD**.
