# Tag 1 · Exercise 02 — Commit-Rule: Scope per Pfad

**Slot:** Block 2, ~15 Minuten (Rules & Hooks Kurzdemo, Einstieg)

## Concept

Rules = `.claude/rules/<name>.md`, aktiviert per `paths:`-Frontmatter (Liste
von Glob-Mustern) — **immer aktiv, aber nur für passende Dateien**, nicht
global wie CLAUDE.md, nicht on-demand wie eine Skill.

## Die eigentliche Frage, die diese Übung beantwortet

CLAUDE.md und Skill (Übung 00/01) geben **eine** Commit-Konvention für das
ganze Repo. Naheliegend wäre zu fragen: "Und was macht dann die Rule — auch
eine Commit-Konvention, nur als dritte Variante?" Nein — und der Grund ist
lehrreich:

**Eine Rule reagiert auf *welche Dateien gerade angefasst werden*, nicht
auf *welche Aktion gerade ansteht*.** Es gibt keinen Glob für "gerade wird
eine Commit-Message geschrieben" — Commit ist eine Aktion, kein
Dateimuster. Was sich per Glob sinnvoll scopen lässt, ist nicht *ob* eine
Konvention gilt, sondern *welche Variante* der Konvention gilt, abhängig
vom **Ort** im Repo.

Bei einer heterogenen Repo-Landschaft wie bei Barista ist genau das der
Normalfall: unterschiedliche Teams/Services im selben Repo wollen
unterschiedliche Commit-Scopes, ohne dass jemand von Hand daran denken
muss, welcher gerade zutrifft.

## Aufgabe

`exercise/` enthält zwei Platzhalter-Bereiche (**vor dem Workshop durch
echte Barista-Pfade ersetzen, falls ihr ein Beispiel-Repo mitbringt**):

```
exercise/
├── services/api/handler.py
└── services/frontend/component.tsx
```

1. `.claude/rules/commit-scope-api.md` anlegen:
   ```yaml
   ---
   paths:
     - "services/api/**"
   ---
   Commits, die Dateien unter `services/api/` betreffen, nutzen den Scope
   `api`: `<type>(api): <Betreff>`.
   ```
2. `.claude/rules/commit-scope-frontend.md` anlegen:
   ```yaml
   ---
   paths:
     - "services/frontend/**"
   ---
   Commits, die Dateien unter `services/frontend/` betreffen, nutzen den
   Scope `frontend`: `<type>(frontend): <Betreff>`.
   ```
3. Claude Code im `exercise/`-Ordner starten.
4. `services/api/handler.py` ändern, Commit-Message erfragen → Scope `api`.
5. `services/frontend/component.tsx` ändern, Commit-Message erfragen →
   Scope `frontend`.
6. Eine Datei außerhalb beider Pfade ändern (z. B. `README.md`) → keine der
   beiden Rules greift, es zählt nur noch die CLAUDE.md-/Skill-Konvention
   aus Übung 00/01 (kein spezifischer Scope).

## Verify

- Scope wechselt automatisch mit dem bearbeiteten Pfad, ohne dass jemand
  ihn ansagt.
- Dateien außerhalb beider Globs fallen auf die allgemeine Konvention
  zurück.
- Beide Rules gleichzeitig aktiv, kein Konflikt, weil sich ihre Globs nicht
  überschneiden.

## Stretch

- Was passiert, wenn sich zwei Rules mit **überlappenden** Globs
  widersprechen? (Ausprobieren — guter Anknüpfungspunkt für den Twist in
  Block 2: "immer aktiv" heißt nicht "immer eindeutig".)

## Bridge zur Hooks-Kurzdemo

Die Rule hier ist weiterhin eine **Bitte** — nichts hindert Claude
technisch daran, den Scope zu ignorieren. Die Hooks-Demo direkt im
Anschluss (`.env`-Block) zeigt den Unterschied zur harten Leitplanke.

## Solution

Referenzlösung liegt auf Branch **`solution/barista-day-1-02-commit-rule`**
(bewusst nicht auf `client/barista`, damit sie nicht in Claudes Kontext
landet) — beide Rule-Dateien. Erst selbst bauen, dann vergleichen:

```bash
git checkout solution/barista-day-1-02-commit-rule   # inspect solution/.claude/rules/…
git checkout client/barista                          # zurück zur eigenen Arbeit
git show solution/barista-day-1-02-commit-rule:clients/barista/exercises/day-1/02-commit-rule/solution/.claude/rules/commit-scope-api.md
```
