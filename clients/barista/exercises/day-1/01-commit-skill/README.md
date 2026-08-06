# Day 1 · Exercise 01 — Commit Skill: Purpose vs. Instructions

**Slot:** Block 1, ~20 minutes (Foundations, Mechanism)

## Goal

Build the same effect as exercise 00 as a **Skill** — and experience live
why a purpose-described skill is more robust than a step-by-step one. This
runs **alongside**, without a label and without a slide — it is picked up
later, in the Block 2 twist.

## Two variants

Both are supposed to produce a commit message that follows the convention.
Build them in `exercise/.claude/skills/`:

**Variant A — `commit-message-strict`:** precise step-by-step instructions.

```yaml
---
description: Creates a commit message. Follow the steps.
---

1. Open the file `CHANGELOG.md` in the repo root.
2. Read the latest entry to determine the current scope.
3. Write: <type>(<scope from step 2>): <subject>
4. Add the body from the diff.
```

**Variant B — `commit-message-purpose`:** purpose instead of steps.

```yaml
---
description: Creates a commit message following the team convention (Type/Scope/Body/Ref). Use whenever a commit is due.
---

Goal: a commit message that still explains in six months why the change was
made. Derive type and scope from the actual content of the change, not from
a fixed source. Body: why, not just what.
```

## Test — the failure

`exercise/` deliberately contains **no** `CHANGELOG.md`. Ask Claude Code
with each skill separately for a commit message for
`../00-commit-claude-md/exercise/sample.diff`:

- **Strict:** step 1 fails (the file is missing) — Claude gets stuck,
  guesses, or gives up, because the prescribed source is not there.
- **Purpose:** derives the scope from the diff content anyway and produces
  something usable.

## Verify

- The strict variant produces a visibly worse result, or none at all, when
  the expected file is missing.
- The purpose variant produces a usable result in the same situation.

## What you learn

- More precise instructions are not automatically more robust — they are
  only more robust **as long as the assumption holds**.
- A purpose description leaves the model the judgement you are employing it
  for in the first place.

## Bridge to the next exercise

CLAUDE.md and Skill give you **one** convention, wherever you are in the
repo. Exercise 02 shows the limit of that: in a heterogeneous repo
landscape like Barista's you sometimes need different conventions depending
on **where** you are in the repo — that is what a Rule is for.

## Solution

The reference solution lives on branch
**`solution/barista-day-1-01-commit-skill`** (still to be created) — both
SKILL.md variants. Build it yourself first, then compare.
