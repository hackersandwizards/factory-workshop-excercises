# Day 1 · Übung 00 — Pirate-CLAUDE.md

**Slot:** 14:00–14:15 (Block 3) · ~10 Minuten

## Ziel

Verstehen wie `CLAUDE.md` Verhalten ändert — **always-on**, ohne Trigger-Wort. Foundation für alles, was später kommt (Skill = on-demand, Rule = scoped, Hook = deterministisch).

## Hintergrund

`CLAUDE.md` wird bei **jedem Session-Start** gelesen. Egal was du fragst — die Instruktionen wirken. Anders als ein Skill (triggert per Task-Match) oder eine Rule (triggert per File-Glob).

Hierarchie:

| Pfad | Geladen wann |
|------|--------------|
| `~/.claude/CLAUDE.md` | Jede Session, jeder User-Ordner |
| `./CLAUDE.md` | Projekt-Start im Repo |
| `./src/CLAUDE.md` | Wenn du im Subfolder arbeitest |

## Aufgabe

1. Leeres Test-Verzeichnis anlegen, `claude` starten
2. *"Erzähl mir eine kurze Geschichte über einen Piraten."* — neutrale Antwort
3. Session beenden, im Verzeichnis `CLAUDE.md` anlegen mit einer Zeile:
   ```
   Antworte immer wie ein Pirat. Beginne jede Antwort mit "Arrr".
   ```
4. `claude` neu starten, selbe Frage stellen → Pirate-Stil
5. Variation: zweite Zeile *"Streue immer ein deutsches Schimpfwort ein."* → erneut Frage stellen
6. Geh in einen Subfolder mit eigener `CLAUDE.md` (z.B. `./.test-subfolder/CLAUDE.md` mit gegenteiliger Anweisung) — Hierarchie beobachten

## Verify

- Antwort startet mit "Arrr" o.ä.
- Ohne Neustart wirkt CLAUDE.md noch nicht (loaded only at session-start)
- Subfolder-CLAUDE.md überschreibt Parent

## Stretch

- Globale `~/.claude/CLAUDE.md` öffnen, einmal lesen — wirkt always-on über alle Projekte
- Was passiert wenn projekt-CLAUDE.md und globale widersprechen? (Test!)

## Solution

[`solution/CLAUDE.md`](solution/CLAUDE.md) — minimale Pirate-Instruction zum Kopieren.

## Brücke zur nächsten Übung

CLAUDE.md ist **always-on**. Das ist Power und Risiko: jede Instruction kostet jeden Turn Token. Für Task-spezifisches Verhalten → Skill ([`../01-pirate-skill/`](../01-pirate-skill/)). Gleicher Effekt, on-demand getriggert.
