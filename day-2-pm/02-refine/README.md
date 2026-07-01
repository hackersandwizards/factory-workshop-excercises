# Day 2 PM · Exercise 02 — Refine (Plan → Refined Plan)

**Slot:** ~50 minutes · Phase 2 of the Factory pipeline

## Goal

Build a `refine` skill that takes a bean with a filled-in High-Level Plan, explores the codebase via a **subagent fork** (protecting the context of the main conversation), and writes a concrete `## Refined Plan` with real files, signatures, and a test sketch into the bean.

> **Your sandbox.** Wherever this README says `../sandbox`, use your language's folder: `../sandbox` (C++) · `../sandbox-java` (Java) · `../sandbox-python` (Python). Bean IDs carry your prefix (`sandbox-` / `jsandbox-` / `pysandbox-`) — `sandbox-dy91` below is just an example; use the ID your Planner created. Refine is language-neutral: it explores whatever source the subagent finds and writes paths/signatures in your language.

## Prerequisites

- The sandbox calculator for your language is built:
  - **C++** — `cd ../sandbox && cmake -B build && cmake --build build`
  - **Java** — `cd ../sandbox-java && mvn -q test` (compiles + tests)
  - **Python** — `cd ../sandbox-python && python3 -m unittest` (no build step)
- The `beans` CLI is installed. The bean from Exercise 01 has a `## High-Level Plan` in its body.
- Understanding: the Task tool dispatches subagents into isolated sub-contexts

## Task

Detailed hints + build checklist: `exercise/HINTS.md`. Skeleton: `exercise/.claude/skills/.gitkeep` — an empty starting point, the skill is built from scratch.

1. Copy `exercise/.claude/` into the sandbox: `cp -r exercise/.claude ../sandbox/`. Then `mkdir ../sandbox/.claude/skills/refine && touch ../sandbox/.claude/skills/refine/SKILL.md`.
2. Frontmatter: `name: refine`, `argument-hint: <bean-id>`, `allowed-tools: Read, Grep, Glob, Bash, Task`. (No `Edit` — the bean is written via `beans update`.)
3. Phase 1: parse `beans show --json <bean-id>`, read the body, extract the `## High-Level Plan` section. Missing → abort.
4. Phase 2: `beans update <bean-id> -s in-progress`.
5. Phase 3: dispatch **ONE** subagent via the Task tool (`subagent_type=general-purpose`). Word the prompt so it forces the subagent to return a structured map (Files, Functions, Integration points, Test patterns). Read-only.
6. Phase 4: append the Refined Plan via `beans update <bean-id> --body-append "..."` — schema `### Files to change` / `### New signatures` / `### Test sketch`. Line numbers come from the subagent output, not from imagination.
7. Phase 5: self-check — verify every file path via Glob/Grep. No hallucinations. `git status` shows no source diffs.
8. Test: run `/refine sandbox-dy91`. Check `beans show sandbox-dy91`.

## Self-Check

- `beans show <bean-id>` shows a `## Refined Plan` in the body with real paths + line numbers from the source. Per language: C++ `src/lexer.cpp:88`, Java `src/main/java/calc/Lexer.java:42`, Python `calc/lexer.py:31`
- The paths really exist (e.g. `ls ../sandbox/src/lexer.cpp` / `ls ../sandbox-java/src/main/java/calc/Lexer.java` / `ls ../sandbox-python/calc/lexer.py` without error)
- No source files were edited (`git status` in your sandbox shows only the `.beans/<bean-id>--*.md` file as modified)
- The bean status is `in-progress`
- The subagent output does NOT land as a long dump in the main conversation history — only the structured map flows into the Refined Plan

## Solution Comparison

The reference solution lives on branch **`solution/day-2-pm-02-refine`** (kept off
`main` so it stays out of Claude's context). After the exercise, compare your skill
with it. Pay attention to: the exact subagent prompt, the test-sketch format (test
name + input → expected), the self-check phase, and how the hard "read-only on source"
rule is worded.

```bash
git checkout solution/day-2-pm-02-refine   # inspect solution/…
git checkout main                          # back to your work
git show solution/day-2-pm-02-refine:day-2-pm/02-refine/solution/.claude/skills/refine/SKILL.md
```

## Learning Goals

- The Task tool as a context-saving mechanism: the subagent consumes its own context, only the findings come back
- Plan refinement as its own phase: the "what" becomes the "how" — controlled, with verification
- Anti-hallucination: every claimed file must be verifiable, otherwise it gets dropped
- Skill composition: one skill's output (Planner) is the cleanly structured input of the next (Refine)
