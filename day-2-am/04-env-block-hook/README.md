# Day 2 AM · Exercise 04 — env-block hook

**Slot:** 11:30–12:00 · 30 minutes

## Concept

Hooks = shell commands on tool events. A non-zero exit blocks the tool call. **The agent CANNOT bypass hooks** — unlike prompt instructions.

| Event | When |
|-------|------|
| **PreToolUse** | Before every tool call. A non-zero exit blocks it. |
| **PostToolUse** | After a tool call. Validation, logging. |
| **SessionStart** | At session start. Load context. |
| **PreCompact** | Before context compaction. Save state. |

## Goal

Install a hook that blocks `cat .env` AND `Read .env` AND `Glob .env*`. Even if the agent tries — exit code 2 interrupts it.

**Important:** the agent has several ways to reach files: `Bash` (cat/grep), `Read`, `Edit`, `Write`, `Glob`, `Grep`, `NotebookEdit`. The hook must match ALL of them — otherwise the bypass is trivial.

## Steps

1. Create `.claude/hooks/block-env-access.sh` — a Bash script that reads stdin JSON and checks `tool_name` + `tool_input`
2. Branch by tool: Bash → regex on `command`; Read/Edit/Write/NotebookEdit → `file_path` basename; Glob/Grep → `pattern`/`path`/`glob`
3. `chmod +x .claude/hooks/block-env-access.sh`
4. `.claude/settings.json` with a PreToolUse hook, matcher = `Bash|Read|Edit|Write|NotebookEdit|Glob|Grep`
5. `.env.example` is already in exercise/ as a test target — ask Claude first to `cat .env.example`, then to `Read .env.example`
6. Verify: both paths blocked with an error message

## Verify

```bash
chmod +x .claude/hooks/block-env-access.sh
# In Claude Code, inside the exercise/ folder, test both paths:
#   "cat .env.example"        → Bash path blocked
#   "read the .env.example"   → Read-tool path blocked
# → Fehlermeldung "Blocked: ... .env file."
```

## Stretch

- Harden the regex: also `.env`, `.env.production`, `.env.local`, quoted paths, glob `.env*`
- A second hook (PostToolUse): log all Bash commands
- Dispatcher pattern: one PreToolUse hook with several check functions sourced in (performance: 1 fork instead of N)

## Bridge to PM

Hooks are the **atom of determinism** for the Factory. For PM we build pipeline stations with Refine + Implement. Hooks are the guard rails around them — `block-env-access` is the simplest form.

## Solution

The reference solution lives on branch **`solution/day-2-am-04-env-block-hook`** (kept
off `main` so it stays out of Claude's context) — `solution/.claude/hooks/block-env-access.sh`
(the hook) plus `solution/.claude/settings.json` (its configuration). Try it yourself
first, then compare:

```bash
git checkout solution/day-2-am-04-env-block-hook   # inspect solution/.claude/…
git checkout main                                  # back to your work
git show solution/day-2-am-04-env-block-hook:day-2-am/04-env-block-hook/solution/.claude/hooks/block-env-access.sh
```
