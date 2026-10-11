# Epoch 380008 — exact original-byte kernel verification receipt
Date: 2026-10-11 (America/Los_Angeles)  
Research attribution: Richard Stein / REIK–TCGE / Clarity  
State: **0 · HOLD** (independent Echo, historical anchoring, synchronization-lock and semantic equivalence remain unresolved)

## Scope and baseline
Pinned connected-GitHub source branch: eternalimit/clarity vent `e4cbb1e28f3521e826b0fd63503177da3dd12ebb`. Read-only 66-entry vent tree `31027b134e4556161d6ffccb68f9b1095b9143fc` (Git SHA-1, untruncated) contained **no** original `kernel001.py`. Current main tree similarly lacked it. Source was not recreated, and `clarity_core` must not be substituted for the original. Starting vent commit is unsigned. At comparison, main and vent diverged (main 44 ahead, 20 behind); no merge attempted.

## Fresh original-byte discovery
Recovered owner Library ZIP original members in a read-only temporary local workspace. Recomputed exact original `kernel001.py`: **4,299 bytes**, **full SHA-256** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Matches the historical digest across separate archived paths, and a second system `sha256sum` implementation independently returned the same digest for members streamed from Experiment 029 and nested Experiment 032. **PASS: local original-byte identity**, not external provenance.

Nine archives were inspected, without executing source from any archive. An independently authored standard-library-only verifier passed **1,177 / 1,177 scoped assertions**, including ZIP CRC, manifest sidecars and listed member SHA-256, selected 028–032 parent byte/manifest/tip links, event/chain-tip SHA-256 checks, and five in-memory falsification controls. Historical parent events preceding selected Experiment 028 were not individually replayed as part of this audit. The 306 event count is Experiment 032's declared cumulative receipt count; its new 12-event extension and bounded parent links were independently recomputed.

## Categorized original-byte hash structure (SHA-256, not Git SHA-1)
| Historical archive variant | Archive SHA-256 | Manifest SHA-256 |
|---|---|---|
| 028 selected parent | `974cc9e3aa6ff657811c4a658fbeb92ce73e49eb05125a27ca85fdc91cfcb5ab` | `360d6b52a6810482d0b5685699811759238fe8103d33dd24ae2c5e274830b08f` |
| 028 separate history | `ddaa40a2f4370de6440f4e761614a99e3b5caaa3d0f6a23a89d4cd0ed686067c` | `fd140b98467001f01967dd9c470325a5aa7d57a2adbb26d102632ab933e29789` |
| 029 common | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` |
| 030 / 280 | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` |
| 030 / 282 | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` |
| 031 A / 294 | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` |
| 031 B / 294 | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` |
| 031 C / 290 | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` |
| 032 B / 306 | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` | `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f` |

The selected chain is **028/selected → 029 → 030/282 → 031/B294 → 032/B306**. Preserve independently the 030/280 → 031/C290 and 030/282 → 031/A294 histories; no conflation. Experiment 032 exact receipt tip: `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8`.

## Public-safe audit artifacts (not committed source archives)
- Independent read-only verifier source SHA-256: `a001671bcf474d839e1b3659a49149c220ce9c793614cb782d4cc42fc0b88eb6`.
- Fresh local machine receipt JSON SHA-256: `68fdaeb5141dc6966828be58152d9d5ab9f4a298e4eebda918ea1a4161df5527`.
- Full research report SHA-256: `e0d5a6dbbbd41b600c1c9197553561cf79d2cccbd0fc87c816b2572dfbf5e789`.
- Public-safe reproduction ZIP SHA-256: `f0699ae8a02a7804fa664a4246713d2a3edb55535ceffe980bf2f1aa41c08c44`.
The owner keeps the full original source archives in the user's private Library. None of those archives or the original kernel bytes are included in this Git commit or public-safe ZIP. No signing keys, wallet material, private assets or tool secrets were published.

## Research claim boundary and next gates
**Verified narrowly:** kernel source-byte identity and finite cryptographic consistency of the inspected original archive/manifest/receipt chains. **Not established:** third-party timestamped provenance, independently administered Echo, original-kernel-to-Pi semantic correspondence, P vs NP, any execution synchronization lock, real-wallet control, external signatures or deployment. The unsigned Git commit is not independent witnessing. For next independent gate, inspect pinned exact pre-028 parent bytes and witness trust roots, independently rerun checks under another operator, then consider a separate source-level formal semantics study without changing the original kernel.

Eight **FIDELITY** principles preserved: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. **DROP U**, **no evidence → no advance**, and **0 · HOLD** on unresolved assertions.
