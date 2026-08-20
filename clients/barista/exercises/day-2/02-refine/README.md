# Day 2 · Exercise 02 — Refine (Plan → Refined Plan)

**Slot:** Block 4, pairing sessions · phase 2 of the Factory pipeline

## Goal

Build a `refine` skill that takes the ticket your planner created (Jira
issue or bean, `## High-Level Plan` in the body/description), explores your
**own repo** via a **subagent fork** (protecting the main conversation's
context), and writes a concrete `## Refined Plan` back into the ticket —
real files, signatures, and a test sketch.

> **Your repo, not a sandbox.** Unlike the Day 1 planner exercise, there is
> no shared calculator sandbox here — pair up on a real, non-critical piece
> of your own stack (same repo/module you picked or a neighbouring one).
> Refine is language-neutral: it explores whatever source the subagent
> finds and writes paths/signatures in your language.

## Prerequisites

- A ticket exists with `## High-Level Plan` in the body (Jira description or
  bean body) — from `../01-planner`, or your own Day 1 planner run
- The `beans` CLI is installed if you're on the beans fallback; the Jira MCP
  is reachable if you're on Jira
- Understanding: the Task tool dispatches subagents into isolated
  sub-contexts

## Task

Detailed hints + build checklist: `exercise/HINTS.md`. Skeleton:
`exercise/.claude/skills/.gitkeep` — an empty starting point, the skill is
built from scratch.

1. Copy `exercise/.claude/` into the repo you're pairing on.
   `mkdir .claude/skills/refine && touch .claude/skills/refine/SKILL.md`.
2. Frontmatter: `name: refine`, `argument-hint: <ticket-id>`,
   `allowed-tools: Read, Grep, Glob, Bash, Task` (+ your Jira MCP tool if
   applicable). (No `Edit` — the ticket is written via `beans update` or the
   Jira MCP, never by hand.)
3. Phase 1: read the ticket (`beans show --json <id>` or the Jira issue via
   MCP), extract `## High-Level Plan`. Missing → abort.
4. Phase 2: mark it in-progress (`beans update <id> -s in-progress` or the
   Jira transition your board uses).
5. Phase 3: dispatch **ONE** subagent via the Task tool
   (`subagent_type=general-purpose`). Word the prompt so it forces the
   subagent to return a structured map (Files, Functions, Integration
   points, Test patterns). Read-only.
6. Phase 4: write the Refined Plan back — `beans update <id> --body-append`
   or a Jira description update via MCP — schema `### Files to change` /
   `### New signatures` / `### Test sketch`. Line numbers come from the
   subagent output, not from imagination.
7. Phase 5: self-check — verify every file path via Glob/Grep against your
   actual repo. No hallucinations. `git status` shows no source diffs.
8. Test: run `/refine <ticket-id>`. Check the ticket.

## Self-Check

- The ticket shows a `## Refined Plan` with real paths + line numbers from
  your repo
- The paths really exist (`ls <path>` without error)
- No source files were edited (`git status` shows no changes outside the
  ticket/bean bookkeeping)
- The ticket status is in-progress
- The subagent output does NOT land as a long dump in the main conversation
  history — only the structured map flows into the Refined Plan

## Solution

No reference solution exists yet for this Barista-specific version — the
original repo's generic version lives on `solution/day-2-pm-02-refine`
(`day-2-pm/02-refine/`, calculator sandbox, beans-only). Useful for
comparing the subagent-fork mechanic and the anti-hallucination self-check;
not for the Jira/beans dual-backend handling, which is new here.

```bash
git checkout solution/day-2-pm-02-refine   # inspect solution/…
git checkout client/barista                # back to your own work
git show solution/day-2-pm-02-refine:day-2-pm/02-refine/solution/.claude/skills/refine/SKILL.md
```

## Learning Goals

- The Task tool as a context-saving mechanism: the subagent consumes its own
  context, only the findings come back
- Plan refinement as its own phase: the "what" becomes the "how" —
  controlled, with verification
- Anti-hallucination: every claimed file must be verifiable, otherwise it
  gets dropped
- Skill composition: one skill's output (Planner) is the cleanly structured
  input of the next (Refine)

## Bridge

Output → input for `/implement` in `../03-implement`.
