# Tag 2 — Termin offen, vor Ort Hamburg, Nils + Björn

**Format:** Vor Ort, ganztägig, zwei Trainer. Hackathon-Spirit — Ziel ist ein
echtes Artefakt, kein Übungs-Repo. Setzt Tag 1 voraus (Planner-Skill steht,
Roadmap + Pitfalls sind besprochen).

**Taktung:** dieselben 7 Blöcke wie Tag 1 (siehe `README.md`, Abschnitt
„Taktung"), 5–10 Minuten Pause je Block, 1h Mittag.

| Block | Zeit | Dauer | Inhalt |
|---|---|---|---|
| 1 | 09:00–09:55 | 55 min | Recap + Tagesziel · Refine: Hook + Mechanismus |
| — | 09:55–10:00 | 5 min | Pause |
| 2 | 10:00–10:50 | 50 min | Refine: Twist + Abschluss · Implement: Hook + Mechanismus (Start) |
| — | 10:50–11:00 | 10 min | Pause |
| 3 | 11:00–12:00 | 60 min | Implement: Mechanismus (Fortsetzung) + Twist + Abschluss |
| — | 12:00–13:00 | 60 min | Mittag |
| 4 | 13:00–13:55 | 55 min | NEU: Orchestration / Review-Rework-Converge-Loop |
| — | 13:55–14:00 | 5 min | Pause |
| 5 | 14:00–14:50 | 50 min | NEU: Marketplace-/Plugin-Mechanik: Hook + Mechanismus |
| — | 14:50–15:00 | 10 min | Pause |
| 6 | 15:00–15:55 | 55 min | Marketplace/Plugin: Twist + Abschluss · Transfer-Hackathon (Start) |
| — | 15:55–16:00 | 5 min | Pause |
| 7 | 16:00–17:00 | 60 min | Transfer-Hackathon (Ende) · Wrap-up |

**Ziel des Tages:** Starter Kit (Rules, Configs, Hooks, Skills, Repo zum
Weiterentwickeln) — gebaut **mit dem Team**, nichts Vorgefertigtes mitbringen.
Pipeline komplett: Planner (Tag 1) → Refine → Implement → Review-Loop, plus
Marketplace-/Plugin-Mechanik zur Verteilung der Konventionen.

**Herkunft:** aus `day-2-pm/` (Refine, Implement) + zwei neuen Bausteinen, die
im Original-Repo fehlen (Orchestration/Review-Rework-Converge, Marketplace/
Plugin) + `day-3` (Transfer-Hackathon-Idee: eigene Codebase statt Sandbox) —
hier aber gegen einen echten Barista-Repo-Ausschnitt statt des Calc-Sandkastens.

**Stand Vorbereitung:** Nils hat den Marketplace-/Plugin-Mechanismus
mittlerweile selbst durchgespielt (Demo-Plugin `capability-vs-command-demo`
inkl. Marketplace, lokal getestet über `--plugin-dir` und
`plugin marketplace add` → `install` → `reload-plugins`). Offen: das
Demo-Plugin noch mit einem echten Barista-Beispiel statt Spielzeug-Repo
nachbauen, bevor es im Block eingesetzt wird.

---

## Block 1 · 09:00–09:55 · Recap + Tagesziel · Refine (Hook + Mechanismus)

**Recap + Tagesziel (~15 min):** Planner-Skill, Roadmap, Pitfalls kurz
zusammenfassen (Brücke zurück, falls die Tage weit auseinander liegen).
Tagesziel klar benennen: heute entsteht das Starter Kit.

**Refine, Hook (~10 min):** den Bean aus Tag 1 direkt an Implement übergeben,
ohne Refine dazwischen. Der Agent muss raten, welche Datei gemeint ist, nennt
vermutlich einen Pfad, der nicht existiert oder nicht passt.

**Refine, Mechanismus (~30 min):** aus `day-2-pm/02-refine`: Bean mit
High-Level-Plan → Subagent-Fork erkundet die Codebase (read-only, Schritt für
Schritt aufgebaut) → strukturierte Rückgabe (Files/Functions/Integration
points/Test-Patterns) → Selbstcheck jedes Pfads via Glob/Grep → konkreter
`## Refined Plan` zurück in den Bean. **Gegen einen echten Barista-Repo-
Ausschnitt**, nicht den Calc-Sandkasten — das Team bringt dafür ein passendes,
nicht zu sensibles Repo/Modul mit (in Tag 1 klären).

## Pause · 09:55–10:00

## Block 2 · 10:00–10:50 · Refine (Twist + Abschluss) · Implement (Start)

**Refine, Twist (~10 min):** Erwartung wäre "mehr Freiheit für den Subagent
bringt bessere Ergebnisse". Auflösung: das Gegenteil — read-only plus
erzwungene Verifikation schlägt freie Exploration, weil Halluzinationen
technisch ausgeschlossen werden, statt auf Vertrauen zu beruhen.

**Refine, Abschluss (~5 min):** "Der Subagent, der am wenigsten darf, ist der,
dem man am meisten glauben kann."

**Implement, Hook (~10 min):** den Agenten den gesamten Refined Plan in einem
Rutsch umsetzen lassen, ohne Zwischenschritte — in der sicheren Sandbox zeigt
sich schnell ein kaputter Zwischenstand, den niemand mehr sauber zurückrollen
kann.

**Implement, Mechanismus, Start (~25 min):** aus `day-2-pm/03-implement`:
Branch anlegen, ersten Schritt editieren/bauen/testen/committen. Fortsetzung
in Block 3.

## Pause · 10:50–11:00

## Block 3 · 11:00–12:00 · Implement (Fortsetzung, Twist, Abschluss)

**Mechanismus, Fortsetzung (~35 min):** weitere Schritte editieren/bauen/
testen/committen, harter Abbruch nach zwei Fehlversuchen. Implementation Log
in den Bean. Hard rules: nie auf main committen, nie pushen, nie mergen, Tests
müssen grün sein vor jedem Commit.

**Twist (~15 min):** Erwartung wäre "kleine Commits sind langsamer als einmal
durchzuprogrammieren". Auflösung: die kleinen Schritte plus 2-Versuch-Abbruch
verhindern genau die stundenlangen Aufräum-Sessions, die der Hook in Block 2
live gezeigt hat — langsamer pro Schritt, aber insgesamt schneller am Ziel.

**Abschluss (~10 min):** "Zehn kleine Commits sind langweiliger als einer,
aber nur einer davon lässt sich um 2 Uhr nachts noch guten Gewissens
reverten."

## Mittag · 12:00–13:00

## Block 4 · 13:00–13:55 · NEU: Orchestration / Review-Rework-Converge-Loop

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

**Mechanismus:** Review-Skill/Subagent bauen, der Implementation-Log + Diff
gegen die Acceptance Criteria prüft, nicht nur gegen den Testlauf. Bei
Abweichung zurück zu Refine (Converge-Schritt), sonst `completed`.

**Twist:** Erwartung wäre "grüne Tests heißen fertig". Auflösung: Tests prüfen
nur, was jemand vorher zu testen für nötig hielt — nicht, was eigentlich
verlangt war. Der AC-Check schließt genau diese Lücke.

**Abschluss:** "Grün heißt nicht fertig, grün heißt nur: niemand hat bisher
gemerkt, dass es nicht fertig ist."

*Baustein muss vor dem Workshop noch gebaut werden (kein Original-Vorbild) —
Aufwand realistisch einplanen, nicht erst am Vorabend von Tag 2.*

**Bewusst nicht Thema dieses Blocks:** Prompt-Engineering-Tipps und
Formulierungstricks, vollständige Spec-Driven-Development-Methodik (siehe
Glossar-Eintrag SDD — das ist ein größeres Fass), Messung individueller
Entwickler-Produktivität. Der Loop ist die Einheit, nicht der einzelne Prompt
oder die einzelne Person.

## Pause · 13:55–14:00

## Block 5 · 14:00–14:50 · NEU: Marketplace-/Plugin-Mechanik (Hook + Mechanismus)

Ebenfalls fehlt im Original (nur `/skill-creator`-Stretch-Erwähnung). Ziel:
Konventionen (Skills/Rules/Hooks aus Tag 1 + heute) als **Plugin** verpacken,
damit sie sich über die heterogene Repo-Landschaft verteilen lassen, statt in
jedem Repo neu erfunden zu werden — direkt an Björns Slack-Einschätzung
("früh relevant, Exercises darum aufbauen") orientiert.

**Hook:** vorrechnen (oder live zeigen), wie oft dieselbe Rule/derselbe Skill
in den letzten Wochen händisch in verschiedene Repos kopiert wurde — das Team
kennt das Problem aus eigener Erfahrung.

**Mechanismus (~35 min):**

1. *Live-Demo:* das mitgebrachte Übungs-Plugin installieren
   (`capability-vs-command-demo` — Skill vs. Command am Beispiel Conventional
   Commits, in einem Marketplace registriert). Ein `/plugin install`, fertig
   — beide Bausteine sind sofort in einem zweiten Repo nutzbar.
2. *Erweitern, was sich sonst noch teilen lässt* — pro Kategorie ein
   Barista-naher Beispiel, kein Frontalvortrag, im Dialog erfragen ("was
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
     blockt (nicht danach, wie ein Git-Hook); ein PostToolUse-Hook, der nach
     jedem Edit sofort die betroffenen Tests re-runnt — Sekunden-Feedback
     statt CI-Minuten; ein Stop-Hook, der beim "fertig"-Melden die Acceptance
     Criteria aus Block 4 re-checkt, bevor der Agent wirklich aufhören darf.
   - **Subagents:** eine Rolle mit engem Werkzeugkasten, geteilt statt pro
     Repo neu definiert — z. B. ein Code-Reviewer-Agent, der lesen und
     testen, aber nicht schreiben darf.
   - **MCP-Server:** Zugriff auf interne Systeme, zentral betrieben statt pro
     Team eigene Tokens — z. B. Jira/Confluence-Anbindung für Ticket-Links.
   - **Settings-Defaults:** Permission-Listen, Modell-Routing über das
     LightLLM-Gateway — im Plugin mitgeliefert, damit niemand es von Hand
     einstellen muss.
3. *Governance kompakt, inklusive Adopt-or-Retire:* Teams probieren lokal
   in ihrem `.claude/` aus; was sich bewährt, wandert per PR ins zentrale
   Marketplace-Repo und wird dort versioniert (`plugin.json`), nicht in
   jedem Repo einzeln gepflegt. Genauso wichtig der Rückweg: ungenutzte
   oder veraltete Plugins brauchen einen klaren Retire-Pfad, sonst wächst
   das Marketplace-Repo nur in eine Richtung — bei dieser heterogenen Repo-Landschaft
   mit vielen Teams kein Nebenaspekt, sondern von Anfang an Teil der
   Governance.

*Vor dem Workshop noch zu tun:* das Demo-Plugin mit einem echten,
unkritischen Barista-Ausschnitt statt des Conventional-Commits-Spielzeugs
nachbauen (siehe Hinweis oben) — Wirkung ist größer, wenn das Team sein
eigenes Repo im Beispiel wiedererkennt.

**Bewusst nicht Thema dieses Blocks:** Marketplace-Publishing und
Distributions-Ökonomie, Vendor-Vergleich verschiedener Plugin-Ökosysteme, ein
produktionsreifes internes Plugin im Workshop selbst fertigbauen. Es geht um
das Prinzip (Bündeln + Verteilen), nicht um ein Referenz-Plugin für den
Ernstfall.

## Pause · 14:50–15:00

## Block 6 · 15:00–15:55 · Marketplace/Plugin (Twist + Abschluss) · Transfer-Hackathon (Start)

**Twist (~10 min):** Erwartung wäre "mehr Repos heißt linear mehr
Pflegeaufwand". Erste Auflösung: mit einem Plugin bleibt der Pflegeaufwand
konstant — ein Update im Plugin, alle installierenden Repos ziehen nach.
Zweiter, unerwarteter Dreh direkt danach: geteilt heißt nicht erzwungen.
Legt ein Repo lokal eine gleichnamige Skill/einen gleichnamigen Subagent an
(z. B. einen eigenen `code-reviewer`), überschreibt das lautlos die
zentrale Version — kein Fehler, keine Warnung. Genau das Not-invented-here-
Muster, das heute schon in den Repos steckt, funktioniert im Plugin-System
also munter weiter, wenn niemand hinschaut.

**Abschluss (~5 min):** "Ein Marketplace macht Standards verfügbar. Ob sie
auch verbindlich sind, entscheidet jedes Repo für sich — mit einer gleich
benannten Datei."

**Transfer-Hackathon, Start (~45 min):** Team wendet die komplette Pipeline
(Planner → Refine → Implement → Review-Loop) auf eine echte, kleine
Barista-Aufgabe an. Fortsetzung in Block 7.

## Pause · 15:55–16:00

## Block 7 · 16:00–17:00 · Transfer-Hackathon (Ende) · Wrap-up

**Transfer-Hackathon, Ende (~45 min):** Ergebnis: erstes Starter-Kit-Artefakt
im eigenen Repo — Rules, Configs, Hooks, Skills, alles was heute entstanden
ist, geht mit ins Team-Repo.

**Wrap-up (~15 min):** Ergebnis-Review, was hat funktioniert / was hakt noch,
Übergang in die Mentoring-Phase (punktuell, pull-basiert).
