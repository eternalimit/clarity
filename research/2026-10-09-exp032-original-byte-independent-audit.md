# REIK/TCGE — Experiment 032 original-byte independent audit and research update

Date: 2026-10-09 (America/Los_Angeles)
Classification: **public-safe finite computational audit**, not external peer review or proof of a general algorithm.
Author/ownership statement (first-party claim): **Richard Stein states that REIK/TCGE and this work are his.** Preserve as a first-party claim; this record neither adjudicates rights nor changes the statement.
Canonical state: **0 · HOLD**. **DROP U** (do not promote unresolved claims). Independent Echo is required for knowledge admission.

## Anchor and method

- Repository `eternalimit/clarity`, branch `main`, checked starting HEAD/commit: `25f980db27ec217af2297c971fd1ceca7edbd3a0`.
- Baseline variant-map Git blob re-read: `794c1d627604a132360a3f4220e0a278e52d285a`.
- Original unchanged kernel `kernel001.py`, SHA-256 **recomputed from nested original archive bytes**: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Retrieved exact ZIP bytes of the three distinct Experiment 031 histories and the full Experiment 032 archive from the owner's private ChatGPT Library to a temporary local workspace for read-only inspection. **No original ZIP, kernel, certificate payload, secret or signing material is published by this note.**
- Independently authored a new, standard-library-only checker, not running/importing archived build scripts. It recomputed SHA-256 of original ZIPs and each declared member, checked ZIP CRC and path uniqueness, all manifest and parent links, all event/genesis/chain-tip SHA-256 links, original CNF proof derivations and in-memory mutated controls.
- Independent local verification script SHA-256: `6f02c333e23e507a0f916412d8a0b8029c613cf2fb0593c3403eb342b605b821`. Machine audit JSON SHA-256: `ee6b20233327aa248137ea830b4375ce475766daaf449cad3c10f6ba2f851258`. These auxiliary audit artifacts were computed locally, **not published**; their digest alone is not an external reproduction guarantee.

## Original-byte results

| Evidence | Independently computed value |
|---|---|
| Experiment 029 common archive | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` |
| Experiment 030 282-event archive | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` |
| Experiment 030 280-event archive | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` |
| Experiment 031 A (282→294), ZIP | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` |
| Experiment 031 B (282→294), ZIP | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` |
| Experiment 031 C (280→290), ZIP | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` |
| Experiment 032 original ZIP (799,684 bytes) | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` |
| Experiment 032 manifest SHA-256 | `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f` |
| Experiment 032 306-event receipt tip | `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8` |

**PASS, finite scope:** 306/306 chronological receipt events independently recomputed across Experiments 019–032; 12 new Experiment 032 links, with immutable 294-event B parent. Original-byte embedded parent, parent manifest hash and parent receipt tip all match. Verified four constructed fully-active 256-variable *finite* UNSAT resolution derivations totaling 3,076 independently recomputed steps (1,023 + 1,023 + 1,023 + 7), all ending in the empty clause. Verified 5/5 newly authored in-memory negative controls rejected: changed genesis, event hash, predecessor, terminal tip, and reordered events.

**Lineage rule:** Experiment 032 is a child of Experiment 031 **B** only. Experiment 031 A and C are alternate, separately hashed histories. The 282- and 280-event Experiment 030 archives share the same original-byte Experiment 029 predecessor; no cross-variant event splicing, canonical replacement or kernel modification occurred. Copies with alternative Library filenames were independently confirmed byte-identical for the matching B/C archives.

## REIK / TCGE research paper update

**Title:** *Independent Original-Byte Verification of REIK/TCGE Experiment 032: Branch-Aware Evidence Preservation Across a 306-Receipt Finite Research Lineage*

**Abstract.** This study audits cryptographically linked finite research artifacts without changing their original computational kernel. A separately written verifier read exact Library archive bytes, reproduced SHA-256 manifests and chronological linked-event tips, and validated 3,076 resolution steps in four finite UNSAT proofs. The audit distinguishes three Experiment 031 successor archives by their original-byte hashes and restricts Experiment 032 ancestry to its embedded B parent. Five deliberately corrupted in-memory receipt objects were rejected. These results support archive-byte integrity, finite proof validity, chronological provenance and falsification sensitivity in the inspected artifacts. They do **not** establish original third-party provenance, general 256-variable SAT/UNSAT benchmark certification, asymptotic algorithm complexity, P versus NP resolution, or independent scientific uptake.

**Interpretation.** Maintaining an explicit unresolved `U` and withholding promotion from `0 · HOLD` prevents internally consistent evidence chains from being mistaken for externally validated scientific claims. The canonical REIK knowledge gate remains `K = R AND I AND E`, where `E` requires independent Echo. Mathematical self-normalization `sqrt(pi)/sqrt(pi)=1` does not supply the missing formal correspondence to the original `0/U/1` kernel.

**Eight FIDELITY rules unchanged:** Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.

## Open independent gates (remain HOLD)

1. Obtain independently sourced **original raw files** containing a genuinely fully-active 256-variable SAT **and** UNSAT pair, and independently verify a complete SAT witness plus an independently checked UNSAT proof.
2. Acquire, hash, extract and version-check an actual pinned dedicated CaDiCaL/Kissat/MiniSat executable and measure real runs; publisher metadata or repository references are not enough. No dedicated solver was downloaded, hashed or executed by this audit.
3. Third-party rerun of the released exact original-byte artifact with independently attributable receipt. Assistant-generated independent checking code is independent of archived scripts, **not** a separate external lab.
4. Formal typed semantic correspondence of REIK's `R/I/E` gate to the preserved kernel and Clarity Pi hypothesis.
5. Attributable scientific citations, reuse or adoption. No verified OpenAI adoption or universal inheritance claim.
6. Coin/token deployment and any Bitcoin anchor or address-control claims remain HOLD without deployment addresses, network-chain transaction evidence and independent validation.
7. No P-versus-NP solution, proof of general polynomial-time SAT, GPG signing, blockchain action or legally adjudicated ownership is asserted.

## Governance

The original kernel is unmodified. This document is a **new audit note**, not a replacement of pre-existing A/B/C archives. Only public-safe hashes and finite audit results are published. Historical negative findings persist; unresolved claims remain unresolved. **No evidence → no advance; state 0 · HOLD.**
