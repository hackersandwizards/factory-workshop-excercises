# Day 2 AM · Übung 01 — Planning-Skill

**Slot:** 09:00–10:00 · 60 Minuten

## Ziel

Eigenen Planning-Skill bauen, der mindestens **3 der 6 Mechaniken** für gutes Planen nutzt. Brücke zu PM: dieser Skill wird als `@refine`-Subagent wiederkehren.

## Pädagogisches Pattern: Consume → Deconstruct → Reconstruct

| Phase | Was | Dauer |
|-------|-----|-------|
| A — Concept-Anker | SKILL.md-Struktur kurz | 5min |
| B — Show | Trainer demo Superpowers / Brainstorm-Skill live | 10min |
| C — Deconstruct | Plenum: Welche Mechaniken machen Planen gut? | 15min |
| D — Reconstruct | Eigener Planning-Skill bauen | 25min |
| Share-out | Description-Check mit Nachbarn | 5min |

## Die 6 Mechaniken (Phase C — Target-Liste)

| Mechanik | Was es bewirkt |
|----------|----------------|
| Eine Frage pro Message (Multiple-Choice) | Explizite Entscheidungspunkte, kein Sammeln vager Wünsche |
| 2-3 Alternativen vor Convergenz | Force-the-trade-off, nicht "first idea wins" |
| Spec → File, nicht Conversation | File ist Vertrag, Conversation ist flüchtig |
| Hard Approval Gate vor Implementation | Plan- + Execute-Phase getrennt |
| Constraints/Non-Goals explizit | Verhindert Scope-Creep + Vagueness |
| Wiederholbare Routine | Process > Inspiration, jeder kann's nachmachen |

Siehe auch [`exercise/HINTS.md`](exercise/HINTS.md) als Build-Checkliste.

## Schritte (Phase D)

1. Wähle eine Planning-Domäne aus deinem Stack:
   - `refactor-planner`, `migration-planner`, `test-coverage-planner`, `feature-planner`
   - Oder: SSW-domain-spezifisch
2. `.claude/skills/<dein-name>/SKILL.md` anlegen
3. Frontmatter: `name` + `description` (Description = Activation-Key!)
4. Workflow-Body mit **mindestens 3 der 6 Mechaniken**
5. Testen: Trigger-Phrase eingeben → triggert Skill?

## Verify

- Description triggert für richtige Tasks, nicht für falsche
- Nachbar liest Description und versteht wann zu triggern
- Mindestens 3 Mechaniken im Workflow erkennbar

## Stretch

- Skill mit `/skill-creator` (Anthropic's Skill) professionell bauen — Interview-Flow
- Skill testen mit mehreren Trigger-Phrasen, Activation tunen

## Brücke zu nächster Übung

Tag 2 AM 02 — Rules: Was Skills on-demand sind, sind Rules always-on per File-Scope.

## Solution

Zwei Referenz-Skills in `solution/`:
- [`refactor-planner/SKILL.md`](solution/.claude/skills/refactor-planner/SKILL.md) — Refactoring planen
- [`migration-planner/SKILL.md`](solution/.claude/skills/migration-planner/SKILL.md) — Migration planen

Erst selbst probieren. Dann vergleichen welche Mechaniken die Solutions nutzen.
