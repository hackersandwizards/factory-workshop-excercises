# factory-starter

Mini Notizen-App. **Ohne** `.claude/` Setup. **Mit** drei seed-Beans in `.beans/`.

Das `.claude/`-Verzeichnis baut ihr im Workshop selbst — das ist die Übung.

## Stack

- **Runtime:** Bun (kein Node)
- **Backend:** Hono (TypeScript)
- **Frontend:** Vanilla HTML + JS (kein Build-Step)
- **DB:** JSON-Datei (`data/notes.json`)

Bewusst minimal. Realistisch genug für nicht-triviale Pläne, klein genug für 5min Setup.

## Setup (idealerweise **vor** Tag 2 erledigt)

### Voraussetzungen

- **Bun** (Runtime, statt Node) — siehe Install-Tabelle unten
- **jq** (für `.claude/hooks/` JSON-Parsing in Tag 2 PM Hook-Exercise)
- **git** mit gesetztem `user.name` + `user.email` (Implement-Agent committed)
- Claude Code installiert + eingeloggt

#### Install-Befehle pro OS

**Mit Package-Manager (empfohlen — ein Befehl):**

| OS | Befehl (Bun + jq in einem) |
|----|----|
| **macOS** (Homebrew) | `brew install bun jq` |
| **Linux (Debian/Ubuntu)** | `sudo apt install jq && curl -fsSL https://bun.sh/install \| bash` |
| **Linux (Fedora/RHEL)** | `sudo dnf install jq && curl -fsSL https://bun.sh/install \| bash` |
| **Linux (Arch)** | `sudo pacman -S jq bun` |
| **Windows** | WSL2 → dann wie Linux (Ubuntu) |

**Ohne Package-Manager (oder wer Homebrew bewusst meidet):**

| Tool | Befehl |
|------|--------|
| **Bun** (alle Unix-OS) | `curl -fsSL https://bun.sh/install \| bash` |
| **jq** | Binary von [jqlang.github.io/jq/download](https://jqlang.github.io/jq/download/) → in `$PATH`, `chmod +x` |

Bun-Doku: [bun.sh](https://bun.sh). Homebrew: [brew.sh](https://brew.sh).

### Repo

```bash
# Fork dieses Verzeichnis (Trainer gibt Link / Snapshot)
cd factory-starter
bun install
bun run dev
# → http://localhost:3000
```

`bun run dev` startet Hono auf 3000 und serviert `public/index.html`.

Wenn Setup im Workshop läuft: 5-10min Buffer für Bun-Install bei TN ohne JS-Stack einplanen.

## Workshop-Pfad (Tag 2 PM 15:00–16:00)

Ziel: v0-Pipeline aus zwei Subagents. Du baust:

1. `.claude/agents/refine.md` — Subagent, der Bean liest + Plan in Bean-Body schreibt
2. `.claude/agents/implement.md` — Subagent, der Plan liest + Code schreibt
3. `.claude/commands/refine.md` und `.claude/commands/implement.md` — Slash-Wrappers

Workshop-Anleitung: `../README.md` (Phase A-D). Solution-Vorlage: `../solution/.claude/`.

Dann lass laufen:

```
/refine bean-001
/implement bean-001
```

## Seed-Beans

| ID | Titel | Typ |
|----|-------|-----|
| `bean-001` | PATCH-Endpoint für Note-Update | Backend-only, kleiner Scope |
| `bean-002` | Tag-Filter UI + Backend | Full-Stack, mittlerer Scope |
| `bean-003` | Migration JSON → SQLite | Data-Flow-Change, Behavioral Contract |

Empfehlung Tag 2 PM: `bean-001` für ersten v0-Run (schnell, sichtbar). `bean-002` als Stretch wenn Zeit. `bean-003` für Tag 3, wenn jemand "Migration" als Kandidaten-Typ hat — guter Mynab-Pattern-Lookup.

## Verzeichnisstruktur

```
factory-starter/
├── package.json
├── tsconfig.json
├── .gitignore
├── README.md            (diese Datei)
├── CLAUDE.md            (placeholder, ihr füllt's auf)
├── src/
│   └── server.ts        (Hono app)
├── public/
│   └── index.html       (vanilla frontend)
├── data/
│   └── notes.json       (file-as-db, mit seed data)
└── .beans/
    ├── bean-001--patch-note-endpoint.md
    ├── bean-002--tag-filter.md
    └── bean-003--migrate-to-sqlite.md
```

## Was NICHT drin ist (Absicht)

- ❌ `.claude/` Verzeichnis → ihr baut's
- ❌ Hooks → kommt im Workshop
- ❌ Tests → bewusst weggelassen, dass Refine-Pläne Testing-Strategy enthalten müssen
- ❌ Database-Migration-Tool → in `bean-003` enthalten, müsst ihr planen
- ❌ Linting-Setup → falls Refine das aufgreifen will, soll's das

## Authenticity-Hinweis

Erste Runs werden schief gehen. Refine wird Sachen erfinden. Implement wird falsche Pfade nehmen. Das ist Material für die Refine-Diskussion und zeigt **warum** Challenge/Review-Stationen existieren.
