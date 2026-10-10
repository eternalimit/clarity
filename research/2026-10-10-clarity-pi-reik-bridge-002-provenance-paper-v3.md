# BRIDGE-002: Provenance Independence, Equivocation, and Evidence-State Admission

**Research stream:** Clarity Pi Math / REIK-TCGE  
**Date:** 2026-10-10  
**Research attribution:** Richard Stein, project/research attribution only  
**Version:** 3.0 (BRIDGE-002 follow-on to BRIDGE-001)  
**Status:** FINITE SYNTHETIC TESTS PASS; ORIGINAL-KERNEL CORRESPONDENCE **0 · HOLD**  
**Parent GitHub checkpoints:** `eternalimit/clarity@b194306b1afeb14a057ad8667b1f170122f6c098`; `eternalimit/chatgpt@9d21a4e6a508ba5c375f9589ac573e588bd7fda7`

## Abstract

This study evaluates adversarial evidence controls for an **external, research-only** admission overlay inspired by the public Clarity `REIK_ROOT.md` gate `K = R AND I AND E`. The new protocol models claim-scoped receipt hashes, a synthetic trusted-anchor registry, independently attributed witness roots, witness aliases, chronology, replay prevention, falsifier conflict, revocation, and equivocation. A local Python harness passes 41 defined controls; an elementary Boolean reference table agrees on all 64 assignments; and an additional supplementary sweep of 4,144 input-order evaluations found no order-dependent **verdicts in its tested fixture subset**. During development, a genuine order-of-processing counterexample was discovered, documented, and corrected. None of these results constitutes actual independent Echo: all witness names, controller relationships, and anchor records originate within the same synthetic implementation. No existing REIK/TCGE kernel was modified, recovered, executed, or source-byte-verified.

## 1. Exact lineage recovery and non-expansion

Both stipulated parent commits were fetched by full SHA and each one-parent relationship was confirmed. At those refs, the following paths were read in full and their Git blob IDs matched across both repositories:

| Source | Git blob SHA-1 |
|---|---|
| `REIK_ROOT.md` (Clarity only) | `f6cf9d97ab2be5322336857b7624978acec75f51` |
| BRIDGE-001 paper v2 | `69eb0aa04e578c3b740c8815c1b5794edf44fc9b` |
| BRIDGE-001 executed Python | `107a80524c3cbd93d1db09d5238519786e44bd1c` |
| BRIDGE-001 result JSON | `f8542b12aa910f069bf3857f10007d5e56db7cbd` |
| BRIDGE-001 continuity receipt | `8ea04fd38cdcea63446e3283ebcec15f72ed8a92` |
| Standing prompt-commit policy | `812b4ecac14d7ec0991b017313341314b01ce8f1` |

The exact local BRIDGE-001 source and JSON from the previous session were rehashed against their previously published SHA-256 digests and `git hash-object` identifiers, and the 64-case/9-control baseline replayed. Git SHA-1 blob IDs are not SHA-256 hashes of the original REIK kernel.

Library and GitHub text searches found reports referring to an original `kernel001.py` and a historical length of 4,299 bytes, but **not a retrieved exact 4,299-byte source file with an independently matching SHA-256**. Code-search and Library-search nonmatches do not establish nonexistence. Correspondence to the original kernel is withheld.

## 2. Established identity, still no Pi-to-evidence shortcut

For a nonzero real `x`, `N(x)=x/x=1` is exact. In particular, `sqrt(pi)/sqrt(pi)=1`, while `sqrt(pi) != 1`. Normalization is non-injective. It loses input identity and does not prove independent evidence for an arbitrary proposition. The REIK root gate concerns admission of knowledge based on Reality, Inference and independent Echo—not the numerical identity `1`.

The historical protected 0/U/1 kernel may be a partial-assignment evaluator, according to earlier descriptions; its **actual semantics cannot be re-established from those descriptions alone**. No 0/U/1 truth-table replacement, source-level proof, or kernel implementation was generated here.

## 3. BRIDGE-002 proposed evidence model (research only)

Each synthetic evidence record contains: event identifier, source, claim, disposition, challenge, issue and expiry times, an asserted-independence flag, and an SHA-256 digest of a deterministic JSON encoding (digest field excluded). A fixture-only trusted registry maps a source to its controller, root and derivation lineage. A distinct fixture-only anchor set records expected byte digests.

The test proceeds conservatively:

1. Recompute and compare record digest, and require membership in the assumed anchor store.
2. Check event scope, challenge, chronology, expiry, and revocation.
3. Compare controllers, roots and derivation lineages with the originating inference; reject re-labeled self-Echo or shared lineage.
4. Count at most one qualifying witness identity per controller/root/lineage independence relation, with an optional, **noncanonical** stricter two-root quorum.
5. Fail closed on contradictory anchored dispositions from one identity or different anchored hashes using one event ID.
6. Classify supporting and admissible contradicting evidence: support only -> ADMITTED; refutation only -> REFUTED; neither or both -> HOLD.

These are **policy assumptions inside synthetic test fixtures**, not externally established authenticity. In particular, an SHA-256 digest proves neither signer identity nor that a signature or independent trust root exists. The claimed `asserted_independent` Boolean cannot override the registry/lineage checks. A model generated registry and anchor store cannot count as independent scientific Echo.

## 4. Falsification and bug persistence

### Discovered failure — record-order collision

The initial harness marked an event identifier as consumed **before** checking digest and anchor eligibility. An unanchored record using the same identifier could therefore suppress a legitimate record if placed first. The observed order-dependent example was:

- authenticated-by-fixture record then unanchored collision -> ADMITTED;
- unanchored collision then legitimate record -> HOLD.

