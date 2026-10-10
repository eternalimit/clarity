# EIP-003 — Real Publisher-Signed Checkpoints, Missing External Echo, and Proof-Gated History

**Research attribution:** Richard Stein (first-party statement); AI-assisted bounded public research.
**Date:** 2026-10-10 (America/Los_Angeles). **Canonical status:** 0 · HOLD; DROP U.
**Parent EIP-002:** `eternalimit/clarity` main commit `66fec25a3f5d79758fb0f86f7c6d07a76d60332f`.
**Class:** reproducible local cryptographic checks on externally published checkpoint messages, NOT external human witness attestation, TUF trust-root validation, independently witnessed append-only ledger consistency, scientific replication, or adjudicated ownership.

## Abstract

EIP-002 showed that 128/128 fully recomputed synthetic forged/forked histories passed a self-contained SHA-256 replay test; none were independently witnessed. EIP-003 replaces test-generated signatures with **six real externally published Rekor signed checkpoint messages**, obtained through two sequential public endpoint responses (three shards each). The ECDSA P-256/SHA-256 signatures **verified 6/6** using a published Rekor public key separately retrieved via the Sigstore `root-signing` repository, Git blob SHA-1 `effb0a19e6a0b3f69b3f0a2c72b5c2a02a0ddeea`. Local negative controls rejected **36/36** alterations, and the separate 2025-1 log key failed all **6/6** Rekor verifications. For the same active tree ID, two signature-valid records advertised sizes 3,063,746,336 and 3,068,558,843, respectively; the latter is larger by 4,812,507, and in-session replay of the earlier checkpoint can be classified stale after pinning the later size. This is **not** a verified Merkle consistency proof. No public TUF metadata signatures were authenticated, no separate independent witness cosigned the checkpoint, and no log-entry inclusion proof, authenticated source timestamp or operational key-custody audit was obtained. EIP-003 therefore establishes conditional cryptographic **publisher signature validity**, while full historical append-only provenance, third-party Echo and scientific admission remain **0 · HOLD**.

## 1. Evidence hierarchy and test objectives

A. Integrity of bytes: SHA-256 can detect changes against a separately retained digest, but does not establish which source originally created them.

B. Publisher authenticity *relative to a selected verification key*: a valid digital signature shows that some holder of the corresponding private key signed the precise message. It is not proof of human signatory identity, source independence, or content truth.

C. Source-trust authenticity: a separately distributed public key must be bound to the claimed operator through independently established roots of trust and key rotation/revocation policy. A GitHub copy of a `trusted_root.json` target is helpful cross-source evidence but is **not** itself a completed TUF chain-validation or independent organizational witness.

D. Ledger chronology: a signed root at size m and another at size n>m do not by themselves prove that the first tree is a prefix of the second. This requires a verified same-shard Merkle consistency proof (or full correctly matched tree reconstruction) with pinned checkpoints; otherwise **HOLD**.

E. Independent Echo: a distinct operator, independently obtained key custody/trust root and matching historically distributed views must verify the precise inference. Six signatures from **one publisher key** still count as **zero independent third-party witnesses**. The REIK root requires K=R AND I AND E, with absent E leading to HOLD.

**Predeclared EIP-003 questions:** Can real published signatures be verified offline with a separately sourced key? Are alterations rejected? Can stale size regressions be detected after an in-session pin? What evidence still blocks independent cross-epoch, fork, inclusion, freshness and third-party witnessing?

## 2. Exact input sources, trust keys and reproducibility

