---
# sandbox-vzwt
title: Decimal Number Support in the Calculator
status: todo
type: feature
created_at: 2026-05-26T13:22:49Z
updated_at: 2026-05-26T13:22:49Z
---

The calculator currently supports only integer arithmetic. Users want to compute with decimal values (e.g. `1,5 + 2,5`). This feature converts the entire computation pipeline to floating point, accepts the comma as the decimal separator in input, and prints results without superfluous zeros.

**Notes:**
- Complete migration of the internal number type to floating point (no coexistence with an integer type).
- The decimal separator in input and output is exclusively the comma; the period is neither accepted nor printed.
- Output trims trailing zeros; integer results appear without a comma.
- The existing division semantics deliberately change: `7/2` now yields `3,5` instead of `3`. This is part of the feature, not a regression.
- Division by zero remains a runtime error via `std::runtime_error`; the REPL stays the single catch point.

## High-Level Plan

**Approach** — Direct migration in a single Bean. Since changing the value type inherently runs through all pipeline layers (lexer, AST, evaluator, REPL output), a single coherent change stays clearer than an artificially split-up intermediate state. The tests for each module are updated alongside it.

**Steps**
- The lexer accepts decimal literals with the comma as separator; the number token carries a floating-point value.
- AST nodes and parser constants hold values as a floating-point type.
- The evaluator computes in floating point throughout; division by zero remains a runtime error.
- REPL output formats results: trailing zeros removed, comma as decimal separator, integer results without a comma.
- Existing unit tests for each module and an end-to-end test through the REPL reflect the new behavior.

**Acceptance Criteria**
- `2+2` produces output `4` (not `4,0`).
- `1,5+2,5` produces output `4`.
- `7/2` produces output `3,5`.
- `1,5*2` produces output `3`.
- `1/0` throws a runtime error; the REPL catches it, prints an understandable message, and keeps running.
- Output never contains a period as a decimal separator.
- Output never contains trailing zeros after the comma.
- Existing tests stay green unless they explicitly check the old integer behavior of division — those are adapted to the new behavior.

**Non-Goals**
- No scientific notation (`1e5`, `2,5e3`).
- No period as an alternative decimal separator.
- No separate integer type in the AST or evaluator.
- No configurability of the number of decimal places.
- No thousands separator in input or output.
- No addition of new operators (e.g. `%`, `^`).
