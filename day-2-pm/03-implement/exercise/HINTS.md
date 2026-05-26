# Implement-Skill Build-Checkliste

Du baust einen neuen Skill `implement` von Null. **Erster Skill, der schreibt** — auf Branch, mit Test-Gate, Commits pro Step. Niemals push, niemals merge.

## Pflicht — Kern-Mechanik

- [ ] **Frontmatter** — `name: implement`, `argument-hint: <bean-id>`, `model: claude-sonnet-4-6` (schneller für Code), `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`
- [ ] **Phase 1 (Preflight)** — Bean lesen, Refined Plan extrahieren. Abort wenn leer / Placeholder. Working-Tree muss clean sein. HEAD muss `main` sein.
- [ ] **Phase 2 (Branch)** — Slug aus Bean-Title bauen. Branch: `feat/<bean-id>-<slug>`. Abort wenn Branch existiert. Verify per `git rev-parse --abbrev-ref HEAD`.
- [ ] **Phase 3 (Implement-Loop)** — pro Refined-Plan-Step: Edit → `cmake --build build` → `ctest` → Commit. Test rot? Max 2 Fix-Versuche, dann Abort.
- [ ] **Phase 4 (Implementation Log)** — Bean-Sektion `## Implementation Log` befüllen: Branch-Name, Commit-SHAs + Beschreibungen, Final-Test-Status.

## Pflicht — Disziplin (harte Regeln)

- [ ] **Niemals commit auf `main`** — vor jedem Commit `git rev-parse --abbrev-ref HEAD` checken
- [ ] **Niemals `git push`, `git merge`, `git rebase`**
- [ ] **Tests grün vor jedem Commit** — keine "fix it later"-Commits
- [ ] **Max 2 Fix-Versuche pro Step** — danach stoppen + State loggen
- [ ] **Ein Logischer Step pro Commit** — nicht batchen

## Self-Check vor Solution-Vergleich

```bash
cd ../sandbox
cp -r ../03-implement/exercise/.claude .  # leeres Skeleton
# Skill bauen, dann komplette v0:
/planner bean-001
/refine bean-001
/implement bean-001
```

- [ ] Branch `feat/bean-001-klammer-support` (oder ähnlich) existiert
- [ ] `git log feat/bean-001-...` zeigt mehrere Commits, einer pro Refined-Plan-Step
- [ ] `ctest --test-dir build` grün
- [ ] Bean hat `## Implementation Log` mit SHAs
- [ ] Skill weigert sich, auf `main` zu committen (Test: nach Phase 2 absichtlich `git checkout main` → Skill muss abbrechen)

## Erwartete Bugs (notieren, nicht fixen während Build)

- Halluzinierte Files (Refined Plan war zu vage)
- Test-Loop / Endlos-Fix-Versuche
- Commit auf `main` (Skill ignoriert Constraint)
- Subagent-Token-Bloat

Diese Bugs sind die Vorlage für den Pitfalls-Slot 16:30–17:00.