Here “authenticated-by-fixture” refers *only* to the predeclared anchor list, not to an actual cryptographic signature. This is a real counterexample **to the draft test implementation's order independence**, not to the original REIK kernel.

### Correction and retest

Move duplicate-accounting after eligibility checks, add deterministic preflight detection of conflicting anchored event identifiers and conflicting stances under the same modeled witness identity, and rerun controls. The final script reports **41/41 passing** local checks, including both collision orders, two source-equivocation orders, and six permutations of an independent-positive/conflicting-negative fixture.

A separate supplementary sweep tested all permutations of 2-, 3-, and 4-element subsets from eight fixture records at one- and two-witness policies: **4,144 evaluations, zero order-dependent verdicts**. This is a bounded finite observation, not a general order-independence theorem over all possible inputs. More complex partially overlapping controller/root/lineage graphs need further tests.

The original failure is retained as a falsification finding; the correction does not erase it.

## 5. Execution receipts and hashes

Local Python 3 and SymPy were used. The final BRIDGE-002 result JSON reports:

- 41/41 named test cases passed;
- 64/64 Boolean reference-table cases passed;
- fixture-reported ADMITTED, REFUTED and HOLD behavior follows the *proposed* policy under its assumptions;
- all external-world evidence, independent witnessing, source-kernel correspondence and 270-event historical replay remain unverified.

**Exact locally executed source-byte SHA-256:**

`e8b0072a946a3b596d481f26ab8ddc50532855635af5acea28f45fb9b1b39066`

**Exact final JSON result SHA-256:**

`05124e340ddc19959eb52c314dbf00b6e8524c4499ed3433166c5abf49136820`

The exact source and JSON results are archived in each GitHub repository as reversible gzip-compressed, Base64-encoded **text**:

- `research/experiments/bridge-002/adversarial_echo_check.py.gz.b64` — Git blob SHA `a35d169581ebda95d3851d27714f8c1e93740aa3`; original source 12,625 bytes.
- `research/experiments/bridge-002/bridge002_results.json.gz.b64` — Git blob SHA `892b3c2e233fa2e917faba4b6b010ad8a67bcae7`; original JSON 11,024 bytes.

Their Git blobs matched local compressed/Base64 files byte-for-byte (including Base64 with no trailing newline).

Decode reproducibly from a checked-out repository:

```bash
base64 -d research/experiments/bridge-002/adversarial_echo_check.py.gz.b64 | gzip -d > /tmp/adversarial_echo_check.py
base64 -d research/experiments/bridge-002/bridge002_results.json.gz.b64 | gzip -d > /tmp/bridge002_results.json
sha256sum /tmp/adversarial_echo_check.py /tmp/bridge002_results.json
python3 /tmp/adversarial_echo_check.py
```

The decoded SHA-256 digests must match the two original source-byte references above. Execute only within a trusted, isolated environment. The script includes no actual network connections, wallets, crypto-key material or external witness credentials.

## 6. Limits and necessary independent Echo

A registrar-controlled synthetic source list cannot establish that controllers are genuinely independent. To raise the evidence level, the research needs verified external identity and independent trust-root acquisition; publication of immutable original payloads; actual cryptographic verification where applicable; independent observational sources; reproducible tests by different operators and implementations; and longitudinal non-equivocation checks with durable checkpoints.

The demonstration is a controlled experiment in **evidence admission software**, not validation of a new physical or mathematical theory and not a Lean proof. An output of UNSAT for a finite Boolean proposition would not supply a SAT Competition proof certificate, the historical REIK source equivalence theorem, or a Millennium Prize result.

## 7. Historical SHA-256 reference structure — unchanged and HOLD

| Category | Historical asserted SHA-256 (not rehashed from exact original bytes here) |
|---|---|
| Immutable REIK/TCGE 0-U-1 kernel | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` |
| EC-025 manifest | `c7d121fde0e2f7c827ee78805181c9adcaf1a8b41910d3f692a656a38e489835` |
| EC-026 manifest | `bfc9d82285e7dc4934115d0c28153b18e1cedee27144a32ca4e93b03bf5a380e` |
| Experiment 029 manifest | `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78` |
| Experiment 029 270-event receipt tip | `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd` |

Source bytes were not acquired and receipt links were not replayed. No original archived kernel was altered. Only new research experiment files and public-safe notes are added.

## 8. BRIDGE-003 falsifiable next steps

1. Attempt independently sourced acquisition of the **exact, immutable original kernel001.py bytes**. Verify 4,299-byte claim, SHA-256 and chronology; do not reconstruct missing source text and call it original.
2. Formally define a typed abstraction map between the *actual original kernel semantics* and the external evidence overlay. State proof obligations; use a proof checker only when runnable and pinned.
3. Add fixture sets with partially overlapping controller/root/lineage graphs and test order independence exhaustively over those bounded domains; fail closed when transitive independence cannot be established.
4. Obtain real independent witness attestations from separately controlled providers. Validate signatures, proof origins and time/claim scope without self-attestation.
5. Preserve contradictory evidence and revoked checkpoints in an append-only chronological audit. Record rollback detection separately.
6. Rehash independently acquired EC-025, EC-026 and Experiment 029 original manifests and replay the full event history **only when exact bytes are available**.

## 9. FIDELITY and outcome

**FIDELITY:** Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. **DROP U** means do not promote unresolved evidence; **0 · HOLD** remains for missing source bytes or independent attestations.

**Conclusion:** BRIDGE-002 establishes a reproducible finite synthetic adversarial test result and an explicitly preserved implementation falsifier. It does not establish independent Echo, original kernel correspondence, historical chain verification, a cryptographic signature, or external execution.
