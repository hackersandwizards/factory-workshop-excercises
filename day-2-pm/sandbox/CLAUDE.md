# CLAUDE.md — calc sandbox

Context for Claude Code sessions inside this sandbox.

## What this is

A tiny C++17 CLI calculator used as the **shared codebase** for the Tag 2 PM
exercise on factory-pipeline Skills (Planner -> Refine -> Implement).

Participants build their own Skills against this code. Each feature increment
is captured as a **Bean** in `.beans/<id>.md`. The Skills read and write those
files.

## File layout

```
src/lexer.{h,cpp}      Token stream. Types: NUMBER, PLUS, MINUS, STAR, SLASH, END.
src/parser.{h,cpp}     Recursive descent. AST = struct Node { kind, value, op, left, right }.
src/evaluator.{h,cpp}  Walks AST, returns int64_t. Throws std::runtime_error on div-by-zero.
src/main.cpp           REPL. Catches std::exception, prints, continues.
tests/*_test.cpp       GoogleTest. One file per source module.
CMakeLists.txt         C++17, FetchContent GoogleTest 1.14.
.beans/<id>.md         Per-feature bean files (see format below).
```

## Build & test

```bash
cmake -B build
cmake --build build
ctest --test-dir build
./build/calc        # REPL
```

## Stack conventions

- **C++17.** Use `std::variant`, `std::optional`, `std::string_view` where they
  clarify intent. Don't reach for newer standards.
- **GoogleTest only.** No Boost, no Catch2, no extra dependencies. New deps
  go through FetchContent or they don't go in.
- **Simple structs over deep OOP.** AST nodes are a single `struct Node` with
  a `kind` discriminator. Add new node kinds by extending the enum + the
  evaluator's switch. Resist abstract base classes unless the cost of the
  switch becomes real.
- **Errors throw `std::runtime_error`** with a readable message. The REPL is
  the single catch point. Don't introduce error-code returns.
- **No allocations in hot loops, but no premature optimization either.**
  Clarity wins. This is a teaching codebase.
- **Naming.** snake_case for functions and variables, PascalCase for types,
  `kFoo` for compile-time constants. Match what's already in `src/`.

## Bean format

Each feature increment is a single markdown file at `.beans/<id>.md` with
**exactly these four sections, in this order**:

```markdown
# Bean <id>: <short title>

## Description
Human-written. What the feature is and why we want it. 2–5 sentences. No
implementation detail — that's what the other sections are for.

## High-Level Plan
Produced by the **Planner** Skill. Bullet list of plan steps + explicit
acceptance criteria (AC) the implementation must satisfy. Plan steps reference
files at the module level ("extend the lexer", not full diffs).

## Refined Plan
Produced by the **Refine** Skill. Concrete files to touch, function signatures
to add or change, and a test sketch (test names + one-line intent). This is
the contract Implement consumes.

## Implementation Log
Produced by the **Implement** Skill. Branch name and the commit SHAs that
realised the bean, in order. Append-only — never rewrite history here.
```

Skills append to their own section and leave earlier sections alone. If
Implement finds the Refined Plan inadequate, it stops and bounces the bean
back to Refine rather than silently extending the spec.

## What Claude should not do here

- Don't introduce a build system other than CMake.
- Don't pull in extra C++ libraries (no Boost, fmt, spdlog, abseil).
- Don't restructure the AST into a class hierarchy "for cleanliness" — the
  flat struct is intentional.
- Don't touch files under `01-factory-pipeline/` (sibling dir, obsolete) or
  create `01-planner-rework/` / `02-refine/` / `03-implement/` here — those
  are owned by a different agent.
