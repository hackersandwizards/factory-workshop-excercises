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

## Pflicht — Ticket-Creator (statt Datei-Ablage)

> **Backend:** Standard ist **Jira** (lokaler Jira-MCP), Fallback ist die
> **`beans`-CLI**. Alles unten gilt für beide — nur der Anlege-Schritt
> unterscheidet sich.

- [ ] **Frontmatter** — `argument-hint: [kurze Feature-Beschreibung]` (optional, kein `<bean-id>` — der entsteht erst hier). Beschreibung anpassen: "legt ein neues Ticket an (Jira via MCP, Fallback beans CLI) mit Description + High-Level Plan + AC".
- [ ] **Capture** — Feature-Idee vom Nutzer aufnehmen, in einem Satz zurückspiegeln
- [ ] **STOP-Guard bei den Alternativen** — der Skill präsentiert 2-3 Optionen und **wartet auf eine explizite Auswahl**. Auch wenn vorher "autonom" / "keine Rückfragen" gesagt wurde — die Auswahl der Approach ist ein Pflicht-Gate, keine Rückfrage im eigentlichen Sinn.
- [ ] **Ticket anlegen — ein Schreibvorgang** mit vollständigem Body:
  - *Jira:* Issue über den Jira-MCP. Summary = Titel, Description = Description + Notizen + `## High-Level Plan` (Approach, Steps, AC, Non-Goals) in einem Rutsch. Issue-Key an den Nutzer zurückgeben (`/refine <key>`, Tag 2)
  - *Beans:* `beans create "<title>" -t feature -d "<heredoc>"` mit demselben Inhalt. Kein `--body-append`-Flag — für sehr lange Bodies `--body-file <path>` statt `-d`. ID aus stdout parsen
  - Kein zweiter Schreibvorgang zum Nachtragen — der Body geht in einem Rutsch raus
- [ ] **Schema festzurren** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Heading-Contract** — der Plan steht wortwörtlich unter der Überschrift `## High-Level Plan`. `/refine` parst per Exact-Match — fehlt die Überschrift, bricht Refine ab. Bei Jira nach dem ersten Ticket prüfen, ob die Description das Heading wörtlich behalten hat.
- [ ] **Harte Regel** — keine Dateipfade, keine Funktionssignaturen, keine Klassennamen im Plan (Acceptance Criteria statt Implementierungsdetails)

## Pflicht — Trigger-Verhalten

- [ ] **`disable-model-invocation: true`** in der Frontmatter setzen — der Planner startet einen Ticket-Nebeneffekt und eine mehrstufige Rückfrage-Dialog-Kette. Beides soll bewusst per `/planner ...` angestoßen werden, nicht vom Modell selbst inferiert.
- [ ] Verifiziert, dass eine beiläufige Bitte ("kannst du das kurz planen?") den Skill **nicht** von selbst triggert

## Pflicht — Disziplin

- [ ] Backend nie am Werkzeug vorbei beschreiben — Jira nur über den MCP, `.beans/*.md` nur über die CLI
- [ ] Quellcode nie editieren — der Planner ist read-only auf Source
- [ ] Self-Review bleibt drin — das ist der letzte Guardrail vor der Übergabe

## Self-Check vor der Solution

- [ ] `/planner <euer Feature>` → ein neues Ticket entsteht (Jira-Issue bzw. `beans list`)
- [ ] Die Description zeigt Description + `## High-Level Plan` mit Approach/Steps/AC/Non-Goals
- [ ] Der Plan enthält **keine** Dateipfade, **keine** Funktionsnamen, **keine** Zeilenreferenzen
- [ ] Der Skill triggert NICHT von selbst bei einer beiläufigen Formulierung (siehe oben)
- [ ] Der Skill verweigert sich sauber, wenn sein Backend fehlt (Jira-MCP weg bzw. `beans`-CLI fehlt)

## Snippet-Template (falls ihr einen Startpunkt wollt)

```markdown
---
name: planner
description: Legt ein neues Ticket an (Jira via MCP, Fallback beans CLI) mit Description + High-Level Plan + AC. Nur explizit per /planner aufrufen.
disable-model-invocation: true
argument-hint: [kurze Feature-Beschreibung]
---

# Planner

Du bist Planning-Partner, nicht Executor. Das Ergebnis ist ein Ticket, kein Code.

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

### Phase 5: Ticket anlegen
- Backend: Jira via MCP. Ist der MCP nicht erreichbar, auf
  `beans create "<title>" -t feature -d "<heredoc>"` ausweichen und das
  ansagen — niemals still in eine Datei planen
- Body enthält Description + `## High-Level Plan` (Approach, Steps, AC, Non-Goals)
- Keine Dateipfade, keine Funktionssignaturen, keine Klassennamen
- ID bzw. Issue-Key an den Nutzer zurückgeben, Hinweis auf `/refine <id>` (Tag 2)

## Regeln

- Nie während der Planung implementieren
- Nie Explore überspringen — blinde Pläne sind Ratespiele
- Nie Self-Review überspringen — letzter Guardrail vor der Übergabe
- Nie den Ticket-Anlege-Schritt überspringen (Konversation ≠ Gedächtnis)
- Nie ohne explizite Alternativen vorschlagen
- Wird der Nutzer ungeduldig: trotzdem eine Frage stellen. Disziplin > Tempo.
- Backend nur über sein Werkzeug beschreiben (Jira-MCP bzw. beans-CLI), nie daran vorbei
```

**Einsteiger:** Snippet übernehmen und Domain/Beschreibung anpassen.
**Fortgeschritten:** von Grund auf — eigene Phasen-Struktur, eigene Auswahl der Mechanik. Das 4★-Subset bleibt Pflicht.

## Run

```bash
cd exercise
cp -r .claude <euer-sandbox-ordner>/            # + .beans.yml, falls Fallback
cd <euer-sandbox-ordner>
claude
> /planner <euer Feature>
```
