# Setup

Ideally done **before Day 1**. At the latest during the Day 1 lunch break.

## Required

- **cmake** (>= 3.20) + a C++17 compiler (to build the Day 2 PM calc sandbox)
- **beans CLI** (bean management for the Day 2 PM Factory pipeline)
- **jq** (for hook JSON parsing on Day 2 AM)
- **git** with `user.name` + `user.email` set (the implement agent commits)
- **Claude Code** installed + logged in ([claude.com/code](https://claude.com/claude-code))

## Install per OS

### With a package manager (recommended)

| OS | Command |
|----|----|
| **macOS** (Homebrew) | `brew install cmake jq hmans/beans/beans` |
| **Linux (Debian/Ubuntu)** | `sudo apt install cmake jq build-essential` + beans via Homebrew or release binary |
| **Linux (Fedora/RHEL)** | `sudo dnf install cmake jq gcc-c++` + beans via Homebrew or release binary |
| **Linux (Arch)** | `sudo pacman -S cmake jq base-devel` + beans via AUR/binary |
| **Windows** | WSL2 → then same as Linux (Ubuntu) |

### beans CLI without Homebrew

Release binary from [github.com/hmans/beans](https://github.com/hmans/beans) → put it in `$PATH`, `chmod +x`.

## Verify

```bash
cmake --version     # >= 3.20
jq --version        # >= 1.6
beans --version     # CLI available
git config user.name && git config user.email
claude --version    # Claude Code installed
```

## Clone the repo

```bash
git clone https://github.com/hackersandwizards/factory-workshop-excercises.git
cd factory-workshop-excercises
```

## Test the calc sandbox (Day 2 PM) in advance

```bash
cd day-2-pm/sandbox
cmake -B build
cmake --build build
ctest --test-dir build
./build/calc        # REPL
```

If the tests pass green and the REPL starts, you're Day 2 PM ready.

## If you run into problems

Ask a trainer, use a pair setup (two people at one machine) — don't debug setup problems on your own while the workshop is running.
