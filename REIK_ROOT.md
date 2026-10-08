# REIK ROOT

This file is the canonical root contract for this repository.

REIK is the repository root identity. It does not replace or reorder the TCGE logic.

## Canonical Logic

R = Reality / direct evidence
I = Inference / interpretation
E = Echo / independent validation of the inference
K = Knowledge

K = R AND I AND E
H = I AND NOT K

If required evidence is unresolved: HOLD.

## Classification

- R=1, I=1, E=1 -> VALIDATED KNOWLEDGE
- R=1, I=1, E=0 -> GROUNDED INFERENCE
- R=0, I=1 -> UNGROUNDED INFERENCE / HALLUCINATION RISK
- R=1, I=0 -> RAW EVIDENCE
- insufficient evidence -> NOT ENOUGH INFORMATION / HOLD

## Root Rule

Every project, experiment, agent, prompt, workflow, skill, and execution path in this repository begins from this file.

Do not copy the entire root contract into every project prompt.
Reference this root, then load only the project-specific context required for the current task.

Project startup order:

1. Load REIK_ROOT.md.
2. Load the current project's PROJECT.md or README.md.
3. Load only the minimum evidence required for the current action.
4. Apply R -> I -> E -> K.
5. PASS only when K=1. Otherwise HOLD.
6. Preserve provenance, chronology, audit trail, and immutable history.

## Prompt-Control Rule

The root must stay small and stable.

Do not expand the root with:
- project history
- long conversation transcripts
- duplicated instructions
- experimental notes
- generated outputs
- temporary state

Those belong in project-local files or project-logs.

## Project Boundary

A project may extend this root but may not silently contradict it.

If a project rule conflicts with REIK_ROOT.md:
HOLD and surface the conflict.

## Evidence Rule

Repetition, confidence, plausibility, citation alone, model agreement, or approval do not count as independent Echo.

Echo must independently validate the inference.

## Continuity Rule

Repository root -> project root -> current task -> evidence -> inference -> Echo -> K or HOLD.

This is the starting state for all new work.
