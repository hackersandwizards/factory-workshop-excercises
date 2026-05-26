# Rework-Checkliste

Startpunkt: `.claude/skills/planner/SKILL.md` (Kopie aus Tag-2-AM-Solution). Du baust diesen Skill um — nicht von Null neu. **Falls Du Deinen eigenen Tag-2-AM-Skill hast**, ersetze die Kopie zuerst.

## Voraussetzung — Beans CLI

`brew install hmans/beans/beans` muss installiert sein (Check: `beans --version`). `.beans.yml` existiert in `../sandbox/` (prefix `sandbox-`).

## Pflicht — Bean-Creator Rework

- [ ] **Frontmatter** — `argument-hint: [brief feature description]` (optional, nicht `<bean-id>`). Description anpassen: "creates a new bean via beans CLI with description + High-Level Plan + AC".
- [ ] **Phase 1 (Capture)** — Feature-Idee vom User aufnehmen, in einem Satz zurückspiegeln
- [ ] **Phase 3 (Approaches) — STOP-Guard** — Skill präsentiert 2-3 Optionen und **wartet auf explizite User-Wahl**. Auch wenn "autonomously" / "no clarifying questions" vorher gesagt wurde — Approach-Pick ist Pflicht-Gate, keine Klarstellung.
- [ ] **Phase 5 (Create Bean)** — **Ein** CLI-Call mit komplettem Body:
  - `beans create "<title>" -t feature -d "<heredoc>"` mit Description + Hinweise + `## High-Level Plan` (Approach, Steps, AC, Non-Goals) in einem Rutsch
  - Die `beans` CLI hat **kein** `--body-append`-Flag. Für sehr lange Bodies: `--body-file <path>` statt `-d`.
  - ID anschließend aus stdout parsen für User-Hand-off (`/refine <id>`).
- [ ] **Schema festschreiben** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Hard Rule** — keine File-Pfade, keine Funktions-Signaturen, keine Klassen-Namen im Plan

## Pflicht — Disziplin

- [ ] Niemals `.beans/*.md` direkt editieren — immer via CLI
- [ ] Niemals Source-Code editieren — Planner ist read-only auf Source
- [ ] Self-Review-Phase (4★-Mechanik aus Tag 2 AM) bleibt drin

## Self-Check vor Solution-Vergleich

- [ ] `/planner Klammer-Support für Calculator` → neue Bean entsteht (`beans list` zeigt sie)
- [ ] `beans show <new-id>` zeigt Description + `## High-Level Plan` mit Approach/Steps/AC/Non-Goals
- [ ] Im Plan steht **kein** `src/lexer.cpp`, **keine** `tokenize()`, **keine** Zeilen-Referenz
- [ ] Skill weigert sich elegant, wenn `beans` CLI fehlt

## Ausführen

```bash
cd ../sandbox
cp -r ../01-planner-rework/exercise/.claude .
claude
> /planner Klammer-Support für Calculator
```

## Bridge

Output dieses Skills = neue Bean-ID. Input für `/refine <bean-id>` in Übung 02. High-Level-Plan + AC reichen — Files und Signaturen kommen erst dort.
