---
# jsandbox-exercise-olqc
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
- src/main/java/calc/TokenType.java — Extend the TokenType enum with `LPAREN` and `RPAREN`
- src/main/java/calc/Lexer.java — Add branches for `(` and `)` to the punctuation switch in `Lexer.next()`, each returning a single-char token
- src/main/java/calc/Lexer.java — Add names for `LPAREN`/`RPAREN` to the `tokenTypeName` switch (parser error messages)
- src/main/java/calc/Parser.java — Update the grammar comment: `factor := NUMBER | '(' expr ')'`
- src/main/java/calc/Parser.java — Extend `parseFactor()` with an `LPAREN` alternative: `advance()` past `(`, recurse via `parseExpr()`, then expect `RPAREN`; empty `()` and missing `)` throw `CalcException` in the style of `expectEnd()`/`parseFactor()`
- src/test/java/calc/LexerTest.java — new `@Test` `Parentheses` analogous to `AllOperators`
- src/test/java/calc/ParserTest.java — new `@Test`s `ParensGroupOverridesPrecedence`, `NestedParens` analogous to `MulBindsTighterThanAdd`
- src/test/java/calc/ParserTest.java — new `@Test`s `MissingClosingParenThrows`, `EmptyParensThrows`, `StrayClosingParenThrows` analogous to `TrailingTokenThrows`/`MissingOperandThrows`
- src/test/java/calc/EvaluatorTest.java — new `@Test`s `ParensSimple`, `ParensRightSide`, `NestedParens`, `ParensOverridePrecedence`, `RegressionNoParens` via the `evalStr` helper

### New signatures
- (no new classes/methods) — `Token Lexer.next()` and `Node Parser.parseFactor()` keep their signatures; the extension is purely within existing switches/branches
- AST/Evaluator unchanged — grouping is encoded by the tree shape, no new `NodeKind`

### Test sketch
- LexerTest.Parentheses — Input `"()"` → token sequence `LPAREN, RPAREN, END`
- ParserTest.ParensGroupOverridesPrecedence — Input `"(1+2)*3"` → AST `Mul(Add(1,2), 3)`
- ParserTest.NestedParens — Input `"((1+2)*(3+4))"` → AST `Mul(Add(1,2), Add(3,4))`
- ParserTest.MissingClosingParenThrows — Input `"(1+2"` → `CalcException`
- ParserTest.EmptyParensThrows — Input `"()"` → `CalcException`
- ParserTest.StrayClosingParenThrows — Input `"1+2)"` → `CalcException`
- EvaluatorTest.ParensSimple — Input `"(1+2)*3"` → `9`
- EvaluatorTest.ParensRightSide — Input `"2*(3+4)"` → `14`
- EvaluatorTest.NestedParens — Input `"((1+2)*(3+4))"` → `21`
- EvaluatorTest.ParensOverridePrecedence — Input `"(2+3)*(4-1)"` → `15`
- EvaluatorTest.RegressionNoParens — Input `"1+2*3"` → `7` (unchanged behavior)

## Implementation Log

**Branch:** feat/jsandbox-exercise-olqc-parenthesis-support

**Commits:**
- 8cd1d76 — Add LPAREN/RPAREN token types to lexer
- 5827d64 — Extend parseFactor() with parenthesised grouping
- dbec914 — Add tests for parentheses: lexer, parser, evaluator

**Final test status:** PASS  (mvn -q test → 27/27 green)

## Summary of Changes

- **8cd1d76** — `TokenType` enum extended with `LPAREN`/`RPAREN`; `Lexer.next()` recognises `(` and `)`; `tokenTypeName()` returns human-readable names for both.
- **5827d64** — `parseFactor()` extended with LPAREN branch: consumes `(`, recurses via `parseExpr()`, expects `)`. Empty `()` and missing `)` throw `CalcException`. Grammar comment in `Parser.java` updated.
- **dbec914** — New tests across all three test files: `LexerTest.Parentheses`, five new `ParserTest` cases (grouping, nesting, three error paths), five new `EvaluatorTest` cases plus regression.

All Acceptance Criteria from the High-Level Plan were exercised by the tests: `(1+2)*3→9`, `2*(3+4)→14`, `((1+2)*(3+4))→21`, `(2+3)*(4-1)→15`, `1+2*3→7` (regression), and all three error paths (missing `)`, empty `()`, stray `)`) throw `CalcException` as required.
