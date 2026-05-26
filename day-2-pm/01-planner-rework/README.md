# Day 2 PM · Übung 01 — Planner-Rework (Bean-Creator)

**Slot:** ~35 Minuten · Phase 1 der Factory-Pipeline

## Ziel

Tag-2-AM `planner` Skill umbauen: statt einen freien Plan in `.plans/` zu schreiben, **erzeugt der Skill eine neue Bean** via `beans create` + `beans update` mit Description + High-Level Plan + Acceptance Criteria. Strikt auf "Was"-Ebene (keine Pfade, keine Signaturen). Refine + Implement bekommen die Bean-ID später als Argument — Planner nicht.

## Voraussetzung

- Sandbox-Calculator existiert unter `../sandbox/` (vom Trainer gebaut)
- `beans` CLI installiert (`brew install hmans/beans/beans`, Check: `beans --version`)
- `.beans.yml` existiert in `../sandbox/` (prefix `sandbox-`)
- Startpunkt-Skill liegt unter `exercise/.claude/skills/planner/SKILL.md` (Kopie aus Tag-2-AM-Solution). Falls Du Deinen eigenen Tag-2-AM-Skill hast: ersetze die Kopie damit.

## Aufgabe

1. `exercise/.claude/` in Sandbox kopieren: `cp -r exercise/.claude ../sandbox/`.
2. Frontmatter: `argument-hint: [brief feature description]` (optional, kein bean-id). Description: "creates a new bean via beans CLI with description + High-Level Plan + AC".
3. Phase 1 (Capture) umbauen: Feature-Idee aufnehmen — entweder aus Skill-Argument oder vom User abfragen. Kein Repo-Scan, kein Bean-Read.
4. Phase 5 (Create Bean) umbauen: **ein** CLI-Call mit komplettem Body:
   - `beans create "<title>" -t feature -d "<heredoc mit Description + Hinweise + High-Level Plan>"` → ID aus stdout
   - Die `beans` CLI hat **kein** `--body-append`-Flag. Body wird in einem Rutsch geschrieben. Für sehr lange Bodies: `--body-file <path>` statt `-d`.
   - **Niemals** `.beans/*.md` direkt editieren.
5. Phase 3 (Approaches) absichern: Skill **stoppt** nach Präsentation der Optionen und wartet auf explizite User-Wahl. Auch wenn "autonomously" / "no clarifying questions" vorher gesagt wurde — Approach-Pick ist Pflicht-Gate, keine Klarstellung.
6. Harte Regel ergänzen: **keine** File-Pfade, **keine** Funktions-Signaturen, **keine** Klassen-Namen im Plan. Acceptance Criteria stattdessen.
7. Test: `cd ../sandbox && claude` → `/planner Klammer-Support für Calculator` ausführen. `beans list` + `beans show <new-id>` prüfen.

Detail-Hinweise: `exercise/HINTS.md`.

## Self-Check

- `beans list` enthält eine neue Bean nach `/planner`-Run
- `beans show <new-id>` zeigt Description (Mensch-Brief) + `## High-Level Plan` mit **Approach**, **Steps**, **Acceptance Criteria**, **Non-Goals**
- Im Plan steht **kein** `src/lexer.cpp`, **keine** `tokenize()`, **keine** Zeilen-Referenz
- Status der neuen Bean ist `todo`
- Skill weigert sich elegant, wenn `beans` CLI fehlt

## Solution-Vergleich

Nach der Übung — vergleich deinen Skill mit `solution/.claude/skills/planner/SKILL.md`. Was ist anders? Was würdest du übernehmen? Achte besonders auf: Self-Review-Phase, Wording der harten Regeln, Schema der externalisierten Sektion, Parsing der ID aus `beans create`-Output.

## Lernziele

- Skill-Refactor: bestehenden Skill auf neuen Output (Bean-Creation statt Plan-File) umbauen
- Output-Disziplin: Skill schreibt nur via CLI, niemals direkt in `.beans/*.md`
- Disziplin der Abstraktions-Ebene: "Was" trennen vom "Wie"
- Hand-off-Design: Output eines Skills (neue Bean-ID) ist Input des nächsten (`/refine <id>`)
