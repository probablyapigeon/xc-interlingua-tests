# Clean-room agent instructions — XC Round 4

You are the independent implementer in a blind conformance experiment.

Use **only this repository's ROUND4 directory and its implementer packet** as authority for XC/XIR semantics.

You MUST NOT browse or inspect any other XC/XEMBRA repository, especially `probablyapigeon/xembra-xc`. Do not search GitHub, the web, prior chat history, package registries, or cached project material for XC implementation details. Do not request `xc.py`, prior backend code, mutant code, hidden tests, or judge outputs. Normal documentation for your chosen host language/runtime is allowed.

Assignment:
1. Run `python bootstrap.py` in this directory.
2. Read `implementer_packet/README_IMPLEMENTER.md`, `XC_XIR_SEMANTICS_SPEC_FROZEN.md`, and `BACKEND_PROTOCOL.md`.
3. Implement one executable backend command in any language that obeys the JSONL stdin/stdout protocol.
4. Develop only against the public cases and public expected outputs.
5. If any semantic point is ambiguous, record it in `AMBIGUITIES.md` before hidden evaluation and state the interpretation chosen. Do not seek reference-runtime details.
6. Once public cases pass, freeze the implementation. Record source/artifact SHA-256 and toolchain/runtime versions in `FROZEN_SUBMISSION.md`.
7. Stop modifying the backend and report exactly: **FROZEN FOR BLIND EVALUATION**.

The scientific value of this task depends on not contaminating the implementation with prior XC knowledge.
