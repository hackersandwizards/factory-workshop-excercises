# Day 2 AM · Übung 03 — Subagent

**Slot:** 10:45–11:30 · 45 Minuten

## Concept

Subagent läuft in **isoliertem Context** (eigene Conversation). Macht Heavy-Lifting (viel lesen, viel Code), gibt nur **Summary** zurück an Hauptlauf. Du sparst Context-Tokens im Main.

Skill = on-demand Markdown im aktuellen Context. Subagent = explizit delegiert in isolierten Context.

## Frontmatter — was du konfigurieren kannst

```yaml
---
name: codebase-explorer
description: Use when the user wants to understand where a concept lives in the code
tools: Read, Grep, Glob, Bash
model: claude-sonnet-4-6
---
```

| Feld | Zweck |
|------|-------|
| `tools` | Whitelist — Subagent kann nur diese nutzen |
| `model` | Haiku für Routine, Sonnet/Opus für Schwieriges |
| `description` | Activation-Key (gleich wie Skill) |

## Ziel

Subagent für einen wiederkehrenden Workflow aus deinem Stack. Output-Contract definieren.

## Vorschläge

1. **`codebase-explorer`** — *"finde alle Stellen wo X passiert + summarize"*
2. **`test-runner-and-summarizer`** — `npm test` ausführen, parse, kurzer Bericht
3. **`dependency-analyzer`** — `package.json` + Lock-File lesen, Outdated/Risks zusammenfassen
4. **`legacy-code-explainer`** — alte Datei lesen, moderner Kommentar (C++/Java-Legacy)
5. **`pr-diff-summarizer`** — `git diff main...HEAD`, strukturierte Zusammenfassung

## Schritte

1. `.claude/agents/<dein-name>.md` anlegen
2. Frontmatter mit `name`, `description`, `tools` (Whitelist!), `model`
3. Body: Rolle + Workflow + Output-Contract + Rules
4. Trigger im Main-Context: `@<name>` oder via Task tool
5. Verify: Output unter 400 Wörter, Summary + Findings strukturiert

## Verify

- Subagent läuft, gibt Summary zurück
- Output ist kompakter als das gelesene Material (Context-Schutz!)
- Tools-Whitelist verhindert ungewollte Side-Effects

## Stretch

- Model-Tuning: Haiku vs Sonnet — fühlt's anders an?
- Mehrere Subagents komponieren: `@explorer` → `@summarizer`

## Brücke zu nächster Übung

Tag 2 AM 04 — Hooks: Subagents sind Soft-Boundaries (Prompt-basiert). Hooks sind Hard-Boundaries (Shell-Exit-Code, unumgehbar).

Tag 2 PM: Was du gerade gebaut hast, wird `@refine` — gleicher Job, isolierter Context, Plan landet in Bean.

## Solution

Zwei Referenz-Subagents in `solution/`:
- [`codebase-explorer.md`](solution/.claude/agents/codebase-explorer.md) — Read-only Discovery
- [`pr-diff-summarizer.md`](solution/.claude/agents/pr-diff-summarizer.md) — Strukturierte Diff-Zusammenfassung
