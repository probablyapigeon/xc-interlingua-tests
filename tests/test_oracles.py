import unittest

from backends import default_backends
from oracles import max_absolute_error, max_relative_error, traces_equivalent, verify_structural_invariants
from test_harness import discover_fixtures


class OracleTests(unittest.TestCase):
    def test_error_helpers(self) -> None:
        self.assertEqual(0.5, max_absolute_error((1.0, 2.0), (1.5, 2.0)))
        self.assertEqual(0.2, max_relative_error((2.0,), (2.5,)))

    def test_reference_backends_are_equivalent(self) -> None:
        fixture = next(
            fixture
            for fixture in discover_fixtures("/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/fixtures")
            if fixture.name == "nonlinear_policy"
        )
        left, right, *_ = [backend.run(fixture) for backend in default_backends()]
        outcome = traces_equivalent(left.trace, right.trace)
        self.assertTrue(outcome.equivalent)
        self.assertEqual(0.0, outcome.max_absolute_error)
        self.assertTrue(verify_structural_invariants(left).valid)


if __name__ == "__main__":
    unittest.main()
