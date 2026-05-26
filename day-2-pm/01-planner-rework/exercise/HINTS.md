# Rework-Checkliste

Startpunkt: `.claude/skills/planner/SKILL.md` (Kopie aus Tag-2-AM-Solution). Du baust diesen Skill um — nicht von Null neu. **Falls Du Deinen eigenen Tag-2-AM-Skill hast**, ersetze die Kopie zuerst.

## Voraussetzung — Beans CLI

`brew install hmans/beans/beans` muss installiert sein (Check: `beans --version`). In `../sandbox/` zeigt `beans list` drei Beans (Klammer-Support, Variablen, Math-Funktionen). Bean-IDs lauten z.B. `sandbox-dy91`.

## Pflicht — Bean-aware Rework

- [ ] **Frontmatter** — `argument-hint: <bean-id>` ergänzen, Description anpassen: "reads bean via beans CLI, appends High-Level Plan + AC"
- [ ] **Phase 1 (Explore)** — statt Repo-Scan jetzt `beans show --json <bean-id>` parsen, Body lesen, 2-3 Findings zur Bean surfacen
- [ ] **Phase 5 (Externalize)** — `beans update <bean-id> --body-append "..."` mit Heredoc, **kein** direktes Editieren von `.beans/*.md`
- [ ] **Schema festschreiben** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Hard Rule** — keine File-Pfade, keine Funktions-Signaturen, keine Klassen-Namen im Plan

## Self-Check vor Solution-Vergleich

- [ ] `/planner sandbox-dy91` → `beans show sandbox-dy91` zeigt `## High-Level Plan` im Body
- [ ] Im Plan steht **kein** `src/lexer.cpp`, **keine** `tokenize()`, **keine** Zeilen-Referenz
- [ ] Skill weigert sich elegant, wenn Bean-ID nicht existiert (`beans show` exit-code prüfen)
- [ ] Self-Review-Phase ist erhalten geblieben (4★-Mechanik aus Tag 2 AM)

## Ausführen

```bash
cd ../sandbox
cp -r ../01-planner-rework/exercise/.claude .
claude
> /planner sandbox-dy91
```

## Bridge

Output dieses Skills = Input für `/refine` in Übung 02. High-Level-Plan + AC reichen — Files und Signaturen kommen erst dort.
