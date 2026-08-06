# Day 1 · Exercise 02 — Commit Rule: scope by path

**Slot:** Block 1, ~15 minutes (Rules & Hooks short demo, opener)

## Concept

Rules = `.claude/rules/<name>.md`, activated via the `paths:` frontmatter (a
list of glob patterns) — **always active, but only for matching files**.
Not global like CLAUDE.md, not on-demand like a Skill.

## The actual question this exercise answers

CLAUDE.md and Skill (exercises 00/01) give **one** commit convention for the
whole repo. The obvious question is: "So what does the Rule do — another
commit convention, just a third variant?" No — and the reason is
instructive:

**A Rule reacts to *which files are being touched*, not to *which action is
about to happen*.** There is no glob for "a commit message is being written
right now" — a commit is an action, not a file pattern. What you can
sensibly scope by glob is not *whether* a convention applies, but *which
variant* of it applies, depending on **where** you are in the repo.

In a heterogeneous repo landscape like Barista's that is the normal case:
different teams/services in the same repo want different commit scopes,
without anyone having to remember by hand which one currently applies.

## Task

`exercise/` contains two placeholder areas (**replace with real Barista
paths before the workshop if you bring an example repo**):

```
exercise/
├── services/api/handler.py
└── services/frontend/component.tsx
```

1. Create `.claude/rules/commit-scope-api.md`:
   ```yaml
   ---
   paths:
     - "services/api/**"
   ---
   Commits touching files under `services/api/` use the scope
   `api`: `<type>(api): <subject>`.
   ```
2. Create `.claude/rules/commit-scope-frontend.md`:
   ```yaml
   ---
   paths:
     - "services/frontend/**"
   ---
   Commits touching files under `services/frontend/` use the scope
   `frontend`: `<type>(frontend): <subject>`.
   ```
3. Start Claude Code inside the `exercise/` folder.
4. Change `services/api/handler.py`, ask for a commit message → scope `api`.
5. Change `services/frontend/component.tsx`, ask for a commit message →
   scope `frontend`.
6. Change a file outside both paths (e.g. `README.md`) → neither rule
   applies, only the CLAUDE.md/Skill convention from exercises 00/01 is
   left (no specific scope).

## Verify

- The scope switches automatically with the path being edited, without
  anyone announcing it.
- Files outside both globs fall back to the general convention.
- Both rules are active at the same time with no conflict, because their
  globs do not overlap.

## Stretch

- What happens when two rules with **overlapping** globs contradict each
  other? (Try it — a good hook for the Block 2 twist: "always active" does
  not mean "always unambiguous".)

## Bridge to the Hooks short demo

The rule here is still a **request** — technically nothing stops Claude from
ignoring the scope. The hooks demo right afterwards (`.env` block) shows the
difference to a hard guardrail.

## Solution

The reference solution lives on branch
**`solution/barista-day-1-02-commit-rule`** (deliberately not on
`client/barista`, so it does not end up in Claude's context) — both rule
files. Build it yourself first, then compare:

```bash
git checkout solution/barista-day-1-02-commit-rule   # inspect solution/.claude/rules/…
git checkout client/barista                          # back to your own work
git show solution/barista-day-1-02-commit-rule:clients/barista/exercises/day-1/02-commit-rule/solution/.claude/rules/commit-scope-api.md
```
