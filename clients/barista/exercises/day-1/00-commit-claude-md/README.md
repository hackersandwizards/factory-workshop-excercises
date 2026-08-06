# Day 1 · Exercise 00 — Commit-Convention CLAUDE.md

**Slot:** Block 1, ~10 minutes (Foundations, Hook + start of Mechanism)

## Goal

Understand how CLAUDE.md changes behaviour — **always active**, no trigger
word needed. This is the foundation for everything that follows (Skill =
on-demand, Rule = scoped).

## Background

CLAUDE.md is read at **every session start**. Whatever you ask, the
instructions apply. That is different from a Skill (triggers on a task
match) or a Rule (triggers on a file glob).

Hierarchy:

| Path | Loaded when |
|------|-------------|
| `~/.claude/CLAUDE.md` | Every session, in every user folder |
| `./CLAUDE.md` | On project start inside the repo |
| `./services/legacy/CLAUDE.md` | When working in that subfolder |

## Task

1. Create an empty test directory and start `claude`.
2. Show the diff `exercise/sample.diff` and ask: *"Write a commit message
   for this diff."* → generic result (no fixed format, no ticket reference,
   no scope).
3. End the session, create a `CLAUDE.md` in the directory with the
   convention you want, for example:
   ```
   Commit messages always follow this format:
   <type>(<scope>): <subject in the imperative, max. 72 characters>

   <body: why this change was necessary>

   Ref: <ticket ID, if there is one>
   ```
4. Restart `claude` and ask the same question → the convention is followed.
5. Variation: add a second line ("Scope is always the top-level directory
   name of the largest changed path") → ask again.
6. Move into a subfolder that has its own `CLAUDE.md` (e.g.
   `./services/legacy/CLAUDE.md` with a different convention) — watch the
   hierarchy live.

## Verify

- The commit message now follows Type/Scope/Body/Ref.
- Without a restart the CLAUDE.md has no effect yet (it is only loaded at
  session start).
- The subfolder CLAUDE.md **overrides** the parent one instead of adding to
  it.

## Stretch

- Open your global `~/.claude/CLAUDE.md` and read it once — it applies
  across all projects, always.
- What happens when the project CLAUDE.md and the global one contradict
  each other? (Try it!)

## Bridge to the next exercise

CLAUDE.md is an **always-active convention** — every commit message follows
the same format, in every context. Exercise 01 builds the same effect as a
**Skill**: on-demand, and able to adapt when an assumption turns out to be
wrong instead of failing rigidly.

## Solution

The reference solution lives on branch
**`solution/barista-day-1-00-commit-claude-md`** (deliberately not on
`client/barista`, so it does not end up in Claude's context — still to be
created). Try it yourself first, then compare.
