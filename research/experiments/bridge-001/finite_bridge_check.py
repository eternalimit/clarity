#!/usr/bin/env python3
"""Research-only finite model checks; does NOT implement or replace the REIK/TCGE kernel."""
import hashlib
import itertools
import json
import platform

import sympy as s
from sympy.logic.inference import satisfiable


def proposed_gate(r, i, echo_reported, independent, falsifier_reported, falsifier_admissible):
    """Proposed external evidence overlay; booleans mean genuinely established predicates."""
    knowledge = r and i and echo_reported and independent
    refutation = falsifier_reported and falsifier_admissible
    if knowledge and not refutation:
        return "ADMITTED"
    if refutation and not knowledge:
        return "REFUTED"
    return "HOLD"


def oracle_via_sets(bits):
    """Independent finite-set formulation, not calling proposed_gate."""
    established = {name for name, bit in zip(("R", "I", "E", "Independent", "F", "F_admissible"), bits) if bit}
    admits = {"R", "I", "E", "Independent"}.issubset(established)
    rejects = {"F", "F_admissible"}.issubset(established)
    return "HOLD" if admits == rejects else ("ADMITTED" if admits else "REFUTED")


def run():
    counts = {"ADMITTED": 0, "REFUTED": 0, "HOLD": 0}
    for bits in itertools.product((False, True), repeat=6):
        actual = proposed_gate(*bits)
        expected = oracle_via_sets(bits)
        assert actual == expected, (bits, actual, expected)
        counts[actual] += 1
    assert sum(counts.values()) == 64

    # A separate symbolic Boolean solver attempts to find counterexamples to the
    # correspondence, exclusivity, completeness, and conservative-refutation laws.
    R, I, E, D, F, A = s.symbols("R I E D F A", boolean=True)
    k = s.And(R, I, E, D)
    f = s.And(F, A)
    p = s.And(k, ~f)
    n = s.And(f, ~k)
    u = s.Or(s.And(k, f), s.And(~k, ~f))
    failed_conditions = s.Or(
        ~s.Or(p, n, u),
        s.And(p, n), s.And(p, u), s.And(n, u),
        s.And(p, f), s.And(n, k),
        s.Xor(p, s.And(k, ~f)),
        s.Xor(n, s.And(f, ~k)),
        s.Xor(u, s.Not(s.Xor(k, f))),
    )
    assert satisfiable(failed_conditions) is False

    pi = s.pi
    x = s.symbols("x", real=True, nonzero=True)
    assert s.simplify(s.sqrt(pi)/s.sqrt(pi)) == 1
    assert s.simplify(x/x) == 1
    assert s.simplify(s.sqrt(pi)-1) != 0
    assert s.sqrt(pi) != 2
    assert s.simplify(s.sqrt(pi)/s.sqrt(pi)) == s.simplify(s.Integer(2)/2)
    assert s.sympify(0)/s.sympify(0) is s.nan

    negative_controls = {
        "no_independent_echo": proposed_gate(True, True, True, False, False, False) == "HOLD",
        "no_echo_report": proposed_gate(True, True, False, True, False, False) == "HOLD",
        "falsifier_not_admissible": proposed_gate(False, False, False, False, True, False) == "HOLD",
        "admissible_falsifier": proposed_gate(False, False, False, False, True, True) == "REFUTED",
        "positive_negative_conflict": proposed_gate(True, True, True, True, True, True) == "HOLD",
        "zero_denominator_rejected": s.sympify(0)/s.sympify(0) is s.nan,
        "false_pi_equation_rejected": s.simplify(s.sqrt(pi)-1) != 0,
        "normalization_loses_identity": s.simplify(s.sqrt(pi)/s.sqrt(pi)) == s.simplify(s.Integer(2)/2) and s.sqrt(pi) != 2,
    }
    original = b"claim=normalization;verdict=HOLD\n"
    manipulated = b"claim=normalization;verdict=PASS\n"
    negative_controls["tampered_receipt_detected"] = (
        hashlib.sha256(original).digest() != hashlib.sha256(manipulated).digest()
    )
    assert all(negative_controls.values()), negative_controls
    return {
        "research_status": "bounded_formal_overlay_not_canonical_kernel",
        "python_version": platform.python_version(),
        "sympy_version": s.__version__,
        "tested_boolean_assignments": 64,
        "classification_counts": counts,
        "oracle_agreement": "64/64",
        "symbolic_counterexample_to_proved_obligations": "UNSAT (sympy.satisfiable == False)",
        "negative_controls_passed": len(negative_controls),
        "negative_controls": negative_controls,
        "exact_pi_self_normalization": "1",
        "kernel_source_bytes_rehashed": False,
        "historical_manifests_rehashed": False,
        "experiment_029_receipts_replayed": False,
        "independent_REIK_scientific_Echo": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
