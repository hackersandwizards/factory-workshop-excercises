# Day 2 PM · Exercise 02 — Refine (Plan → Refined Plan)

**Slot:** ~50 minutes · Phase 2 of the Factory pipeline

## Goal

Build a `refine` skill that takes a bean with a filled-in High-Level Plan, explores the codebase via a **subagent fork** (protecting the context of the main conversation), and writes a concrete `## Refined Plan` with real files, signatures, and a test sketch into the bean.

## Prerequisites

- The sandbox calculator under `../sandbox/` is built (`cmake -B build && cmake --build build`)
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

- `beans show sandbox-dy91` shows a `## Refined Plan` in the body with real paths like `src/lexer.cpp:88` (with a line number from the source)
- The paths really exist (`ls ../sandbox/src/lexer.cpp` without error)
- No source files were edited (`git status` in `../sandbox/` shows only `.beans/sandbox-dy91--parenthesis-support.md` as modified)
- The bean status is `in-progress`
- The subagent output does NOT land as a long dump in the main conversation history — only the structured map flows into the Refined Plan

## Solution Comparison

After the exercise, compare your skill with `solution/.claude/skills/refine/SKILL.md`. Pay attention to: the exact subagent prompt, the test-sketch format (test name + input → expected), the self-check phase, and how the hard "read-only on source" rule is worded.

## Learning Goals

- The Task tool as a context-saving mechanism: the subagent consumes its own context, only the findings come back
- Plan refinement as its own phase: the "what" becomes the "how" — controlled, with verification
- Anti-hallucination: every claimed file must be verifiable, otherwise it gets dropped
- Skill composition: one skill's output (Planner) is the cleanly structured input of the next (Refine)
