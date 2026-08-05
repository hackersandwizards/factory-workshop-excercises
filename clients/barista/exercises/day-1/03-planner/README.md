# Tag 1 · Exercise 03 — Planner-Skill mit Bean-Anbindung

**Slot:** Block 3, 11:00–12:00 · 60 Minuten (Hands-on)

## Goal

Einen eigenen Planner-Skill bauen, der bei `/planner` **direkt ein Ticket
anlegt** statt in eine `.md`-Datei zu planen — das "Was" der Pipeline, ohne
Pfade oder Signaturen.

**Zwei Backends, ein Vertrag.** Standard ist **Jira** (über den lokalen
Jira-MCP). Fallback ist die **`beans`-CLI**, falls der MCP-Zugriff nicht
steht. Die Mechanik des Skills ist in beiden Fällen identisch — nur der
letzte Schritt (Phase 5) unterscheidet sich. Genau das ist der Punkt: der
Planner kennt sein Backend nicht, er erfüllt einen Vertrag.

## Herkunft

Kombiniert aus `day-2-am/01-planning-skill` (4★-Subset: Explore / One
question per message / Alternatives / Self-Review) und
`day-2-pm/01-planner-rework` (Bean-Creator statt `.plans/`-Datei) — im
Original zwei getrennte Übungen an verschiedenen Tagen, hier **in einem
Schritt**. Spart einen Umbauschritt, bringt sofort den echten
Pipeline-Baustein.

## Vorbereitung

**Backend prüfen.** Für den Jira-Weg: der Jira-MCP muss erreichbar sein und
Schreibrechte auf ein Projekt haben, in dem ihr Tickets anlegen, bearbeiten
und schließen dürft. Für den Fallback: `brew install hmans/beans/beans`,
prüfen mit `beans --version`. Wenn möglich beides bereithalten — dann kostet
ein Ausfall zur Laufzeit keine Übungszeit.

Kopiere `exercise/.claude` (und für den Fallback `exercise/.beans.yml`) in
ein Verzeichnis deiner Wahl — am besten ein
echtes, unkritisches Stück deines eigenen Stacks, nicht ein leeres
Test-Verzeichnis. Wähle vorher eine Planungsdomäne, z. B.
`migration-planner`, `refactor-planner`, `feature-planner`.

## Hook (~10 min, geführt vom Trainer)

Claude Code ohne jeden Planner eine größere, mehrschrittige Aufgabe geben
("bau Feature X komplett um"). Beobachten: es rennt los, trifft eigene
Annahmen, ändert vermutlich die falschen Dateien zuerst. Kontrollverlust
live erlebt, bevor über Planning gesprochen wird.

## Mechanismus — Bauen (~35 min)

1. `exercise/.claude` + `exercise/.beans.yml` in dein gewähltes Verzeichnis
   kopieren.
2. `.claude/skills/planner/SKILL.md` von Grund auf bauen (kein
   Copy-Paste-Startpunkt — siehe `HINTS.md` für Checkliste +
   Schnipsel-Vorlage).
3. Pflicht-Subset (4★): Kontext explorieren, bevor die erste Frage gestellt
   wird · eine Frage pro Nachricht · 2–3 Alternativen vor der Konvergenz,
   ohne selbst eine zu bevorzugen · Self-Review vor Abschluss.
4. Ticket-Erzeugung statt Datei-Plan — **ein** Schreibvorgang mit
   vollständigem Body:
   - *Jira (Standard):* Issue über den Jira-MCP anlegen. Summary = Titel,
     Description = Description + `## High-Level Plan`. Issue-Key (z. B.
     `BAR-123`) für die Übergabe an `/refine` (Tag 2) zurückgeben.
   - *Beans (Fallback):* `beans create "<Titel>" -t feature -d "<Heredoc mit
     Description + ## High-Level Plan>"`. Die `beans`-CLI hat **kein**
     `--body-append` — bei langen Bodies `--body-file <pfad>` statt `-d`
     nutzen. ID aus stdout parsen.
5. Heading-Vertrag: der Plan steht wortwörtlich unter der Überschrift
   `## High-Level Plan` — `/refine` an Tag 2 parst per Exact-Match, fehlt
   die Überschrift, bricht Refine ab. **Bei Jira aufpassen:** die
   Description darf das Markdown-Heading nicht wegformatieren. Nach dem
   ersten Ticket einmal nachlesen, was tatsächlich gespeichert wurde.
6. Harte Regel: **keine** Dateipfade, **keine** Funktionssignaturen,
   **keine** Klassennamen im Plan — stattdessen Acceptance Criteria.
