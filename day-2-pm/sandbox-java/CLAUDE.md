# CLAUDE.md — calc sandbox (Java)

Context for Claude Code sessions inside this sandbox.

## What this is

A tiny Java 21 CLI calculator used as the **shared codebase** for the Day 2 PM
exercise on factory-pipeline Skills (Planner -> Refine -> Implement).

Participants build their own Skills against this code. Each feature increment
is captured as a **Bean** in `.beans/<id>.md`, managed by the **beans CLI**
(`brew install hmans/beans/beans`). Skills read beans via `beans show --json
<id>` and write back via `beans update <id>` — never edit bean files directly.

Run `beans prime` once to load the full agent-facing reference (types,
statuses, commands, workflow). The SessionStart hook does this automatically.

## File layout

```
src/main/java/calc/TokenType.java   Token kinds: NUMBER, PLUS, MINUS, STAR, SLASH, END.
src/main/java/calc/Token.java       Token data holder (type, value, pos).
src/main/java/calc/Lexer.java       Token stream.
src/main/java/calc/NodeKind.java    AST node kinds: Number, BinaryOp.
src/main/java/calc/BinOp.java       Binary operators: Add, Sub, Mul, Div.
src/main/java/calc/Node.java        Flat node: { kind, value, op, left, right }.
src/main/java/calc/Parser.java      Recursive descent.
src/main/java/calc/Evaluator.java   Walks AST, returns long. Throws CalcException on div-by-zero.
src/main/java/calc/Main.java        REPL. Catches CalcException, prints, continues.
src/main/java/calc/CalcException.java  Single parse/eval error type (extends RuntimeException).
src/test/java/calc/*Test.java       JUnit 5. One file per source module.
pom.xml                             Java 21, JUnit 5 (Jupiter), exec-maven-plugin.
.beans/<id>.md                      Per-feature bean files (managed by beans CLI).
.beans.yml                          Beans CLI config (prefix, id length, defaults).
```

## Build & test

```bash
mvn -q test
mvn -q compile exec:java   # REPL
```

## Stack conventions

- **Java 21.** Use modern, idiomatic Java where it clarifies intent. Don't reach
  for preview features.
- **Maven + JUnit 5 (Jupiter) only.** No extra dependencies — no Guava, no
  Lombok, no AssertJ. New deps go in `pom.xml` deliberately or they don't go in.
- **Simple data classes over deep OOP.** AST nodes are a single flat `Node`
  class with a `NodeKind kind` discriminator. Add new node kinds by extending
  the enum + the evaluator's switch. Resist class hierarchies unless the cost of
  the switch becomes real.
- **Errors throw `CalcException`** (extends `RuntimeException`) with a readable
  message. The REPL is the single catch point. Don't introduce error-code
  returns or checked exceptions.
- **No allocations in hot loops, but no premature optimization either.**
  Clarity wins. This is a teaching codebase.
- **Naming.** camelCase for methods and variables, PascalCase for types,
  `UPPER_SNAKE` for compile-time constants. Match what's already in
  `src/main/java/calc/`.

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

- Don't introduce a build system other than Maven.
- Don't pull in extra Java libraries (no Guava, Lombok, AssertJ, JUnit 4).
- Don't restructure the `Node` data class into a class hierarchy "for
  cleanliness" — the flat class is intentional.
- Don't touch files under sibling exercise directories or create new
  pipeline-stage directories here — those are owned by a different agent.
