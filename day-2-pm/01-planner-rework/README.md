# Day 2 PM · Übung 01 — Planner-Rework (Bean-aware)

**Slot:** ~35 Minuten · Phase 1 der Factory-Pipeline

## Ziel

Den Tag-2-AM `planner` Skill so umbauen, dass er Bean-aware wird: Statt einen freien Plan in `.plans/` zu schreiben, liest er eine Bean per ID, befüllt nur deren `## High-Level Plan`-Sektion und bleibt strikt auf "Was"-Ebene (keine Pfade, keine Signaturen).

## Voraussetzung

- Sandbox-Calculator existiert unter `../sandbox/` (vom Trainer gebaut)
- `beans` CLI installiert (`brew install hmans/beans/beans`, Check: `beans --version`)
- Beans liegen unter `../sandbox/.beans/sandbox-*.md` (3 Stück: Klammer, Variablen, Math-Funktionen). `beans list` zeigt sie an.
- Startpunkt-Skill liegt unter `exercise/.claude/skills/planner/SKILL.md` (Kopie aus Tag-2-AM-Solution). Falls Du Deinen eigenen Tag-2-AM-Skill hast: ersetze die Kopie damit.

## Aufgabe

1. `exercise/.claude/` in den Sandbox kopieren (oder symlinken): `cp -r exercise/.claude ../sandbox/`. Damit hat der Sandbox-Repo `.claude/skills/planner/SKILL.md` als Ausgangsbasis.
2. Frontmatter anpassen: `argument-hint: <bean-id>`, Description um "reads bean by ID, appends High-Level Plan + Acceptance Criteria" ergänzen.
3. Phase 1 (Explore) umbauen: statt Repo-Scan jetzt `beans show --json <bean-id>` parsen, Body lesen, 2-3 Findings zur Bean surfacen.
4. Phase 5 (Externalize) umbauen: statt `.plans/<task>.md` schreiben jetzt `beans update <bean-id> --body-append "..."` mit Heredoc. **Niemals** `.beans/*.md` direkt editieren.
5. Harte Regel ergänzen: **keine** File-Pfade, **keine** Funktions-Signaturen, **keine** Klassen-Namen im Plan. Acceptance Criteria stattdessen.
6. Test: `cd ../sandbox && claude` → `/planner sandbox-dy91` ausführen. `beans show sandbox-dy91` prüfen.

Detail-Hinweise: `exercise/HINTS.md`.

## Self-Check

- `beans show sandbox-dy91` zeigt im Body einen befüllten `## High-Level Plan` mit **Approach**, **Steps**, **Acceptance Criteria**, **Non-Goals**
- Im Plan steht **kein** `src/lexer.cpp`, **keine** `tokenize()`, **keine** Zeilen-Referenz
- Die ursprüngliche Description (Body vor `## High-Level Plan`) ist unverändert
- Skill weigert sich elegant, wenn die Bean-ID nicht existiert (`beans show` exit-code prüfen)

## Solution-Vergleich

Nach der Übung — vergleich deinen Skill mit `solution/.claude/skills/planner/SKILL.md`. Was ist anders? Was würdest du übernehmen? Achte besonders auf: Self-Review-Phase, Wording der harten Regeln, Schema der externalisierten Sektion.

## Lernziele

- Skill-Refactor: bestehenden Skill auf neuen Input (Bean statt freier Task) umbauen
- Strikte Sektions-Edits: ein Skill, der nur einen bestimmten Markdown-Abschnitt anfasst
- Disziplin der Abstraktions-Ebene: "Was" trennen vom "Wie"
- Hand-off-Design: Output eines Skills ist Input des nächsten (Refine)
