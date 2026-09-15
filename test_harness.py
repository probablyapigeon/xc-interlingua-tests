from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from backends import Backend, FixtureSpec, default_backends
from oracles import EquivalenceOutcome, branching_consistent, traces_equivalent, verify_structural_invariants

FIXTURE_PREFIX = "# xc-test:"


@dataclass(frozen=True)
class HarnessResult:
    fixtures: tuple[FixtureSpec, ...]
    backend_names: tuple[str, ...]
    equivalence: dict[str, dict[str, object]]
    boundary_fixtures: tuple[FixtureSpec, ...]


def parse_fixture(path: Path) -> FixtureSpec:
    metadata: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith(FIXTURE_PREFIX):
            continue
        key, value = line[len(FIXTURE_PREFIX) :].split("=", 1)
        metadata[key.strip()] = value.strip()

    return FixtureSpec(
        name=metadata.get("name", path.stem),
        path=str(path),
        category=metadata.get("category", "semantic-equivalence"),
        expressible=metadata.get("expressible", "true").lower() == "true",
        state_dim=int(metadata.get("state_dim", "4")),
        cycles=int(metadata.get("cycles", "3")),
        operator_complexity=metadata.get("operator_complexity", "linear"),
        memory_capacity=int(metadata.get("memory_capacity", "0")),
        policy_actions=int(metadata.get("policy_actions", "2")),
        measure_count=int(metadata.get("measure_count", "1")),
        notes=tuple(part.strip() for part in metadata.get("notes", "").split("|") if part.strip()),
    )


def discover_fixtures(fixtures_dir: str | Path = "fixtures") -> tuple[FixtureSpec, ...]:
    root = Path(fixtures_dir)
    return tuple(sorted((parse_fixture(path) for path in root.glob("*.xc")), key=lambda fixture: fixture.name))


def evaluate_fixture(fixture: FixtureSpec, backends: tuple[Backend, ...]) -> dict[str, object]:
    run_results = [backend.run(fixture) for backend in backends]
    if not fixture.expressible:
        return {"fixture": fixture.name, "equivalent": True, "max_abs_error": 0.0, "invariants": True}

    reference = run_results[0]
    invariant_outcomes = [verify_structural_invariants(result) for result in run_results]
    equivalence_outcomes: list[EquivalenceOutcome] = [
        traces_equivalent(reference.trace, candidate.trace) for candidate in run_results[1:]
    ]
    return {
        "fixture": fixture.name,
        "equivalent": all(outcome.equivalent for outcome in equivalence_outcomes) and branching_consistent(run_results),
        "max_abs_error": max((outcome.max_absolute_error for outcome in equivalence_outcomes), default=0.0),
        "invariants": all(outcome.valid for outcome in invariant_outcomes),
    }


def run_harness(fixtures_dir: str | Path = "fixtures", backends: tuple[Backend, ...] | None = None) -> HarnessResult:
    selected_backends = backends or default_backends()
    fixtures = discover_fixtures(fixtures_dir)
    equivalence = {fixture.name: evaluate_fixture(fixture, selected_backends) for fixture in fixtures}
    boundary_fixtures = tuple(fixture for fixture in fixtures if not fixture.expressible)
    return HarnessResult(
        fixtures=fixtures,
        backend_names=tuple(backend.name for backend in selected_backends),
        equivalence=equivalence,
        boundary_fixtures=boundary_fixtures,
    )


if __name__ == "__main__":
    from report import render_markdown_report

    print(render_markdown_report(run_harness()))
