# Day 2 · Exercise 03 — Implement (Refined Plan → Code on a Branch)

**Slot:** Block 4, pairing sessions · phase 3 of the Factory pipeline

## Goal

Build an `implement` skill that takes the ticket's Refined Plan, creates a
feature branch, implements + builds + tests + commits each step
individually, and finally writes an Implementation Log back into the
ticket. Never merge, never push.

> **Hard rules — do not skip, do not soften.** These are the ones the
> Hook block called out explicitly so they don't get lost in the Hackathon
> pace: **never commit to `main`**, **never `git push`**, **never
> `git merge`**, **tests must be green before every commit**. Say them out
> loud to your pair before you start coding the skill, not after.

## Prerequisites

- Your own repo's tests pass green on `main` before you start
- The ticket from `../02-refine` has a `## Refined Plan`, status
  in-progress
- Your toolchain is installed and you know your repo's build/test commands
- `git status` is clean, `HEAD` is on `main`

## Task

Detailed hints + build checklist + expected bugs: `exercise/HINTS.md`.
Skeleton: `exercise/.claude/skills/.gitkeep` — an empty starting point, the
skill is built from scratch.

1. Copy `exercise/.claude/` into the repo you're pairing on.
   `mkdir .claude/skills/implement && touch .claude/skills/implement/SKILL.md`.
2. Frontmatter: `name: implement`, `argument-hint: <ticket-id>`,
   `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`.
3. Phase 1 (Preflight): read the ticket, extract `## Refined Plan`. Check
   the working tree is clean. Check `HEAD == main`. If not → abort with a
   clear message.
4. Phase 2 (Branch): generate a slug from the ticket's title. Create the
   branch `feat/<ticket-id>-<slug>`. If it already exists → abort.
5. Phase 3 (Loop): per `### Files to change` entry: edit → build → test
   (your repo's own commands). If red: max 2 fix attempts, then abort. If
   green: commit with a descriptive message.
6. Phase 4 (Log): write the Implementation Log back into the ticket — branch
   name, a list of commit SHAs + descriptions, final test status.
7. Phase 5 (Status): if green → mark the ticket completed + append
   `## Summary of Changes`. If red → status stays in-progress, append notes.
8. Hard rules (see above): never commit to `main`, never `git push`, never
   `git merge`. Tests must be green before every commit. Never edit the
   ticket by hand — always through `beans update` or the Jira MCP.

## Self-Check

- `git branch` shows `feat/<ticket-id>-...`
- `git log feat/<ticket-id>-...` shows several small commits, one per
  logical step
- `main` is unchanged (`git log main` contains no new commits)
- Tests are green
- The ticket shows status completed, an `## Implementation Log` with branch
  + commits + status, and a `## Summary of Changes`
- For an artificially broken step → the skill stops after 2 attempts,
  writes `aborted-tests-red` into the log, status stays in-progress, and it
  does not ruin the repo

## Solution

No reference solution exists yet for this Barista-specific version — the
original repo's generic version lives on `solution/day-2-pm-03-implement`
(`day-2-pm/03-implement/`, calculator sandbox, beans-only). Useful for
comparing the preflight guards, the 2-attempt limit, and the branch-naming
logic; not for the Jira/beans dual-backend handling, which is new here.

```bash
git checkout solution/day-2-pm-03-implement   # inspect solution/…
git checkout client/barista                   # back to your own work
git show solution/day-2-pm-03-implement:day-2-pm/03-implement/solution/.claude/skills/implement/SKILL.md
```

## Learning Goals

- Hard constraints in skills: "never X" must be stated clearly, checkably,
  and unambiguously
- Test-driven implementation loop: build/test/commit per step is a safety
  pattern
- Fail loud instead of fail silent: a clean abort with state in the log
  beats "somehow done"
- End-to-end pipeline: Planner → Refine → Implement as a factory that
  carries a ticket from idea to branch — without the main conversation ever
  seeing the code

## Bridge

Output → input for `/review` in `../04-review`.
