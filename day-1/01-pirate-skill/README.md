# Day 1 · Übung 01 — Pirate-Skill

**Slot:** Block 4a, ~30 Minuten

## Ziel

Skill bauen, der **on-demand** Text in Piraten-Sprache umwandelt. Kontrast zu Übung 00 (CLAUDE.md, always-on Persönlichkeit): hier ein **Werkzeug**, das nur greift wenn jemand "piraterize this" o.ä. sagt.

## Was unterscheidet das vom CLAUDE.md-Pirate?

| | CLAUDE.md (00) | Skill (01) |
|---|---|---|
| Trigger | Always-on, jede Session | On-demand, per Task-Match |
| Effekt | Claude redet immer pirate | Claude bleibt normal, transformiert nur wenn gefragt |
| Ort | `./CLAUDE.md` | `.claude/skills/<name>/SKILL.md` |
| Token-Cost | Jeder Turn | Nur wenn aktiviert |

Skill = Tool im Werkzeugkasten. CLAUDE.md = Charakter-Layer.

## Schritte

1. Test-Projekt (oder hier in `exercise/`): `.claude/skills/pirate-speak/SKILL.md` anlegen
2. Frontmatter setzen — **Description ist der Activation-Key**, präzise Trigger-Phrasen nennen:
   ```yaml
   ---
   name: pirate-speak
   description: Rephrase text in pirate language. Use when the user asks to "piraterize", "make it pirate", "talk like a pirate", or wants any text converted to pirate dialect.
   ---
   ```
3. Body: was der Skill tut
   - Vocabulary-Swaps (you→ye, hello→ahoy, the→th', ...)
   - Interjections ("Arrr!", "Avast!", "Shiver me timbers!") sparsam
   - Grammar-Shifts (-ing → -in', "going to" → "settin' sail to")
   - **Was NICHT angefasst wird:** Code, URLs, file paths, technische Identifier
4. Test ohne Skill: *"Make this pirate: Hello team, I'll update the deployment."* → triggert?
5. Test mit irrelevanter Frage: *"What's the weather in Hamburg?"* → triggert **nicht**, Skill bleibt off
6. Tune Description bis Trigger-Verhalten sauber ist

## Verify

- Trigger-Phrase aktiviert Skill → Text wird transformiert
- Normale Frage (Code, Wetter) lässt Skill schlafen
- Code-Blöcke / URLs / Paths bleiben in Pirate-Output unverändert

## Was du lernst

- SKILL.md = Markdown, nichts Magisches
- `description` ist Activation-Key — Agent entscheidet selbst ob triggern; je präziser, desto verlässlicher
- Anti-Pattern: zu generische Description → Skill triggert ständig oder nie
- Preserving-Rules wichtig (was bleibt, was wird transformiert) — sonst zerstört Skill Code

## Stretch

- Mode-Switching: `light` vs `medium` vs `heavy` Intensität per User-Hint
- File-Replace-Mode: "Piraterize README.md" → Skill liest Datei, transformiert, schreibt zurück (Code-Blöcke unangetastet)
- `/skill-creator` Demo (Anthropic's eigener Skill) — Skill-Building per Interview-Flow

## Brücke zu Tag 2

Tag 2 AM bauen wir ernsthaftere Skills — Planning-Skills mit 6 Mechaniken. Pirate-Speak war Aufwärm: zeigt Frontmatter + Activation-Trigger + Preserving-Rules. Drei Bausteine, die in jedem Skill wiederkehren.

## Solution

[`solution/.claude/skills/pirate-speak/SKILL.md`](solution/.claude/skills/pirate-speak/SKILL.md) — Reference-Implementation mit Vocabulary-Tabelle, Interjections, Grammar-Shifts, Preserving-Rules, Operating-Modes, Calibration. Erst selbst probieren, dann vergleichen.
