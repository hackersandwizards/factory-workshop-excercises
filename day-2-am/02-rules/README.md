# Day 2 AM · Exercise 02 — Rules (pirate spin)

**Slot:** 10:10–10:40 · 30 minutes (15min build + stretch)

## Concept

Rules = scoped behavior instructions in `.claude/rules/<name>.md`. The `glob:` frontmatter defines when a rule loads → a rule **becomes part of the context only when a matching file is in play**.

Difference from CLAUDE.md / skills:

| Layer | Loading behavior | Example |
|-------|---------------|----------|
| **CLAUDE.md** | Always-on globally, across the whole repo | Project architecture, tech stack |
| **Rules** | Always-on per glob scope | Code conventions per file type |
| **Skills** | On-demand per description match | Workflow on request |

## Goal

The pirate returns — this time as a rule with a glob scope. The glob mechanic, made **visceral**: participants see the behavior change as they switch files, not just in theory.

**The pirate appears three times in the workshop:**

| Day | Layer | Where |
|-----|-------|----|
| Day 1 | CLAUDE.md | Always-on globally |
| Day 1 | Skill | On-demand per description |
| Day 2 AM | **Rule** | **Always-on per glob** |

Same content, different layer. The loading mechanic becomes tangible through experience.

## Steps

1. In the exercise folder: create `.claude/rules/pirate.md`
2. Frontmatter with `glob: "**/*.md"`
3. Body: short, one or two sentences ("Reply in pirate language when working on Markdown files")
4. Start Claude Code in the exercise folder
5. Test A: edit `README.md` or any `.md` file → ask for an edit → **pirate**
6. Test B: edit a non-MD file → ask for an edit → **normal**. Use the one for your stack: `main.cpp` (C++), `main.java` (Java), or `main.py` (Python).

## Verify

- When editing `.md` files, Claude switches into pirate language
- When editing `.cpp`/`.h`/`.java`/`.py` files, Claude stays normal
- The glob scope is the activation condition — not a description, not a skill trigger

## Stretch — conventions for your stack

For those who are quick: a second rule for your own language. Use a glob that matches your files and list a handful of conventions. Example (C++):

```markdown
---
glob: "**/*.{cpp,h,hpp}"
---

# Modern C++ Conventions

- `nullptr` instead of `NULL` or `0`
- Smart pointers (`std::unique_ptr`, `std::shared_ptr`) — no `new`/`delete`
- `auto` for iterator types and complex templates
- Rule-of-Five when you have a custom destructor
```

Globs for the other stacks: Java → `glob: "**/*.java"`, Python → `glob: "**/*.py"`.

Test it on the sample file for your stack (`main.cpp` / `main.java` / `main.py` — each carries a few intentional anti-patterns): ask Claude "What do you see in this file?" → it names the violations and cites the rule as the source.

## Bridge to the next exercise

Day 2 AM 03 — Subagents: where rules are **always-on per scope**, subagents are **on-demand in an isolated context**. Combo: rules define *how* code must look, subagents *execute* within that convention.

## Solution

The reference solution lives on branch **`solution/day-2-am-02-rules`** (kept off
`main` so it stays out of Claude's context) — four rule files under
`solution/.claude/rules/`: `pirate.md` (glob `**/*.md`) plus `cpp-modern.md`,
`java-modern.md`, `python-modern.md` (the per-language stretch rules). Try it
yourself first, then compare:

```bash
git checkout solution/day-2-am-02-rules   # inspect solution/.claude/rules/…
git checkout main                         # back to your work
git show solution/day-2-am-02-rules:day-2-am/02-rules/solution/.claude/rules/pirate.md
```
