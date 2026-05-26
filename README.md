# factory-workshop-excercises

Übungs-Repo für den **3-Tages-Workshop "Agentic Coding"** (h&w · SSW).

Geklont ein Mal am Tag-1-Morgen. Enthält pro Übung: Aufgabe (`README.md`), Start-Punkt (`exercise/`), Referenz-Lösung (`solution/`).

## Voraussetzungen

Siehe [SETUP.md](SETUP.md). Kurz: cmake, beans CLI, jq, git, Claude Code installiert.

## Struktur

```
day-1/                      Foundations — Pirate-CLAUDE.md (always-on) + Pirate-Skill (on-demand)
day-2-am/                   Customization-Atoms: Skills → Rules → Subagents → Hooks
day-2-pm/                   Factory-Pipeline (Planner → Refine → Implement gegen calc-Sandbox)
```

Tag 3 (Transfer-Hackathon) bringt ihr eure eigene Codebase mit — kein Folder hier.

## Pro Übung

| Folder | Inhalt |
|--------|--------|
| `README.md` | Ziel · Zeit · Schritte · Verify · Stretch · Brücke zur nächsten Übung |
| `exercise/` | Start-Punkt — ihr baut hier |
| `solution/` | Referenz-Lösung (nicht reinschauen bevor ihr selbst probiert habt) |

## Klon

```bash
git clone https://github.com/hackersandwizards/factory-workshop-excercises.git
cd factory-workshop-excercises
```

## Tag-Navigation

- [Day 1: Pirate-CLAUDE.md](day-1/00-pirate-claude-md/)
- [Day 1: Pirate-Skill](day-1/01-pirate-skill/)
- [Day 2 AM 01: Planning-Skill](day-2-am/01-planning-skill/)
- [Day 2 AM 02: Rules](day-2-am/02-rules/)
- [Day 2 AM 03: Subagent](day-2-am/03-subagent/)
- [Day 2 AM 04: env-block-Hook](day-2-am/04-env-block-hook/)
- [Day 2 PM 01: Planner-Rework](day-2-pm/01-planner-rework/)
- [Day 2 PM 02: Refine](day-2-pm/02-refine/)
- [Day 2 PM 03: Implement](day-2-pm/03-implement/)
