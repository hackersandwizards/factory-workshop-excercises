# Refine-Skill Build-Checkliste

Du baust einen neuen Skill `refine` von Null. Output: `## Refined Plan`-Sektion in der Bean mit echten File-Pfaden, Signaturen, Test-Sketch. Inspiriert vom Claude-Code-Plan-Modus.

## Pflicht — Kern-Mechanik

- [ ] **Frontmatter** — `name: refine`, `argument-hint: <bean-id>`, `allowed-tools: Read, Grep, Glob, Bash, Edit, Task`
- [ ] **Phase 1 (Read Bean)** — Bean lesen, High-Level Plan + AC extrahieren. Abort wenn Placeholder noch da.
- [ ] **Phase 2 (Explore via Subagent)** — **ein** Task-Subagent (`subagent_type: general-purpose`) mit fokussiertem Prompt. Read-only. Subagent gibt strukturierte Map zurück (Files / Functions / Integration-Points / Test-Patterns).
- [ ] **Phase 3 (Refined Plan)** — Bean-Sektion `## Refined Plan` befüllen mit Schema:
  - `### Files to change` — `path:line — what changes`
  - `### New signatures` — `ReturnType Class::method(Args)`
  - `### Test sketch` — Test-Namen + Input → Expected
- [ ] **Phase 4 (Self-Check)** — File-Pfade via Glob/Read verifizieren. Halluzinierte Pfade markieren als `:NEW` oder fixen.

## Pflicht — Disziplin

- [ ] **Read-only auf Source** — Skill editiert **nur** Bean
- [ ] **File-Pfade verifizierbar** — keine Fabrikation
- [ ] **Subagent in Fork** — Explore-Transkript landet nicht im Main-Context
- [ ] **Abort sauber** — wenn High-Level Plan leer

## Self-Check vor Solution-Vergleich

```bash
cd ../sandbox
cp -r ../02-refine/exercise/.claude .  # leeres Skeleton
# Skill bauen, dann:
/refine bean-001
```

- [ ] Bean hat `## Refined Plan` mit realen `src/lexer.cpp`-, `src/parser.cpp`-Pfaden
- [ ] `git grep` für jeden referenzierten Pfad findet ihn
- [ ] Andere 3 Sektionen unverändert
- [ ] Subagent hat read-only gearbeitet (kein Code-Diff im Sandbox)

## Bridge

Output → Input für `/implement` in Übung 03.
