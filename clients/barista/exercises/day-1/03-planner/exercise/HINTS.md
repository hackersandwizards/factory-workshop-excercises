# Build checklist

Kein Copy-Paste-Startpunkt diesmal — `.claude/skills/` ist leer. Ihr baut die
SKILL.md von Grund auf. Zwei Quellen fließen hier zusammen: die
Explore→Clarify→Propose→Self-Review-Mechanik aus dem Planning-Skill und die
Bean-Creator-Rework-Punkte, die aus der Dateiablage `.plans/<task>.md` eine
echte `beans create` macht.

## Pflicht — die 4★-Mechanik (Kern des Planners)

- [ ] **Explore project context** — Recon VOR der ersten Frage (README, Top-Level-Dirs, relevante Dateien lesen)
- [ ] **One question per message** — Multiple-Choice wo möglich, auf Antwort warten
- [ ] **2-3 Alternativen vor Konvergenz** — explizite Trade-offs, NICHT selbst werten
- [ ] **Self-Review (Guardrail)** — ein Check-Schritt vor dem Finalisieren, bevor der Bean angelegt wird

## Pflicht — Bean-Creator (statt Datei-Ablage)

- [ ] **Frontmatter** — `argument-hint: [kurze Feature-Beschreibung]` (optional, kein `<bean-id>` — der entsteht erst hier). Beschreibung anpassen: "legt einen neuen Bean an via beans CLI mit Description + High-Level Plan + AC".
- [ ] **Capture** — Feature-Idee vom Nutzer aufnehmen, in einem Satz zurückspiegeln
- [ ] **STOP-Guard bei den Alternativen** — der Skill präsentiert 2-3 Optionen und **wartet auf eine explizite Auswahl**. Auch wenn vorher "autonom" / "keine Rückfragen" gesagt wurde — die Auswahl der Approach ist ein Pflicht-Gate, keine Rückfrage im eigentlichen Sinn.
- [ ] **Bean anlegen — ein CLI-Call** mit vollständigem Body:
  - `beans create "<title>" -t feature -d "<heredoc>"` mit Description + Notizen + `## High-Level Plan` (Approach, Steps, AC, Non-Goals) in einem Rutsch
  - Die `beans`-CLI hat **kein** `--body-append`-Flag. Für sehr lange Bodies `--body-file <path>` statt `-d` verwenden.
  - ID aus stdout parsen für die Übergabe an den Nutzer (`/refine <id>`, Tag 2)
- [ ] **Schema festzurren** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Heading-Contract** — der Plan steht wortwörtlich unter der Überschrift `## High-Level Plan`. `/refine` parst per Exact-Match — fehlt die Überschrift, bricht Refine ab.
- [ ] **Harte Regel** — keine Dateipfade, keine Funktionssignaturen, keine Klassennamen im Plan (Acceptance Criteria statt Implementierungsdetails)

## Pflicht — Trigger-Verhalten

- [ ] **`disable-model-invocation: true`** in der Frontmatter setzen — der Planner startet einen Bean-Nebeneffekt und eine mehrstufige Rückfrage-Dialog-Kette. Beides soll bewusst per `/planner ...` angestoßen werden, nicht vom Modell selbst inferiert.
- [ ] Verifiziert, dass eine beiläufige Bitte ("kannst du das kurz planen?") den Skill **nicht** von selbst triggert

## Pflicht — Disziplin

- [ ] `.beans/*.md` nie direkt editieren — immer über die CLI
- [ ] Quellcode nie editieren — der Planner ist read-only auf Source
- [ ] Self-Review bleibt drin — das ist der letzte Guardrail vor der Übergabe

## Self-Check vor der Solution

- [ ] `/planner <euer Feature>` → ein neuer Bean entsteht (`beans list` zeigt ihn)
- [ ] `beans show <neue-id>` zeigt eine Description + ein `## High-Level Plan` mit Approach/Steps/AC/Non-Goals
- [ ] Der Plan enthält **keine** Dateipfade, **keine** Funktionsnamen, **keine** Zeilenreferenzen
- [ ] Der Skill triggert NICHT von selbst bei einer beiläufigen Formulierung (siehe oben)
- [ ] Der Skill verweigert sich sauber, wenn die `beans`-CLI fehlt

## Snippet-Template (falls ihr einen Startpunkt wollt)

```markdown
---
name: planner
description: Legt einen neuen Bean an via beans CLI mit Description + High-Level Plan + AC. Nur explizit per /planner aufrufen.
disable-model-invocation: true
argument-hint: [kurze Feature-Beschreibung]
---

# Planner

Du bist Planning-Partner, nicht Executor. Das Ergebnis ist ein Bean, kein Code.

## Workflow

### Phase 1: Projekt-Kontext explorieren
- README, Top-Level-Dirs, relevante Kern-Dateien lesen
- Einstiegspunkte, Tests, Konventionen identifizieren
- Befunde VOR der ersten Frage kurz zurückmelden

### Phase 2: Klären (eine Frage pro Nachricht)
- Genau EINE Frage pro Nachricht
- Multiple-Choice wo möglich
- Nicht weitergehen, bevor die aktuelle Frage beantwortet ist

### Phase 3: Alternativen vorschlagen
- 2-3 verschiedene Ansätze mit ehrlichen Trade-offs
- Auf explizite Auswahl warten (STOP-Guard)
- Nicht selbst werten — die Wahl liegt beim Nutzer

### Phase 4: Self-Review (Guardrail)
- Vor der Übergabe: eigenen Vorschlag nochmal lesen
- Prüfen: Constraints eingehalten? Trade-offs ehrlich? Etwas handgewedelt?
- Bei Lücken: zurück zu Phase 2

### Phase 5: Bean anlegen
- Ein `beans create "<title>" -t feature -d "<heredoc>"`-Call
- Body enthält Description + `## High-Level Plan` (Approach, Steps, AC, Non-Goals)
- Keine Dateipfade, keine Funktionssignaturen, keine Klassennamen
- ID aus stdout an den Nutzer zurückgeben, Hinweis auf `/refine <id>` (Tag 2)

## Regeln

- Nie während der Planung implementieren
- Nie Explore überspringen — blinde Pläne sind Ratespiele
- Nie Self-Review überspringen — letzter Guardrail vor der Übergabe
- Nie den Bean-Anlege-Schritt überspringen (Konversation ≠ Gedächtnis)
- Nie ohne explizite Alternativen vorschlagen
- Wird der Nutzer ungeduldig: trotzdem eine Frage stellen. Disziplin > Tempo.
- `.beans/*.md` nie direkt schreiben, nur über die CLI
```

**Einsteiger:** Snippet übernehmen und Domain/Beschreibung anpassen.
**Fortgeschritten:** von Grund auf — eigene Phasen-Struktur, eigene Auswahl der Mechanik. Das 4★-Subset bleibt Pflicht.

## Run

```bash
cd exercise
cp -r .claude .beans.yml <euer-sandbox-ordner>/
cd <euer-sandbox-ordner>
claude
> /planner <euer Feature>
```
