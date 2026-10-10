# REIK/TCGE Research Significance: Identity Retention and Evidence Admission
## Bounded paper and audit — 2026-10-10

**Research attribution:** Richard Stein; AI-assisted synthetic pilot.  
**Admission:** **0 · HOLD**; **DROP U**.  
**Original kernel:** preserved unchanged.  
**Scope:** mathematical information-loss result, locally executed finite Python tests, and a proposed external falsification protocol. The shared Gemini conversation was not accessible or verified. No physical-law, P-versus-NP, external adoption, deployed consensus, or real independent-Echo claim is made.

### Abstract
Self-normalization N(x)=x/x=1 for nonzero x is many-to-one; a normalized result does not identify its origin. A standard-library finite test over 256 source values confirmed 256 possible inputs for output 1, 8 bits of remaining identity uncertainty under a uniform prior, and 128 possibilities after retaining one parity bit. Within this finite set, SHA-256 distinguished all 256 canonically serialized source records, and retaining old digests detected all 256 changed-source controls. A synthetic 16-event SHA-256 receipt chain rejected 16 altered events, 15 adjacent swaps and 16 drops. Such checks demonstrate bounded byte integrity and local chronology, **not** authenticity: an adversary can replace the data and recompute internally valid hashes. Independent trustworthy source or witness evidence is a distinct gate.

### 1. Mathematical significance and separation of meaning
For x ≠ 0, N(x)=x/x=1. In particular N(sqrt(pi))=N(2)=1 while sqrt(pi)≠2. Therefore N is not injective and no function of the output alone recovers the unique original x for every input. The valid exact identity is sqrt(pi)/sqrt(pi)=1, not sqrt(pi)=1.

If X is uniform on {1,...,256}, Y=N(X)=1, and P=X mod 2, then H(X|Y)=8 bits and H(X|Y,P)=7 bits. These are elementary consequences of counting, not discoveries of new physics or a novel complexity theorem.

A value of 1, an assertion's truth status, a source SHA-256 digest, a signed statement, and an evidence-admission decision are **distinct objects**. The repository root specifies R=Reality, I=Inference, E=independent Echo, K=R AND I AND E; missing required evidence -> HOLD. Failing the K gate does not necessarily falsify the substantive claim. The preserved original 0/U/1 kernel has not been modified or replaced.

### 2. Pilot method and reproducible checks
A newly authored standard-library-only Python pilot used source bytes `f"X={x:03d}\\n".encode("ascii")` for integers 1..256 and SHA-256 of those exact bytes. For synthetic event i, a canonical JSON object with sorted keys and separators (",",":") contained `index`, `source_sha256`, and `prev`; its digest became event `hash`. The checker verified exact successive index values, predecessor links, event hashes and an expected 16-event length. It ran with no external network, signatures, wallet material, original archived CNF, or old kernel source.

| Finite check | Local outcome |
| --- | ---: |
| Candidates given normalized output only | 256 |
| Candidates retaining parity | 128 |
| Unique candidate by digest within finite sample | 256 / 256 |
| Source mutation while preserving old claimed digest rejected | 256 / 256 |
| Unmodified synthetic 16-event chain | PASS |
| Event mutations rejected | 16 / 16 |
| Adjacent swaps rejected | 15 / 15 |
| Event drops rejected | 16 / 16 |
| Adversarial data+hash recomputation | Internally consistent, **not authenticated** |
| Independent real-world Echo | **NOT OBTAINED** |

**Exact SHA-256 freshly computed from new local files:**
- Full pilot Python source: `eef6955e9ee5fc41c5808110b41cc4f6c2edba18d92a870065b37c0fd79d4130`.
- JSON test results: `dd4270ddec1090672257c507ffa9b933ddbd0ed6e80699f41ae59b5dbd94f871`.
- Synthetic receipt genesis: `a29fbaf21d8905e294ec820fd6d34112c321db3f98548ff34c5450985b73a338`.
- Synthetic 16-event tip: `727d93d51c68683f6bc7065833d929805b9491797d7e794d1b71f831cfe2e7d2`.

