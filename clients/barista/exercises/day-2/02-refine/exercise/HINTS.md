# Refine Skill Build Checklist

You are building a new `refine` skill from scratch. Output: a `## Refined
Plan` section written back into the ticket, with real file paths,
signatures, and a test sketch. Inspired by Claude Code's plan mode.

## Prerequisite — your ticket backend

Same dual backend as the Day 1 planner: **Jira** (default, via MCP) or
**`beans`** (fallback). The ticket from `../01-planner` should already have
a `## High-Level Plan`. Everything below applies to both — only the
read/write calls in Phase 1 and Phase 4 differ.

## Required — Core Mechanic

- [ ] **Frontmatter** — `name: refine`, `argument-hint: <ticket-id>`,
  `allowed-tools: Read, Grep, Glob, Bash, Task` (+ Jira MCP tool if used)
- [ ] **Phase 1 (Read ticket)** — Jira: fetch the issue via MCP, read the
  description. Beans: `beans show --json <id>`, read the body. Find the
  `## High-Level Plan` section. Abort if missing.
- [ ] **Phase 2 (Status)** — move the ticket to in-progress (Jira
  transition or `beans update <id> -s in-progress`)
- [ ] **Phase 3 (Explore via subagent)** — **one** Task subagent
  (`subagent_type: general-purpose`) with a focused prompt against your own
  repo. Read-only. The subagent returns a structured map (Files / Functions
  / Integration points / Test patterns).
- [ ] **Phase 4 (Refined Plan)** — write back without clobbering the
  existing description/body: fetch current content, concatenate locally,
  write it back in one call (`beans update --body-file`, or a Jira
  description update via MCP). Schema:
  - `### Files to change` — `path:line — what changes`
  - `### New signatures` — in your repo's language
  - `### Test sketch` — test names + input → expected

  **Beans body-fetch trap:** use `beans show <id> --json | jq -r '.body'`.
  `beans query '{ bean(id:…){body} }' --json | jq -r '.data.bean.body'`
  returns **`null`** and the next `--body-file` write wipes the bean body.
  Check for non-null before writing.
- [ ] **Phase 5 (Self-Check)** — verify file paths via Glob/Read against
  your actual repo. Mark hallucinated paths as `:NEW` or fix them.

## Required — Discipline

- [ ] **Read-only on source** — the skill produces no `git status` diffs
- [ ] **File paths verifiable** — no fabrication
- [ ] **Subagent in a fork** — the explore transcript does not land in the
  main context
- [ ] **Never edit the ticket by hand** — always via `beans update` or the
  Jira MCP, never a direct file/API edit around it
- [ ] **Abort cleanly** — when `## High-Level Plan` is missing

## Self-Check before comparing against the generic solution

```bash
cd <your repo>
cp -r ../02-refine/exercise/.claude .
claude
> /refine <ticket-id>
```

- [ ] The ticket shows a `## Refined Plan` with real source paths
- [ ] `git grep` finds every referenced path
- [ ] `git status` shows no changes in source/test dirs
- [ ] The ticket status is in-progress

## Bridge

Output → input for `/implement` in `../03-implement`.
