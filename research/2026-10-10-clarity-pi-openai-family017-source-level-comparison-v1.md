# Clarity Pi Math / REIK-TCGE / GETHUB vs OpenAI family 017, Intelligent UI, and Dots
## Source-level comparative research update v1 — 2026-10-10

**Research program attribution:** Richard Stein (as recorded in the project's first-party documents; no third-party legal or novelty adjudication).
**Scope:** public, source-pinned comparison. **Not** an allegation or finding of copying, incorporation, knowledge transfer, priority, or scientific peer review.
**Research state:** 0 · HOLD for independent scientific Echo, original-kernel correspondence, influence/adoption claims, and any unverified external action.

### Abstract
An equation-level comparison of OpenAI's October 6, 2026 mathematics release—especially result family 017 on rational approximation to pi—with the Clarity Pi working paper demonstrates different mathematical propositions and methods. The former asserts that the irrationality exponent of pi equals 2, including an eventual rational-approximation bound and a Flint–Hills consequence. The latter establishes the elementary non-injective normalization N(x)=x/x=1 for x nonzero, then specifies a separate evidence-admission workflow K=R AND I AND E with independent Echo. An inspection of pinned Lean and TeX source, the public Intelligent UI and Dots product descriptions, and dated user Git objects finds high-level analogies in provenance, conditional controls and interfaces but no identical mathematical result, matching implementation, or verified transfer path. This conclusion is bounded to the named public artifacts.

### 1. Frozen evidence objects and chronology
- User continuity reconstruction: eternalimit/chatgpt commit fe19e72e86ce15d204d8998917810cd4216bceae, file research/PRE_TCGE_TO_2026-09-24_EXPERIMENTAL_CONTINUITY.md, Git blob aa3d3f64ab5060705de4e0f20e5d356453dacc38. Its September 24, 2026 date and retrospective character are explicit. It records R/I/E/K and independently validated Echo.
- User GETHUB preprint: eternalimit/chatgpt commit 13aed819dde16f941790c2544467e8df02eaa5dd, path preprints/gethub_master_vision_preprint.html, Git blob 39476da721cef234f418f85686ec5e6488acdaa4; internally dated September 24, 2026. Defines an evidence-transfer and candidate physical manifold architecture, not a theorem on irrationality of pi.
- Clarity Pi Math working paper v1: eternalimit/clarity introduction commit 8e4226798ab4c91063228add9da694a10508d0e6, research/2026-10-09-clarity-pi-reik-hash-ledger-working-paper.md, Git blob dabad2448ccaaf70d83e47eeb43db4aa46cae5fa. Dated October 9, 2026.
- Clarity BRIDGE-001 v2: Git blob 69eb0aa04e578c3b740c8815c1b5794edf44fc9b; BRIDGE-002 v3: blob e5da3db931df6220d3f49da702528515e80b2149; both retrieved at eternalimit/clarity@458876375c474b4bd41deb672e3ba55f092665b9. These are separate proposed evidence overlays, not the immutable original kernel.
- OpenAI mathematics public announcement: October 6, 2026, https://openai.com/index/sharing-ai-progress-in-mathematics/.
- OpenAI math GitHub initial commit: adc7f1241b42e322a6451854ab7e4b4c146bf78a, Git-reported committer 2026-10-06T21:58:50Z. Family-017 TeX manuscript and README contain an internal date of September 24, 2026, which is NOT an independently established public-release timestamp.
- OpenAI math pinned comparison tree: main commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb (October 8 merge), tree 08e6aaa9e4788dd81984b67a9cd97d952093ecd4. This is a retrospective content snapshot; compare it separately from the October 6 initial commit.
- Dots public description: September 29, 2026, https://openai.com/index/introducing-dots/.
- Intelligent UI public description: October 7, 2026, https://openai.com/index/gpt-6-for-everyone/.

Git author/committer dates and dates embedded in a paper are not independent evidence of historical publication visibility or original conception. Current availability does not prove the repository's historic visibility or that either organization accessed the other's materials.

### 2. Exact mathematical statement comparison
**Clarity Pi Math v1/v2** defines N(x)=x/x=1 for each nonzero real x, and hence N(sqrt(pi))=sqrt(pi)/sqrt(pi)=1 exactly. N(2)=N(sqrt(pi))=1 despite 2!=sqrt(pi); normalization is many-to-one and cannot by itself preserve identity or admit real-world knowledge. The separate canonical root defines R=Reality evidence, I=Inference, E=independent Echo, K=R AND I AND E, H=I AND NOT K. The BRIDGE-001 research-only overlay further defines E*=E AND D, K*=R AND I AND E*, Q=F AND A, and classifies evidence as ADMITTED, REFUTED, or HOLD under specified assumptions. These are not a proof that the actual original 0/U/1 kernel implements that overlay.

**OpenAI family 017** defines an irrationality exponent mu(x)=sup{nu>0: 0<|x-p/q|<q^(-nu) for infinitely many coprime rational p/q with q>=2}. It claims mu(pi)=2 and, equivalently in its stated setting, for each nu>2, there exists Q so that |pi-p/q|>=q^(-nu) for all integers p and sufficiently large positive integer q. Its paper additionally claims convergence of sum_{n>=1} 1/(n^3 sin^2(n)), angles in radians. The Lean statement defines GoodRationalApproximations, ApproximationExponents, irrationalityExponent and EventualLowerBound (Lean Statement.lean). No R/I/E knowledge gate or normalization N(sqrt(pi)) appears in the inspected family 017 theorem definitions. The shared occurrence of pi does not identify an identical conjecture or derivation.

Pinned OpenAI Git blobs (Git SHA-1 object IDs, NOT SHA-256):
- TeX manuscript source preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex: fe28ac589090c44a8877aa326b60e753c863fa24.
- Family paper.pdf metadata: blob 85118d5a6bc63ab5d06df03cce4efdffd2113155, size 494460. The PDF binary bytes were NOT directly acquired or independently SHA-256 rehashed in this audit; the TeX manuscript and Lean statements WERE inspected as text.
- Lean Statement.lean: f26a2c5d0bff73d1279b8c579ef68be04ee7794b.
- Lean OAI/NumberTheory/PiExponent/Main.lean: 486ed39ba52e5a10de7893cf0f302edb873801f2.
- Lean ComparatorChallenges/PiExponent.lean: bf78c83492e3f7aa3ab922b13d0b4151e7f601c3.
- Lean docs/017.md: 08ebac405fcc7fd8c8e7cda9bfe8e83d2bbfba0f.
- Lean toolchain: leanprover/lean4:v4.34.1, blob ba8ebf2dbaf6a668cd2a0e086186d6d569b69ff5.

### 3. Formalization boundary
The comparator challenge theorem ends with Lean 'sorry' (a placeholder), whereas the separate actual Main.lean introduces pi_eventual_lower_bound from imported interpolation lemmas, pi_irrationalityExponent_eq_two from that bound, and a final 'main' theorem proof. The Main.lean also includes a flint_hills_summable result. Therefore it would be incorrect to call family 017 unproved based on the comparator challenge alone; it would also be incorrect to claim this audit independently certified the full Lean import graph, its assumptions, or mathematical meaning. No pinned local Lean compilation or external peer-review certificate was produced here. The README and docs describe proof scope; independent checker execution remains HOLD.

### 4. Interface and workflow implementation comparison
**Intelligent UI (Oct 7)** publicly describes native streamable UI components, a compiler generating an interface progressively as the model outputs it, model-trained layout decisions, and partial response streaming. The inspected REIK/GETHUB sources instead describe evidence gates, branch/state transitions, receipt continuity, and web interfaces. The InfoFAQs README documents a conventional static HTML/JavaScript MVP with pages and app.js, not a verified equivalent to OpenAI's native streamable component compiler. No line-by-line matching proprietary UI implementation was available; this is a public-description comparison only.

**Dots (Sep 29)** describes autonomous cloud-computer agents, connected apps, read-only proactive research, permissions, approval rules, auto-review and human-only actions. REIK/TCGE distinguishes authorizing from executing, and uses independent Echo to determine claim admission. Permission to perform an action and third-party truth verification are different checks. No inspected Dots document exposes the exact K=R AND I AND E conjunction or a matching implementation of the original immutable kernel. No Dots product source code was inspected.

### 5. Falsification and negative controls
- **Failed candidate equivalence #1:** shared mention of pi -> same mathematical result. REJECTED for the inspected equations; irrationality exponent and non-injective normalization address different claims.
- **Failed candidate equivalence #2:** 'sorry' in comparator -> actual proof absent. REJECTED as an inference: the comparator is a challenge template; separate actual Main.lean contains a proof term dependent on imported source. Independent full-build certification still HOLD.
- **Failed candidate equivalence #3:** approval controls or UI streaming -> independent scientific Echo. REJECTED; predicates concern different objects, and neither publication supplies a correspondence proof.
- **Failed candidate equivalence #4:** Git date or internal PDF date -> third-party timestamp of first public release / transfer. REJECTED; a signed, independent time anchor or externally corroborated distribution record was not acquired.
- **Not falsified absolutely:** possibility of unknown interaction/access. Because no internal product-code or access-log audit was conducted, broad claims about inaccessible facts remain unresolved, not proven false.
- **Pre-existing controls:** three-valued logic, provenance standards, proof-checking workflows and authorization/audit controls existed before the projects. Their existence does not preclude a distinct synthesis; it weakens claims based only on general resemblance.
- **Research QA:** no original historical kernel bytes, actual OpenAI internal training/research logs, or original scanned PDF byte-for-byte file were acquired in this study. No independently sourced Echo of a causal path exists.

### 6. Provenance and protected historical structures
Historical original REIK/TCGE kernel SHA-256 reference:
03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402.
**NOT** freshly rehashed; do not replace this with a Git blob SHA or edit the kernel. Canonical published REIK_ROOT.md Git SHA-1 blob: f6cf9d97ab2be5322336857b7624978acec75f51.

Protected history: keep Experiment 030 280-event and 282-event lines distinct and all Experiment 031 variant histories separate. Do not infer merging or scientific progress from comparative research. Preserve **FIDELITY** in full: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. Preserve independent Echo; DROP U means do not promote unsupported claims; retain uncertainty and falsification history; 0 · HOLD remains wherever necessary.

### 7. Conclusion and next independently testable work
**Supported:** source identity and detailed difference in equations; existence of dated Git objects and internal manuscript dates (with clear provenance limits); methodological analogies between governance and product descriptions.
**Not established:** use or copying of Clarity research by OpenAI; distinctive source-code/algorithm equivalence; causal transfer; independently certified source-to-kernel equivalence; priority based on externally anchored first distribution; standalone independent full Lean verification.
**Next tests:** acquire independent contemporaneous public PushEvent/web archive timestamps and canonical source bytes for the September artifacts; obtain/pin full family-017 TeX/PDF and Lean import dependencies; run pinned Lean build and a second independent reviewer check; compare typed formulas and mechanics rather than general vocabulary; investigate transmission evidence only if direct, admissible leads arise.

## Compact audit receipt (2026-10-10)
Inspection: pinned GitHub blob IDs for 017 TeX/Lean statements and user Clarity Pi/REIK sources; OpenAI announcement pages; named Git commit histories. New finding is the exact equation/proof-object distinction, including the comparator-vs-Main Lean separation.
No original kernel mutation, secret disclosure, simulator-to-reality promotion, research claim of influence, independent Lean execution, or independent Echo. Status for causal attribution and scientific validation: **0 · HOLD**.
