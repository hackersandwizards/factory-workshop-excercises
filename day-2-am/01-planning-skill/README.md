# Day 2 AM · Übung 01 — Planning-Skill

**Slot:** 09:00–10:10 · 70 Minuten

## Ziel

Eigenen Planning-Skill bauen, der ein **4-Mechaniken-Subset** aus `obra/superpowers/brainstorming` umsetzt. Output ist ein **Markdown-Plan-File** in `.plans/<task>.md` — Bean-File-Form, die in PM-Factory wiederkehrt.

## Pädagogisches Pattern: Demo → Deconstruct → Reconstruct

| Phase | Was | Dauer |
|-------|-----|-------|
| Demo | Trainer Walk-Through `obra/superpowers/brainstorming` SKILL.md auf GitHub | 10min |
| Deconstruct | Plenum: was sehen wir? 8 Mechaniken extrahieren | 10min |
| Reconstruct | Eigener Planning-Skill mit `/skill-creator`, 4★ Subset | 25min |
| Share-out | Description + File-Output mit Nachbarn checken | 5min |

Rest ist Puffer + Übergang Rules.

## Referenz-Skill

`https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md`

**Inspiration, nicht Template.** Eigenen massgeschneiderten Anzug bauen.

## Die 8 Mechaniken

| Mechanik | Was es bewirkt | |
|----------|----------------|---|
| **Explore project context** | Recon vor Frage — kein Blind-Plan | ★ |
| **Eine Frage pro Message** | Explizite Entscheidungspunkte | ★ |
| **2-3 Alternativen vor Convergenz** | Force-the-trade-off | ★ |
| **Self-Review (Guardrail)** | Check vor Plan-Abschluss | ★ |
| Spec → File, nicht Conversation | File ist Vertrag | |
| Hard Approval Gate | Plan + Execute getrennt | |
| Constraints/Non-Goals explizit | Scope-Creep verhindern | |
| Wiederholbare Routine | Process > Inspiration | |

★ = Pflicht-Subset für die Übung. Rest sehen, später ergänzen.

Build-Checkliste: [`exercise/HINTS.md`](exercise/HINTS.md).

## Schritte (Reconstruct)

1. Planning-Domäne aus eigenem Stack wählen:
   - `refactor-planner`, `migration-planner`, `test-coverage-planner`, `feature-planner`
   - Oder: SSW-domain-spezifisch
2. `/skill-creator` starten — Interview-Flow durch Frontmatter + Body
3. `name` + `description` (Description = Activation-Key)
4. Workflow-Body mit **4★ Pflicht-Subset**: Explore Context · Eine Frage pro Message · 2-3 Approaches · Self-Review
5. Output-Pfad: Skill schreibt Plan nach `.plans/<task>.md`
6. Testen: Trigger-Phrase eingeben → triggert Skill? → schreibt er wirklich `.md`-File?

## Verify

- Description triggert für richtige Tasks, nicht für falsche
- Nachbar liest Description und versteht wann zu triggern
- 4★ Mechaniken im Workflow erkennbar
- Output landet als File in `.plans/`, nicht nur in Conversation

## Stretch

- Restliche 4 Mechaniken ergänzen (Approval Gate, Constraints, etc.)
- Skill mit mehreren Trigger-Phrasen testen, Activation tunen
- Eigenen Subagent-Type via `.claude/agents/<name>.md` definieren und im Skill via `agent:` referenzieren

## Brücke zu PM

Markdown-File in `.plans/` = **Bean-File-Form**. PM-Factory nutzt File-as-Contract zwischen Agents — Planning-Skill ist der erste Schritt in Richtung Multi-Agent-Pipeline.

## Solution

Ein generischer Referenz-Skill in `solution/`:
- [`planner/SKILL.md`](solution/.claude/skills/planner/SKILL.md) — domain-agnostisch, 4★ Subset + Externalize-Phase

Erst selbst bauen. Dann vergleichen wie das Subset abgebildet ist.