The full local script and JSON are not asserted to be uploaded by this commit. The numbers above are **synthetic experiment digests, not original kernel digests**. Tests are locally executed, not third-party independently reproduced.

### 3. Immutable hash structure and separate histories
Preserve the **original kernel historical SHA-256** `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`, reported as independently rehashed from original archive bytes by earlier Experiment 032 and 048 audits, **not rehashed in this study**. EC-025 `c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835` and EC-026 `bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e` remain historical reference manifests.

The separate prior original-byte-audited ZIP SHA-256 values recorded in the public 032 audit are:
- 029: `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`;
- 030 / 282: `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942`;
- 030 / 280: `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed`;
- 031 A / 294 from 282: `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a`;
- 031 B / 294 from 282: `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff`;
- 031 C / 290 from 280: `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce`;
- 032 child of **031 B only**: ZIP `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c`; manifest `2df8a8e2159ccbde355e8a895f1a10356ab3af5a76c9d28f452f8f8f2325a03f`; 306-event tip `c3f2b34b63463f497a53462cd0494cc2c1f63dd243e32e0c8ecde5d488f323d8`.

Additional distinct later anchors: Experiment 035 ZIP `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` is a previously reported original-byte digest in the public 048 paper. Experiment 036 ZIP `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce` remains an **unreplayed historical reference** in that paper. Experiment 048 public Git **commit SHA-1** `a0102fd8320aa8f5ea267ce48f57c740068cf600`, public paper Git **blob SHA-1** `73f98e70598cb378cdb13e5e038da546015d7c47`: Git history does not prove scientific truth. No alternate 030/031 lineage was joined, no exact old archive was freshly rehashed here, and 033/034/035 parent chains are not claimed freshly replayed. See linked variant map and 032 audit for manifests and receipt tips.

### 4. Connection to Experiment 048
Experiment 048 reports **38/38** synthetic controls on checkpoint verification. One important negative control demonstrated that conflicting cryptographically valid certificates can exist when signer non-equivocation is deliberately broken. This supports a methodological caution about authentication assumptions, **not** external scientific Echo or a new theory of physical reality. Its test identities were synthetic and the independent external witness gate remains HOLD.

### 5. Next falsifiable study: EIP-002 independent provenance witnesses
Pre-register **256 blinded trials**: 64 genuine anchored records, 64 mutations retaining old digest, 64 forged replacements with updated internally consistent digests, and 64 rollback/fork histories. Compare output-only admission, hash-chain-only admission, and externally anchored chronological admission using independent witnessed checkpoints. Obtain independently administered, authenticated external witnesses with disjoint key custody, and publish the exact checker versions, test records, precommitment, false positives, false negatives and disagreements.

The strong finite **pass threshold**, given valid witness availability, is **64/64 genuine cases admitted and 192/192 attacks rejected or held**. Any attack admitted as verified falsifies the strong finite target; any genuine sufficiently witnessed case refused violates the stated availability target. No finite pass establishes universal security. Keep Experiment 049's separate checkpoint-roster origin and key-rotation agenda unmodified. A second function written by the same assistant is not external independent Echo.

### 6. Preservation, novelty boundary, sources
FIDELITY unchanged: **Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty**. Preserve falsification records, avoid promoting unresolved U, do not reveal secrets, preserve one chronological public branch, and keep 0 · HOLD on external evidence, claimed semantic equivalence, universal algorithms, signed deployments or outside adoption. The paper demonstrates known mathematics and bounded software behavior, not a novel proof. The Gemini share link was unreadable; **no assertions from it are verified or used**.

- Root: https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md
- Pi paper: https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-clarity-pi-reik-hash-ledger-working-paper.md
- 032 original-byte audit: https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-exp032-original-byte-independent-audit.md
- Separate 030/031 map: https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-reik-tcge-refresh-exp031-variant-map.md
- 048 synthetic checkpoint paper: https://github.com/eternalimit/chatgpt/blob/main/research/reik-tcge/experiment-048/REIK_TCGE_RESEARCH_PAPER_048.md
- C. H. Bennett, *Logical Reversibility of Computation* (1973), DOI: https://doi.org/10.1147/rd.176.0525
