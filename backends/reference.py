from __future__ import annotations

import math

from .base import BackendRunResult, FixtureSpec, TraceStep


class DeterministicReferenceBackend:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, fixture: FixtureSpec) -> BackendRunResult:
        if not fixture.expressible:
            return BackendRunResult(
                backend_name=self.name,
                fixture=fixture,
                expressible=False,
                warnings=("Fixture is outside XC's deterministic expressiveness boundary.",),
                metadata={"status": "non-expressible"},
            )

        state = tuple((index + 1) / (fixture.state_dim + 1) for index in range(fixture.state_dim))
        trace: list[TraceStep] = []
        memory_size = 0
        for cycle in range(fixture.cycles):
            bias = (cycle + 1) * 0.05 + fixture.measure_count * 0.001
            next_state = tuple(
                round(math.tanh(value + bias + (index + 1) * 0.01), 12)
                for index, value in enumerate(state)
            )
            observation = next_state[: min(4, len(next_state))]
            measures = {
                "state_l1": round(sum(abs(value) for value in next_state), 12),
                "state_mean": round(sum(next_state) / len(next_state), 12),
            }
            selected_action = f"action_{cycle % max(1, fixture.policy_actions)}"
            if fixture.memory_capacity:
                memory_size = min(fixture.memory_capacity, memory_size + 1)
            trace.append(
                TraceStep(
                    cycle=cycle,
                    state=next_state,
                    observation=observation,
                    measures=measures,
                    selected_action=selected_action,
                    memory_size=memory_size,
                )
            )
            state = next_state

        return BackendRunResult(
            backend_name=self.name,
            fixture=fixture,
            expressible=True,
            trace=tuple(trace),
            metadata={"status": "ok", "operator_complexity": fixture.operator_complexity},
        )
