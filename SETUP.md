# Setup

Idealerweise **vor Tag 1** erledigt. Spätestens in Mittagspause Tag 1.

## Pflicht

- **cmake** (>= 3.20) + C++17-Compiler (Tag 2 PM calc-Sandbox bauen)
- **beans CLI** (Bean-Management für Factory-Pipeline Tag 2 PM)
- **jq** (für Hook-JSON-Parsing in Tag 2 AM)
- **git** mit `user.name` + `user.email` (Implement-Agent committed)
- **Claude Code** installiert + eingeloggt ([claude.com/code](https://claude.com/claude-code))

## Install pro OS

### Mit Package-Manager (empfohlen)

| OS | Befehl |
|----|----|
| **macOS** (Homebrew) | `brew install cmake jq hmans/beans/beans` |
| **Linux (Debian/Ubuntu)** | `sudo apt install cmake jq build-essential` + beans via Homebrew oder Release-Binary |
| **Linux (Fedora/RHEL)** | `sudo dnf install cmake jq gcc-c++` + beans via Homebrew oder Release-Binary |
| **Linux (Arch)** | `sudo pacman -S cmake jq base-devel` + beans via AUR/Binary |
| **Windows** | WSL2 → dann wie Linux (Ubuntu) |

### beans CLI ohne Homebrew

Release-Binary von [github.com/hmans/beans](https://github.com/hmans/beans) → in `$PATH`, `chmod +x`.

## Verify

```bash
cmake --version     # >= 3.20
jq --version        # >= 1.6
beans --version     # CLI verfügbar
git config user.name && git config user.email
claude --version    # Claude Code installed
```

## Repo klonen

```bash
git clone https://github.com/hackersandwizards/factory-workshop-excercises.git
cd factory-workshop-excercises
```

## calc-Sandbox (Tag 2 PM) vorab testen

```bash
cd day-2-pm/sandbox
cmake -B build
cmake --build build
ctest --test-dir build
./build/calc        # REPL
```

Wenn Tests grün laufen und REPL startet, bist du Tag-2-PM-ready.

## Bei Problemen

Trainer ansprechen, Pair-Setup nutzen (zu zweit an einem Rechner) — Setup-Probleme nicht alleine debuggen während Workshop läuft.
