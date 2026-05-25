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

Hook installieren, der `cat .env` UND `Read .env` UND `Glob .env*` blockt. Selbst wenn Agent es versucht — Exit-Code 2 unterbricht.

**Wichtig:** Agent hat mehrere Wege auf Files: `Bash` (cat/grep), `Read`, `Edit`, `Write`, `Glob`, `Grep`, `NotebookEdit`. Hook muss ALLE matchen — sonst Bypass trivial.

## Schritte

1. `.claude/hooks/block-env-access.sh` anlegen — Bash-Skript, liest stdin JSON, checkt `tool_name` + `tool_input`
2. Branchen nach Tool: Bash → Regex auf `command`; Read/Edit/Write/NotebookEdit → `file_path` basename; Glob/Grep → `pattern`/`path`/`glob`
3. `chmod +x .claude/hooks/block-env-access.sh`
4. `.claude/settings.json` mit PreToolUse-Hook, matcher = `Bash|Read|Edit|Write|NotebookEdit|Glob|Grep`
5. `.env.example` als Test-Target ist schon im exercise/ — bitte Claude erst `cat .env.example`, dann `Read .env.example`
6. Verify: beide Pfade geblockt mit Fehlermeldung

## Verify

```bash
chmod +x .claude/hooks/block-env-access.sh
# In Claude Code im exercise/ Folder, beide Pfade testen:
#   "cat .env.example"        → Bash-Pfad geblockt
#   "lies die .env.example"   → Read-Tool-Pfad geblockt
# → Fehlermeldung "Blocked: ... .env file."
```

## Stretch

- Regex härten: auch `.env`, `.env.production`, `.env.local`, gequotete Pfade, Glob `.env*`
- Zweiter Hook (PostToolUse): logging aller Bash-Commands
- Dispatcher-Pattern: ein PreToolUse-Hook mit mehreren Check-Functions gesourced (Performance: 1 Fork statt N)

## Brücke zu PM

Hooks sind das **Determinismus-Atom** für die Factory. PM bauen wir Pipeline-Stationen mit Refine + Implement. Hooks sind die Guard-Rails drumherum — `block-env-access` ist die einfachste Form.

## Solution

- [`solution/.claude/hooks/block-env-access.sh`](solution/.claude/hooks/block-env-access.sh) — der Hook
- [`solution/.claude/settings.json`](solution/.claude/settings.json) — die Hook-Konfiguration
