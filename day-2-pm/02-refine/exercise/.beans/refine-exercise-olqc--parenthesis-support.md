---
# refine-exercise-olqc
title: Parenthesis Support in the Calculator
status: todo
type: feature
created_at: 2026-05-26T12:06:51Z
updated_at: 2026-05-26T12:06:51Z
---

The calculator currently supports only flat expressions with `+ - * /` and a hard-wired precedence order. Users cannot explicitly control the evaluation order. We add round parentheses `(` and `)` as grouping, so that arbitrarily deeply nested subexpressions are evaluated before the surrounding expression. Behavior without parentheses remains unchanged.

**Notes:**
- Chosen approach: minimal delta — add parentheses as additional input symbols and extend the innermost expression level with a grouping alternative
- Existing precedence and associativity rules remain untouched
- Unary minus, functions, and other bracket forms are explicitly not part of this Bean

## High-Level Plan

**Approach** — Grammar extension. Round parentheses are recognized as new input symbols and allowed as an additional alternative at the innermost expression level. This way grouping fits cleanly into the existing recursive structure; operator precedence and associativity remain unchanged.

**Steps**
- Step 1 — Extend input recognition with the two parenthesis symbols, so that `(` and `)` become their own tokens
- Step 2 — Extend the innermost expression level with the "parenthesized subexpression" alternative, which may recursively contain a full expression
- Step 3 — Report error cases (missing closing parenthesis, extra closing parenthesis, empty parenthesis content) as understandable parser errors without terminating the REPL
- Step 4 — Add tests at all levels: symbol recognition, grammar with nesting, end-to-end evaluation, and error paths

**Acceptance Criteria**
- `(1+2)*3` yields `9`
- `2*(3+4)` yields `14`
- Nested parentheses are resolved correctly, e.g. `((1+2)*(3+4))` yields `21`
- Parentheses override precedence, e.g. `(2+3)*(4-1)` yields `15`
- All previous expressions without parentheses yield the same results unchanged (regression-free)
- A missing closing parenthesis (`(1+2`) produces an understandable parser error message; the REPL keeps running
- An extra closing parenthesis (`1+2)`) produces a parser error message; the REPL keeps running
- An empty parenthesized expression `()` produces a parser error message

**Non-Goals**
- Unary minus / unary plus
- Square `[]` or curly `{}` brackets
- Variables, functions, additional operators
- Changes to the existing operator precedence order
- Performance optimizations of the parser
