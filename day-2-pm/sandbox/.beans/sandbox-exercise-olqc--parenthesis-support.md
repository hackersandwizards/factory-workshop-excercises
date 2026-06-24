---
# sandbox-exercise-olqc
title: Parenthesis Support in the Calculator
status: completed
type: feature
priority: normal
created_at: 2026-05-26T12:06:51Z
updated_at: 2026-05-26T13:16:25Z
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
## Refined Plan

### Files to change
- src/lexer.h:9 — Extend the TokenType enum with `LPAREN` and `RPAREN`
- src/lexer.cpp:39 — Add branches for `(` and `)` to the punctuation switch in `Lexer::next()`, each returning a single-char token
- src/lexer.cpp:55 — Add names for `LPAREN`/`RPAREN` to the `token_type_name` switch (parser error messages)
- src/parser.h:13 — Update the grammar comment: `factor := NUMBER | '(' expr ')'`
- src/parser.cpp:64 — Extend `parse_factor()` with an `LPAREN` alternative: `advance()` past `(`, recurse via `parse_expr()`, then expect `RPAREN`; empty `()` and missing `)` throw `std::runtime_error` in the style of :40/:68
- tests/lexer_test.cpp:16 — new TEST `LexerTest.Parentheses` analogous to `AllOperators`
- tests/parser_test.cpp:28 — new TESTs `ParensGroupOverridesPrecedence`, `NestedParens` analogous to `MulBindsTighterThanAdd`
- tests/parser_test.cpp:39 — new TESTs `MissingClosingParenThrows`, `EmptyParensThrows`, `StrayClosingParenThrows` analogous to `TrailingTokenThrows`/`MissingOperandThrows`
- tests/evaluator_test.cpp:16 — new TESTs `ParensSimple`, `ParensRightSide`, `NestedParens`, `ParensOverridePrecedence`, `RegressionNoParens` via the `eval_str` helper

### New signatures
- (no new classes/functions) — `Token Lexer::next()` and `NodePtr Parser::parse_factor()` keep their signatures; the extension is purely within existing switches/branches
- AST/Evaluator unchanged — grouping is encoded by the tree shape, no new `NodeKind`

### Test sketch
- LexerTest.Parentheses — Input `"()"` → token sequence `LPAREN, RPAREN, END`
- ParserTest.ParensGroupOverridesPrecedence — Input `"(1+2)*3"` → AST `Mul(Add(1,2), 3)`
- ParserTest.NestedParens — Input `"((1+2)*(3+4))"` → AST `Mul(Add(1,2), Add(3,4))`
- ParserTest.MissingClosingParenThrows — Input `"(1+2"` → `std::runtime_error`
- ParserTest.EmptyParensThrows — Input `"()"` → `std::runtime_error`
- ParserTest.StrayClosingParenThrows — Input `"1+2)"` → `std::runtime_error`
- EvaluatorTest.ParensSimple — Input `"(1+2)*3"` → `9`
- EvaluatorTest.ParensRightSide — Input `"2*(3+4)"` → `14`
- EvaluatorTest.NestedParens — Input `"((1+2)*(3+4))"` → `21`
- EvaluatorTest.ParensOverridePrecedence — Input `"(2+3)*(4-1)"` → `15`
- EvaluatorTest.RegressionNoParens — Input `"1+2*3"` → `7` (unchanged behavior)

## Implementation Log

**Branch:** feat/sandbox-exercise-olqc-parenthesis-support

**Commits:**
- 8cd1d76 — Add LPAREN/RPAREN token types to lexer
- 5827d64 — Extend parse_factor() with parenthesised grouping
- dbec914 — Add tests for parentheses: lexer, parser, evaluator

**Final test status:** PASS  (ctest --test-dir build → 27/27 green)

## Summary of Changes

- **8cd1d76** — `TokenType` enum extended with `LPAREN`/`RPAREN`; `Lexer::next()` recognises `(` and `)`; `token_type_name()` returns human-readable names for both.
- **5827d64** — `parse_factor()` extended with LPAREN branch: consumes `(`, recurses via `parse_expr()`, expects `)`. Empty `()` and missing `)` throw `std::runtime_error`. Grammar comment in `parser.h` updated.
- **dbec914** — New tests across all three test files: `LexerTest.Parentheses`, five new `ParserTest` cases (grouping, nesting, three error paths), five new `EvaluatorTest` cases plus regression.

All Acceptance Criteria from the High-Level Plan were exercised by the tests: `(1+2)*3→9`, `2*(3+4)→14`, `((1+2)*(3+4))→21`, `(2+3)*(4-1)→15`, `1+2*3→7` (regression), and all three error paths (missing `)`, empty `()`, stray `)`) throw `std::runtime_error` as required.
