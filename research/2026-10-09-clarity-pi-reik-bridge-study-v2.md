# Identity-Preserving Evidence Admission: A Bounded Correspondence Study
## Clarity Pi Math / REIK-TCGE Working Paper, Version 2.0

**Date:** 2026-10-09  
**Research attribution:** Richard Stein / Clarity REIK-TCGE  
**Document status:** VERIFIED BOUNDED BOOLEAN MODEL; CANONICAL 0-U-1 KERNEL CORRESPONDENCE ON HOLD  
**Parent ledger (Clarity):** `d2d42054f370f17c3e2c25f693dcc39802903ad9`  
**Parent ledger (ChatGPT):** `04169946f02d02f27bc0f45ccb5c6dc22605ebc4`  
**Scope:** Reproducible external overlay and limited proof checks; no modification of the original kernel.

### Abstract
This study continues the Clarity Pi Math investigation from the October 9, 2026 hash ledger. It distinguishes exact numerical normalization from evidence-based admission of propositions. We supply a *separate* six-input Boolean overlay that honors the public REIK root's admission gate under explicit assumptions, preserves unsupported claims in HOLD, and distinguishes independently admissible refutations from mere absence of supporting evidence. The overlay is checked by exhaustive enumeration of its 64 Boolean assignments, a differently implemented set-membership oracle, and symbolic satisfiability-based searches for counterexamples. Nine negative controls pass. These results establish consistency of this **defined finite overlay**, not its equivalence to the uninspected original immutable REIK/TCGE 0-U-1 kernel, not external scientific validation, and not any Millennium Prize result.

### 1. Canonical sources and evidence scope
Both specified parent GitHub commits were fetched and their one-parent histories inspected. The complete v1 working paper, ledger receipt, governance policy and `eternalimit/clarity/REIK_ROOT.md` were read by exact path/ref. The root Git blob at the baseline is `f6cf9d97ab2be5322336857b7624978acec75f51`. The root states `K = R AND I AND E` and `H = I AND NOT K`; independent Echo is required, and unsupported claims must HOLD. These formulas are the **source contract**, not a derivation from pi. An earlier research note establishes `sqrt(pi)/sqrt(pi) = 1` for positive pi but does not claim `sqrt(pi) = 1`.

The original 0-U-1 kernel's **historical reference** SHA-256 remains `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`; exact bytes were **not available and were not freshly rehashed**. We did not retrieve or replay the reported EC-025/026 and Experiment 029 source manifests and receipts. All hashes must remain typed as historical SHA-256 references, checked source-byte SHA-256, Git blob SHA, or Git commit SHA as applicable.

### 2. Proven normalization fact and information loss
For any real `x != 0`, `N(x) = x/x = 1`. Therefore `N(sqrt(pi)) = 1` exactly, while `sqrt(pi) != 1` in standard arithmetic. Since `N(2) = N(sqrt(pi)) = 1` but `2 != sqrt(pi)`, the function is not injective and cannot recover input identity.

**Information-loss theorem:** If a proposed truth/evidence classifier depends only on `N(x)`, it cannot distinguish two claims that have the same normalized value but different appropriate evidence classifications. **Proof:** Assume such a classifier `C` exists and two objects `a,b` have `N(a)=N(b)=1` but independently required classifications differ. Then `C(1)` would have to equal both distinct classifications, a contradiction. This conditional theorem is about the information carried by `N`; it is not a proof that all possible rich Clarity systems collapse in that fashion. A verified claim needs source/evidence metadata separate from the normalized number.

### 3. Conservative external admission overlay: definitions
Let six Boolean inputs denote whether the following claim-specific conditions have actually been established:

- `R`: applicable direct reality evidence;
- `I`: applicable candidate inference;
- `E`: an Echo result has been established;
- `D`: Echo provenance is independent of the originating inference;
- `F`: an applicable falsifier has been reported;
- `A`: the falsifier has passed independent admissibility checks.

Define effective `E* = E AND D`, `K* = R AND I AND E*`, and `Q = F AND A`. Notice that `D` is an *assumption* whose truth must be established by an actual independence assessment, not by a source's assertion about itself.

Define the **research-only** overlay outcome `B`:

| K* | Q | B | Reason |
|---:|---:|---|---|
| 0 | 0 | HOLD | Supporting Echo chain incomplete; no admissible falsifier |
| 1 | 0 | ADMITTED | Full proposed REIK gate and no admissible refutation |
| 0 | 1 | REFUTED | Admissible specific counterevidence; no completed positive chain |
| 1 | 1 | HOLD | Positive and negative chains conflict; retain both |

Here `REFUTED` applies **only to the specified claim in this overlay**; it does not assert that the original kernel maps falsification to the numeral 0 or that the kernel shares these transition rules. The original 0/U/1 source semantics remain out of scope. Equating `E*` with canonical independent Echo likewise requires source-level correspondence proof. Incomplete evidence, false-or-missing model agreement and unsupported assertions cannot count as independent Echo.

### 4. Elementary finite correspondence proposition
Under the definitions above:

```
B = ADMITTED  iff  K* AND NOT Q
B = REFUTED   iff  Q AND NOT K*
B = HOLD      iff  (K* AND Q) OR (NOT K* AND NOT Q).
```

