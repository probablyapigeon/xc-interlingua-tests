from .base import Backend, BackendRunResult, FixtureSpec, TraceStep
from .reference import DeterministicReferenceBackend


def default_backends() -> tuple[Backend, ...]:
    return (
        DeterministicReferenceBackend("python-reference"),
        DeterministicReferenceBackend("javascript-reference"),
        DeterministicReferenceBackend("cpp-reference"),
    )


__all__ = [
    "Backend",
    "BackendRunResult",
    "FixtureSpec",
    "TraceStep",
    "DeterministicReferenceBackend",
    "default_backends",
]
