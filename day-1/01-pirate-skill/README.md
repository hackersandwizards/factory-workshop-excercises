# Day 1 · Exercise 01 — Pirate-Skill

**Slot:** Block 4a, ~30 minutes

## Goal

Build a skill that transforms text into pirate speech **on-demand**. In contrast to Exercise 00 (CLAUDE.md, an always-on personality): here a **tool** that only kicks in when someone says "piraterize this" or similar.

## What sets this apart from the CLAUDE.md pirate?

| | CLAUDE.md (00) | Skill (01) |
|---|---|---|
| Trigger | Always-on, every session | On-demand, on a task match |
| Effect | Claude always talks like a pirate | Claude stays normal, transforms only when asked |
| Location | `./CLAUDE.md` | `.claude/skills/<name>/SKILL.md` |
| Token cost | Every turn | Only when activated |

A skill is a tool in the toolbox. CLAUDE.md is a character layer.

## Steps

1. In a test project (or here in `exercise/`): create `.claude/skills/pirate-speak/SKILL.md`
2. Set the frontmatter — **the description is the activation key**; name precise trigger phrases:
   ```yaml
   ---
   name: pirate-speak
   description: Rephrase text in pirate language. Use when the user asks to "piraterize", "make it pirate", "talk like a pirate", or wants any text converted to pirate dialect.
   ---
   ```
3. Body: what the skill does
   - Vocabulary swaps (you→ye, hello→ahoy, the→th', ...)
   - Interjections ("Arrr!", "Avast!", "Shiver me timbers!"), used sparingly
   - Grammar shifts (-ing → -in', "going to" → "settin' sail to")
   - **What must NOT be touched:** code, URLs, file paths, technical identifiers
4. Test without the skill: *"Make this pirate: Hello team, I'll update the deployment."* → does it trigger?
5. Test with an irrelevant question: *"What's the weather in Hamburg?"* → does **not** trigger, the skill stays off
6. Tune the description until the trigger behavior is clean

## Verify

- A trigger phrase activates the skill → the text gets transformed
- A normal question (code, weather) lets the skill stay asleep
- Code blocks / URLs / paths stay unchanged in the pirate output

## What you learn

- SKILL.md = Markdown, nothing magical
- `description` is the activation key — the agent decides for itself whether to trigger; the more precise, the more reliable
- Anti-pattern: too generic a description → the skill triggers constantly or never
- Preserving rules matter (what stays, what gets transformed) — otherwise the skill destroys code

## Stretch

- Mode switching: `light` vs `medium` vs `heavy` intensity based on a user hint
- File-replace mode: "Piraterize README.md" → the skill reads the file, transforms it, writes it back (code blocks untouched)
- `/skill-creator` demo (Anthropic's own skill) — skill building via an interview flow

## Bridge to Day 2

On Day 2 AM we build more serious skills — planning skills with 6 mechanics. Pirate-speak was the warm-up: it shows frontmatter + activation triggers + preserving rules. Three building blocks that recur in every skill.

## Solution

[`solution/.claude/skills/pirate-speak/SKILL.md`](solution/.claude/skills/pirate-speak/SKILL.md) — a reference implementation with a vocabulary table, interjections, grammar shifts, preserving rules, operating modes, and calibration. Try it yourself first, then compare.
