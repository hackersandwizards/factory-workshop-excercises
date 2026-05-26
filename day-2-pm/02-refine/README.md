# Day 2 PM · Übung 02 — Refine (Plan → Refined Plan)

**Slot:** ~50 Minuten · Phase 2 der Factory-Pipeline

## Ziel

Einen `refine` Skill bauen, der eine Bean mit gefülltem High-Level Plan nimmt, die Codebase via **Subagent-Fork** explored (Context-Schutz für die Haupt-Konversation) und einen konkreten `## Refined Plan` mit echten Files, Signaturen und Test-Sketch in die Bean schreibt.

## Voraussetzung

- Sandbox-Calculator unter `../sandbox/` ist gebaut (`cmake -B build && cmake --build build`)
- `beans` CLI installiert. Bean aus Übung 01 hat `## High-Level Plan` im Body.
- Verständnis: Task-Tool dispatched Subagents in isolierten Sub-Contexts

## Aufgabe

Detail-Hinweise + Build-Checkliste: `exercise/HINTS.md`. Skeleton: `exercise/.claude/skills/.gitkeep` — leerer Startpunkt, Skill von Null gebaut.

1. `exercise/.claude/` in Sandbox kopieren: `cp -r exercise/.claude ../sandbox/`. Dann `mkdir ../sandbox/.claude/skills/refine && touch ../sandbox/.claude/skills/refine/SKILL.md`.
2. Frontmatter: `name: refine`, `argument-hint: <bean-id>`, `allowed-tools: Read, Grep, Glob, Bash, Task`. (Kein `Edit` — Bean wird via `beans update` geschrieben.)
3. Phase 1: `beans show --json <bean-id>` parsen, Body lesen, `## High-Level Plan`-Sektion extrahieren. Fehlt → abort.
4. Phase 2: `beans update <bean-id> -s in-progress`.
5. Phase 3: **EINEN** Subagent via Task-Tool dispatchen (`subagent_type=general-purpose`). Prompt formulieren, der den Subagent zwingt, eine strukturierte Map (Files, Functions, Integration points, Test patterns) zurückzugeben. Read-only.
6. Phase 4: Refined Plan via `beans update <bean-id> --body-append "..."` anhängen — Schema `### Files to change` / `### New signatures` / `### Test sketch`. Zeilen-Nummern kommen aus dem Subagent-Output, nicht aus Imagination.
7. Phase 5: Self-Check — jeden File-Pfad via Glob/Grep verifizieren. Keine Halluzinationen. `git status` zeigt keine Source-Diffs.
8. Test: `/refine sandbox-dy91` ausführen. `beans show sandbox-dy91` prüfen.

## Self-Check

- `beans show sandbox-dy91` zeigt im Body einen `## Refined Plan` mit echten Pfaden wie `src/lexer.cpp:88` (mit Zeilen-Nummer aus dem Source)
- Pfade existieren wirklich (`ls ../sandbox/src/lexer.cpp` ohne Error)
- Keine Source-Files wurden editiert (`git status` in `../sandbox/` zeigt nur `.beans/sandbox-dy91--klammer-support.md` als modifiziert)
- Bean-Status ist `in-progress`
- Subagent-Output landet NICHT als langer Dump im Hauptkonversations-Verlauf — nur die strukturierte Map fließt in den Refined Plan

## Solution-Vergleich

Nach der Übung — vergleich deinen Skill mit `solution/.claude/skills/refine/SKILL.md`. Achte auf: den exakten Subagent-Prompt, das Test-Sketch-Format (Test-Name + Input → Expected), die Self-Check-Phase, und wie die harte "Read-only auf Source"-Regel formuliert ist.

## Lernziele

- Task-Tool als Context-Spar-Mechanismus: Subagent verbraucht eigenen Context, nur Findings kommen zurück
- Plan-Verfeinerung als eigene Phase: das "Was" wird zum "Wie" — kontrolliert, mit Verifikation
- Anti-Halluzination: jede behauptete Datei muss verifizierbar sein, sonst fliegt sie raus
- Skill-Komposition: Output eines Skills (Planner) ist sauber strukturierter Input des nächsten (Refine)
