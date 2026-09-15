# XC Interlingua Test Methodology

## Scope

This repository evaluates whether XC can act as a semantic interlingua for deterministic, stateful, history-dependent, adaptive systems.

## Initial assumptions

- XC fixtures in this scaffold are deterministic by construction.
- Cross-backend equivalence is defined over trace length, state evolution, policy decisions, measures, and memory growth.
- Fixtures marked `expressible=false` define known boundary cases that should be reported rather than executed.

## Initial limitations

- The current backends are deterministic reference wrappers intended to exercise the harness, not full language runtimes.
- Numeric fidelity metrics currently report maximum absolute error; the scaffold exposes extension points for relative error and richer divergence analysis.
- Boundary fixtures document unsupported constructs such as stochastic choice until real XC loaders are added.
