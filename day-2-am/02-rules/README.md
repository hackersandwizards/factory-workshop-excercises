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
6. Test B: edit `main.cpp` (or any other non-MD file) → ask for an edit → **normal**

## Verify

- When editing `.md` files, Claude switches into pirate language
- When editing `.cpp`/`.h`/`.py` files, Claude stays normal
- The glob scope is the activation condition — not a description, not a skill trigger

## Stretch — C++ conventions

For those who are quick: a second rule for your own stack.

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

Test it on a file with anti-patterns: ask Claude "What do you see in this file?" → it names the violations and cites the rule as the source.

## Bridge to the next exercise

Day 2 AM 03 — Subagents: where rules are **always-on per scope**, subagents are **on-demand in an isolated context**. Combo: rules define *how* code must look, subagents *execute* within that convention.

## Solution

- [`solution/.claude/rules/pirate.md`](solution/.claude/rules/pirate.md) — pirate rule, glob `**/*.md`
- [`solution/.claude/rules/cpp-modern.md`](solution/.claude/rules/cpp-modern.md) — C++ stretch rule
