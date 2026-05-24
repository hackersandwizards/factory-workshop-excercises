# Day 1 · Übung 01 — Pirate-Skill

**Slot:** Block 4a, ~30 Minuten

## Ziel

Pirate-Effekt aus Trainer-Demo als **Skill** verpacken. Warum Skill statt CLAUDE.md? On-demand statt always-on, triggert durch Task-Match, wiederverwendbar.

## Schritte

1. In dein Test-Projekt (oder hier in `exercise/`): `.claude/skills/pirate-mode/SKILL.md` anlegen
2. Frontmatter setzen:
   ```yaml
   ---
   name: pirate-mode
   description: Use when the user wants responses in pirate language
   ---
   ```
3. Body: Pirate-Verhalten beschreiben — "Arrr", "matey", "ye", in Character bleiben
4. Test: Frage stellen, die den Skill triggern sollte (z.B. *"How's the weather in Hamburg?"*)
5. Variation: Activation tunen — wann triggert, wann nicht?

## Verify

- Frage triggert Skill → Antwort in Pirate-Sprache
- Andere Frage (Code-Refactoring) triggert **nicht** → Skill bleibt off

## Was du lernst

- SKILL.md = Markdown, nichts Magisches
- `description` ist Activation-Key — Agent entscheidet selbst ob triggern
- Wiederverwendbar über Projekte hinweg
- On-demand-Loading spart Tokens

## Stretch

- Variation: Spanisch-Skill, Emoji-Start-Skill, ASCII-Art-Skill
- `/skill-creator` Demo (Anthropic's eigener Skill) — professionelles Skill-Building per Interview-Flow

## Brücke zu Tag 2

Tag 2 AM bauen wir ernsthaftere Skills — Planning-Skills mit 6 Mechaniken. Pirate-Skill war Aufwärm.

## Solution

Siehe [`solution/.claude/skills/pirate-mode/SKILL.md`](solution/.claude/skills/pirate-mode/SKILL.md) — Reference-Implementation. Erst selbst probieren, dann vergleichen.
