# factory-starter

Mini Notizen-App. Workshop-Starter — `.claude/` Verzeichnis baust du im Workshop selbst.

## Stack

- **Runtime:** Bun
- **Backend:** Hono, `src/server.ts`
- **Frontend:** Vanilla HTML + JS, `public/index.html`
- **DB:** JSON-Datei, `data/notes.json`

## Commands

```bash
bun install
bun run dev          # http://localhost:3000
```

## Verzeichnis-Map

| Pfad | Zweck |
|------|-------|
| `src/server.ts` | Hono app, alle Endpoints |
| `public/index.html` | Frontend (vanilla, kein Build) |
| `data/notes.json` | File-als-DB, mit Seed-Data |
| `.beans/*.md` | Workshop-Beans für Refine/Implement |
| `.claude/` | (existiert noch nicht — ihr baut's) |

## Convention

- TypeScript strict
- Hono-Style-Routing
- Frontend ohne Framework
- Keine Tests (bewusst — Pläne sollen Testing-Strategy ergänzen)

## Bean-Format

Beans in `.beans/<bean-id>--<slug>.md`. Frontmatter:

```markdown
---
id: bean-001
title: <kurz>
status: todo | in-progress | completed
---

# <Titel>

## Description
<Was soll passieren>

## Checklist
- [ ] <Sub-Schritt>

## Definition of Done
- [ ] Tests grün (falls Tests existieren)
- [ ] Manual Verify durchgeführt

(Refine fügt `## Implementation Plan` hinzu.)
```

## Notes für Refine-Agents (wenn ihr einen baut)

- Refine ist read-only. Schreibt Plan in Bean-Body, nicht Source.
- Code-Konvention: TypeScript strict, kein `any` ohne Begründung
- Frontend ändert ihr in `public/index.html`. Kein Bundler.
- DB-Operationen über `data/notes.json` File-IO. Atomare Writes mit temp file + rename.
