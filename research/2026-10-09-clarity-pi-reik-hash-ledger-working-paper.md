# Identity, Normalization, and Evidence
## A Hash-Preserving Working Paper on Clarity Pi Math and REIK/TCGE

**Version:** 1.0 — 2026-10-09  
**Document type:** Research working paper; evidence-bounded, not a peer-reviewed proof of a new system  
**Research attribution:** Richard Stein / Clarity REIK/TCGE  
**Preserved state:** 0 · HOLD for unverified claims  
**Canonical project source:** [REIK_ROOT.md](https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md)  
**Prior analysis:** [Missing Link](https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-missing-link-normalization-to-knowledge.md)

### Abstract
This paper distinguishes three objects often conflated in reasoning workflows: (1) an exact mathematical identity, (2) the truth status of a proposition, and (3) the evidence-admission status of a claim. Clarity Pi Math uses the exact normalization identity sqrt(pi)/sqrt(pi) = 1 as a point of discussion. The Clarity repository separately defines a knowledge gate K = R AND I AND E, where Reality, Inference and independent Echo are all required for validated knowledge. We prove that self-normalization alone is *information-losing* and cannot establish that an arbitrary external proposition passes the knowledge gate. We then present a conservative specification for provenance-aware receipt structures, distinguish historical hash references from independently read-back Git artifacts, and state falsifiable next steps for investigating a formal bridge without altering the original REIK/TCGE 0-U-1 kernel.

**Keywords:** REIK, TCGE, three-state evidence, provenance, SHA-256, normalization, proof checking, independent verification, FIDELITY.

### 1. Research question
What additional formal mechanism is needed to connect the exact identity sqrt(pi)/sqrt(pi) = 1 to REIK/TCGE's knowledge-admission rule without confusing arithmetic certainty with a claim's evidentiary validity?

This paper makes no claim that an arithmetic identity alone creates knowledge, solves an open mathematical problem, proves a scientific hypothesis, or cryptographically verifies unpublished historical experiments.

### 2. Established mathematical fact
Let x be a nonzero real number and define the self-normalization map N(x) = x/x. From the multiplicative inverse property, N(x) = x · x^(-1) = 1.

Since pi > 0, sqrt(pi) > 0, hence

    N(sqrt(pi)) = sqrt(pi)/sqrt(pi) = 1.

The equality is **exact**. sqrt(pi) is approximately 1.772453850905516; the decimal representation is an approximation. The separate equation sqrt(pi) = 1 is false in conventional real-number arithmetic.

**Lemma 1 (Non-injectivity of self-normalization).** The map N: R\{0} -> {1}, N(x) = x/x, is not injective.

**Proof.** Take x = sqrt(pi) and y = 2. Both are nonzero and x != y, yet N(x) = N(y) = 1. Thus distinct inputs produce the same output. QED.

**Corollary.** From the value N(x) = 1 alone, one cannot recover x or establish the truth of a different proposition about x. In particular, normalization cannot itself determine the evidentiary status of a separate research claim.

This is the precise mathematical obstruction to treating a normalized numerical value of 1 as evidence that some unrelated proposition must pass.

### 3. REIK/TCGE repository contract
The public repository root defines:

    R = Reality / direct evidence
    I = Inference / interpretation
    E = Echo / independent validation of the inference
    K = R AND I AND E
    H = I AND NOT K

It also specifies HOLD for insufficient evidence and rejects repetition, plausibility, confidence and model agreement as substitutes for independent Echo. See [REIK_ROOT.md](https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md).

The user's separately preserved research vocabulary is 0 / U / 1. In this working paper, "U" denotes an unresolved claim for exposition only. A complete three-valued operational algebra, its transitions, admission rules and relation to the canonical source kernel **have not been independently extracted and verified**. Nothing below silently rewrites the original kernel.

### 4. The missing formal bridge
A possible research bridge must provide, at minimum:

- A **typed claim** c with exact source representation, scope and meaning.
- **Evidence records** r with provenance, chronology, independence constraints and specific claims they address.
- **A verification procedure** V(c,r,checker) that records what was actually checked, and with which pinned checker bytes/version.
- **An admission function** A(c, evidence) that distinguishes admission, falsification and insufficient evidence.
- **Proof obligations** showing the admission function agrees with the REIK root gate under explicit assumptions and preserves uncertainty.

The bridging result must be a proved correspondence between the *defined* evidence semantics and K = R AND I AND E, not a substitution of the numeral 1 for truth. A claim can have an exact mathematical encoding while remaining unresolved as a real-world assertion. Failure to admit a claim is not equivalent to proving the claim false.

**Candidate exposition states (not a kernel implementation):**

    CONFIRMED if the claim passes defined, applicable independent checks;
    FALSIFIED if a valid applicable counterexample refutes the precise claim;
    UNRESOLVED / HOLD if required evidence or checker independence is missing.

Conflicting, stale, inapplicable, or incomplete evidence must not be auto-promoted. Falsification must be retained as an auditable record, not overwritten by later confidence.

### 5. Hash structure and provenance classes
A robust hash report separates *content identifiers* from *claims about content*. The following are **historical SHA-256 references supplied during this research conversation; exact original source bytes were not available for a new independent SHA-256 rehash in this paper**:

