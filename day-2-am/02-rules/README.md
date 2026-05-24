# Day 2 AM · Übung 02 — Rules

**Slot:** 10:00–10:30 · 30 Minuten

## Concept

Rules = scoped Behavior-Instruktionen in `.claude/rules/<name>.md`. Frontmatter mit `glob:`-Pattern → Rule wird **nur geladen wenn passende File im Context**.

Unterschied zu CLAUDE.md / Skills:

| Layer | Lade-Verhalten | Beispiel |
|-------|---------------|----------|
| **CLAUDE.md** | Always-on global, gesamtes Repo | Projekt-Architektur, Tech-Stack |
| **Rules** | Always-on per Glob-Scope | Code-Konventionen pro File-Typ |
| **Skills** | On-demand per Task | Spezifischer Workflow auf Anforderung |

## Ziel

Eine Rule **tief** bauen: TypeScript-Konventionen für `**/*.ts` mit mehreren konkreten Enforcements. Testen anhand `exercise/src/legacy-component.ts` — File mit Anti-Patterns drin.

## Schritte

1. `exercise/src/legacy-component.ts` öffnen — diese File hat absichtlich Violations
2. `.claude/rules/typescript.md` anlegen mit:
   - Frontmatter: `glob: "**/*.ts"`
   - Body: 2-3 konkrete Code-Konventionen mit Beispielen
3. Claude Code öffnen im exercise/ Folder
4. Bitte Claude: "Lies legacy-component.ts und schlage Verbesserungen vor"
5. Verify: Claude erkennt die Violations dank deiner Rule

## Konventionen-Kandidaten (wähle 2-3)

- **Kein `any` ohne `// reason:` Kommentar** — wenn `any`, dann Begründung in Inline-Comment
- **Kein `// @ts-ignore` ohne `// reason:`** — `@ts-ignore` braucht Issue-Link oder Erklärung
- **Explizite Return-Types auf exported Functions** — keine impliziten Inferenz-Returns für Public-API
- **Kein `console.log` außer in Test-Files** — Logging via dedicated Logger
- **Keine TODOs ohne Issue-Link** — `// TODO(#123)` oder Ticket-Referenz

Wähle **2-3 zusammenhängende** Konventionen — Thema "Types stay typed" oder "Code stays explicit".

## Verify

- Edit `legacy-component.ts` mit Claude Code geöffnet
- Frage: "Welche Probleme siehst du in dieser Datei?"
- Claude erkennt die Violations und nennt die Rule als Quelle

## Stretch

- Zweite Rule für anderen Glob (`**/*.test.ts` — Test-Konventionen)
- Glob-Spezifität testen: ändert sich Verhalten in `*.tsx` vs `*.ts`?

## Brücke zu nächster Übung

Tag 2 AM 03 — Subagents: Was Rules always-on per Scope sind, sind Subagents on-demand in isoliertem Context. Combo: Rules definieren *wie* Code aussehen muss, Subagents *exekutieren* in dieser Konvention.

## Solution

Siehe [`solution/.claude/rules/typescript.md`](solution/.claude/rules/typescript.md) — Reference-Rule mit 3 zusammenhängenden Enforcements.
