# XC Round 4 — Final Blind Rosetta Challenge

This directory is an **isolation chamber for a clean-room implementation test** of the XC/XIR semantic specification.

## Your task

Implement the computational semantics defined **only** by the contents of `XC_ROUND4_IMPLEMENTER_PACKET.zip`.

Do **not** consult, search for, request, or reuse:

- any existing XC/XEMBRA runtime (including `xc.py`);
- `probablyapigeon/xembra-xc`;
- Round 2/3 JavaScript backends;
- Round 3B mutant implementations;
- any private Judge Packet, hidden cases, or hidden expected outputs;
- prior conversations or notes that reveal reference-runtime behavior beyond this packet.

The experiment asks whether the **written specification alone** is sufficient to transmit executable meaning to a clean-room implementation.

Run `python bootstrap.py`, then read the extracted `implementer_packet/README_IMPLEMENTER.md` first.

If the frozen specification is ambiguous, do not silently infer reference behavior. Record the ambiguity and chosen interpretation in `AMBIGUITIES.md` before hidden evaluation.

When all public cases pass, stop editing the backend, hash/archive it, record the toolchain/runtime version in `FROZEN_SUBMISSION.md`, and report **FROZEN FOR BLIND EVALUATION**.

There is intentionally **no private judge or hidden answer data here**.
