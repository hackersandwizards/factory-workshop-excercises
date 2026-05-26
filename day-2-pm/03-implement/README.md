# Day 2 PM · Übung 03 — Implement (Refined Plan → Code auf Branch)

**Slot:** ~60 Minuten · Phase 3 der Factory-Pipeline

## Ziel

Einen `implement` Skill bauen, der die Refined-Plan-Sektion einer Bean nimmt, einen Feature-Branch erstellt, jeden Step einzeln implementiert + baut + testet + committed, und am Ende ein Implementation Log in die Bean schreibt. Niemals merge, niemals push.

## Voraussetzung

- Sandbox-Calculator unter `../sandbox/` ist gebaut und Tests laufen grün
- Bean hat einen gefüllten `## Refined Plan` (aus Übung 02)
- `cmake` und `ctest` sind installiert
- `git status` in `../sandbox/` ist clean, HEAD ist auf `main`

## Aufgabe

1. Lege im Sandbox-Repo `.claude/skills/implement/SKILL.md` an.
2. Frontmatter: `name: implement`, `argument-hint: <bean-id>`, `model: claude-sonnet-4-6`, `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`.
3. Phase 1 (Preflight): Bean lesen, Refined Plan extrahieren. Working-Tree-clean prüfen. HEAD == `main` prüfen. Wenn nicht → abort mit klarer Meldung.
4. Phase 2 (Branch): Slug aus Bean-Title generieren. Branch `feat/<bean-id>-<slug>` erstellen. Existiert er schon → abort.
5. Phase 3 (Loop): pro `### Files to change`-Eintrag: edit → `cmake --build build` → `ctest --test-dir build`. Wenn rot: max 2 Fix-Versuche, dann abort. Wenn grün: commit mit beschreibendem Message.
6. Phase 4 (Log): `## Implementation Log`-Sektion der Bean befüllen mit Branch-Name, Liste der Commit-SHAs + Beschreibungen, finalem Test-Status.
7. Harte Regeln: niemals zu `main` committen, niemals `git push`, niemals `git merge`. Tests müssen grün sein vor jedem Commit.

## Self-Check

- `git branch` in `../sandbox/` zeigt `feat/bean-001-klammer-support` (oder ähnlich)
- `git log feat/bean-001-...` zeigt mehrere kleine Commits, einer pro logischem Step
- `main` ist unverändert (`git log main` enthält keine neuen Commits)
- `ctest --test-dir build` ist grün
- Bean hat befüllten `## Implementation Log` mit Branch + Commits + Status
- Bei künstlich kaputtem Step (z.B. Refined Plan absichtlich falsch) → Skill stoppt nach 2 Versuchen, schreibt `aborted-tests-red` ins Log, ruined nicht die Codebase

## Solution-Vergleich

Nach der Übung — vergleich deinen Skill mit `solution/.claude/skills/implement/SKILL.md`. Achte auf: die Preflight-Guards (clean tree, on main), den 2-Versuche-Limit, das exakte Implementation-Log-Schema, und die Branch-Naming-Logik. Was ist defensiver formuliert als bei dir?

## Lernziele

- Hard Constraints in Skills: "niemals X" muss klar, prüfbar und unmissverständlich stehen
- Test-driven Implementation Loop: build/test/commit pro Step ist ein Sicherheits-Pattern
- Fail-Loud statt Fail-Silent: lieber sauberer Abort mit State im Log als "irgendwie fertig"
- End-to-end-Pipeline: Planner → Refine → Implement als Factory, die einen Bean von Idee zu Branch trägt — ohne dass die Haupt-Konversation den Code je sieht