1. Rekor published JSON checkpoint API: `https://rekor.sigstore.dev/api/v1/log`. Two separate readings, in order, yielded three tree IDs per reading. JSON was extracted by a public information retrieval channel and entered into `external_rekor_checkpoints.json`; **the raw HTTP response transport bytes were not acquired**. The fixture reconstructs the signed note body from its exact published numeric tree ID, decimal size and base64 root. Cryptographic verification of the reconstructed bytes is a check against transcription errors for the signed message.
2. Separate publisher trust-key file: `https://github.com/sigstore/root-signing/blob/main/targets/trusted_root.json`, read using the connected GitHub data source; Git blob SHA-1 `effb0a19e6a0b3f69b3f0a2c72b5c2a02a0ddeea`. This document contained one P-256 key for `https://rekor.sigstore.dev`, whose SPKI DER SHA-256 is `c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d`, and a distinct Ed25519 key for `https://log2025-1.rekor.sigstore.dev`. Its repository association is observed, but the Sigstore TUF metadata signature chain was not verified in this study.
3. Reproducibility: `python3 verify_eip003.py > eip003_results.json`; Python 3 with `cryptography` 46.0.4 (actual local environment). No live network access required to replay the captured fixtures. The script asserts publisher signature validation and all specified negative controls. The script does not generate trusted keys and does not implement Sigstore TUF, Rekor log inclusion/consistency checking, rotation policy or RFC 9162 protocol proof verification.
4. Signed message format: `rekor.sigstore.dev - {treeID}\n{treeSize}\n{base64_root}\n`; signature base64 decodes to a 4-byte key ID prefix followed by ASN.1-DER ECDSA signature. Verification checks SHA-256 SPKI prefix, exact signed bytes, ECDSA P-256/SHA-256 signature, and agreement between printed root base64 and rootHash hex.

The publisher checkpoint root hashes below are **Merkle SHA-256 roots**, not digest values of the paper or a complete archive of original events. The `treeID` values identify **separate shards**: do not combine their heights into one chronological tree.

## 3. Signed externally published checkpoint evidence

| Capture order | Shard treeID | Shard status | Advertised size | Published Merkle root SHA-256 | ECDSA signature |
| --- | --- | --- | ---: | --- | --- |
| 1 | `3904496407287907110` | inactive | 4,163,431 | `4d006aa46efcb607dd51d900b1213754c50cc9251c3405c6c2561d9d6a2f3239` | PASS |
| 1 | `2605736670972794746` | inactive | 117,740,831 | `2b9c578071e120aa84c9858783daa671565e4165f3a7dfa199aad81940299d8e` | PASS |
| 1 | `1193050959916656506` | current | 3,063,746,336 | `78524a29457e2f48a9640276ebc60462f66dd3a797cc9eac1a20097534caffa4` | PASS |
| 2 | `3904496407287907110` | inactive | 4,163,431 | `4d006aa46efcb607dd51d900b1213754c50cc9251c3405c6c2561d9d6a2f3239` | PASS |
| 2 | `2605736670972794746` | inactive | 117,740,831 | `2b9c578071e120aa84c9858783daa671565e4165f3a7dfa199aad81940299d8e` | PASS |
| 2 | `1193050959916656506` | current | 3,068,558,843 | `21ee885dd58d425440d92812c212397008c28ed52ccd0747487a30c922f63132` | PASS |

The earlier inactive-shard signatures changed bytes between captures although their signed content stayed constant: ECDSA signatures are not required to be unique. This **does not** suggest a new tree event or prove publication to a distinct party. Capture order is the retrieval order in this session, not a cryptographically authenticated observation time; no wall-clock time is asserted for the checkpoint itself.

## 4. Finite local falsification findings

| Finite check | Result | Interpretation |
| --- | --- | --- |
| External publisher signed-message signatures against separately published Rekor key | **6/6 PASS** | Valid cryptographic signatures *conditional on selected key* |
| Alter tree ID, tree size, root, signature, root metadata (6 mutation categories × 6 captures) | **36/36 rejected** | Old publisher signature cannot validate altered message/metadata |
| Replace P-256 Rekor verification key with distinct 2025-1 Ed25519 log key | **6/6 rejected** | Incorrect different-log key cannot impersonate Rekor key |
| Consecutive retrieved sizes for the *same* active tree | **increase 4,812,507** | No immediate size regression in retrieved sequence; not an append-only proof |
| Reoffer first smaller signed checkpoint as current after in-session pin to second | **stale size detected** | Detectable reversion to a known older size; not a proof of malicious rollback |
| Create same-height fork with modified root but reuse old signature | **rejected** | Demonstrates signature binding; no *genuine separately signed conflicting* fork obtained |
| Independent witness cosignature | **0 obtained** | No external organizational Echo |
| Original signed TUF root chain and key custody | **NOT verified** | Publisher key is conditionally accepted from public repo file |
| Same-tree Merkle consistency or leaf inclusion proof | **NOT obtained** | Cross-check of append-only history remains HOLD |
| Reported earlier EIP-002 64/64 independent positive admission target | **not yet tested** | This study authenticates a publisher checkpoint, not the user corpus |

