# Tag 1 · Exercise 00 — Commit-Convention-CLAUDE.md

**Slot:** Block 1, ~10 Minuten (Foundations, Hook + Start Mechanismus)

## Goal

Verstehen, wie CLAUDE.md Verhalten ändert — **immer aktiv**, ohne Trigger-Wort.
Das Fundament für alles, was folgt (Skill = on-demand, Rule = scoped).

## Hintergrund

CLAUDE.md wird bei **jedem Session-Start** gelesen. Egal was gefragt wird —
die Anweisungen wirken. Anders als ein Skill (triggert bei Aufgaben-Match)
oder eine Rule (triggert bei Datei-Glob).

Hierarchie:

| Pfad | Geladen wann |
|------|--------------|
| `~/.claude/CLAUDE.md` | Jede Session, in jedem Nutzer-Ordner |
| `./CLAUDE.md` | Beim Projektstart im Repo |
| `./services/legacy/CLAUDE.md` | Bei Arbeit im Unterordner |

## Aufgabe

1. Leeres Testverzeichnis anlegen, `claude` starten.
2. Diff `exercise/sample.diff` zeigen und bitten: *"Schreib eine
   Commit-Message für diesen Diff."* → generisches Ergebnis (kein festes
   Format, keine Ticket-Referenz, kein Scope).
3. Session beenden, im Verzeichnis eine `CLAUDE.md` anlegen mit der
   gewünschten Konvention, z. B.:
   ```
   Commit-Messages folgen immer diesem Format:
   <type>(<scope>): <Betreff im Imperativ, max. 72 Zeichen>

   <Body: warum diese Änderung nötig war>

   Ref: <Ticket-ID, falls vorhanden>
   ```
4. `claude` neu starten, dieselbe Frage stellen → Konvention wird befolgt.
5. Variation: zweite Zeile ergänzen ("Scope ist immer der oberste
   Verzeichnisname des größten geänderten Pfads") → erneut fragen.
6. In einen Unterordner mit eigener `CLAUDE.md` gehen (z. B.
   `./services/legacy/CLAUDE.md` mit abweichender Konvention) — Hierarchie
   live beobachten.

## Verify

- Die Commit-Message folgt jetzt Type/Scope/Body/Ref.
- Ohne Neustart wirkt die CLAUDE.md noch nicht (nur bei Session-Start
  geladen).
- Die Unterordner-CLAUDE.md überschreibt die übergeordnete, statt sie zu
  ergänzen.

## Stretch

- Globale `~/.claude/CLAUDE.md` öffnen, einmal lesen — wirkt
  projektübergreifend immer.
- Was passiert, wenn Projekt- und globale CLAUDE.md sich widersprechen?
  (Ausprobieren!)

## Bridge zur nächsten Übung

CLAUDE.md ist eine **immer aktive Konvention** — jede Commit-Message folgt
demselben Format, in jedem Kontext. Übung 01 baut denselben Effekt als
**Skill**: on-demand, mit der Fähigkeit, sich an eine falsche Annahme
anzupassen statt starr zu scheitern.

## Solution

Referenzlösung liegt auf Branch **`solution/barista-day-1-00-commit-claude-md`**
(bewusst nicht auf `client/barista`, damit sie nicht in Claudes Kontext
landet — noch anzulegen). Erst selbst versuchen, dann vergleichen.
