# Day 2 PM · Übung 02 — Refine (Plan → Refined Plan)

**Slot:** ~50 Minuten · Phase 2 der Factory-Pipeline

## Ziel

Einen `refine` Skill bauen, der eine Bean mit gefülltem High-Level Plan nimmt, die Codebase via **Subagent-Fork** explored (Context-Schutz für die Haupt-Konversation) und einen konkreten `## Refined Plan` mit echten Files, Signaturen und Test-Sketch in die Bean schreibt.

## Voraussetzung

- Sandbox-Calculator unter `../sandbox/` ist gebaut (`cmake -B build && cmake --build build`)
- Bean hat einen gefüllten `## High-Level Plan` (aus Übung 01)
- Verständnis: Task-Tool dispatched Subagents in isolierten Sub-Contexts

## Aufgabe

Detail-Hinweise + Build-Checkliste: `exercise/HINTS.md`. Skeleton: `exercise/.claude/skills/.gitkeep` — leerer Startpunkt, Skill von Null gebaut.

1. `exercise/.claude/` in Sandbox kopieren: `cp -r exercise/.claude ../sandbox/`. Dann `mkdir ../sandbox/.claude/skills/refine && touch ../sandbox/.claude/skills/refine/SKILL.md`.
2. Frontmatter: `name: refine`, `argument-hint: <bean-id>`, `allowed-tools: Read, Grep, Glob, Bash, Edit, Task`.
3. Phase 1: Bean lesen, High-Level Plan extrahieren. Wenn Placeholder → abort.
4. Phase 2: **EINEN** Subagent via Task-Tool dispatchen (`subagent_type=general-purpose`). Prompt formulieren, der den Subagent zwingt, eine strukturierte Map (Files, Functions, Integration points, Test patterns) zurückzugeben. Read-only.
5. Phase 3: Refined Plan in die Bean schreiben — Schema `### Files to change` / `### New signatures` / `### Test sketch`. Zeilen-Nummern kommen aus dem Subagent-Output, nicht aus Imagination.
6. Phase 4: Self-Check — jeden File-Pfad via Glob/Grep verifizieren. Keine Halluzinationen.
7. Test: `/refine bean-001` ausführen. Bean prüfen.

## Self-Check

- `## Refined Plan` enthält echte Pfade wie `src/lexer.cpp:88` (mit Zeilen-Nummer aus dem Source)
- Pfade existieren wirklich (`ls ../sandbox/src/lexer.cpp` ohne Error)
- Keine Source-Files wurden editiert (`git status` in `../sandbox/` zeigt nur `.beans/bean-001--parens.md`)
- High-Level Plan, Description, Implementation Log sind unverändert
- Subagent-Output landet NICHT als langer Dump im Hauptkonversations-Verlauf — nur die strukturierte Map fließt in den Refined Plan

## Solution-Vergleich

Nach der Übung — vergleich deinen Skill mit `solution/.claude/skills/refine/SKILL.md`. Achte auf: den exakten Subagent-Prompt, das Test-Sketch-Format (Test-Name + Input → Expected), die Self-Check-Phase, und wie die harte "Read-only auf Source"-Regel formuliert ist.

## Lernziele

- Task-Tool als Context-Spar-Mechanismus: Subagent verbraucht eigenen Context, nur Findings kommen zurück
- Plan-Verfeinerung als eigene Phase: das "Was" wird zum "Wie" — kontrolliert, mit Verifikation
- Anti-Halluzination: jede behauptete Datei muss verifizierbar sein, sonst fliegt sie raus
- Skill-Komposition: Output eines Skills (Planner) ist sauber strukturierter Input des nächsten (Refine)
