# Day 2 AM · Übung 02 — Rules (Pirate-Spin)

**Slot:** 10:10–10:40 · 30 Minuten (15min Build + Stretch)

## Concept

Rules = scoped Behavior-Instruktionen in `.claude/rules/<name>.md`. Frontmatter `glob:` definiert wann sie lädt → Rule wird **nur Teil des Contexts wenn passende File im Spiel ist**.

Unterschied zu CLAUDE.md / Skills:

| Layer | Lade-Verhalten | Beispiel |
|-------|---------------|----------|
| **CLAUDE.md** | Always-on global, gesamtes Repo | Projekt-Architektur, Tech-Stack |
| **Rules** | Always-on per Glob-Scope | Code-Konventionen pro File-Typ |
| **Skills** | On-demand per Description-Match | Workflow auf Anforderung |

## Ziel

Der Pirat kommt zurück — diesmal als Rule mit Glob-Scope. Glob-Mechanik **viscerale**: TN sieht Verhalten am Datei-Wechsel, nicht nur an Theorie.

**Der Pirat erscheint im Workshop dreimal:**

| Tag | Layer | Wo |
|-----|-------|----|
| Day 1 | CLAUDE.md | Always-on global |
| Day 1 | Skill | On-demand per Description |
| Day 2 AM | **Rule** | **Always-on per Glob** |

Same content, different layer. Loading-Mechanik wird durch Erfahrung greifbar.

## Schritte

1. Im exercise-Folder: `.claude/rules/pirate.md` anlegen
2. Frontmatter mit `glob: "**/*.md"`
3. Body: kurz, ein-zwei Sätze ("Reply in pirate language when working on Markdown files")
4. Claude Code starten im exercise-Folder
5. Test A: Edit `README.md` oder eine `.md` File → bittet um Edit → **Pirate**
6. Test B: Edit `main.cpp` (oder anderes Nicht-MD-File) → bittet um Edit → **normal**

## Verify

- Beim Editieren `.md`-Files wechselt Claude in Pirate-Sprache
- Beim Editieren `.cpp`/`.h`/`.py`-Files bleibt Claude normal
- Glob-Scope ist die Aktivierungs-Bedingung — nicht Description, nicht Skill-Trigger

## Stretch — C++ Konventionen

Für die, die schnell sind: zweite Rule für eigenen Stack.

```markdown
---
glob: "**/*.{cpp,h,hpp}"
---

# Modern C++ Konventionen

- `nullptr` statt `NULL` oder `0`
- Smart Pointers (`std::unique_ptr`, `std::shared_ptr`) — keine `new`/`delete`
- `auto` für Iterator-Typen und komplexe Templates
- Rule-of-Five wenn eigener Destructor
```

Testen an einer File mit Anti-Patterns: fragt Claude "Was siehst du in dieser Datei?" → nennt Violations + Rule als Quelle.

## Brücke zu nächster Übung

Tag 2 AM 03 — Subagents: Was Rules **always-on per Scope** sind, sind Subagents **on-demand in isoliertem Context**. Combo: Rules definieren *wie* Code aussehen muss, Subagents *exekutieren* in dieser Konvention.

## Solution

- [`solution/.claude/rules/pirate.md`](solution/.claude/rules/pirate.md) — Pirate-Rule, Glob `**/*.md`
- [`solution/.claude/rules/cpp-modern.md`](solution/.claude/rules/cpp-modern.md) — C++ Stretch-Rule
