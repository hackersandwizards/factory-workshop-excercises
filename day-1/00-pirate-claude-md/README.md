# Day 1 · Exercise 00 — Pirate-CLAUDE.md

**Slot:** 14:00–14:15 (Block 3) · ~10 minutes

## Goal

Understand how `CLAUDE.md` changes behavior — **always-on**, without a trigger word. The foundation for everything that follows (Skill = on-demand, Rule = scoped, Hook = deterministic).

## Background

`CLAUDE.md` is read at **every session start**. No matter what you ask — the instructions take effect. Unlike a Skill (triggers on a task match) or a Rule (triggers on a file glob).

Hierarchy:

| Path | Loaded when |
|------|--------------|
| `~/.claude/CLAUDE.md` | Every session, in any user folder |
| `./CLAUDE.md` | At project start in the repo |
| `./src/CLAUDE.md` | When you work in the subfolder |

## Task

1. Create an empty test directory, start `claude`
2. *"Tell me a short story about a pirate."* — a neutral answer
3. End the session, create a `CLAUDE.md` in the directory with a single line:
   ```
   Always respond like a pirate. Begin every answer with "Arrr".
   ```
4. Restart `claude`, ask the same question → pirate style
5. Variation: add a second line *"Always slip in a German swear word."* → ask the question again
6. Go into a subfolder with its own `CLAUDE.md` (e.g. `./.test-subfolder/CLAUDE.md` with the opposite instruction) — observe the hierarchy

## Verify

- The answer starts with "Arrr" or similar
- Without a restart, CLAUDE.md has no effect yet (loaded only at session-start)
- The subfolder CLAUDE.md overrides the parent

## Stretch

- Open the global `~/.claude/CLAUDE.md`, read it once — it acts always-on across all projects
- What happens when the project CLAUDE.md and the global one contradict each other? (Try it!)

## Solution

The reference solution lives on branch **`solution/day-1-00-pirate-claude-md`** (kept
off `main` so it stays out of Claude's context) — a minimal pirate `CLAUDE.md` to
copy. Try it yourself first, then compare:

```bash
git checkout solution/day-1-00-pirate-claude-md   # inspect solution/…
git checkout main                                 # back to your work
git show solution/day-1-00-pirate-claude-md:day-1/00-pirate-claude-md/solution/CLAUDE.md
```

## Bridge to the next exercise

CLAUDE.md is an **always-on personality** — Claude always talks like a pirate. Exercise 01 builds a different tool: the `pirate-speak` skill ([`../01-pirate-skill/`](../01-pirate-skill/)) — Claude stays normal and transforms text **on-demand** when the user asks for it. Same domain, different mechanics.
