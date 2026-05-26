# Rework-Checkliste

Startpunkt: `.claude/skills/planner/SKILL.md` (Kopie aus Tag-2-AM-Solution). Du baust diesen Skill um — nicht von Null neu. **Falls Du Deinen eigenen Tag-2-AM-Skill hast**, ersetze die Kopie zuerst.

## Pflicht — Bean-aware Rework

- [ ] **Frontmatter** — `argument-hint: <bean-id>` ergänzen, Description anpassen: "reads bean by ID, appends High-Level Plan + Acceptance Criteria"
- [ ] **Phase 1 (Explore)** — statt Repo-Scan jetzt nur `./.beans/<bean-id>.md` lesen, 2-3 Findings zur Bean surfacen
- [ ] **Phase 5 (Externalize)** — statt `.plans/<task>.md` jetzt die Bean editieren, **nur** die `## High-Level Plan`-Sektion
- [ ] **Schema festschreiben** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Hard Rule** — keine File-Pfade, keine Funktions-Signaturen, keine Klassen-Namen im Plan

## Self-Check vor Solution-Vergleich

- [ ] `/planner bean-001` → Bean öffnen → `## High-Level Plan` ist befüllt, andere 3 Sektionen unverändert
- [ ] Im Plan steht **kein** `src/lexer.cpp`, **keine** `tokenize()`, **keine** Zeilen-Referenz
- [ ] Skill weigert sich elegant, wenn Bean nicht existiert
- [ ] Self-Review-Phase ist erhalten geblieben (4★-Mechanik aus Tag 2 AM)

## Ausführen

```bash
cd ../sandbox
# Skill nach sandbox kopieren (oder symlinken):
cp -r ../01-planner-rework/exercise/.claude .
claude
> /planner bean-001
```

## Bridge

Output dieses Skills = Input für `/refine` in Übung 02. High-Level-Plan + AC reichen — Files und Signaturen kommen erst dort.
