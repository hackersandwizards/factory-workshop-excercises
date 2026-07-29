# Tag 2 — Termin offen, vor Ort Hamburg, Nils + Björn

**Format:** Vor Ort, ganztägig, zwei Trainer. Hackathon-Spirit — Ziel ist ein
echtes Artefakt, kein Übungs-Repo. Setzt Tag 1 voraus (Planner-Skill steht,
Roadmap + Pitfalls sind besprochen).

**Taktung:** dieselben 7 Blöcke wie Tag 1 (siehe `README.md`, Abschnitt
„Taktung"), 5–10 Minuten Pause je Block, 1h Mittag.

| Block | Zeit | Dauer | Inhalt |
|---|---|---|---|
| 1 | 09:00–09:55 | 55 min | Recap · Marketplace/Plugin — Hook + Mechanismus Teil 1 |
| — | 09:55–10:00 | 5 min | Pause |
| 2 | 10:00–10:50 | 50 min | Marketplace Teil 2 (Entwicklungstricks · Twist · Abschluss · Governance) · Factory-Erklärung Teil 1 |
| — | 10:50–11:00 | 10 min | Pause |
| 3 | 11:00–12:00 | 60 min | Factory-Erklärung Teil 2 (Capabilities vs. Commands) · Refine: Hook + Mechanismus + Twist + Abschluss |
| — | 12:00–13:00 | 60 min | Mittag |
| 4 | 13:00–13:55 | 55 min | Implement: Hook + Mechanismus + Twist |
| — | 13:55–14:00 | 5 min | Pause |
| 5 | 14:00–14:50 | 50 min | Implement: Abschluss · Orchestration/Review-Rework-Converge-Loop (Start) |
| — | 14:50–15:00 | 10 min | Pause |
| 6 | 15:00–15:55 | 55 min | Orchestration (Ende) · Transfer-Hackathon (Start) |
| — | 15:55–16:00 | 5 min | Pause |
| 7 | 16:00–17:00 | 60 min | Transfer-Hackathon (Ende) · Wrap-up |

**Ziel des Tages:** Starter Kit (Rules, Configs, Hooks, Skills, Repo zum
Weiterentwickeln) — gebaut **mit dem Team**, nichts Vorgefertigtes mitbringen.
Pipeline komplett: Planner (Tag 1) → Refine → Implement → Review-Loop, plus
Marketplace-/Plugin-Mechanik zur Verteilung der Konventionen, gleich zu
Beginn des Tages, damit das Team von Block 3 an alles, was es baut, direkt
im Paketierungs-Denken verortet.

---

## Block 1 · 09:00–09:55 · Recap · Marketplace/Plugin (Hook + Mechanismus Teil 1)

**Ablauf:**
- Recap (8): Planner/Roadmap/Pitfalls zusammenfassen, Tagesziel benennen
- Marketplace-Hook (5): Copy-Paste-Problem vorrechnen/zeigen
- Live-Install (15): `capability-vs-command-demo` installieren
- Kategorien im Dialog (27): Commands, Skills, Hooks, Subagents, MCP-Server, Settings-Defaults

**Recap (~8 min):** Planner-Skill, Roadmap, Pitfalls kurz zusammenfassen
(Brücke zurück, falls die Tage weit auseinander liegen). Tagesziel benennen:
heute entsteht das Starter Kit — und wir fangen diesmal mit der
Verteil-Mechanik an, nicht mit dem Bauen selbst.

**Marketplace, Hook (~5 min):** vorrechnen (oder live zeigen), wie oft
dieselbe Rule/derselbe Skill in den letzten Wochen händisch in verschiedene
Repos kopiert wurde — das Team kennt das Problem aus eigener Erfahrung.

**Marketplace, Mechanismus Teil 1 (~42 min):**

1. *Live-Demo:* das mitgebrachte Übungs-Plugin installieren
   (`capability-vs-command-demo` — Skill vs. Command am Beispiel Conventional
   Commits, in einem Marketplace registriert, echter Barista-Ausschnitt statt
   Spielzeug-Repo). Ein `/plugin install`, fertig — beide Bausteine sind
   sofort in einem zweiten Repo nutzbar.
2. *Erweitern, was sich sonst noch teilen lässt* — pro Kategorie ein
   Barista-nahes Beispiel, kein Frontalvortrag, im Dialog erfragen ("was
   davon habt ihr schon, nur nicht zentral?"):
   - **Commands:** Format-Standards, die exakt gleich aussehen sollen (Commit
     mit Ticket-Link, PR-Beschreibung).
   - **Skills:** Domänenwissen, das dort entsteht, wo es gebraucht wird —
     z. B. ein Observability-/Debugging-Skill vom Ops-Team, ein
     UI-Design-Skill von der Frontend-Lib. Wandert vom Team, das es hat, zum
     Team, das es braucht, statt in jedem Repo neu erfunden zu werden.
   - **Hooks:** nicht nur Git-Hook-Äquivalente (Lint/Format nach dem Commit).
     Harness-eigene Beispiele, die es ohne Agent so nicht gäbe: ein
     PreToolUse-Hook, der gefährliche Bash-Kommandos vor der Ausführung
     blockt; ein PostToolUse-Hook, der nach jedem Edit sofort die betroffenen
     Tests re-runnt; ein Stop-Hook, der beim "fertig"-Melden Acceptance
     Criteria re-checkt (Vorgriff auf Block 5/6 — dort bauen wir genau das).
   - **Subagents:** eine Rolle mit engem Werkzeugkasten, geteilt statt pro
     Repo neu definiert — z. B. ein Code-Reviewer-Agent, der lesen und
     testen, aber nicht schreiben darf.
   - **MCP-Server:** Zugriff auf interne Systeme, zentral betrieben statt pro
     Team eigene Tokens — z. B. Jira/Confluence-Anbindung für Ticket-Links.
   - **Settings-Defaults:** Permission-Listen, Modell-Routing über das
     LightLLM-Gateway — im Plugin mitgeliefert, damit niemand es von Hand
     einstellen muss.

*Bewusst nicht Thema dieses Blocks:* Marketplace-Publishing und
Distributions-Ökonomie, Vendor-Vergleich verschiedener Plugin-Ökosysteme.

## Pause · 09:55–10:00

## Block 2 · 10:00–10:50 · Marketplace Teil 2 · Factory-Erklärung Teil 1

**Ablauf:**
- Entwicklungstricks (15): lokaler Pfad, `--plugin-dir`, `install` → `reload-plugins`
- Twist (8): Pflegeaufwand konstant, aber lokal überschreibbar
- Abschluss (3): "Marketplace macht verfügbar, nicht verbindlich"
- Governance (4): Adopt per PR, Retire-Pfad
- Factory-Erklärung Teil 1 (20): Addi-Osmandi-Analogie, Pipeline-Überblick

**Marketplace, Entwicklungstricks (~15 min):** Plugins vom lokalen Pfad
installieren (`--plugin-dir`, `plugin marketplace add` → `install` →
`reload-plugins`) — direkt am eigenen Übungs-Plugin zeigen, wie man während
der Entwicklung iteriert, bevor etwas ins zentrale Marketplace-Repo geht.

**Marketplace, Twist (~8 min):** Erwartung wäre "mehr Repos heißt linear mehr
Pflegeaufwand". Erste Auflösung: mit einem Plugin bleibt der Pflegeaufwand
konstant — ein Update im Plugin, alle installierenden Repos ziehen nach.
Zweiter, unerwarteter Dreh direkt danach: geteilt heißt nicht erzwungen. Legt
ein Repo lokal eine gleichnamige Skill/einen gleichnamigen Subagent an,
überschreibt das lautlos die zentrale Version — kein Fehler, keine Warnung.
Genau das Not-invented-here-Muster, das heute schon in den Repos steckt,
funktioniert im Plugin-System also munter weiter, wenn niemand hinschaut.

**Marketplace, Abschluss (~3 min):** "Ein Marketplace macht Standards
verfügbar. Ob sie auch verbindlich sind, entscheidet jedes Repo für sich —
mit einer gleich benannten Datei."

**Governance kompakt, inkl. Adopt-or-Retire (~4 min):** Teams probieren lokal
in ihrem `.claude/` aus; was sich bewährt, wandert per PR ins zentrale
Marketplace-Repo und wird dort versioniert (`plugin.json`). Genauso wichtig
der Rückweg: ungenutzte oder veraltete Plugins brauchen einen klaren
Retire-Pfad — bei dieser heterogenen Repo-Landschaft mit vielen Teams kein
Nebenaspekt, sondern von Anfang an Teil der Governance.

*Vor dem Workshop noch zu tun:* das Demo-Plugin mit einem echten,
unkritischen Barista-Ausschnitt statt des Conventional-Commits-Spielzeugs
nachbauen — Wirkung ist größer, wenn das Team sein eigenes Repo im Beispiel
wiedererkennt.

**High-Level Factory-Erklärung, Teil 1 (~20 min):** Zoom raus — was wir
gerade in klein gebaut haben (ein Plugin, das Konventionen verteilt), ist
das Rückgrat einer ganzen Factory. Hohes Niveau, keine Folienschlacht:
Ticket rein, Lösung raus, aber phasiert (Analogie zum letzten
Addi-Osmandi-Post — Vortragender bringt eigene Zusammenfassung mit, kein
wörtliches Zitat). Pipeline im Überblick: Planner (Tag 1, das "Was") → Refine
(das "Wie" konkretisieren) → Implement (Branch/Code) → Review-Rework-
Converge-Loop (Qualitätssicherung ohne Menschen im Loop) → Marketplace
(Verteilung dessen, was sich bewährt hat, an alle anderen Repos). Rahmen für
den Rest des Tages: "Wir bauen jetzt Stück für Stück genau diese Teile."

## Pause · 10:50–11:00

## Block 3 · 11:00–12:00 · Factory-Erklärung Teil 2 · Refine

**Ablauf:**
- Capability/Command-Rückblick (8): Trigger-Design, Commit-Beispiel → Repo, Planner-Beispiel → Team
- Refine-Hook (10): Bean ohne Refine → falscher Pfad
- Refine-Mechanismus (25): Subagent-Fork, Trainer führt vor, Team macht Self-Check
- Refine-Twist (10): read-only + Verifikation schlägt Freiheit
- Refine-Abschluss (5): "wenigsten darf, meisten glauben"

**Factory-Erklärung Teil 2 — Capabilities vs. Commands, Rückblick (~8 min):**
Kurzer Rückgriff auf Tag 1, Block 2: der Commit-Skill ist eine Capability
(Intent-getriggert, kein bewusster Aufruf — sobald die Arbeit fertig ist und
committed werden soll, springt er an), der Planner ein Command (bewusst per
`/planner` aufgerufen). Der Unterschied ist keine Frage von "was darf geteilt
werden" — beide lassen sich, wie eben in Block 1–2 gezeigt, gleich gut als
Plugin verpacken und verteilen. Er ist eine Frage des Trigger-Designs: wie
zuverlässig lässt sich der richtige Moment automatisch erkennen (→
Capability), und wo braucht es stattdessen einen bewussten, expliziten
Anstoß, weil sich der richtige Moment nicht zuverlässig automatisch
erkennen lässt und der Prozess bewussten Dialog braucht (→ Command)? Für die
Factory heißt das: bei jedem neuen Baustein, den ihr paketiert, bewusst
diese Frage stellen, statt Command per Default zu bauen, weil es der
einfachere Reflex ist.

Abschluss-Satz: "Eine Capability muss den richtigen Moment selbst erkennen.
Bei einem Command sagst du ihr, wann sie dran ist."

**Refine, Hook (~10 min):** den Bean aus Tag 1 direkt an Implement übergeben,
ohne Refine dazwischen. Der Agent muss raten, welche Datei gemeint ist, nennt
vermutlich einen Pfad, der nicht existiert oder nicht passt.

**Refine, Mechanismus, verdichtet (~25 min):** aus `day-2-pm/02-refine`: Bean
mit High-Level-Plan → Subagent-Fork erkundet die Codebase (read-only, Schritt
für Schritt) → strukturierte Rückgabe (Files/Functions/Integration
points/Test-Patterns) → konkreter `## Refined Plan` zurück in den Bean.
Trainer führt den Subagent-Fork-Durchlauf einmal live am eigenen Beispiel
vor, statt dass jede:r ihn komplett selbst nachbaut — das Team übernimmt nur
den Selbstcheck jedes Pfads via Glob/Grep hands-on. Gegen einen echten
Barista-Repo-Ausschnitt (das Team bringt dafür ein passendes, nicht zu
sensibles Repo/Modul mit, in Tag 1 klären).

**Refine, Twist (~10 min):** Erwartung wäre "mehr Freiheit für den Subagent
bringt bessere Ergebnisse". Auflösung: das Gegenteil — read-only plus
erzwungene Verifikation schlägt freie Exploration, weil Halluzinationen
technisch ausgeschlossen werden, statt auf Vertrauen zu beruhen.

**Refine, Abschluss (~5 min):** "Der Subagent, der am wenigsten darf, ist der,
dem man am meisten glauben kann."

## Mittag · 12:00–13:00

## Block 4 · 13:00–13:55 · Implement (Hook + Mechanismus, verdichtet) + Twist

**Ablauf:**
- Implement-Hook (10): kompletter Plan in einem Rutsch → kaputter Zwischenstand
- Implement-Mechanismus (35): 2er-Teams, max. 2 Commit-Zyklen, Hard rules (nie main, nie push/merge, Tests grün)
- Implement-Twist (10): kleine Commits langsamer pro Schritt, schneller am Ziel

**Implement, Hook (~10 min):** den Agenten den gesamten Refined Plan in einem
Rutsch umsetzen lassen, ohne Zwischenschritte — in der sicheren Sandbox zeigt
sich schnell ein kaputter Zwischenstand, den niemand mehr sauber zurückrollen
kann.

**Implement, Mechanismus, verdichtet (~35 min):** aus `day-2-pm/03-implement`:
Branch anlegen, editieren/bauen/testen/committen. In 2er-Teams statt jede:r
für sich, harter Zeitbox-Cutoff nach zwei Commit-Zyklen statt offen weiter
(zusätzlich zum bisherigen harten Abbruch nach zwei Fehlversuchen).
Implementation Log in den Bean. Hard rules: nie auf main committen, nie
pushen, nie mergen, Tests müssen grün sein vor jedem Commit.

**Implement, Twist (~10 min):** Erwartung wäre "kleine Commits sind langsamer
als einmal durchzuprogrammieren". Auflösung: die kleinen Schritte plus
2-Versuch-Abbruch verhindern genau die stundenlangen Aufräum-Sessions, die
der Hook in diesem Block live gezeigt hat — langsamer pro Schritt, aber
insgesamt schneller am Ziel.

## Pause · 13:55–14:00

## Block 5 · 14:00–14:50 · Implement (Abschluss) · Orchestration (Start)

**Ablauf:**
- Implement-Abschluss (5): "zehn kleine Commits, einer revertierbar"
- Orchestration-Rahmung (5): Rollenwandel, Card `harness-engineering-outlook`
- Orchestration-Hook (10): grün getestet, Acceptance-Criterion verfehlt
- Orchestration-Mechanismus Start (30): Review-Skill/Subagent bauen

**Implement, Abschluss (~5 min):** "Zehn kleine Commits sind langweiliger als
einer, aber nur einer davon lässt sich um 2 Uhr nachts noch guten Gewissens
reverten."

**Orchestration / Review-Rework-Converge-Loop, Start (~45 min):**

Fehlt im Original-Repo komplett (dort ist die Pipeline linear, ohne
Rücksprung). Für Barista relevant wegen heterogener Standards + Agency-Code-
Altlasten: nach Implement einen Review-Schritt einziehen (automatisiert oder
Subagent-basiert), der bei Bedarf **zurück zu Refine** schickt statt stur
weiterzulaufen.

**Rahmung zum Einstieg** (Card `harness-engineering-outlook` aus der
Trainer-Base): der Rollenwandel geht über Tag 1 hinaus weiter — von der
Prüfung einzelner Outputs hin zum Entwerfen von Verifikations-Loops für
autonom laufende Arbeit. Mehr Orchestrierung, weniger Eingreifen im Detail.
Genau das bauen wir hier gerade — guter Ein-Satz-Aufhänger vor dem Hook.

**Hook:** einen Implement-Lauf zeigen, der grün testet, aber ein
Acceptance-Criterion aus dem High-Level-Plan trotzdem verfehlt (bewusst
präpariertes Beispiel). Die Gruppe merkt: "fertig" laut Tests ≠ "fertig" laut
Auftrag.

**Mechanismus, Start:** Review-Skill/Subagent bauen, der Implementation-Log +
Diff gegen die Acceptance Criteria prüft, nicht nur gegen den Testlauf.
Fortsetzung in Block 6.

*Baustein muss vor dem Workshop noch gebaut werden (kein Original-Vorbild) —
Aufwand realistisch einplanen, nicht erst am Vorabend von Tag 2.*

## Pause · 14:50–15:00

## Block 6 · 15:00–15:55 · Orchestration (Ende) · Transfer-Hackathon (Start)

**Ablauf:**
- Orchestration-Mechanismus Ende (5): zurück zu Refine oder `completed`
- Orchestration-Twist (3): grün ≠ fertig
- Orchestration-Abschluss (2): "niemand hat's bisher gemerkt"
- Hackathon Start (45): komplette Pipeline auf echte Barista-Aufgabe

**Mechanismus, Ende (~5 min):** bei Abweichung zurück zu Refine
(Converge-Schritt), sonst `completed`.

**Twist (~3 min):** Erwartung wäre "grüne Tests heißen fertig". Auflösung:
Tests prüfen nur, was jemand vorher zu testen für nötig hielt — nicht, was
eigentlich verlangt war. Der AC-Check schließt genau diese Lücke.

**Abschluss (~2 min):** "Grün heißt nicht fertig, grün heißt nur: niemand hat
bisher gemerkt, dass es nicht fertig ist."

*Bewusst nicht Thema dieses Blocks:* Prompt-Engineering-Tipps und
Formulierungstricks, vollständige Spec-Driven-Development-Methodik (siehe
Glossar-Eintrag SDD — das ist ein größeres Fass), Messung individueller
Entwickler-Produktivität. Der Loop ist die Einheit, nicht der einzelne Prompt
oder die einzelne Person.

**Transfer-Hackathon, Start (~45 min):** Team wendet die komplette Pipeline
(Planner → Refine → Implement → Review-Loop) auf eine echte, kleine
Barista-Aufgabe an. Fortsetzung in Block 7.

## Pause · 15:55–16:00

## Block 7 · 16:00–17:00 · Transfer-Hackathon (Ende) · Wrap-up

**Ablauf:**
- Hackathon Ende (45): Starter-Kit-Artefakt fertigstellen
- Wrap-up (15): Ergebnis-Review, Übergang Mentoring-Phase

**Transfer-Hackathon, Ende (~45 min):** Ergebnis: erstes Starter-Kit-Artefakt
im eigenen Repo — Rules, Configs, Hooks, Skills, alles was heute entstanden
ist, geht mit ins Team-Repo.

**Wrap-up (~15 min):** Ergebnis-Review, was hat funktioniert / was hakt noch,
Übergang in die Mentoring-Phase (punktuell, pull-basiert).
