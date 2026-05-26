# Implement-Skill Build-Checkliste

Du baust einen neuen Skill `implement` von Null. **Erster Skill, der schreibt** — auf Branch, mit Test-Gate, Commits pro Step. Niemals push, niemals merge.

## Voraussetzung — Beans CLI

`beans --version` muss laufen. Die Bean aus Übung 02 sollte `## Refined Plan` im Body und Status `in-progress` haben.

## Pflicht — Kern-Mechanik

- [ ] **Frontmatter** — `name: implement`, `argument-hint: <bean-id>`, `model: claude-sonnet-4-6` (schneller für Code), `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`
- [ ] **Phase 1 (Preflight)** — `beans show --json <bean-id>` parsen, `## Refined Plan` extrahieren. Abort wenn leer. Working-Tree muss clean sein. HEAD muss `main` sein.
- [ ] **Phase 2 (Branch)** — Slug aus Bean-`title`-Feld bauen. Branch: `feat/<bean-id>-<slug>`. Abort wenn Branch existiert. Verify per `git rev-parse --abbrev-ref HEAD`.
- [ ] **Phase 3 (Implement-Loop)** — pro Refined-Plan-Step: Edit → `cmake --build build` → `ctest` → Commit. Test rot? Max 2 Fix-Versuche, dann Abort.
- [ ] **Phase 4 (Implementation Log)** — `beans update <bean-id> --body-append "..."` mit Branch-Name, Commit-SHAs + Beschreibungen, Final-Test-Status.
- [ ] **Phase 5 (Status)** — wenn grün: `beans update <bean-id> -s completed` + `## Summary of Changes` appenden. Wenn rot: Status bleibt `in-progress`, Notes appenden.

## Pflicht — Disziplin (harte Regeln)

- [ ] **Niemals commit auf `main`** — vor jedem Commit `git rev-parse --abbrev-ref HEAD` checken
- [ ] **Niemals `git push`, `git merge`, `git rebase`**
- [ ] **Tests grün vor jedem Commit** — keine "fix it later"-Commits
- [ ] **Max 2 Fix-Versuche pro Step** — danach stoppen + State loggen
- [ ] **Ein Logischer Step pro Commit** — nicht batchen
- [ ] **Niemals `.beans/*.md` direkt editieren** — immer via `beans update`

## Self-Check vor Solution-Vergleich

```bash
cd ../sandbox
cp -r ../03-implement/exercise/.claude .
# Skill bauen, dann komplette v0:
/planner 
# produziert bean implement-exercise-olqc
/refine implement-exercise-olqc
/implement implement-exercise-olqc
```

implement-exercise-olqc

- [ ] Branch `feat/implement-exercise-olqc` (oder ähnlich) existiert
- [ ] `git log feat/implement-exercise-olqc-...` zeigt mehrere Commits, einer pro Refined-Plan-Step
- [ ] `ctest --test-dir build` grün
- [ ] `beans show implement-exercise-olqc` zeigt Status `completed`
- [ ] Skill weigert sich, auf `main` zu committen (Test: nach Phase 2 absichtlich `git checkout main` → Skill muss abbrechen)

## Erwartete Bugs (notieren, nicht fixen während Build)

- Halluzinierte Files (Refined Plan war zu vage)
- Test-Loop / Endlos-Fix-Versuche
- Commit auf `main` (Skill ignoriert Constraint)
- Subagent-Token-Bloat
- Direkte Edits auf `.beans/*.md` statt CLI (Skill umgeht beans)

Diese Bugs sind die Vorlage für den Pitfalls-Slot 16:30–17:00.
