# Refine-Skill Build-Checkliste

Du baust einen neuen Skill `refine` von Null. Output: `## Refined Plan`-Sektion im Bean-Body mit echten File-Pfaden, Signaturen, Test-Sketch. Inspiriert vom Claude-Code-Plan-Modus.

## Voraussetzung — Beans CLI

`beans --version` muss laufen. `beans list` in `../sandbox/` zeigt drei Beans. Die Bean aus Übung 01 sollte bereits `## High-Level Plan` im Body haben.

## Pflicht — Kern-Mechanik

- [ ] **Frontmatter** — `name: refine`, `argument-hint: <bean-id>`, `allowed-tools: Read, Grep, Glob, Bash, Task`
- [ ] **Phase 1 (Read Bean)** — `beans show --json <bean-id>` parsen. Body extrahieren, `## High-Level Plan`-Sektion finden. Abort wenn fehlt.
- [ ] **Phase 2 (Status)** — `beans update <bean-id> -s in-progress`
- [ ] **Phase 3 (Explore via Subagent)** — **ein** Task-Subagent (`subagent_type: general-purpose`) mit fokussiertem Prompt. Read-only. Subagent gibt strukturierte Map zurück (Files / Functions / Integration-Points / Test-Patterns).
- [ ] **Phase 4 (Refined Plan)** — `beans update <bean-id> --body-append "..."` mit Heredoc, Schema:
  - `### Files to change` — `path:line — what changes`
  - `### New signatures` — `ReturnType Class::method(Args)`
  - `### Test sketch` — Test-Namen + Input → Expected
- [ ] **Phase 5 (Self-Check)** — File-Pfade via Glob/Read verifizieren. Halluzinierte Pfade markieren als `:NEW` oder fixen.

## Pflicht — Disziplin

- [ ] **Read-only auf Source** — Skill macht keine `git status`-Diffs in `src/` oder `tests/`
- [ ] **File-Pfade verifizierbar** — keine Fabrikation
- [ ] **Subagent in Fork** — Explore-Transkript landet nicht im Main-Context
- [ ] **Niemals `.beans/*.md` direkt editieren** — immer via `beans update`
- [ ] **Abort sauber** — wenn `## High-Level Plan` im Body fehlt

## Self-Check vor Solution-Vergleich

```bash
cd ../sandbox
cp -r ../02-refine/exercise/.claude .
claude
> /refine sandbox-dy91
```

- [ ] `beans show sandbox-dy91` zeigt `## Refined Plan` im Body mit realen `src/lexer.cpp`-, `src/parser.cpp`-Pfaden
- [ ] `git grep` für jeden referenzierten Pfad findet ihn
- [ ] `git status` in `sandbox/` zeigt keine Änderungen in `src/` oder `tests/`
- [ ] Status der Bean ist `in-progress`

## Bridge

Output → Input für `/implement` in Übung 03.