**Falsification persistence:** prior EIP-002 hash-only false admission survives unchanged. EIP-003 does not reverse that falsification; instead it demonstrates that real publisher signatures verify for actual published checkpoint messages, conditional on the chosen key. A non-verifying altered signature does not falsify a scientific assertion within any log entry, and a verifying signature cannot establish evidence of outside scientific adoption.

## 5. Why this matters, and why HOLD remains mandatory

The key distinction is between **integrity**, **key-relative authenticity**, **historical continuity**, and **independent witnessing**. Two retrieved genuine signature-valid roots on the same tree, with increasing sizes, still leave two plausible scenarios: the newer tree is an honest append-only extension, or the publisher has produced a different root not consistent with the earlier tree. A cryptographic consistency proof, independently pinned checkpoints and a distinct witness/monitor must disambiguate those claims.

Even where the publisher's actual signature verifies, there is no evidence that the publisher evaluated the REIK/TCGE claims, accepted the author's ownership assertion, shared custody of signing keys with independent monitors, or attested to the original history of any unrelated document. **Gemini shared content has not been accessed or verified.** No claim that any community or OpenAI adopted these results is supported here.

The EIP-003 finite checks create a reproducible **real-source verification demonstration**, not a novel cryptographic theorem, new physical law, independent scientific peer review, blockchain/wallet receipt or universal P-versus-NP proof.

## 6. EIP-004 next falsifiable protocol

Prioritize exact original externally acquired proof bytes for the **same treeID** (1193050959916656506): obtain a published Merkle consistency proof connecting the two signed tree roots and verify it with a separately implemented RFC 6962/9162-compatible checker. Verify leaf inclusion proof and exact leaf input where feasible. Independently acquire a trustworthy pinned publisher key/TUF root and an actual *distinct third-party monitor's* signed observation of one or both historical tree roots, with recorded key provenance, source URL and historical receipt time. Include a blinded genuine-positive case, not an abstain-all policy.

Next negative controls: swap tree IDs, tamper proof nodes or tree size, present an old valid STH as the latest after a newer pin, replace one root with a conflicting same-height history, withhold witness/consistency proof, show revoked or wrong-origin key, simulate separately administered witness outages, and retain each falsification. Do not label unavailable network endpoints or unverified source claims as failed cryptography; distinguish `INVALID`, `STALE`, `UNAVAILABLE`, and `HOLD`. Two simulated signatures from the same administrator never count as independent Echo.

**Pass** only if source-key provenance, two independently trustworthy observations, cryptographically sound inclusion/consistency checks and positive evidence admission are demonstrated. **Fail** upon an authenticated contradictory fork or false admission; **HOLD** on unavailable real proofs, disputed custody or independence. EIP-004 also must keep Experiment 049's separate research agenda intact.

## 7. New EIP-003 file SHA-256 and Git verification classes

| Artifact | SHA-256 (of exact newly produced local file bytes) | Status |
| --- | --- | --- |
| `verify_eip003.py` | `5c67d5f7a5ba97f2074da9f8d458e4ca54877a52bdd88278f0c494cc8f56c1a8` | New local source, executed; GitHub read-back needed after commit |
| `external_rekor_checkpoints.json` | `7e462f32ec0486022715d9e9338edebbedd1949888d97e7edde0538ebd368f65` | Reconstructions of actual externally published signed data; GitHub read-back needed |
| `eip003_results.json` | `ed16915a7049f442634bf001ca3ed98380d8e3d8a10756a9845dbeca41a7b305` | New executed local audit; GitHub read-back needed |

