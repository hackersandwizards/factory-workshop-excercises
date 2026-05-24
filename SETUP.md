# Setup

Idealerweise **vor Tag 1** erledigt. Spätestens in Mittagspause Tag 1.

## Pflicht

- **Bun** (Runtime, statt Node)
- **jq** (für Hook-JSON-Parsing in Tag 2 AM)
- **git** mit `user.name` + `user.email` (Implement-Agent committed)
- **Claude Code** installiert + eingeloggt ([claude.com/code](https://claude.com/claude-code))

## Install pro OS

### Mit Package-Manager (empfohlen — ein Befehl)

| OS | Befehl (Bun + jq in einem) |
|----|----|
| **macOS** (Homebrew) | `brew install bun jq` |
| **Linux (Debian/Ubuntu)** | `sudo apt install jq && curl -fsSL https://bun.sh/install \| bash` |
| **Linux (Fedora/RHEL)** | `sudo dnf install jq && curl -fsSL https://bun.sh/install \| bash` |
| **Linux (Arch)** | `sudo pacman -S jq bun` |
| **Windows** | WSL2 → dann wie Linux (Ubuntu) |

### Ohne Package-Manager

| Tool | Befehl |
|------|--------|
| **Bun** (alle Unix-OS) | `curl -fsSL https://bun.sh/install \| bash` |
| **jq** | Binary von [jqlang.github.io/jq/download](https://jqlang.github.io/jq/download/) → in `$PATH`, `chmod +x` |

Bun-Doku: [bun.sh](https://bun.sh). Homebrew: [brew.sh](https://brew.sh).

## Verify

```bash
bun --version       # >= 1.0
jq --version        # >= 1.6
git config user.name && git config user.email
claude --version    # Claude Code installed
```

## Repo klonen

```bash
git clone https://github.com/hackersandwizards/factory-workshop-excercises.git
cd factory-workshop-excercises
```

## Factory-Starter (Tag 2 PM) vorab testen

```bash
cd day-2-pm/01-factory-pipeline/exercise
bun install
bun run dev
# → http://localhost:3000 → Notes-App lädt
```

Wenn das läuft, bist du Tag-2-PM-ready.

## Bei Problemen

Trainer ansprechen, Pair-Setup nutzen (zu zweit an einem Rechner) — Setup-Probleme nicht alleine debuggen während Workshop läuft.
