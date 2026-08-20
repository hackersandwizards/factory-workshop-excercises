# Tag 2 — 21.08.2026, remote, Nils solo (Kamil ab 15:00)

**Format:** Remote, ganztägig, 9:00–17:00. Nils solo bis 15:00, danach kommt
Kamil dazu (Block 6–7) — er hat Evals für seine eigene Factory bereits gebaut
und bringt das aus erster Hand mit. Björn ist diesmal nicht dabei.
Hackathon-Spirit — Ziel ist ein echtes Artefakt, kein Übungs-Repo. Setzt
Tag 1 voraus (Planner-Skill steht, Roadmap + Pitfalls sind besprochen).

**Wichtige Korrektur vor dem Tag (Call vom 18.08.):** das Team hat sich
selbst einen MCP-Server als Marketplace-Ersatz gebaut — in der Annahme, ein
Plugin-Marketplace biete kein Auto-Update. Das stimmt nicht. Block 2 ist
deshalb keine leichte Demo mehr, sondern eine volle Session: Marketplace
vollständig zeigen, live beweisen, dass Auto-Update funktioniert, und die
MCP-Lösung sauber einordnen (löst ein anderes Problem: Zugriff, nicht
Verhalten-Verteilung).

**Taktung:** dieselben 7 Blöcke wie Tag 1 (siehe `README.md`, Abschnitt
„Taktung"), 5–10 Minuten Pause je Block, 1h Mittag.

| Block | Zeit | Dauer | Inhalt |
|---|---|---|---|
| 1 | 09:00–09:55 | 55 min | Tagesziel · Recap Tag 1 · Show & Tell · Planner-Hints (aus dem Show & Tell) |
| — | 09:55–10:00 | 5 min | Pause |
| 2 | 10:00–10:50 | 50 min | Marketplace — vollständig: Setup, Auto-Update-Beweis, Governance, Edge Cases |
| — | 10:50–11:00 | 10 min | Pause |
| 3 | 11:00–12:00 | 60 min | Anatomy of the Agentic Factory (Addi-Osmandi) · Review-Loop-Tiefe · Trade-off: Dark Factory |
| — | 12:00–13:00 | 60 min | Mittag |
| 4 | 13:00–13:55 | 55 min | Hackathon-Start: Hard Rules · Paare · Hints je Skill (Refiner/Implementer/Reviewer) |
| — | 13:55–14:00 | 5 min | Pause |
| 5 | 14:00–14:50 | 50 min | Fertigbauen · Ticket + Planner · Marketplace-Merge (Versuch) · Orchestrator · Testlauf bis zum Light-Switch |
| — | 14:50–15:00 | 10 min | Pause |
| 6 | 15:00–15:55 | 55 min | Wie man Evals baut (Kamil, aus seiner eigenen Factory) |
| — | 15:55–16:00 | 5 min | Pause |
| 7 | 16:00–17:00 | 60 min | Recap · Marketplace-Merge nachholen (falls nötig) · Q&A · Mentoring-Angebot · Wrap-up |

**Ziel des Tages:** ein echtes Starter Kit — eine erste lokal lauffähige
Factory (Refiner, Implementer, Reviewer entstehen heute — Planner steht seit
Tag 1), gebaut **mit dem Team**, gegen echte, unkritische Repo-Ausschnitte,
und am Ende des Tages gemeinsam live in eine Marketplace-Repo einsortiert
(Block 7), damit sie ab morgen von jedem Repo im Team installierbar ist —
nicht nur ein loses Bündel Skill-Dateien. Kein Copy-Paste-Marketplace mehr
als Rätsel, sondern korrekt verstanden und eingeordnet. Anders als in der
ursprünglichen Fassung ist das Ergebnis nicht zwingend vier komplett fertige
Skills — Hackathon-Spirit heißt: offen im Ergebnis, nicht in der Zeit. Was
am Ende des Tages steht, steht; der Rest ist Mentoring-Phase.

---

## Block 1 · 09:00–09:55 · Tagesziel · Recap · Show & Tell · Planner-Hints

**Ablauf:**
- Tagesziel (5): Pipeline zu Ende bauen (Refiner/Implementer/Reviewer), Tag endet mit lokaler Mini-Factory
- Recap (10): Planner/Roadmap/Pitfalls aus Tag 1 zusammenfassen
- Show & Tell (25): Team zeigt Planner-Stand + die eigene MCP-Marketplace-Lösung
- Planner-Hints (15): live aus dem, was im Show & Tell auffällt, statt vorgefertigt

**Tagesziel (~5 min):** heute wird die Pipeline zu Ende gebaut — Refine,
Implement, Review fehlen noch. Ergebnis ist eine erste lokal lauffähige
Mini-Factory, kein individuelles Starter-Kit pro Person.

**Recap (~10 min):** Planner-Skill, Roadmap, Pitfalls aus Tag 1 kurz
zurückspiegeln — Brücke, falls der Abstand zwischen den Tagen die Erinnerung
hat verblassen lassen.

**Show & Tell (~25 min):** das Team zeigt selbst, statt vorgeführt zu
bekommen — zwei Dinge: (1) der Planner-Stand, live gegen eine echte Aufgabe;
(2) die eigene MCP-Server-Lösung fürs Marketplace-/Copy-Paste-Problem.
Trainer moderiert, fragt nach ("wie löst das den Copy-Paste-Fall?", "was war
der Grund, selbst etwas zu bauen statt den Marketplace zu nehmen?") — genau
hier kommt die Auto-Update-Annahme auf den Tisch, ohne dass der Trainer sie
vorwegnehmen muss. Das ist die Steilvorlage für Block 2.

Im Prep-Call hat bereits jemand aus dem Team angekündigt, den eigenen
MCP-Server auf einen echten Marketplace umstellen zu wollen — das dürfte
hier von selbst zur Sprache kommen. Nebenbei einordnen: diese Person ist
damit der naheliegende Kandidat für den Marketplace-Merge in Block 7 —
nicht laut ankündigen, nur im Kopf behalten, in Block 4 wird das explizit
bestätigt.

**Planner-Hints (~15 min):** bewusst **nicht** aus einer mitgebrachten
Exercise-Kopie, sondern direkt aus dem, was im Show & Tell sichtbar wurde —
wo hakt der Planner-Stand des Teams gerade (Fragen-Disziplin? Alternativen
vor Konvergenz? Self-Review?). Rückgriff auf `exercises/day-1/05-planner/`
nur als Hintergrundmaterial für den Trainer, falls konkrete Nachbesserungen
nötig sind, nicht als auszuteilende Kopie.

## Pause · 09:55–10:00

## Block 2 · 10:00–10:50 · Marketplace — vollständig

**Ablauf:**
- Hook (5): die Annahme aus dem Show & Tell direkt aufgreifen — warum das Team dachte, es gäbe kein Auto-Update
- Live-Beweis (15): deterministischer Update-Ablauf, kein Warten auf den Hintergrund-Timer
- Kategorien + Entwicklungstricks (15): was sich über Skills/Refine/Review hinaus teilen lässt, `--plugin-dir`-Workflow
- Governance + Edge Cases (10): Adopt per PR, Retire-Pfad, echte Edge Cases mit Namen
- Twist + Abschluss (5): geteilt heißt nicht erzwungen — MCP-Lösung sauber einordnen

**Hook (~5 min):** die Annahme, die eben im Show & Tell aufkam, offen
benennen — und gleich mitliefern, warum sie entstanden ist, statt sie nur zu
widerlegen: Auto-Update ist bei offiziellen Anthropic-Marketplaces
**standardmäßig an**, bei Marketplaces von Dritten oder selbstgebauten/
lokalen Marketplaces **standardmäßig aus** (Toggle unter `/plugin` →
Marketplaces → "Enable auto-update"). Wer mit einem eigenen/lokalen
Marketplace experimentiert und den Toggle nie gesetzt hat, sieht nie ein
Auto-Update — und schließt daraus "das Feature gibt's nicht", statt "der
Default steht bei mir auf aus". Genau das ist vermutlich beim Team passiert.

**Live-Beweis, Auto-Update (~15 min):** nicht auf den automatischen
Hintergrund-Check warten (bis zu 10 Min. Zufalls-Delay, ungeeignet für einen
15-Minuten-Block) — stattdessen den deterministischen, manuellen Pfad
zeigen, der jederzeit sofort funktioniert, unabhängig vom Auto-Update-Toggle:
`/plugin marketplace add <repo>` → `/plugin install <name>@<marketplace>` →
Änderung im Marketplace-Repo committen → `/plugin marketplace update
<marketplace-name>` (erzwingt sofortigen Refresh) → `/reload-plugins`
(wendet die Änderung an, kein Neustart nötig). Übungs-Skeleton:
`exercises/day-2/01-marketplace/`. Der Punkt, an dem die alte Annahme
fällt, muss die Gruppe selbst sehen, nicht nur hören.

**Kategorien + Entwicklungstricks (~15 min):** kurzer Durchgang, was sich
über die reine Marketplace-Frage hinaus teilen lässt — Commands
(Format-Standards), Skills (Domänenwissen, z. B. ein Observability-Skill vom
Ops-Team), Hooks (PreToolUse-Block, PostToolUse-Test-Rerun), Subagents
(Code-Reviewer-Rolle mit engem Werkzeugkasten), Settings-Defaults
(Permission-Listen, Modell-Routing). Dazu, wie man während der Entwicklung
iteriert, bevor etwas ins zentrale Repo geht: lokaler Pfad, `--plugin-dir`,
`install` → `reload-plugins`.

**Governance + Edge Cases (~10 min):** Teams probieren lokal in ihrem
`.claude/` aus; was sich bewährt, wandert per PR ins zentrale
Marketplace-Repo und wird versioniert. Rückweg genauso wichtig: ungenutzte
oder veraltete Plugins brauchen einen Retire-Pfad. Edge Cases konkret
ansprechen: Versions-Constraints (ein Plugin kann eine Abhängigkeit zu einem
anderen Plugin per Semver-Range deklarieren, z. B. `~2.1.0` — Auto-Update
holt die höchste Version *innerhalb* der Range, nicht zwingend die
allerneueste, damit ein Update nicht stillschweigend eine Abhängigkeit
bricht); Session-Isolation (die laufende Session bleibt auf dem Stand vom
Sessionstart, bis Reload/Neustart); Cross-Marketplace-Abhängigkeiten
(standardmäßig gesperrt, müssen im `marketplace.json` explizit erlaubt
werden); Offline-Rechner (kein dauerhafter Drift, nächster Online-Check
zieht einfach nach); Fehler landen sichtbar im `/plugin`-Tab "Errors", nicht
versteckt.

**Twist + Abschluss (~5 min):** Erwartung wäre "eine lokale Skill mit
gleichem Namen wie eine Marketplace-Skill überschreibt die lautlos, kein
Fehler, keine Warnung" — **das stimmt nicht**, und zwar bewusst by design:
Marketplace-Skills sind **immer namespaced** (`/plugin-name:skill-name`),
lokale Skills bleiben unnamespaced (`/skill-name`). Beide koexistieren
nebeneinander, kein Konflikt, keine Kollision — genau dafür ist das
Namespacing da. Auflösung fürs Team: der Copy-Paste-Instinkt ("wir bauen
uns lieber was Eigenes, sonst überschreibt uns wer") war unnötige Vorsicht,
nicht begründet. (Was tatsächlich still kollidieren kann, laut einem
GitHub-Issue statt offizieller Doku, mit entsprechender Vorsicht zu
behandeln, falls gefragt: eine Plugin-Skill kann einen **eingebauten**
Slash-Command gleichen Namens überdecken — anderes Szenario als lokal vs.
Marketplace.)

Und: die MCP-Lösung des Teams ist deshalb nicht falsch, nur für ein anderes
Problem gebaut — MCP löst *Zugriff* (Jira, interne APIs), ein Marketplace
löst *Verhalten-Verteilung* (Skills, Rules, Hooks). Beide bleiben nötig,
nebeneinander. Abschlusssatz: "Ein Marketplace macht Standards verfügbar.
Ob sie auch verbindlich sind, entscheidet jedes Repo
für sich — mit einer gleich benannten Datei."

## Pause · 10:50–11:00

## Block 3 · 11:00–12:00 · Anatomy of the Agentic Factory · Trade-off Dark Factory

**Ablauf:**
- Loop · Harness · Factory (10): der Rahmen, an dem sich der Rest des Blocks entlanghangelt
- Pipeline-Überblick (20): Planner → Refine → Implement → Review-Rework-Converge → Marketplace, angewendet auf den Rahmen
- Review-Loop-Tiefe (15): warum ein Rücksprung nötig ist, was "converge" konkret heißt (Vorgriff auf `04-review`)
- Capability vs. Command, kurzer Rückgriff (3): nur Erinnerung, an Tag 1 vollständig behandelt
- Trade-off: Dark Factory (12): volle Autonomie vs. Kontrollverlust, Comprehension Debt, Bezug zu den Pitfalls aus Tag 1

**Loop · Harness · Factory (~10 min):** der konkrete Rahmen (eigene
Zusammenfassung, kein wörtliches Zitat vom Addi-Osmandi-Post), an dem die
Pipeline-Übersicht direkt danach nur noch entlangläuft — keine Vorrede,
sondern das Werkzeug selbst:

- **Loop:** ein Agent, der einen Job wiederholt — Refiner ist ein Loop
  (Ticket lesen → Subagent forken → Pfade verifizieren → zurückschreiben).
- **Harness:** die Wände um den Loop — welche Tools er greifen darf, was er
  sich zwischen Durchläufen merkt, was "fertig" heißt. Und hier wird's
  konkret uneinheitlich, bewusst: Refiner bekommt ein **eigenes,
  session-persistiertes Gedächtnis pro Ticket** (`claude --resume
  <session-id>`, die ID liegt im Ticket) — bei einem Rework-Zyklus knüpft
  er an seine frühere Exploration an, statt neu zu graben. Implementer und
  Reviewer starten dagegen **jedes Mal bei null** (kein `--resume`) — für
  Reviewer bewusst so, damit das Urteil unabhängig bleibt und nicht an der
  eigenen Vorgeschichte klebt. Zwei Skills, zwei Harness-Entscheidungen,
  gleiche Pipeline.
- **Factory:** mehrere Loop+Harness-Paare — Planner, Refiner, Implementer,
  Reviewer, jeder ein eigenständiger Agent — hintereinander verkettet, das
  Ticket als dauerhaftes, crash-resistentes Übergabe-Artefakt zwischen
  ihnen und als Gedächtnis des Orchestrators selbst (welche Stufe ist ein
  Ticket gerade).

Eselsbrücke zum Abschluss dieses Punkts: **Loop ist der Motor, Harness
Karosserie/Lenkrad/Pedalerie, Factory der Fuhrparkservice**, der viele
Fahrzeuge gleichzeitig koordiniert — wer wo unterwegs ist, wer als
nächstes rausmuss, wer in die Werkstatt (Rework) zurückmuss.

*Für die Q&A in der Hinterhand, nicht von selbst erzählen:* das Session-
Resume funktioniert nur, wenn der Orchestrator Refiner als **eigenständigen
`claude`-Prozess per Bash-Shellout** aufruft (`claude -p --resume ...`) —
ruft er ihn stattdessen über das **Task-Tool** als klassischen Subagenten
auf, ist der Context immer ephemer, Resume unmöglich, egal wie wichtig die
Exploration war. Und: das hier ist die **Ziel-Architektur** mit
automatisiertem Orchestrator — was die Paare heute Nachmittag bauen, ist der
manuelle Vorläufer davon (ein Mensch ruft `/refine`, `/implement`,
`/review` nacheinander auf), nicht die Automatisierung selbst. Genau die
"mentored → autonom"-Phasierung aus der Roadmap von Tag 1.

**Pipeline-Überblick (~20 min):** Planner (Tag 1, das "Was", steht schon) →
Refine (das "Wie" konkretisieren) → Implement (Branch/Code) →
Review-Rework-Converge-Loop (Qualitätssicherung ohne Menschen im Loop) →
Marketplace (Verteilung dessen, was sich bewährt hat). Für jede Stufe kurz:
was geht rein, was kommt raus, wer/was liest das Ergebnis weiter — und
welche Harness-Entscheidung (Memory ja/nein, welche Tools) dahintersteckt.

**Review-Loop-Tiefe (~15 min):** bewusst mehr Raum als die anderen Stufen —
dieser Baustein hat kein Vorbild im Original-Repo und ist neu für Barista
(`exercises/day-2/04-review/`). Konkret machen: Implement testet grün,
verfehlt aber ein Acceptance Criterion aus dem High-Level-Plan (dasselbe
Beispiel, das später als Eval-Fall in Block 6 wieder auftaucht). Review prüft
den Diff **pro Acceptance Criterion einzeln**, nicht pauschal gegen den
Testlauf. Ergebnis ist ein echter Branch-Punkt: alle AC erfüllt →
`completed`; sonst zurück zu Refine (Status wieder `in-progress`, die
fehlenden AC stehen konkret im Ticket). Genau das macht aus der bisher
linearen Planner→Refine→Implement-Kette einen Loop.

**Hard Rule: Rework-Cap gegen teure Endlos-Loops.** Ohne Obergrenze kann ein
Ticket beliebig oft zwischen Refine und Implement pendeln, ohne je zu
konvergieren — teuer und, schlimmer, unbemerkt. Deshalb: **maximal zwei
Rework-Zyklen**, dieselbe Zahl wie beim "zwei Fehlversuche, dann Abbruch"-
Muster, das heute schon zweimal auftaucht (Implement-Fix-Loop, Block 4;
Planner-Mini-Eval, Tag 1) — bewusst ein durchgehendes Motiv, kein Zufall.
Wird der Cap erreicht, eskaliert Review an einen Menschen (Status z. B.
`needs-human`), statt ein drittes Mal zurück zu Refine zu schicken.

Und, konsequent zu Tag 1 Block 2 ("eine Prompt-Anweisung ist eine Bitte, kein
Zwang"): dieser eine Cap wird **hart per Hook durchgesetzt**, nicht nur als
Text in der Skill-Datei. Review schreibt bei jedem "zurück zu Refine" einen
lokalen Zähler (`.claude/state/rework-count/<ticket-id>.txt`) hoch. Ein
PreToolUse-Hook sitzt vor genau dem Tool-Call, der den Status wieder auf
"zurück zu Refine" setzt — liest den Zähler, und blockt (exit 2) den
dritten Versuch. Bewusster Kontrast zu den anderen Hard Rules des
Nachmittags (Implements "nie push/merge" bleibt aus Zeitgründen nur Prompt-
Text) — hier, wo es um die teuerste Endlosschleife geht, ziehen wir den
harten Weg einmal wirklich durch.

**Capability vs. Command, kurzer Rückgriff (~3 min):** nur als Erinnerung,
ein Satz: der Unterschied ist Trigger-Design (automatisch erkennbarer
Moment vs. bewusster Zuruf), vollständig an Tag 1 Block 2 behandelt — nicht
neu aufrollen.

**Trade-off: Light vs. Dark Factory (~12 min):** Rahmung zum Nachmittag.
Osmanis Unterscheidung (eigene Zusammenfassung): eine **Light Factory**
hat an definierten Punkten einen Menschen im Loop, eine **Dark Factory**
läuft komplett durch, Ticket rein, PR/Lösung raus, niemand greift
unterwegs ein. Volle Autonomie klingt nach dem Ziel — aber ohne Gates
(Hooks, Tests, Standards, jetzt auch Review-Loop) wird daraus
Kontrollverlust, nicht Geschwindigkeit. Rückbezug auf die Pitfalls aus
Tag 1: der Agent trifft Entscheidungen, die eigentlich dem Team gehören,
wenn niemand die Leitplanken vorher gesetzt hat. Der Übergang von Dark
zurück zu Light — der Punkt, an dem die Kontrolle wieder an einen
Menschen geht — kommt heute Nachmittag als konkreter, benannter Moment
wieder (Block 5: der "Light-Switch").

**Comprehension Debt** (eigene Zusammenfassung von Osmanis Artikel, kein
Zitat) macht diesen Punkt konkret statt vage: die wachsende Lücke zwischen
wie viel Code im System existiert und wie viel davon irgendein Mensch noch
wirklich versteht. Anders als klassische technische Schuld, die sich durch
Reibung meldet (langsame Builds, Dread beim Anfassen), erzeugt
Comprehension Debt **falsche Sicherheit** — die Codebase sieht gesund aus,
Tests bleiben grün, während das Verständnis darunter still aushöhlt. Eine
Dark Factory zahlt diese Schuld nicht ab, sie nimmt sie so schnell wie
möglich auf, Tests die ganze Zeit grün. Direkte Brücke zum Leitmotiv des
Tages: "deliberate architecture is what buys back autonomy" — Gates kaufen
nicht nur Korrektheit zurück, sondern auch Verständnis.

Daraus eine Zuspitzung, die über Osmanis Artikel hinausgeht: der Loop allein
(Planner → Refine → Implement → Review) hält vor allem *Korrektheit* fest —
was ein Ticket wollte, was gebaut wurde, ob es passt. Er hält nicht von
selbst fest, *wie sich die Architektur als Ganzes entwickelt*. Dafür braucht
es zusätzliche, absichtlich erzeugte Output-Artefakte (z. B. ein
laufend aktualisiertes Architektur-Überblicksdokument, das ein Skill nach
jedem Merge pflegt) — nicht damit der Loop schneller baut, sondern damit
ein Mensch jederzeit den Überblick behalten kann, ohne die ganze Codebase
selbst zu lesen. Das Ziel verschiebt sich damit: nicht "schnellere Builds",
sondern **bessere Produkte**, weil die Architektur eine Instanz behält, die
sie versteht. Übergang: "Alles, was ihr heute Nachmittag baut, ist genau so
ein Gate — nicht nur gegen falschen Code, sondern gegen das leise Verlieren
des eigenen Überblicks."

## Mittag · 12:00–13:00

## Block 4 · 13:00–13:55 · Hackathon-Start: Hard Rules · Paare · Hints je Skill

**Ablauf:**
- Rahmung + Hard Rules (10): laut aussprechen, bevor jemand committet
- Paare bilden (10): reales Repo/Modul pro Paar, Rollen freistellen
- Hints je Skill (30): Refiner/Implementer/Reviewer kompakt vorstellen, Planner nur als Fußnote
- Los geht's (5): Paare wählen ihren Einstiegspunkt

> ⚠️ **Hard Rules — nicht vergessen zu sagen.** Bevor die Paare anfangen zu
> coden, laut aussprechen, nicht nur in den `HINTS.md` stehen lassen: **nie
> auf `main` committen · nie `git push` · nie `git merge`/`git rebase` ·
> Tests müssen grün sein vor jedem Commit.** Das Team baut heute gegen
> echte, wenn auch unkritische Repos.

**Rahmung + Hard Rules (~10 min):** kurz, warum diese Regeln nicht
verhandelbar sind (ein kaputter Zwischenstand lässt sich sonst nicht sauber
zurückrollen) — dann weiter zum Bauen, kein langer Mechanismus-Walkthrough.

**Paare bilden (~10 min):** je ein reales, nicht zu kritisches Repo/Modul pro
Paar (aus Tag 1 mitgebracht oder aus dem Discovery bekannt). Rollen im Paar
freistellen — nicht vorschreiben, wer tippt.

Dabei kurz bestätigen, wer in Block 7 den Marketplace-Merge übernimmt — die
Person aus dem Prep-Call/Show & Tell ist der naheliegende Kandidat, aber
kurz nachfragen statt stillschweigend voraussetzen, falls sich das seither
geändert hat oder diese Person am Nachmittag anderweitig eingebunden ist.

**Hints je Skill (~30 min):** kompakter Tour durch die drei fehlenden
Bausteine, damit jedes Paar weiß, was "fertig" für seinen gewählten Skill
heißt, bevor es losgeht — Details liegen in den jeweiligen `HINTS.md`,
hier nur der Kern:

- **Refiner** (`exercises/day-2/02-refine/`): Ticket mit `## High-Level Plan`
  rein, Subagent-Fork erkundet das eigene Repo read-only, `## Refined Plan`
  mit echten Pfaden/Signaturen/Test-Skizze zurück ins Ticket. Kein Edit auf
  Quellcode, nur auf das Ticket.
- **Implementer** (`exercises/day-2/03-implement/`): Branch anlegen, pro
  Datei aus dem Refined Plan editieren → bauen → testen → committen, bei Rot
  maximal zwei Fix-Versuche, dann Abbruch mit klarer Meldung. Implementation
  Log zurück ins Ticket, nie `main`, nie push, nie merge.
- **Reviewer** (`exercises/day-2/04-review/`): kein Vorbild, komplett neu für
  Barista — prüft den Diff gegen jedes Acceptance Criterion einzeln (nicht
  pauschal gegen den Testlauf), Verdikt ist entweder `completed` oder
  zurück zu Refine mit den konkret fehlenden AC im Ticket. **Hard Rule,
  hook-durchgesetzt:** maximal zwei Rework-Zyklen, dann Eskalation an einen
  Menschen statt eines dritten Rücksprungs — Details und der PreToolUse-Hook
  dazu stehen in `04-review/exercise/HINTS.md`.
- **Planner (Fußnote):** wer aus dem Show & Tell/Block 1 noch Nachbesserung
  am eigenen Planner braucht, macht das zuerst kurz nebenbei — Refine/
  Implement/Review hängen alle am `## High-Level Plan`-Vertrag.

**Los geht's (~5 min):** Paare wählen ihren Einstiegspunkt (meist Refiner,
da Implement/Review darauf aufbauen) und legen los.

## Pause · 13:55–14:00

## Block 5 · 14:00–14:50 · Fertigbauen · Ticket vorbereiten · Marketplace-Merge · Orchestrator · Testlauf

**Ablauf:**
- Weiterbauen (15): letzte Lücken schließen, Trainer geht zwischen den Paaren
- Ticket + Planner, gemeinsam (10): echtes Jira-Ticket, Planner grillt die Gruppe, Status → `Ready-for-Factory`
- Marketplace-Merge, Versuch (10): Skills gemeinsam einsortieren — klappt es nicht rechtzeitig, Ausweichen auf Block 7
- Orchestrator bauen (10): ein Prompt, eine Person, die ganze Pipeline
- Testlauf (5): gegen das vorbereitete Ticket, bis zum Light-Switch

**Weiterbauen (~15 min):** kein Frontalteil in diesem Fenster — Trainer geht
zwischen den Paaren, hilft dort, wo es hakt. Hackathon-Spirit heißt hier
konkret: offen im Ergebnis, nicht in der Zeit — nicht jedes Paar muss alle
drei Skills fertig haben, bevor es weitergeht.

**Ticket + Planner, gemeinsam (~10 min):** ein echtes Ticket aus Jira holen
(Jira-MCP), den Planner aus Tag 1 live draufloslassen — als Gruppe, nicht
paarweise. Der Planner grillt: fragt nach, was fehlt, bis die Story wirklich
vollständig ist. Dauert etwa 10 gemeinsame Minuten, gern auch mal
spannend/kontrovers, wenn die Gruppe selbst über Lücken in der eigenen
Anforderung stolpert. Ergebnis: `## High-Level Plan` zurück ins Ticket,
Status auf `Ready-for-Factory` — das genaue Label, nach dem der Orchestrator
gleich sucht.

**Marketplace-Merge, Versuch (~10 min):** wie in Block 4 vorbereitet — die
Paare liefern ihre fertigsten Skill-Ordner, eine Person aus dem Team trägt
sie sequenziell in die `marketplace.json` ein und pusht. Erwartung: klappt
in 10 Minuten. Falls nicht (Zeit läuft davon, technisches Hindernis) —
**kein Blocker**, ausweichen auf den lokalen Copy-Merge und den vollen
Marketplace-Merge in Block 7 nachholen, wo mehr Luft ist.

**Orchestrator bauen (~10 min):** kein Skript, kein Code — eine Person
tippt einen einzigen Prompt, der die ganze Pipeline in Prosa beschreibt.
Fertiger Prompt zum Copy-Pasten: `exercises/day-2/05-orchestrator/README.md`
— **bewusst ohne Checkpoints** (eine frühere Fassung hatte pro-Checkpoint-
Review innerhalb von Implement, rausgenommen wegen unnötiger Komplexität;
der Rework-Cap-Hook aus `04-review` deckt nur die Ticket-weite Schleife,
nicht so eine engere — als verbale Randnotiz erwähnbar, nicht heute bauen).
Der Prompt endet mit dem **Light-Switch** — dem Moment, an dem die Dark
Factory die Kontrolle bewusst an einen Menschen zurückgibt (Rückbezug auf
Block 3) — und hat einen expliziten Fehlerausgang (kein Ticket gefunden /
ein Schritt schlägt fehl → stoppen und melden), damit der Orchestrator bei
einem Problem nicht still hängen bleibt. Technisch läuft das als eine
einzige, durchgehende Orchestrator-Session, die Refiner/Implementer/
Reviewer per Task-Tool aufruft — die vereinfachte Variante aus Block 3,
nicht die Session-Resume-Zielarchitektur mit externem `claude -p
--resume`. Das ist bewusst so, nicht aus Zeitnot: der heutige Nachmittag
baut den manuellen Vorläufer, nicht die volle Automatisierung.

**Testlauf (~5 min):** den Orchestrator-Prompt gegen das vorbereitete
`Ready-for-Factory`-Ticket laufen lassen, als Gruppe zuschauen, bis zum
Light-Switch. Bei einer Review-Abweichung: live nachvollziehen, ob der
"zurück zu Refine"-Pfad tatsächlich greift. Guter Aufhänger für Block 6 —
wie würde man das systematisch statt live entdecken?

## Pause · 14:50–15:00

## Block 6 · 15:00–15:55 · Wie man Evals baut (Kamil)

**Kamil steigt zu Beginn dieses Blocks ein** — kurz einordnen, wo der Tag
gerade steht, bevor er übernimmt.

**Ablauf:**
- Ankommen (5): kurzer Stand der Dinge für Kamil
- Kamils Eval-Ansatz (25): wie er Evals in seiner eigenen Factory gebaut hat, konkretes Beispiel
- Übertragen auf Barista (20): Skill-Evals + Factory-Eval gemeinsam anwenden
- Abschluss (5): "grün heißt nicht fertig" — Rückbezug auf Tag 1 und Block 3

**Ankommen (~5 min):** kurzer Stand der Dinge — was ist heute entstanden,
wo hakt es gerade (aus Block 5 mitgenommen).

**Kamils Eval-Ansatz (~25 min):** Kamil bringt das aus erster Hand mit —
wie er in seiner eigenen Factory geprüft hat, ob Skills zuverlässig das tun,
was sie sollen, statt sich auf Einzelbeobachtung zu verlassen. Konkretes
Beispiel aus seiner Praxis, keine generische Eval-Theorie.

**Übertragen auf Barista (~20 min):** gemeinsam anwenden — 2–3 Testfälle je
Skill (Refine, Implement, Review) gegen das, was heute entstanden ist,
laufen lassen: hält die Format-/Fragen-Disziplin, prüft Review wirklich
Kriterium für Kriterium? Dazu ein Factory-Eval mit dem präparierten Beispiel
aus Block 3 (Tests grün, ein AC verfehlt) gegen die zusammengesetzte
Mini-Factory: fängt der Review-Schritt es ab, oder rutscht es durch?

**Abschluss (~5 min):** "Grün heißt nicht fertig, grün heißt nur: niemand
hat bisher gemerkt, dass es nicht fertig ist." — derselbe Satz wie in den
Pitfalls von Tag 1, jetzt mit einer echten Prüfung dagegen statt nur der
Beobachtung.

## Pause · 15:55–16:00

## Block 7 · 16:00–17:00 · Recap · Marketplace-Merge nachholen (falls nötig) · Q&A · Mentoring-Angebot · Wrap-up

**Ablauf:**
- Recap (10): was heute entstanden ist, Ergebnis-Review
- Marketplace-Merge, Fallback (20 oder 0): nur falls Block 5 nicht durchgekommen ist
- Q&A (10 oder 30): offene Fragen aus dem Hackathon-Nachmittag
- Nächste Schritte + Sparring-/Mentoring-Angebot (15): konkret machen, nicht nur ankündigen
- Wrap (5)

**Recap (~10 min):** was heute gebaut wurde (Refiner, Implementer, Reviewer,
erste lokale Mini-Factory, Orchestrator-Prompt, Light-Switch), was neu war
gegenüber der ursprünglichen Ablaufplanung (MCP-Korrektur, Review-Loop ohne
Vorbild, Eval mit Kamil).

**Marketplace-Merge, Fallback (~20 min, nur falls nötig):** dieser Punkt ist
**bedingt** — der Merge wurde bereits in Block 5 versucht. Ist er dort
durchgelaufen: hier nur kurz gemeinsam bestätigen (`/plugin install` einmal
live in einem frischen Repo zeigen), keine 20 Minuten nötig, die frei
werdende Zeit wandert zu Q&A oder den Nächsten-Schritten. Ist er dort
gescheitert oder aus Zeitgründen abgebrochen: hier vollständig nachholen,
mit derselben Logik wie in Block 5 — **eine Person aus dem Team**, nicht
der Trainer (es gibt noch kein Team-weites Remote-Repo, und Nils' Gerät hat
ohnehin keinen Zugriff darauf, sobald eines existiert), sequenziell
einfügen statt parallel. Diese Person vorher festlegen (z. B. schon bei der
Paar-Bildung in Block 4 ansprechen), nicht erst spontan suchen. Ebenfalls
vorher klären: wer legt das Remote-Repo an, falls es bis Freitag noch keins
gibt (reicht ein leeres GitHub-Repo mit `marketplace.json`-Grundgerüst, das
Team hat ja schon gesehen, wie eins aussieht). Am Ende, so oder so:
`/plugin marketplace add` + `/plugin install` funktioniert für jedes Repo
im Team, nicht nur für die, die heute dabei waren. Das ist der Satz, der
"Starter Kit" einlöst, den der Tag von Anfang an verspricht.

**Q&A (~10 min):** Raum für das, was während des Hackathon-Nachmittags
liegen geblieben ist — die meisten Detailfragen laufen ohnehin schon
während des Zusammenführens auf.

**Nächste Schritte + Sparring-/Mentoring-Angebot (~15 min):** heute
entstand eine vollständige Factory — Planner → Refine → Implement → Review
läuft echt durch, konvergiert echt — aber als **Basis-Version**, beliebig
erweiterbar. Nicht als Lücke framen, sondern als Fundament: offen
ansprechen, wohin sich das ausbauen lässt, statt es vage zu lassen:

- **Lokal vs. remote:** das Team will die Factory remote laufen lassen,
  nicht nur lokal auf einem Entwickler-Rechner — Grund dafür noch nicht
  abschließend geklärt, gemeinsam im Raum einordnen statt vorzugeben. Zwei
  naheliegende Optionen zum Anreißen: ein Rechner, der durchgehend läuft,
  oder eine Cloud-Lösung (z. B. GitHub Actions als Trigger/Runner). Kein
  fertiges Rezept heute, nur der Rahmen für die nächste Iteration.
- **Rückkanal Observability:** die Factory bekommt aktuell nichts davon
  mit, was in Produktion passiert — kein Automatismus, der Monitoring-
  Signale zurück in neue Tickets übersetzt.
- **Rückkanal Kundenfeedback:** genauso — Feedback aus dem Produkt fließt
  heute nirgends automatisch zurück in die Pipeline.
- **Skills verfeinern über Zeit:** die vier gebauten Skills sind ein erster
  Stand, kein Endzustand — wer verbessert sie, wie oft, anhand wovon?
- **Human-in-the-Loop-Eskalation:** wann genau bricht die Factory ab und
  holt einen Menschen — heute nur für den Rework-Cap in Review konkret
  gelöst (Block 3), für den Rest der Pipeline noch offen.
- **Die Factory an sich verbessern:** wer beobachtet, ob die Pipeline
  selbst noch taugt, und wer darf sie ändern?

Jeder dieser Punkte ist ein legitimer Moment, um extern Rat zu holen, statt
im Team zu raten — direkter Übergang zum Mentoring-Angebot: wie meldet sich
das Team, wie oft, wer ist Ansprechpartner bei h&w, punktuell und
pull-basiert statt fester Termine. Die Marketplace-Zusammenführung von eben
ist bereits die erste erledigte aus dieser Liste, guter Einstieg in den
Rest. Ohne diesen Punkt endet der Workshop ohne klaren nächsten Schritt.

**Wrap (~5 min):** kurzer Ausklang, Dank an alle Paare. Schlusssatz für die
Lückenliste von eben, passend zum "klein enden"-Prinzip: "WWND — What
would Nils do? Ihr müsst nicht raten. Ihr könnt mich einfach buchen. Easy
peasy."

---

## Voraussetzung

Wie im Original-Repo: Harness läuft bei allen vorher (Claude Code
installiert, Setup getestet). Jedes Paar hat ein reales, nicht zu kritisches
Repo/Modul zur Hand (aus Tag 1 mitgebracht oder aus dem Discovery bekannt).
