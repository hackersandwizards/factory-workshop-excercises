# calc — Workshop Sandbox (Java)

A minimal Java 21 CLI calculator. Lexer + recursive-descent parser + tree-walking
evaluator + a REPL. Used as the shared codebase for the Day 2 PM exercise on
factory-pipeline Skills (Planner -> Refine -> Implement).

## Prerequisites

Needs JDK 21 and Maven on the PATH.

## Build & test

```bash
mvn -q test
```

Expected: all tests pass.

## Run the REPL

```bash
mvn -q compile exec:java
```

Example session:

```
calc REPL — type 'exit' or Ctrl-D to quit
> 1+2*3
7
> 10/2
5
> 5-3
2
> 20-6/2
17
> 1/0
error: division by zero
> exit
```

`exit`, `quit`, or Ctrl-D (EOF) leave the loop. Parse and runtime errors are
caught, printed, and the REPL continues.

## Grammar (today)

```
expr   -> term   (('+' | '-') term)*
term   -> factor (('*' | '/') factor)*
factor -> NUMBER
```

Integers only. Left-associative `+ -` and `* /`. Whitespace ignored.

The workshop beans extend this grammar — parentheses, variables, math
functions — see `.beans/`.

## Layout

```
src/main/java/calc/
  TokenType.java     token kinds: NUMBER, PLUS, MINUS, STAR, SLASH, END
  Token.java         token data holder (type, value, pos)
  Lexer.java         tokenization
  NodeKind.java      AST node kinds (Number, BinaryOp)
  BinOp.java         binary operators (Add, Sub, Mul, Div)
  Node.java          flat AST node (kind, value, op, left, right)
  Parser.java        recursive-descent parser
  Evaluator.java     walks AST, returns long
  Main.java          REPL
  CalcException.java parse/eval error type (extends RuntimeException)
src/test/java/calc/
  LexerTest.java
  ParserTest.java
  EvaluatorTest.java
pom.xml              Java 21, JUnit 5 (Jupiter)
.beans/              one .md per workshop bean (see CLAUDE.md)
```