**Proof:** Partition the four possibilities of `(K*,Q)` into `(0,0), (1,0), (0,1), (1,1)`. These rows are pairwise disjoint and collectively exhaustive. Substitution into the table yields the three equivalences. In the consistent non-refuted case `Q=0`, the overlay admits exactly when `K*=1`; with `E*=E AND D` stipulated as canonical Echo's effective condition, this is a conditional correspondence to the root `K=R AND I AND E` gate.

**What it does not prove:** It does not formally compare the overlay against the *original* kernel's source code, semantics, event transitions, regeneration logic, or independent Echo implementation. It does not provide a new mathematical theory of pi or validate external claims.

### 5. Reproducible tests and evidence
The public test harness is a separate file, `research/experiments/bridge-001/finite_bridge_check.py`. It was executed under **Python 3.13.5 / SymPy 1.14.0**. It defines (i) a direct conditional overlay, (ii) a differently implemented set-membership oracle, and (iii) separate SymPy Boolean satisfiability obligations.

Observed execution:
- `64/64` assignments agreed between overlay and set oracle.
- `ADMITTED=3`, `REFUTED=15`, `HOLD=46` of 64 (counts reflect input assumptions, **not probabilities**).
- `sympy.satisfiable(counterexample_conditions) == False`, meaning **UNSAT in this specified finite Boolean formula** for exclusivity, completeness and stated equivalences.
- `9/9` negative controls passed, including no independent Echo, absent Echo, inadmissible refuter, admitted refuter, simultaneous positive/negative evidence, 0/0, invalid `sqrt(pi)=1`, distinct inputs with the same normalizer output, and a locally modified receipt with changed SHA-256.

These facts support a **bounded logical model**. The UNSAT result is not a CNF benchmark, resolution certificate, verified original-byte 3-SAT instance, Lean kernel proof, or any assertion about the P versus NP problem. The negative-control receipt strings are synthetic and are not relabeled as historical experiment receipts.

Reproduce in a Python environment with SymPy 1.14.0:

```bash
python3 research/experiments/bridge-001/finite_bridge_check.py
```

The exact committed script was checked against the locally executed script using matching Git blob SHA `107a80524c3cbd93d1db09d5238519786e44bd1c`; the local source-byte SHA-256 is `778ba6eb874823ebe1f26eda532c5d457fdb97e817046acfa77f6ebecd6b86f4`. The standalone JSON receipt was stored as `research/experiments/bridge-001/finite_bridge_results.json`; its source-byte SHA-256 is `26f15f12c1aead7c1195e6b3f3966a9135e75242664e17f2604e5c87985ed9ca`. Git blob identifiers use Git's SHA-1 object scheme and are **not** the source-byte SHA-256 values.

### 6. Prior art and non-equivalence
Three-valued logical calculi existed well before this research. The Stanford Encyclopedia of Philosophy reviews the difference between truth gaps, truth gluts and systems such as strong Kleene three-valued logic ([Many-Valued Logic](https://plato.stanford.edu/entries/logic-manyvalued/), updated September 29, 2026). The overlay here is a *claim-admission classifier*, not automatically any of those specific truth-functional three-valued logics. Coincidentally using labels 0, U and 1 establishes no mathematical equivalence.

Lean uses a trusted kernel to check proof terms ([Lean Reference](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/)). **Lean was not available in the local execution environment**, and no Lean-generated or Lean-checked certificate is claimed. SymPy plus exhaustive finite enumeration provide a narrower class of checks with stated dependencies.

### 7. Preservation constraints and remaining work
The immutable original REIK/TCGE 0-U-1 kernel remains unchanged and unrehased. All eight FIDELITY principles are retained: Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence and Uncertainty. Independent scientific Echo is **not yet established**. DROP U means no unsupported promotion of unresolved evidence, not that uncertainty is erased from audit history.

The next decisive work is:
1. Acquire the **exact original kernel bytes**, verify its SHA-256 against the historical `03a38...` reference and identify the original transition rules without changing the file.
2. Formalize those original rules in a separate semantics document, and test a proposed **correspondence relation** against this overlay. Keep actual transitions and hypothesized transitions distinct.
3. Acquire independent, original-byte EC-025, EC-026 and Experiment 029 manifests/receipts, rehash them, and replay chronology only after bytes are available.
4. Add explicit evidence-independence adversarial controls (self-Echo, provenance reuse, conflicting source, stale/revoked support).
5. Optionally encode the separate, typed semantics in pinned Lean and check proof terms and theorem meaning before calling a kernel-level correspondence established.

### 8. Historical hash inventory
| Reference | Historical value (SHA-256; not newly rehashed) |
|---|---|
| Original immutable 0-U-1 kernel | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` |
| EC-025 manifest | `c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835` |
| EC-026 manifest | `bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e` |
| Experiment 029 manifest | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` |
| Experiment 029 270-event tip | `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd` |

**Final determination:** Algebraic normalization = established; consistency of this *bounded external overlay* = tested; equivalence to the original immutable REIK/TCGE 0-U-1 kernel, claimed historical hashes/receipt replay, and independent validation of empirical claims = **HOLD**. A Git commit records these results, not a cryptographic signature of their scientific validity.
