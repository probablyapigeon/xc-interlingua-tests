import unittest
from pathlib import Path

from test_harness import discover_fixtures, run_harness


class HarnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixtures_dir = Path("/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/fixtures")

    def test_discovers_expected_fixtures(self) -> None:
        fixtures = discover_fixtures(self.fixtures_dir)
        self.assertEqual(5, len(fixtures))
        self.assertEqual("episodic_memory", fixtures[0].name)
        self.assertEqual("stochastic_boundary", fixtures[-1].name)

    def test_harness_reports_boundary_fixture(self) -> None:
        result = run_harness(self.fixtures_dir)
        self.assertIn("stochastic_boundary", result.equivalence)
        self.assertTrue(result.equivalence["linear_4d"]["equivalent"])
        self.assertEqual(("stochastic_boundary",), tuple(fixture.name for fixture in result.boundary_fixtures))


if __name__ == "__main__":
    unittest.main()
