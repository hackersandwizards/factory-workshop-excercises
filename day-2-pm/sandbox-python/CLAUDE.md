# CLAUDE.md — calc sandbox (Python)

Context for Claude Code sessions inside this sandbox.

## What this is

A tiny Python 3 CLI calculator used as the **shared codebase** for the Day 2 PM
exercise on factory-pipeline Skills (Planner -> Refine -> Implement).

Participants build their own Skills against this code. Each feature increment
is captured as a **Bean** in `.beans/<id>.md`, managed by the **beans CLI**
(`brew install hmans/beans/beans`). Skills read beans via `beans show --json
<id>` and write back via `beans update <id>` — never edit bean files directly.

Run `beans prime` once to load the full agent-facing reference (types,
statuses, commands, workflow). The SessionStart hook does this automatically.

## File layout

```
calc/__init__.py    CalcError — the single exception type, caught by the REPL.
calc/lexer.py       Token stream. Types: NUMBER, PLUS, MINUS, STAR, SLASH, END.
calc/parser.py      Recursive descent. AST = dataclass Node(kind, value, op, left, right).
calc/evaluator.py   Walks AST, returns int. Raises CalcError on div-by-zero.
calc/__main__.py    REPL. Catches CalcError, prints, continues.
tests/test_*.py     stdlib unittest. One file per source module.
.beans/<id>.md      Per-feature bean files (managed by beans CLI).
.beans.yml          Beans CLI config (prefix, id length, defaults).
```

## Build & test

```bash
python3 -m unittest      # run all tests
python3 -m calc          # REPL
```

No build step, no virtualenv required — stdlib only, Python 3.9+.

## Stack conventions

- **Python 3.9+, stdlib only.** Use `dataclasses`, `enum`, `typing` where they
  clarify intent. Don't reach for newer-only syntax that breaks 3.9.
- **stdlib `unittest` only.** No pytest, no third-party deps, no build backend.
  There is nothing to `pip install`. New deps don't go in.
- **Simple structs over deep OOP.** AST nodes are a single `@dataclass Node`
  with a `kind` discriminator. Add new node kinds by extending the enum + the
  evaluator's branch chain. Resist class hierarchies unless the cost of the
  branching becomes real.
- **Errors raise `CalcError`** with a readable message. The REPL is the single
  catch point. Don't introduce error-code returns or scatter `try/except`.
- **No premature optimization.** Clarity wins. This is a teaching codebase.
- **Naming.** snake_case for functions and variables, PascalCase for types and
  enum members that mirror the C++ original. Match what's already in `calc/`.

## Beans workflow

Beans are managed by the `beans` CLI — never `Edit` or `Write` a bean file
directly. The factory-pipeline Skills compose like this:

1. **Planner** appends a `## High-Level Plan` section (approach + AC, no
   file paths) via `beans update <id> --body-append "..."`.
2. **Refine** appends a `## Refined Plan` section (files + signatures + test
   sketch) via the same mechanism. Set status to `in-progress` when work
   starts: `beans update <id> -s in-progress`.
3. **Implement** appends a `## Implementation Log` section with branch + commit
   SHAs. On completion: `beans update <id> -s completed`.

Body sections are conventions, not enforced — the CLI treats the body as one
markdown blob. Skills must append rather than rewrite. Run `beans prime` for
the full reference.

## What Claude should not do here

- Don't introduce a build system or packaging backend (no pyproject build, no
  setuptools, no Poetry). `python3 -m unittest` and `python3 -m calc` are it.
- Don't pull in extra Python libraries (no pytest, numpy, sympy, lark, ply).
- Don't restructure the AST into a class hierarchy "for cleanliness" — the
  flat dataclass is intentional.
- Don't touch files under `01-factory-pipeline/` (sibling dir, obsolete) or
  create `01-planner-rework/` / `02-refine/` / `03-implement/` here — those
  are owned by a different agent.
