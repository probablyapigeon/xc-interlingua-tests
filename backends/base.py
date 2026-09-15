from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True)
class FixtureSpec:
    name: str
    path: str
    category: str
    expressible: bool
    state_dim: int
    cycles: int
    operator_complexity: str
    memory_capacity: int
    policy_actions: int
    measure_count: int
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class TraceStep:
    cycle: int
    state: tuple[float, ...]
    observation: tuple[float, ...]
    measures: dict[str, float]
    selected_action: str
    memory_size: int


@dataclass(frozen=True)
class BackendRunResult:
    backend_name: str
    fixture: FixtureSpec
    expressible: bool
    trace: tuple[TraceStep, ...] = ()
    warnings: tuple[str, ...] = ()
    metadata: dict[str, str] = field(default_factory=dict)


class Backend(Protocol):
    name: str

    def run(self, fixture: FixtureSpec) -> BackendRunResult:
        ...
