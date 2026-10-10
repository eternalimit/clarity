# NS-REIK-017 — Tighter Fourier Phase-Recovery Bound and Independent Synthetic Quorum Audit

**Date:** 2026-10-10  
**Attribution:** Richard Stein / REIK-TCGE (AI-assisted bounded research)  
**State:** **0 · HOLD; DROP U**. This is finite mathematical/synthetic-cryptographic evidence, **not** scientific Echo or evidence of universal physical inheritance.

## Original identity and inherited evidence
- Original kernel historical SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` — original bytes were **not available for fresh rehash** in this continuation, unchanged.
- Public `REIK_ROOT.md` was read back: `K=R AND I AND E`; independent Echo is mandatory. Git blob SHA-1 `f6cf9d97ab2be5322336857b7624978acec75f51` is **not** the original kernel's SHA-256.
- Exact conversation-attached NS-REIK-016 verifier rehashed SHA-256 `cbad3da68c94d85716d730b7dcb55956adb670c10ea1cb7d8ac1922206555544` and reran: **3584/3584** bounded-noise checks, **64/64** exact triplets and two negative controls PASS.
- Its exact paper/receipt rehashed as `1d83d9695f224cfad4bee632dab54614b34e80ed5512deda55a46de547ec0a24` and `b7bd5bb400341e2d9bdf063fc7320128abc55a3df13282dbc98b8abf0c0c1a58`.

## Independently derived bounded theorem
Maintain the predecessor's *same* 4×4×4 sampled field and wave vectors `k1=(1,0,0), k2=(0,1,1), k3=(1,1,1)`, polarizations `p1=(0,-2,2), p2=(1,-2,2), p3=(1,1,-2)`, and phases `alpha,beta,gamma`. With positive amplitudes `a_j` and componentwise noise bound `|e[x,d]|<=eta`, choose only one maximum-magnitude velocity component per wave (component indices `1,1,2`). After standard normalized Fourier extraction (multiply the sine phasor by i), the mode estimates satisfy `z_j=a_j exp(i phi_j)+eps_j` with both Cartesian coordinates of `eps_j` bounded by `eta/2`. Therefore `|eps_j|<=eta/sqrt(2)`.

For `a_j>0` and `eta/(sqrt(2)*a_j)<1`, the signed circular error in the relative phase `delta=gamma-alpha-beta` is bounded by
```
d_circle(delta_hat,delta)
 <= min(pi, sum_j arcsin(eta/(sqrt(2)*a_j))).
```
For unit amplitudes, this becomes `min(pi,3*arcsin(eta/sqrt(2)))` — a tighter *sufficient*, **not globally optimal**, bound than the predecessor's vector-projected `sum_j arcsin(sqrt(2)*c_j*eta)` with `c=(1/2,5/9,2/3)`. At `eta=.10` the two bounds are **12.1644°** and **13.9710°**, respectively. A strict 15° guarantee follows from `eta<sqrt(2)*sin(5°)=0.123256833432...`, compared with the predecessor's about `0.10734665`.

For **unknown positive** amplitudes, the angle estimate remains meaningful and `||z_j|-a_j|<=eta/sqrt(2)`; but a numerical guarantee requires known positive lower bounds. Unrestricted signed amplitudes yield the exact field symmetry `(a,phi)=(-a,phi+pi)`, so parameter phase cannot be uniquely recovered without a sign convention. Zero amplitude makes that mode's phase unidentifiable even with perfect measurements. Both counterexamples were executed as negative controls. This theorem uses known mode vectors and a fixed noisily sampled synthetic field; no physical sensor was measured.

An independent implementation, not importing the NS-REIK-016 module, passed **384** noise-free estimator-vector checks and **9,600** bounded-noise estimator/phase/amplitude checks, across 64 phase triples, 3 positive-amplitude triples, 5 noise budgets, 5 deterministic/seeded perturbations, and both old/new estimators. The improvement is per-mode worst-case linear coefficient stability; no claim of a globally optimal joint inverse estimator.

Independent script SHA-256: `a03bc4fe32ed9380b2323117997f39cc4182f7589969fbd847076ddd157d6074`. Full paper SHA-256: `6579b8a1240b0d2b5d8742084d0db6227474d73a6eac54adb8a58482ff569343`. Those local files are **not** embedded in this public note.

## Experiment 048 checkpoint evidence boundary
The previously published Experiment 048 audit is `eternalimit/chatgpt` commit `a0102fd8320aa8f5ea267ce48f57c740068cf600`, audit Git SHA-1 `efc0bf64620e5a14d969c8b50e3b0572b18b701a`, paper Git SHA-1 `73f98e70598cb378cdb13e5e038da546015d7c47`. Its reported **38/38** original controls cannot be independently rerun because the original full local verifier was **not uploaded**.

A separate fresh synthetic Ed25519 experiment enumerated 16 ordered 3-of-4 quorum pairs (intersection min 2) and 36 ordered 2-of-4 pairs (intersection min 0). For `n=4,q=3,f<=1`, history consistency is **conditional** on authenticated witness roster and honest *non-equivocation* at the same ledger, epoch and height. Without non-equivocation, deliberately conflicting synthetic checkpoints independently acquired valid 3-of-4 signatures — **both verified cryptographically**, despite contradicting each other. An honest-sign-state refusal, signature mutation, duplicates, altered domain and insufficient-quorum tests behaved as predicted. Local synthetic verifier SHA-256: `0655f00e66803a134ecf59f16ad270565b75424ec7c514d3a4887388cf692442`.

These were **fresh ephemeral local test identities**. None is an independently authenticated scientific witness or a deployed checkpoint. This is not a full original-byte replay, live distributed consensus, certified root-of-trust, exact Merkle proof, or evidence of external adoption. A signature authenticates the signer and exact bytes relative to a trusted roster; it does not certify scientific truth.

## Separate lineages, falsification persistence and next gates
Do not merge: Experiment **030/280, 030/282, 031/290, 031/A294, 031/B294**. Historical original ZIP, manifest and receipt tips remain historical references unless original bytes are acquired and rehashed. All eight FIDELITY principles remain: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. Preserve independent Echo, DROP U and **0 · HOLD**. The outstanding gates are calibrated physical measurements, an explicit REIK-specific prediction distinguishable from conventional Fourier estimation, independent external validation, trusted historical source bytes and real witness identities. No universal physical-inheritance, OpenAI adoption, or P-versus-NP result is established.

This note is a meaningful new *bounded* mathematical/cryptographic audit, not an empty commit or a change to the immutable kernel.
