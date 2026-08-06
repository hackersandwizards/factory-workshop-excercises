# Tag 1 · Exercise 03 — Planner-Skill mit Bean-Anbindung

**Slot:** Block 3, 11:00–12:00 · 60 Minuten (Hands-on)

## Goal

Einen eigenen Planner-Skill bauen, der bei `/planner` **direkt einen Bean
anlegt** (`beans create`) statt in eine `.md`-Datei zu planen — das "Was"
der Pipeline, ohne Pfade oder Signaturen.

## Herkunft

Kombiniert aus `day-2-am/01-planning-skill` (4★-Subset: Explore / One
question per message / Alternatives / Self-Review) und
`day-2-pm/01-planner-rework` (Bean-Creator statt `.plans/`-Datei) — im
Original zwei getrennte Übungen an verschiedenen Tagen, hier **in einem
Schritt**. Spart einen Umbauschritt, bringt sofort den echten
Pipeline-Baustein.

## Vorbereitung

Die `beans`-CLI muss installiert sein (`brew install hmans/beans/beans`,
prüfen: `beans --version`). Kopiere `exercise/.claude` und
`exercise/.beans.yml` in ein Verzeichnis deiner Wahl — am besten ein
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
4. Bean-Erzeugung statt Datei-Plan: **ein** CLI-Aufruf mit vollständigem
   Body — `beans create "<Titel>" -t feature -d "<Heredoc mit Description +
   ## High-Level Plan>"`. Die `beans`-CLI hat **kein** `--body-append` — bei
   langen Bodies `--body-file <pfad>` statt `-d` nutzen. ID aus stdout
   parsen für die Übergabe an `/refine` (Tag 2).
5. Heading-Vertrag: der Plan steht wortwörtlich unter der Überschrift
   `## High-Level Plan` — `/refine` an Tag 2 parst per Exact-Match, fehlt
   die Überschrift, bricht Refine ab.
6. Harte Regel: **keine** Dateipfade, **keine** Funktionssignaturen,
   **keine** Klassennamen im Plan — stattdessen Acceptance Criteria.
7. **Neu, bewusste Design-Entscheidung:** `disable-model-invocation: true`
   ins Frontmatter setzen. Zwei Gründe: der Hook oben bleibt sauber (Claude
   kann nicht selbst entscheiden, "vorsichtshalber" zu planen und den
   Kontrollverlust im Hook abzuschwächen), und das Anlegen eines Beans ist
   ein Seiteneffekt — genau der Fall, für den explizite statt automatische
   Auslösung empfohlen wird. Passt außerdem zum
   Human-in-the-loop-Grundton des Workshops.
8. Test: `/planner <eigene Aufgabe>` → `beans list` zeigt einen neuen Bean,
   `beans show <id>` zeigt Description + `## High-Level Plan` mit
   Approach/Steps/AC/Non-Goals.

## Verify

- `beans list` enthält nach dem `/planner`-Lauf einen neuen Bean
- Der Plan enthält keine Dateipfade, keine Funktionsnamen, keine
  Zeilenverweise
- Der Skill fragt eine Frage nach der anderen, nicht alle auf einmal
- Der Skill triggert **nicht** von selbst — nur auf expliziten
  `/planner`-Aufruf (Test: eine komplexe Aufgabe beiläufig erwähnen, ohne
  `/planner` zu tippen — nichts sollte passieren)
- Der Skill scheitert kontrolliert, wenn die `beans`-CLI fehlt

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

Der neue Bean (genauer: seine ID) ist die Übergabe an `/refine
<bean-id>` — Pfade und Signaturen kommen dort dazu, nicht hier.

## Solution

Referenzlösung liegt auf Branch **`solution/barista-day-1-03-planner`**
(bewusst nicht auf `client/barista`, damit sie nicht in Claudes Kontext
landet) — `solution/.claude/skills/planner/SKILL.md` mit vollem
4★-Subset + Bean-Creator + `disable-model-invocation: true`. Erst selbst
bauen, dann vergleichen:

```bash
git checkout solution/barista-day-1-03-planner   # inspect solution/.claude/skills/planner/SKILL.md
git checkout client/barista                      # zurück zur eigenen Arbeit
git show solution/barista-day-1-03-planner:clients/barista/exercises/day-1/03-planner/solution/.claude/skills/planner/SKILL.md
```
