# factory-workshop-excercises

Exercise repo for the **3-day "Agentic Coding" workshop** (h&w · SSW).

Cloned once on the morning of Day 1. Each exercise contains: the task (`README.md`), a starting point (`exercise/`), and a reference solution (`solution/`).

## Prerequisites

See [SETUP.md](SETUP.md). In short: beans CLI, jq, git, Claude Code, and **the toolchain for your language** (C++: cmake; Java: JDK 21 + Maven; Python: 3.9+).

## Structure

```
day-1/                      Foundations — Pirate-CLAUDE.md (always-on) + Pirate-Skill (on-demand)
day-2-am/                   Customization atoms: Skills → Rules → Subagents → Hooks
day-2-pm/                   Factory pipeline (Planner → Refine → Implement against the calc sandbox)
```

For Day 3 (Transfer Hackathon) you bring your own codebase — no folder here.

## Pick your language

The Day 2 PM calc sandbox ships in **three languages** — pick one and stick with it for the whole pipeline:

| Language | Sandbox folder | Build / test |
|----------|----------------|--------------|
| **C++** (reference) | `day-2-pm/sandbox/` | `cmake -B build && cmake --build build` · `ctest --test-dir build` |
| **Java** | `day-2-pm/sandbox-java/` | `mvn -q test` |
| **Python** | `day-2-pm/sandbox-python/` | `python3 -m unittest` |

All three are 1:1 ports — same grammar, same tests, same beans. The Day 2 PM
exercise READMEs carry per-language command blocks; read the block for your
sandbox. The Day 2 AM Rules exercise likewise ships `main.cpp` / `main.java` /
`main.py` plus a convention rule per language. See [SETUP.md](SETUP.md) for the
toolchain per language.

## Per exercise

| Folder | Contents |
|--------|--------|
| `README.md` | Goal · Time · Steps · Verify · Stretch · Bridge to the next exercise |
| `exercise/` | Starting point — you build here |
| `solution/` | Reference solution (don't peek before you've tried it yourself) |

## Clone

```bash
git clone https://github.com/hackersandwizards/factory-workshop-excercises.git
cd factory-workshop-excercises
```

## Day navigation

- [Day 1: Pirate-CLAUDE.md](day-1/00-pirate-claude-md/)
- [Day 1: Pirate-Skill](day-1/01-pirate-skill/)
- [Day 2 AM 01: Planning-Skill](day-2-am/01-planning-skill/)
- [Day 2 AM 02: Rules](day-2-am/02-rules/)
- [Day 2 AM 03: Subagent](day-2-am/03-subagent/)
- [Day 2 AM 04: env-block-Hook](day-2-am/04-env-block-hook/)
- [Day 2 PM 01: Planner-Rework](day-2-pm/01-planner-rework/)
- [Day 2 PM 02: Refine](day-2-pm/02-refine/)
- [Day 2 PM 03: Implement](day-2-pm/03-implement/)