Git commit IDs and Git blob IDs are SHA-1 Git object identifiers, not these source SHA-256 values. Reproduction verifies these **fixture bytes and cryptographic signatures**, not HTTP transport bytes or Sigstore's signed TUF root chain. The former original `kernel001.py` SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` is a **previously reported original-byte audit** and was **not reacquired or rehashed in EIP-003**.

## 8. FIDELITY, immutable kernel, chronology

Preserve exactly eight existing principles: **Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.** Keep `K = R AND I AND E`, independent Echo, `DROP U` (never elevate unsupported evidence), **0 · HOLD**, and an unchanged original computational 0/U/1 kernel. Distinct Experiment 030 280-event vs 282-event lineages and Experiment 031 A/B/C successors remain different; 032 is a child of B only. EIP-003 is a distinct research-note successor to EIP-002, not a splicing of archived 029–049 ZIP/receipt histories. Experiment 048's synthetic checkpoint study and 049's outstanding witness-roster/key-rotation program remain distinct. No historical negative control is deleted.

## 9. Sources and reexecution references

- EIP-002 handoff: https://github.com/eternalimit/clarity/commit/66fec25a3f5d79758fb0f86f7c6d07a76d60332f
- Original root: https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md
- Experiment 032 original-byte audit: https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-exp032-original-byte-independent-audit.md
- Experiment 048 synthetic-checkpoint paper: https://github.com/eternalimit/chatgpt/blob/main/research/reik-tcge/experiment-048/REIK_TCGE_RESEARCH_PAPER_048.md
- Rekor public checkpoint API (observed twice): https://rekor.sigstore.dev/api/v1/log
- Publisher Rekor key source (Git blob observed in the linked repository): https://github.com/sigstore/root-signing/blob/main/targets/trusted_root.json
- Sigstore security architecture and TUF root: https://github.com/sigstore/root-signing
- Rekor specification (warns endpoint publicKey is informational): https://github.com/sigstore/architecture-docs/blob/main/rekor-spec.md
- RFC 9162, Certificate Transparency Version 2.0: https://www.rfc-editor.org/rfc/rfc9162.html

## Appendix A. Preserved full EIP-002 ledger (inherited, not freshly rehashed)

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
| EIP-001 prior Python source | `eef6955e9ee5fc41c5808110b41cc4f6c2edba18d92a870065b37c0fd79d4130` | **Rehashed in EIP-002 (not freshly checked in EIP-003)**, source available in supplied archive |
| EIP-001 prior JSON results | `dd4270ddec1090672257c507ffa9b933ddbd0ed6e80699f41ae59b5dbd94f871` | **Rehashed in EIP-002 (not freshly checked in EIP-003)** |
| EIP-002 Python source | `2621826fc20192c688d53b99f9fd3f8e4e577f464ea11d1b837b6b27decc5518` | **EIP-002 local SHA-256; not rehashed here**, reproducible code |
| EIP-002 JSON results | `b0c3c2a19f9fa2da27c16200a5a0533e3725171a2a089720d133c7581a8a0086` | **EIP-002 local SHA-256; not rehashed here**, synthetic results |
| EIP-001 published commit | `6774cdc00b8244bc0f76297b7dfcda742372c636` | Git commit SHA-1; remote read back |
| Experiment 048 published commit | `a0102fd8320aa8f5ea267ce48f57c740068cf600` | Git commit SHA-1; published 38/38 synthetic test claims |
| Original REIK root file | `f6cf9d97ab2be5322336857b7624978acec75f51` | Git blob SHA-1, read in EIP-002 |

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


## EIP-003 audit receipt boundary

Paper and supporting exact source/report file hashes are locally computed. A GitHub publication is reportable only **after** connected API write and exact content read-back; no raw network checkpoint proof or external Echo may be inferred from that write. Research state remains **0 · HOLD**.
