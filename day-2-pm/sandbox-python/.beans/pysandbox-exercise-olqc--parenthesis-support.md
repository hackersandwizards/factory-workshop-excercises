---
# pysandbox-exercise-olqc
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
- calc/lexer.py — Extend the `TokenType` enum with `LPAREN` and `RPAREN`
- calc/lexer.py — Add `(` and `)` to the `_SINGLE_CHAR_TOKENS` mapping used by `Lexer.next()`, each producing a single-char token
- calc/lexer.py — `token_type_name()` returns `token_type.name`, so `LPAREN`/`RPAREN` get human-readable names automatically (used in parser error messages)
- calc/parser.py — Update the grammar comment in the module docstring: `factor := NUMBER | '(' expr ')'`
- calc/parser.py — Extend `_Parser._parse_factor()` with an `LPAREN` alternative: `_advance()` past `(`, recurse via `parse_expr()`, then expect `RPAREN`; empty `()` and missing `)` raise `CalcError` in the style of `expect_end()`/`_parse_factor()`
- tests/test_lexer.py — new test `test_parentheses` analogous to `test_all_operators`
- tests/test_parser.py — new tests `test_parens_group_overrides_precedence`, `test_nested_parens` analogous to `test_mul_binds_tighter_than_add`
- tests/test_parser.py — new tests `test_missing_closing_paren_throws`, `test_empty_parens_throws`, `test_stray_closing_paren_throws` analogous to `test_trailing_token_throws`/`test_missing_operand_throws`
- tests/test_evaluator.py — new tests `test_parens_simple`, `test_parens_right_side`, `test_nested_parens`, `test_parens_override_precedence`, `test_regression_no_parens` via the `eval_str` helper

### New signatures
- (no new classes/functions) — `Lexer.next()` and `_Parser._parse_factor()` keep their signatures; the extension is purely within the existing mapping/branches
- AST/Evaluator unchanged — grouping is encoded by the tree shape, no new `NodeKind`

### Test sketch
- LexerTest.test_parentheses — Input `"()"` → token sequence `LPAREN, RPAREN, END`
- ParserTest.test_parens_group_overrides_precedence — Input `"(1+2)*3"` → AST `Mul(Add(1,2), 3)`
- ParserTest.test_nested_parens — Input `"((1+2)*(3+4))"` → AST `Mul(Add(1,2), Add(3,4))`
- ParserTest.test_missing_closing_paren_throws — Input `"(1+2"` → `CalcError`
- ParserTest.test_empty_parens_throws — Input `"()"` → `CalcError`
- ParserTest.test_stray_closing_paren_throws — Input `"1+2)"` → `CalcError`
- EvaluatorTest.test_parens_simple — Input `"(1+2)*3"` → `9`
- EvaluatorTest.test_parens_right_side — Input `"2*(3+4)"` → `14`
- EvaluatorTest.test_nested_parens — Input `"((1+2)*(3+4))"` → `21`
- EvaluatorTest.test_parens_override_precedence — Input `"(2+3)*(4-1)"` → `15`
- EvaluatorTest.test_regression_no_parens — Input `"1+2*3"` → `7` (unchanged behavior)

## Implementation Log

**Branch:** feat/pysandbox-exercise-olqc-parenthesis-support

**Commits:**
- 8cd1d76 — Add LPAREN/RPAREN token types to lexer
- 5827d64 — Extend _parse_factor() with parenthesised grouping
- dbec914 — Add tests for parentheses: lexer, parser, evaluator

**Final test status:** PASS  (python3 -m unittest → 27/27 green)

## Summary of Changes

- **8cd1d76** — `TokenType` enum extended with `LPAREN`/`RPAREN`; `Lexer.next()` recognises `(` and `)` via `_SINGLE_CHAR_TOKENS`; `token_type_name()` returns human-readable names for both.
- **5827d64** — `_parse_factor()` extended with LPAREN branch: consumes `(`, recurses via `parse_expr()`, expects `)`. Empty `()` and missing `)` raise `CalcError`. Grammar comment in `parser.py` updated.
- **dbec914** — New tests across all three test files: `LexerTest.test_parentheses`, five new `ParserTest` cases (grouping, nesting, three error paths), five new `EvaluatorTest` cases plus regression.

All Acceptance Criteria from the High-Level Plan were exercised by the tests: `(1+2)*3→9`, `2*(3+4)→14`, `((1+2)*(3+4))→21`, `(2+3)*(4-1)→15`, `1+2*3→7` (regression), and all three error paths (missing `)`, empty `()`, stray `)`) raise `CalcError` as required.
