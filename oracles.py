from __future__ import annotations

from dataclasses import dataclass
from math import isclose
from typing import Iterable

from backends.base import BackendRunResult, TraceStep


@dataclass(frozen=True)
class EquivalenceOutcome:
    equivalent: bool
    max_absolute_error: float
    max_relative_error: float
    failures: tuple[str, ...] = ()


@dataclass(frozen=True)
class InvariantOutcome:
    valid: bool
    failures: tuple[str, ...] = ()


def max_absolute_error(left: Iterable[float], right: Iterable[float]) -> float:
    return max((abs(a - b) for a, b in zip(left, right, strict=True)), default=0.0)


def max_relative_error(left: Iterable[float], right: Iterable[float]) -> float:
    max_error = 0.0
    for a, b in zip(left, right, strict=True):
        scale = max(abs(a), abs(b), 1.0)
        max_error = max(max_error, abs(a - b) / scale)
    return max_error


def traces_equivalent(
    left: tuple[TraceStep, ...],
    right: tuple[TraceStep, ...],
    *,
    atol: float = 1e-12,
    rtol: float = 1e-12,
) -> EquivalenceOutcome:
    failures: list[str] = []
    if len(left) != len(right):
        return EquivalenceOutcome(False, float("inf"), float("inf"), ("Trace lengths differ.",))

    absolute_errors: list[float] = []
    relative_errors: list[float] = []
    for left_step, right_step in zip(left, right, strict=True):
        if left_step.selected_action != right_step.selected_action:
            failures.append(f"Policy mismatch at cycle {left_step.cycle}.")
        if left_step.memory_size != right_step.memory_size:
            failures.append(f"Memory size mismatch at cycle {left_step.cycle}.")
        absolute_errors.append(max_absolute_error(left_step.state, right_step.state))
        relative_errors.append(max_relative_error(left_step.state, right_step.state))
        for measure_name, left_value in left_step.measures.items():
            right_value = right_step.measures.get(measure_name)
            if right_value is None or not isclose(left_value, right_value, rel_tol=rtol, abs_tol=atol):
                failures.append(f"Measure mismatch for {measure_name} at cycle {left_step.cycle}.")

    max_abs = max(absolute_errors, default=0.0)
    max_rel = max(relative_errors, default=0.0)
    numeric_match = max_abs <= atol or max_rel <= rtol
    return EquivalenceOutcome(not failures and numeric_match, max_abs, max_rel, tuple(failures))


def verify_structural_invariants(result: BackendRunResult) -> InvariantOutcome:
    failures: list[str] = []
    expected_dim = result.fixture.state_dim
    for step in result.trace:
        if len(step.state) != expected_dim:
            failures.append(f"State dimension changed at cycle {step.cycle}.")
        if len(step.observation) > len(step.state):
            failures.append(f"Observation shape exceeds state size at cycle {step.cycle}.")
        if step.memory_size > result.fixture.memory_capacity:
            failures.append(f"Memory capacity exceeded at cycle {step.cycle}.")
    return InvariantOutcome(not failures, tuple(failures))


def branching_consistent(results: Iterable[BackendRunResult]) -> bool:
    action_traces = [tuple(step.selected_action for step in result.trace) for result in results if result.expressible]
    return len(set(action_traces)) <= 1
