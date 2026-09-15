# xc-interlingua-tests

Test scaffold for evaluating whether XC serves as a semantic interlingua for deterministic, stateful, history-dependent, adaptive systems.

## Testing philosophy

The initial scaffold focuses on four ideas:

- discover `.xc` fixtures that encode the test matrix in lightweight metadata
- run each expressible fixture through multiple deterministic reference backends
- compare traces with shared equivalence and invariant oracles
- report known expressiveness boundaries explicitly instead of treating them as runtime failures

## Layout

- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/test_harness.py` — fixture discovery and multi-backend orchestration
- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/backends/` — backend interface plus deterministic reference backends
- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/fixtures/` — starter XC fixtures spanning equivalence and boundary cases
- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/oracles.py` — equivalence, error, and invariant helpers
- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/report.py` — markdown report renderer
- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/METHODOLOGY.md` — assumptions, limitations, and semantics under test
- `/home/runner/work/xc-interlingua-tests/xc-interlingua-tests/tests/` — focused standard-library unit tests

## Running the scaffold

```bash
python -m unittest discover -s tests
python test_harness.py
```
