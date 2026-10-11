# Read-only source-structure method (executed 2026-10-11 22:33 UTC)

Input: `openai/NavierStokesAndEuler` commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, files `NavierStokes/R3/PressureFlux.lean` and `NavierStokes/R3/WholeSpaceUniqueness.lean` through the connected GitHub file reader.

1. Split `PressureFlux.lean` into lines; extract lines 576-599 (inclusive, 1-based).
2. Assert the extracted source contains all five literal/regex patterns: `theorem exists_uniform_actual_pressure_flux_bound`, `cutoffL6 (ComparisonCutoffs.cutoff R) (u - v) t`, `dissipationRoot (ComparisonCutoffs.cutoff R) (u - v) t / R`, `R ^ (-(7 / 4 : ℝ))`, `∀ R : ℝ, 1 ≤ R → ∀ t ∈ Ioo 0 T`.
3. For each mutation, rerun the **same gate**, expecting rejection: replace the dissipation expression with `0`; replace all local L6 expressions with `0`; change `7 / 4` to `7 / 3`; rename the theorem. All four rejected.
4. Check the caller file contains `PressureFlux.exists_uniform_actual_pressure_flux_bound`.
5. Compare UTF-8 text returned by `fetch_file` with raw URL fetched via the same GitHub connector; equal. Compute SHA-256 of connector-decoded text using a pure-JavaScript SHA-256 implementation tested on empty string, `abc`, and quick-brown-fox vectors (3/3).

Observed: 5/5 positive patterns, 4/4 mutation rejections, caller invocation present, two text reads equal. The source gate is a *syntactic* admission check, not a mathematical or Lean proof check. No shell command or process exit code applies to the JavaScript connector execution. Separately, an attempted curl original-source acquisition exited code 6 (DNS failure).