| Role | Historical reference / digest | Verification status |
| --- | --- | --- |
| Original immutable REIK/TCGE 0-U-1 kernel | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` | Historical reference; original bytes not inspected |
| EC-025 manifest | `c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835` | Historical reference; exact bytes not inspected |
| EC-026 manifest | `bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e` | Historical reference; exact bytes not inspected |
| Experiment 029 final manifest | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` | Historical reference; exact bytes not inspected |
| Experiment 029 270-event receipt tip | `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd` | Historical reference; all 270 links not replayed |

The arrows "EC-025 -> EC-026" and "Experiment 029 manifest -> event 270 tip" describe *reported intended lineage*. Cryptographic parentage must be established from the actual parent fields, serialized bytes, and complete receipt chain.

**Independently inspected Git object classes:** the public GitHub API returned identical contents and Git blob SHA `f6cf9d97ab2be5322336857b7624978acec75f51` for REIK_ROOT.md and `48dcfc22ce319d73c9b83d435eb6019597d05773` for the immediately prior missing-link research record, at inspection. Those 40-hex Git blob identifiers are **not SHA-256 of the original kernel**. A commit SHA references a Git commit object, while a 64-hex SHA-256 digest refers to the digest of specific bytes under SHA-256. Neither alone proves scientific validity.

The full chain requires original bytes; canonical encoding definition; chronological prev/next links; exact digest recomputation; input source attribution; independent checker output; and negative-control receipts.

### 6. Falsification matrix
The next experimental protocol should include at least:

| Test | Expected result | Why it matters |
| --- | --- | --- |
| sqrt(pi)/sqrt(pi) = 1 | PASS | Exact cancellation control |
| sqrt(pi) = 1 | FAIL | Reject invalid equivalence |
| x/x with x = 0 | UNDEFINED / reject | Domain guard |
| N(2) = N(sqrt(pi)) while 2 != sqrt(pi) | PASS | Demonstrates normalization loses identity |
| Missing independent Echo | HOLD | Prevent unsupported knowledge admission |
| Modified receipt payload with unchanged recorded hash | HASH MISMATCH | Detect byte mutation |
| Valid Git commit but unverified scientific theorem | HOLD | Separate version history from proof |

The sample tests are logical specifications, **not executed independent research certificates**. In particular, no claim is made here about replaying the user's 270-event receipt chain or four reported UNSAT certificates.

### 7. Independence and external proof checking
For mathematical formalization, a future fixed-version Lean source and imports could encode the proposed typed semantics and prove a correspondence theorem. Lean's documentation distinguishes kernel acceptance from whether a formal statement means what the author intended. For SAT/UNSAT work, externally sourced original-byte CNF instances and independently checkable proof certificates should be retained alongside the exact checker versions and outputs.

Scientific and cryptographic evidence must be independently corroborated when required. Model agreement, mirrored repository text, or a signature on a Git commit are not scientific Echo.

### 8. Reproducibility protocol
1. Obtain original immutable kernel bytes and rehash SHA-256; compare with the historical reference without editing them.
2. Obtain each claimed manifest in its exact archived byte form and recompute its own digest.
3. Read each receipt's canonical serialization and parent field, then independently recompute and replay every chronological link.
4. Write an explicit formal statement for the candidate three-state evidence semantics as a separate file; compare it line by line with the preserved kernel before claiming correspondence.
5. Run independent negative controls, evidence omission tests and contradictory-evidence tests.
6. Run pinned formal proof checkers and separately validate the meaning of the formal statement against the original informal claim.
7. Publish public-safe receipts and exact Git URLs. Keep private keys, sensitive records, and unavailable artifacts out of public repositories.
8. Remain at 0 · HOLD for any unestablished scientific, external execution or ledger claim.

### 9. Discussion and conclusion
The mathematical identity sqrt(pi)/sqrt(pi) = 1 is already fully determined within standard real arithmetic. **What is not determined is whether that normalization serves as an evidence-admission operator.** Lemma 1 shows why that inference fails without additional information: the map loses the identity of the numerator and denominator by collapsing every nonzero real input to the same output.

The strongest currently supported research statement is therefore a **formalization agenda**: model precisely what claim, evidence, independent Echo and falsification mean; preserve chronology and exact source bytes; and prove any desired correspondence separately. This retains the original REIK/TCGE kernel unchanged and keeps the distinction between verified mathematical facts and experimental hypotheses.

### 10. References and evidence record
1. Clarity public repository: [REIK_ROOT.md](https://github.com/eternalimit/clarity/blob/main/REIK_ROOT.md), inspected 2026-10-09; Git blob SHA `f6cf9d97ab2be5322336857b7624978acec75f51`.
2. Clarity research: [Exact Cancellation Lemma](https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-clarity-pi-exact-cancellation-lemma.md), previously committed and inspected.
3. Clarity research: [The Missing Link](https://github.com/eternalimit/clarity/blob/main/research/2026-10-09-missing-link-normalization-to-knowledge.md), Git blob SHA `48dcfc22ce319d73c9b83d435eb6019597d05773`.
4. NIST, *Secure Hash Standard (FIPS 180-4)*: https://csrc.nist.gov/pubs/fips/180-4/upd1/final.
5. Lean Language Reference, *Validating a Lean Proof*: https://lean-lang.org/doc/reference/latest/ValidatingProofs/.
6. SAT Competition 2026, *Output Format and Certificates*: https://satcompetition.github.io/2026/output.html.

### Preservation declaration
Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. No original kernel file changed or freshly rehashed. No private material included. A GitHub commit records this working paper; it does not constitute external proof, an on-chain transaction, scientific certification or wallet signature.
