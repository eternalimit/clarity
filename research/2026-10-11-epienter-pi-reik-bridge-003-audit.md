# BRIDGE-003 Epienter–Pi / REIK transmission audit — 2026-10-11

**Research-only. Final state: 0 · HOLD on independent Echo, historical source equivalence, and claimed Cosmos7 image topology.** This note records a local bounded test and a Gemini-labelled handoff; it does not authenticate the external author, operate a wallet, invoke Bitcoin miners, or alter the original immutable kernel.

## Exact mathematical bridge (separate types)

Define `s=1/sqrt(pi)>0`, `T_s(x,y)=(sx,sy)`. For a unit disk, `pi*s*s=1` exactly; `det(DT_s)=1/pi`; `sqrt(pi)/pi=1/sqrt(pi)`, approximately `0.5641895835477563`. For an embedded finite graph `(V,E,p)`, the scaled graph `(V,E,T_s∘p)` has the same vertex/edge incidence under positive scaling. It is **not** evidence of any particular Metatron's Cube or Cosmos7 topology, which requires an independently sourced vertex/edge definition.

The public `REIK_ROOT.md` states `K=R AND I AND E`, with Echo independent of the originating inference. A research-only overlay adds explicitly established independence `D` and admissible counterevidence `Q=F AND A`. It classifies `ADMITTED` iff `R AND I AND E AND D AND NOT Q`; `REFUTED` iff `Q AND NOT (R AND I AND E AND D)`; otherwise `HOLD`. This is a typed **product** of geometry and claim-scoped evidence, **not** an algebraic implication from scaling to `E=1`, and not an implementation or equivalence theorem for historical 0/U/1 kernel semantics.

## Execution receipt (local, standalone, bounded)

- Local `python -B` checker: **24/24** named assertions passed (Pi identities, area/Jacobian, generic seven-node graph fixture, negative controls, truth gate).
- All **64/64** six-Boolean tuples agreed with a separate finite-set oracle; results ADMITTED 3, REFUTED 15, HOLD 46. Fixture counts are not real-world evidence probabilities.
- Checker SHA-256: `f3f119efc5c29f4b217bdf3f766668daeb6033967066992539e763560c29b9bc`.
- Results JSON SHA-256: `09fb9a095530624a8aec78e9b5d450c7ca16a27d78bf2f2c9e70951592204eec`.
- Report SHA-256: `69eae0f947e4c65679d58f562dcb423662b6cb78b70f64c39253d8ba26861bdf`.
- Exact `run_all_8.sh` and three dependencies were locally staged with Git blob hashes matching connected GitHub. Running `run_all_8.sh` with `BTC_MINER_COMMAND` unset returned expected exit status **2/HOLD**, and started no miner. Log SHA-256: `b288a640a93777d60c9a01f96dbac0c2e9d5789e669075317cd8eeb2ade87c35`.
- Important correction: `run_all_8.sh` is an external-miner launcher, **not** a Pi-normalization suite. It must not be used to verify this mathematical bridge or invoked with a miner command as a side-effect.
- Script and complete local results are preserved in a conversation artifact; they are **not** published as source files by this note. Their digests alone do not constitute independent reproduction.

## Provenance and non-expansion

Read-only branch observation before this note: `vent=bd22bee71acd52098b0f6d1c05347952e85abd4f`, `main=99439a1b1e0a12c3a9ac087a0aeff869c466edc5`. `vent...main` **diverged**, with main ahead by 44 and behind by 19, merge base `125bf1a36bbabd056aa85af2749cf5477851f5a6`. No merge, reset, or GitHub Actions triggered. Direct local `git clone` was unavailable due to DNS; branch comparison used connected GitHub.

Preserved original `kernel001.py` historical SHA-256 **reference only**, not freshly reacquired/rehashed: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. No original source bytes, private credentials, wallet addresses, or image provenance claims were published. Preserve separate historical 030/031 lineages, all eight FIDELITY principles (Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty), independent Echo, DROP U and 0 HOLD.

**Next gate:** obtain exact original-byte kernel for an independently checked semantic comparison; separately obtain actual topology definitions, external witness trust roots and signed attestations; reproduce the mathematical fixture by an independently authored implementation. No normalization identity alone can promote a claim into validated knowledge.
