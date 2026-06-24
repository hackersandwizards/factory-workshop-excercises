# calc — Workshop Sandbox (Python)

A minimal Python 3 CLI calculator. Lexer + recursive-descent parser + tree-walking
evaluator + a REPL. Used as the shared codebase for the Day 2 PM exercise on
factory-pipeline Skills (Planner -> Refine -> Implement).

## Build & test

```bash
python3 -m unittest
```

Expected: all tests pass.

## Run the REPL

```bash
python3 -m calc
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
calc/
  __init__.py     CalcError, the single error type
  lexer.py        tokenization: NUMBER, PLUS, MINUS, STAR, SLASH, END
  parser.py       recursive-descent parser, AST nodes (Number, BinaryOp)
  evaluator.py    walks AST, returns int
  __main__.py     REPL (python3 -m calc)
tests/
  test_lexer.py
  test_parser.py
  test_evaluator.py
.beans/           one .md per workshop bean (see CLAUDE.md)
```
