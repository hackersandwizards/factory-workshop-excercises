# Day 2 PM · Exercise 01 — Planner Rework (Bean Creator)

**Slot:** ~35 minutes · Phase 1 of the Factory pipeline

## Goal

Rework the Day 2 AM `planner` skill: instead of writing a freeform plan to `.plans/`, **the skill creates a new bean** via `beans create` + `beans update` with a description, a High-Level Plan, and Acceptance Criteria. Stay strictly at the "what" level (no paths, no signatures). Refine and Implement will receive the bean ID as an argument later — Planner does not.

> **Your sandbox.** Wherever this README says `../sandbox`, use the folder for your language: `../sandbox` (C++) · `../sandbox-java` (Java) · `../sandbox-python` (Python). The beans prefix differs too: `sandbox-` / `jsandbox-` / `pysandbox-`. Planner itself is language-neutral — it writes a High-Level Plan, no code.

## Prerequisites

- The sandbox calculator for your language exists (built by the trainer) — `../sandbox` (C++), `../sandbox-java` (Java), or `../sandbox-python` (Python)
- The `beans` CLI is installed (`brew install hmans/beans/beans`, check: `beans --version`)
- `.beans.yml` exists in your sandbox (prefix `sandbox-` / `jsandbox-` / `pysandbox-`)
- The starting-point skill lives at `exercise/.claude/skills/planner/SKILL.md` (a copy from the Day 2 AM solution). If you have your own Day 2 AM skill, replace the copy with it.

## Task

1. Copy `exercise/.claude/` into the sandbox: `cp -r exercise/.claude ../sandbox/`.
2. Frontmatter: `argument-hint: [brief feature description]` (optional, no bean-id). Description: "creates a new bean via beans CLI with description + High-Level Plan + AC".
3. Rework Phase 1 (Capture): capture the feature idea — either from the skill argument or by asking the user. No repo scan, no bean read.
4. Rework Phase 5 (Create Bean): **one** CLI call with the complete body:
   - `beans create "<title>" -t feature -d "<heredoc with Description + notes + High-Level Plan>"` → ID from stdout
   - Put the plan verbatim under the `## High-Level Plan` heading — `/refine` parses by exact match; if the heading is missing it aborts.
   - The `beans` CLI has **no** `--body-append` flag. The body is written in one go. For very long bodies, use `--body-file <path>` instead of `-d`.
   - **Never** edit `.beans/*.md` directly.
5. Lock down Phase 3 (Approaches): the skill **stops** after presenting the options and waits for an explicit user choice. Even if "autonomously" / "no clarifying questions" was stated earlier — picking an approach is a mandatory gate, not a clarification.
6. Add a hard rule: **no** file paths, **no** function signatures, **no** class names in the plan. Use Acceptance Criteria instead.
7. Test: `cd ../sandbox && claude` → run `/planner Parenthesis support for calculator`. Check `beans list` + `beans show <new-id>`.

Detailed hints: `exercise/HINTS.md`.

## Self-Check

- `beans list` contains a new bean after the `/planner` run
- `beans show <new-id>` shows a description (human brief) + a `## High-Level Plan` with **Approach**, **Steps**, **Acceptance Criteria**, **Non-Goals**
- The plan contains **no** file paths, **no** function names, **no** line references (e.g. no `src/lexer.cpp` / `Lexer.java` / `lexer.py`, no `tokenize()`)
- The new bean's status is `todo`
- The skill refuses gracefully when the `beans` CLI is missing

## Solution Comparison

The reference solution lives on branch **`solution/day-2-pm-01-planner-rework`** (kept
off `main` so it stays out of Claude's context). After the exercise, compare your skill
with it. What is different? What would you adopt? Pay particular attention to: the
self-review phase, the wording of the hard rules, the schema of the externalized
section, and how the ID is parsed from the `beans create` output.

```bash
git checkout solution/day-2-pm-01-planner-rework   # inspect solution/…
git checkout main                                  # back to your work
git show solution/day-2-pm-01-planner-rework:day-2-pm/01-planner-rework/solution/.claude/skills/planner/SKILL.md
```

## Learning Goals

- Skill refactor: rework an existing skill to produce a new output (bean creation instead of a plan file)
- Output discipline: the skill only writes via the CLI, never directly into `.beans/*.md`
- Abstraction-level discipline: separate the "what" from the "how"
- Hand-off design: one skill's output (the new bean ID) is the next one's input (`/refine <id>`)
