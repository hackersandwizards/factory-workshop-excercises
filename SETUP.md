# Setup

Ideally done **before Day 1**. At the latest during the Day 1 lunch break.

## Required — everyone (any language)

- **beans CLI** (bean management for the Day 2 PM Factory pipeline)
- **jq** (for hook JSON parsing on Day 2 AM)
- **git** with `user.name` + `user.email` set (the implement agent commits)
- **Claude Code** installed + logged in ([claude.com/code](https://claude.com/claude-code))

## Required — your language toolchain (pick ONE)

The Day 2 PM calc sandbox exists in three languages. Install only the one you'll use:

- **C++** — `cmake` (>= 3.20) + a C++17 compiler. Sandbox: `day-2-pm/sandbox/`.
- **Java** — **JDK 21** + **Maven** (>= 3.8). Sandbox: `day-2-pm/sandbox-java/`.
- **Python** — **Python 3.9+** (stdlib only, no pip packages needed). Sandbox: `day-2-pm/sandbox-python/`.

## Install per OS

### Common tools (beans, jq) + per-language toolchain

| OS | Common | C++ | Java | Python |
|----|--------|-----|------|--------|
| **macOS** (Homebrew) | `brew install jq hmans/beans/beans` | `brew install cmake` | `brew install openjdk@21 maven` | `brew install python@3.12` (or system Python 3) |
| **Linux (Debian/Ubuntu)** | `sudo apt install jq` + beans via Homebrew/binary | `sudo apt install cmake build-essential` | `sudo apt install openjdk-21-jdk maven` | `sudo apt install python3` |
| **Linux (Fedora/RHEL)** | `sudo dnf install jq` + beans via Homebrew/binary | `sudo dnf install cmake gcc-c++` | `sudo dnf install java-21-openjdk-devel maven` | `sudo dnf install python3` |
| **Linux (Arch)** | `sudo pacman -S jq` + beans via AUR/binary | `sudo pacman -S cmake base-devel` | `sudo pacman -S jdk21-openjdk maven` | `sudo pacman -S python` |
| **Windows** | WSL2 → then same as Linux (Ubuntu) | — | — | — |

### beans CLI without Homebrew

Release binary from [github.com/hmans/beans](https://github.com/hmans/beans) → put it in `$PATH`, `chmod +x`.

## Verify

```bash
# everyone
jq --version        # >= 1.6
beans --version     # CLI available
git config user.name && git config user.email
claude --version    # Claude Code installed

# your language toolchain (run the one you installed)
cmake --version     # C++   — >= 3.20
mvn --version       # Java  — Maven + JDK 21 reported
python3 --version   # Python — >= 3.9
```

## Clone the repo

```bash
git clone https://github.com/hackersandwizards/factory-workshop-excercises.git
cd factory-workshop-excercises
```

## Test the calc sandbox (Day 2 PM) in advance

Run the block for the language you picked.

**C++**
```bash
cd day-2-pm/sandbox
cmake -B build
cmake --build build
ctest --test-dir build
./build/calc          # REPL
```

**Java**
```bash
cd day-2-pm/sandbox-java
mvn -q test
mvn -q compile exec:java   # REPL
```

**Python**
```bash
cd day-2-pm/sandbox-python
python3 -m unittest
python3 -m calc       # REPL
```

If the tests pass green and the REPL starts, you're Day 2 PM ready.

## If you run into problems

Ask a trainer, use a pair setup (two people at one machine) — don't debug setup problems on your own while the workshop is running.
