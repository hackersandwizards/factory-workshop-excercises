# Rework Checklist

Starting point: `.claude/skills/planner/SKILL.md` (a copy from the Day 2 AM solution). You are reworking this skill — not building it from scratch. **If you have your own Day 2 AM skill**, replace the copy with it first.

## Prerequisite — Beans CLI

`brew install hmans/beans/beans` must be installed (check: `beans --version`). `.beans.yml` exists in `../sandbox/` (prefix `sandbox-`).

## Required — Bean-Creator Rework

- [ ] **Frontmatter** — `argument-hint: [brief feature description]` (optional, not `<bean-id>`). Adjust the description: "creates a new bean via beans CLI with description + High-Level Plan + AC".
- [ ] **Phase 1 (Capture)** — capture the feature idea from the user, reflect it back in one sentence
- [ ] **Phase 3 (Approaches) — STOP guard** — the skill presents 2-3 options and **waits for an explicit user choice**. Even if "autonomously" / "no clarifying questions" was stated earlier — picking an approach is a mandatory gate, not a clarification.
- [ ] **Phase 5 (Create Bean)** — **one** CLI call with the complete body:
  - `beans create "<title>" -t feature -d "<heredoc>"` with Description + notes + `## High-Level Plan` (Approach, Steps, AC, Non-Goals) in one go
  - The `beans` CLI has **no** `--body-append` flag. For very long bodies, use `--body-file <path>` instead of `-d`.
  - Then parse the ID from stdout for the user hand-off (`/refine <id>`).
- [ ] **Lock down the schema** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Heading contract** — the plan goes verbatim under the `## High-Level Plan` heading. `/refine` parses by exact match — if the heading is missing, Refine aborts.
- [ ] **Hard rule** — no file paths, no function signatures, no class names in the plan

## Required — Discipline

- [ ] Never edit `.beans/*.md` directly — always via the CLI
- [ ] Never edit source code — Planner is read-only on source
- [ ] The self-review phase (the 4★ mechanic from Day 2 AM) stays in

## Self-Check before the Solution Comparison

- [ ] `/planner Parenthesis support for calculator` → a new bean is created (`beans list` shows it)
- [ ] `beans show <new-id>` shows a Description + a `## High-Level Plan` with Approach/Steps/AC/Non-Goals
- [ ] The plan contains **no** `src/lexer.cpp`, **no** `tokenize()`, **no** line reference
- [ ] The skill refuses gracefully when the `beans` CLI is missing

## Run

```bash
cd ../sandbox
cp -r ../01-planner-rework/exercise/.claude .
claude
> /planner Parenthesis support for calculator
```

## Bridge

This skill's output = a new bean ID. The input for `/refine <bean-id>` in Exercise 02. A High-Level Plan + AC are enough — files and signatures come only there.
