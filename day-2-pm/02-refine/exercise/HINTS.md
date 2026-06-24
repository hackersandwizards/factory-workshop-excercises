# Refine Skill Build Checklist

You are building a new `refine` skill from scratch. Output: a `## Refined Plan` section in the bean body with real file paths, signatures, and a test sketch. Inspired by Claude Code's plan mode.

## Prerequisite — Beans CLI

`beans --version` must run. `beans list` in `../sandbox/` shows three beans. The bean from Exercise 01 should already have a `## High-Level Plan` in its body.

## Required — Core Mechanic

- [ ] **Frontmatter** — `name: refine`, `argument-hint: <bean-id>`, `allowed-tools: Read, Grep, Glob, Bash, Task`
- [ ] **Phase 1 (Read Bean)** — parse `beans show --json <bean-id>`. Extract the body, find the `## High-Level Plan` section. Abort if missing.
- [ ] **Phase 2 (Status)** — `beans update <bean-id> -s in-progress`
- [ ] **Phase 3 (Explore via subagent)** — **one** Task subagent (`subagent_type: general-purpose`) with a focused prompt. Read-only. The subagent returns a structured map (Files / Functions / Integration points / Test patterns).
- [ ] **Phase 4 (Refined Plan)** — `beans update` has **no** `--body-append`. Instead: fetch the current body, concatenate locally, write it back via `--body-file`. Schema:
  - `### Files to change` — `path:line — what changes`
  - `### New signatures` — `ReturnType Class::method(Args)`
  - `### Test sketch` — test names + input → expected

  **Body-fetch trap:** use `beans show <bean-id> --json | jq -r '.body'` — the body sits at the top level. `beans query '{ bean(id:…){body} }' --json | jq -r '.data.bean.body'` returns **`null`** (no `data` wrapper) and the next `--body-file` write wipes the bean body. Check for non-null before writing.
- [ ] **Phase 5 (Self-Check)** — verify file paths via Glob/Read. Mark hallucinated paths as `:NEW` or fix them.

## Required — Discipline

- [ ] **Read-only on source** — the skill produces no `git status` diffs in `src/` or `tests/`
- [ ] **File paths verifiable** — no fabrication
- [ ] **Subagent in a fork** — the explore transcript does not land in the main context
- [ ] **Never edit `.beans/*.md` directly** — always via `beans update`
- [ ] **Abort cleanly** — when `## High-Level Plan` is missing from the body

## Self-Check before the Solution Comparison

```bash
cd ../sandbox
cp -r ../02-refine/exercise/.claude .
claude
> /refine refine-exercise-olqc
```

- [ ] `beans show refine-exercise-olqc` shows a `## Refined Plan` in the body with real `src/lexer.cpp`, `src/parser.cpp` paths
- [ ] `git grep` finds every referenced path
- [ ] `git status` in `sandbox/` shows no changes in `src/` or `tests/`
- [ ] The bean status is `in-progress`

## Bridge

Output → input for `/implement` in Exercise 03.
