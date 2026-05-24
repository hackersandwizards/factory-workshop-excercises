# Day 2 AM · Übung 04 — env-block-Hook

**Slot:** 11:30–12:00 · 30 Minuten

## Concept

Hooks = Shell-Commands auf Tool-Events. Exit ≠ 0 = Tool-Call blockiert. **Agent kann Hooks NICHT bypassen** — anders als Prompt-Instruktionen.

| Event | Wann |
|-------|------|
| **PreToolUse** | Vor jedem Tool-Call. Exit ≠ 0 blockiert. |
| **PostToolUse** | Nach Tool-Call. Validierung, Logging. |
| **SessionStart** | Bei Session-Start. Context laden. |
| **PreCompact** | Vor Context-Compaction. State sichern. |

## Ziel

Hook installieren, der `cat .env` und ähnliche Reads blockt. Selbst wenn Agent es versucht — Exit-Code 2 unterbricht.

## Schritte

1. `.claude/hooks/block-env-access.sh` anlegen — Bash-Skript, liest stdin JSON, checkt Command
2. `chmod +x .claude/hooks/block-env-access.sh`
3. `.claude/settings.json` anlegen mit PreToolUse-Hook für Bash-Tool
4. `.env.example` als Test-Target ist schon im exercise/ — versuch Claude zu bitten, das zu lesen
5. Verify: Bash-Command der `.env` matcht → wird geblockt mit Fehlermeldung

## Verify

```bash
chmod +x .claude/hooks/block-env-access.sh
# In Claude Code im exercise/ Folder:
# Bitte Claude: "cat .env.example"
# → wird geblockt mit "Blocked: command tries to access .env file."
```

## Stretch

- Hook erweitern: auch `.env.production`, `.env.local` blocken
- Zweiter Hook (PostToolUse): logging aller Bash-Commands
- Dispatcher-Pattern: ein PreToolUse-Hook mit mehreren Check-Functions gesourced (Performance: 1 Fork statt N)

## Brücke zu PM

Hooks sind das **Determinismus-Atom** für die Factory. PM bauen wir Pipeline-Stationen mit Refine + Implement. Hooks sind die Guard-Rails drumherum — `block-env-access` ist die einfachste Form.

## Solution

- [`solution/.claude/hooks/block-env-access.sh`](solution/.claude/hooks/block-env-access.sh) — der Hook
- [`solution/.claude/settings.json`](solution/.claude/settings.json) — die Hook-Konfiguration
