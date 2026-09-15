from __future__ import annotations

from collections import Counter

from test_harness import HarnessResult


def render_markdown_report(result: HarnessResult) -> str:
    category_counts = Counter(fixture.category for fixture in result.fixtures)
    lines = [
        "# XC Interlingua Test Report",
        "",
        f"- Fixtures discovered: {len(result.fixtures)}",
        f"- Backends exercised: {len(result.backend_names)}",
        f"- Expressible fixtures: {sum(1 for fixture in result.fixtures if fixture.expressible)}",
        f"- Non-expressible fixtures: {sum(1 for fixture in result.fixtures if not fixture.expressible)}",
        "",
        "## Fixture categories",
    ]
    lines.extend(f"- {category}: {count}" for category, count in sorted(category_counts.items()))
    lines.extend(["", "## Results"])
    for outcome in result.equivalence.values():
        lines.append(
            f"- {outcome['fixture']}: equivalent={outcome['equivalent']} max_abs={outcome['max_abs_error']:.3e}"
        )
    if result.boundary_fixtures:
        lines.extend(["", "## Expressiveness boundaries"])
        lines.extend(f"- {fixture.name}" for fixture in result.boundary_fixtures)
    return "\n".join(lines)
