# Tag 1 · Exercise 01 — Commit-Skill: Purpose vs. Instructions

**Slot:** Block 1, ~20 Minuten (Foundations, Mechanismus)

## Goal

Denselben Effekt wie in Übung 00 als **Skill** bauen — und dabei live
erleben, warum eine zweckbeschriebene Skill robuster ist als eine
schrittgenaue. Läuft **beiläufig** mit, kein eigenes Etikett, keine Folie —
wird erst im Twist von Block 2 aufgegriffen.

## Zwei Varianten

Beide sollen eine Commit-Message nach Konvention erzeugen. Baue sie in
`exercise/.claude/skills/`:

**Variante A — `commit-message-strict`:** schrittgenaue Anleitung.

```yaml
---
description: Erstellt eine Commit-Message. Schritte befolgen.
---

1. Öffne die Datei `CHANGELOG.md` im Repo-Root.
2. Lies den letzten Eintrag, um den aktuellen Scope zu bestimmen.
3. Formuliere: <type>(<scope aus Schritt 2>): <Betreff>
4. Ergänze den Body aus dem Diff.
```

**Variante B — `commit-message-purpose`:** Zweck statt Schritte.

```yaml
---
description: Erstellt eine Commit-Message nach Team-Konvention (Type/Scope/Body/Ref). Nutzen, sobald ein Commit ansteht.
---

Ziel: eine Commit-Message, die in sechs Monaten noch erklärt, warum die
Änderung gemacht wurde. Leite Type und Scope aus dem tatsächlichen Inhalt
der Änderung ab, nicht aus einer festen Quelle. Body: warum, nicht nur was.
```

## Test — der Fehlschlag

`exercise/` enthält **keine** `CHANGELOG.md` (bewusst entfernt). Frag Claude
Code mit jeder Skill einzeln aktiv nach einer Commit-Message für
`../00-commit-claude-md/exercise/sample.diff`:

- **Strict:** Schritt 1 scheitert (Datei fehlt) — Claude hängt fest, rät,
  oder bricht ab, weil die vorgegebene Quelle fehlt.
- **Purpose:** leitet den Scope trotzdem aus dem Diff-Inhalt ab, liefert ein
  brauchbares Ergebnis.

## Verify

- Strict-Variante liefert ein sichtbar schlechteres oder gar kein Ergebnis,
  wenn die erwartete Datei fehlt.
- Purpose-Variante liefert in derselben Situation ein brauchbares Ergebnis.

## Was du lernst

- Genauere Instruktionen sind nicht automatisch robuster — sie sind nur
  robuster **solange die Annahme stimmt**.
- Eine Zweck-Beschreibung überlässt dem Modell die Urteilsfähigkeit, für die
  man es eigentlich einsetzt.

## Bridge zur nächsten Übung

CLAUDE.md und Skill liefern **eine** Konvention, egal wo im Repo. Übung 02
zeigt die Grenze davon: bei einer heterogenen Repo-Landschaft wie bei Barista
braucht es teils unterschiedliche Konventionen je nach **Ort** im Repo —
dafür ist eine Rule da.

## Solution

Referenzlösung liegt auf Branch **`solution/barista-day-1-01-commit-skill`**
(noch anzulegen) — beide SKILL.md-Varianten. Erst selbst bauen, dann
vergleichen.