7. **Neu, bewusste Design-Entscheidung:** `disable-model-invocation: true`
   ins Frontmatter setzen. Zwei Gründe: der Hook oben bleibt sauber (Claude
   kann nicht selbst entscheiden, "vorsichtshalber" zu planen und den
   Kontrollverlust im Hook abzuschwächen), und das Anlegen eines Beans ist
   ein Seiteneffekt — genau der Fall, für den explizite statt automatische
   Auslösung empfohlen wird. Passt außerdem zum
   Human-in-the-loop-Grundton des Workshops.
8. Test: `/planner <eigene Aufgabe>` → ein neues Ticket existiert, und seine
   Description enthält `## High-Level Plan` mit Approach/Steps/AC/Non-Goals.
   (Jira: Issue im Projekt öffnen. Beans: `beans list`, `beans show <id>`.)

## Verify

- Nach dem `/planner`-Lauf existiert ein neues Ticket (Jira-Issue bzw. Bean)
- Der Plan enthält keine Dateipfade, keine Funktionsnamen, keine
  Zeilenverweise
- Der Skill fragt eine Frage nach der anderen, nicht alle auf einmal
- Der Skill triggert **nicht** von selbst — nur auf expliziten
  `/planner`-Aufruf (Test: eine komplexe Aufgabe beiläufig erwähnen, ohne
  `/planner` zu tippen — nichts sollte passieren)
- Der Skill scheitert kontrolliert, wenn sein Backend fehlt (Jira-MCP nicht
  erreichbar bzw. `beans`-CLI nicht installiert) — er erfindet kein Ticket
  und plant nicht still in eine Datei

## Twist (~10 min)

Erwartung wäre: "ein Planungsschritt macht den Agenten langsamer, weil er
erst fragt statt loszulegen." Auflösung: das Gegenteil — der Bean als
Datei-Vertrag macht die nächsten Pipeline-Schritte (Refine, Implement)
günstiger und schneller, weil sie nicht neu explorieren müssen. Die
Investition zahlt sich nicht in der einzelnen Aufgabe aus, sondern über
die ganze Pipeline.

## Abschluss (~5 min)

"Ironischerweise ist der Agent, der zuerst am meisten nachfragt, am Ende
der, der am wenigsten nervt."

## Stretch

- Die restlichen 4 Mechaniken ergänzen (Approval-Gate, explizite
  Constraints/Non-Goals als eigene Sektion, Repeatable Routine)
- Eigenen Subagent-Typ definieren (`.claude/agents/<name>.md`) — aber siehe
  unten, warum das für den Planner selbst (noch) nicht der richtige
  Schritt ist
- Skill mit `skill-creator` evaluieren, siehe `exercise/evals/PLANNED-CASES.md`

## Warum kein Subagent (noch)

Naheliegende Frage: warum bleibt das ein normaler Skill statt
`context: fork`? Der Planner lebt von der Rückfrage — "eine Frage pro
Nachricht" braucht Zugriff auf den laufenden Gesprächsverlauf, den ein
geforkter Subagent nicht hat (er bekommt nur den Skill-Inhalt als Prompt,
isoliert, ohne Historie). Der richtige Ort für einen Fork ist Refine an
Tag 2 (reine, selbstständige Lesearbeit, kein Rückfragebedarf) — dort ist
er auch schon eingeplant. Zusätzlich: Björn möchte den
Planner-Mechanismus erst in der einfacheren, leichter debugbaren Form
stabil sehen, bevor die Architektur verkompliziert wird.

## Bridge zu Tag 2

Die Ticket-ID (Jira-Issue-Key bzw. Bean-ID) ist die Übergabe an `/refine
<id>` — Pfade und Signaturen kommen dort dazu, nicht hier.

## Solution

Referenzlösung liegt auf Branch **`solution/barista-day-1-03-planner`**
(bewusst nicht auf `client/barista`, damit sie nicht in Claudes Kontext
landet) — `solution/.claude/skills/planner/SKILL.md` mit vollem 4★-Subset +
`disable-model-invocation: true`. Die Referenzlösung schreibt nach
**Beans** — wer nach Jira gebaut hat, vergleicht Phase 1–4 eins zu eins und
nur Phase 5 sinngemäß. Erst selbst bauen, dann vergleichen:

```bash
git checkout solution/barista-day-1-03-planner   # inspect solution/.claude/skills/planner/SKILL.md
git checkout client/barista                      # zurück zur eigenen Arbeit
git show solution/barista-day-1-03-planner:clients/barista/exercises/day-1/03-planner/solution/.claude/skills/planner/SKILL.md
```
