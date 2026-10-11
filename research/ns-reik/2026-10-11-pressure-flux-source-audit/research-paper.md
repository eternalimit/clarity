# NS-REIK bounded source audit: pressure-flux equation (10.19)

Date: 2026-10-11 22:33 UTC. Owner/research project: Richard Stein. This is a public-safe source-comparison supplement, **not** a new numbered NS-REIK experiment, a Lean proof check, or a proof of the Navier–Stokes Millennium problem.

## Question and falsifiable comparison

Does the pinned Lean declaration cited for the pressure-flux estimate have the same *stated bound* as equation (10.19) in OpenAI's 166-page natural-language manuscript?

Primary manuscript: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf, printed page 123 / PDF page index 122, equation (10.19). Let B_R denote the local L6 quantity. The manuscript states, schematically (suppressing the left-side flux integral),

    |flux| <= C_T R^(-1) [(B_R+1) B_R^(1/2) + R^(-3/4) B_R^(3/4)].

Pinned Lean source: https://github.com/openai/NavierStokesAndEuler/blob/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/R3/PressureFlux.lean#L574-L598

The declaration `exists_uniform_actual_pressure_flux_bound` (lines 576-598) has an RHS structurally of the form

    CP * ((B^(1/2)+1) * (D/R + 1/R^2) + R^(-7/4) * B^(3/4)),

where B is the Lean `cutoffL6` expression and D is `dissipationRoot`. The displayed Lean bound contains a dissipation term not present explicitly in the manuscript's (10.19) bound; its first summand is therefore structurally different. We have NOT established that B exactly equals B_R or D exactly equals A_R without a full definition-level proof. Nor have we established that one bound implies or contradicts the other under the respective hypotheses.

The pinned caller `NavierStokes/R3/WholeSpaceUniqueness.lean`, lines 60-61, invokes `PressureFlux.exists_uniform_actual_pressure_flux_bound`. This makes the cited Lean declaration relevant to the formal uniqueness route, but not a complete semantic audit of all dependencies.

An independent October 6, 2026 preprint (Bastounis, Circelli and Hansen, arXiv:2610.08144v1) reports the same category of mismatch; this run inspected the manuscript and pinned Lean source rather than adopting the preprint's conclusion as a proof.

## Executed source-admission check

The connected GitHub source reader fetched the pinned `PressureFlux.lean` and `WholeSpaceUniqueness.lean`; the first was fetched a second way through the raw-file reader and text compared equal. A read-only JavaScript source-structure gate checked 5 predicates (declaration identity, local L6 factor, dissipation term, R^(-7/4), uniform R/t quantifiers) and rejected 4 targeted mutations (remove dissipation, remove local L6, change radius exponent, rename theorem). Positive 5/5, mutation 4/4; cross-file invocation present. The SHA-256 implementation used for connector-decoded text passed 3 standard known-answer vectors. See method and manifest. No Lean, nanoda, SAT solver, or mathematical proof checker was run.

## Limits, falsification, and forward gate

This is a **source-level statement comparison**, not an independent formal proof or a refutation of OpenAI's final mathematical theorem. The original manuscript PDF could be read through a web PDF text view but could not be downloaded as original bytes (DNS blocked). SHA-256 reported for Lean is of UTF-8 text returned by the connector, not an independently acquired signed source archive. Source from two GitHub routes is not independent trust-root attestation. The repository's original REIK/TCGE kernel was not read or modified. External independent Echo is absent; `K = R AND I AND E`, `E=0`, `DROP U`, `0 HOLD` remain.

Next evidence gate: acquire and hash the original manuscript PDF bytes and a fixed-version source archive independently, audit definition equivalence for `cutoffL6` and `dissipationRoot`, then seek independent mathematical review or Lean/Comparator/nanoda execution with exact toolchain hashes. Preserve all eight FIDELITY principles (Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty). No SAT/NS lineage merge, no influence/ownership/legal claim, no wallet/deployment action.
