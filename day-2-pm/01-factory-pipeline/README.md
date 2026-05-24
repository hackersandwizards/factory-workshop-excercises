# Day 2 PM · Übung 01 — Factory-Pipeline (v0-Build)

**Slot:** 15:00–16:00 · 60 Minuten

## Ziel

Erste Mini-Factory aus den Atomen vom Vormittag zusammenbauen: `@refine` (Plan) + `@implement` (Code) im factory-starter. Lauffähige v0-Pipeline am Ende.

## Stack

`exercise/` enthält den **factory-starter** (Bun + Hono + Vanilla HTML + JSON-DB) mit 3 Seed-Beans. Kein `.claude/` — das baust du jetzt.

## Phasen

| Phase | Was | Dauer |
|-------|-----|-------|
| A | Trainer-Walkthrough Starter (App, Beans, kein `.claude/`) | 10min |
| B | Build `@refine` Subagent + `/refine` Slash-Command | 25min |
| C | Build `@implement` Subagent + `/implement` Slash-Command | 20min |
| D | Run `/refine bean-001` → `/implement bean-001` | 5min |

## Phase A — Walkthrough

```bash
cd exercise
bun install
bun run dev
# → http://localhost:3000
```

Eine Bean live öffnen: `.beans/bean-001--patch-note-endpoint.md`. Das ist Input für `@refine`. Output: Plan (in Bean-Body) und Code (in Branch).

## Phase B — Build @refine

Erstelle:
1. `.claude/agents/refine.md` — Subagent: liest Bean, schreibt Plan in Body
2. `.claude/commands/refine.md` — Slash-Command: ruft `@refine` via Agent-Tool

**Regel:** `@refine` ist **read-only**. Tools: nur Read, Glob, Grep, Bash. Modifiziert keinen Source-Code. Plan muss reale Files referenzieren (per Grep verifiziert).

## Phase C — Build @implement

Erstelle:
1. `.claude/agents/implement.md` — Subagent: liest Plan aus Bean, schreibt Code, branched, committed
2. `.claude/commands/implement.md` — Slash-Command

**Regel:** Eine Bean = ein Feature-Branch. Commit pro logischem Step. Tests laufen vor Final-Commit. **Niemals merge / push to main.**

## Phase D — Run

```bash
/refine bean-001
# → Read bean, plan in Bean-Body angehängt

/implement bean-001
# → Branch erstellt, Commits gelandet
```

## Verify

- `git log` zeigt neue Commits auf neuem Branch
- Bean-File hat `## Implementation Plan` Section
- App läuft noch (`bun run dev` → http://localhost:3000)
- PATCH-Endpoint funktioniert (für bean-001)

## Authenticity-Hook

**Es wird schief gehen.** Halluzinationen, falsche Pfade, leere Pläne. **Nicht** fixen während Build. Sammeln. Diskussion danach: welche Station (challenge / review / qa) hätte das gefangen?

## Stretch

- bean-002 (Tag-Filter UI + Backend) — komplexer, Frontend involved
- bean-003 (JSON → SQLite Migration) — Behavioral Contract, Mynab-Pattern

## Brücke zu Tag 3

Tag 3 Hackathon: ihr bringt eigene Codebases mit. Was hier mit factory-starter funktioniert, übertragt ihr auf euren Stack. Patterns aus `@refine` + `@implement` sind generisch — Bean-Format, Plan-First, isolated Context.

## Solution

- [`solution/.claude/agents/refine.md`](solution/.claude/agents/refine.md)
- [`solution/.claude/agents/implement.md`](solution/.claude/agents/implement.md)
- [`solution/.claude/commands/refine.md`](solution/.claude/commands/refine.md)
- [`solution/.claude/commands/implement.md`](solution/.claude/commands/implement.md)

Solution ist Overlay über `exercise/factory-starter`. Wenn ihr "solution anwenden" wollt: `cp -r solution/.claude exercise/.claude`.
