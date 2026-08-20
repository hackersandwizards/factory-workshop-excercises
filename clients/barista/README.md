# Workshop-Anpassung — Team Barista

Abgeleitet von `day-1/`, `day-2-am/`, `day-2-pm/` (Björns bisherigem 3-Tage-Format
für h&w · SSW). Für Barista auf **zwei separate Tage** verdichtet — kein Day 3.

## Termine & Setup

| Tag | Datum | Ort | Trainer |
|---|---|---|---|
| **Tag 1** | 06.08.2026, 9:00–17:00 | Remote (Nils aus Thailand zugeschaltet) | **Nils solo** — Björn im Urlaub |
| **Tag 2** | 21.08.2026, 9:00–17:00 | Remote | **Nils solo**, Kamil ab Block 6 (15:00) dazu — Björn nicht dabei |

Die beiden Tage liegen **getrennt**, nicht an aufeinanderfolgenden Tagen wie im
Original-Format. Beide Tage sind remote — Tag 2 war ursprünglich als
Vor-Ort-Tag geplant, wurde aber auf Vorschlag der Trainer auf remote
umgestellt, weil ein Teil der Teilnehmenden in Rumänien sitzt. Das beeinflusst
den Zuschnitt: Tag 1 ist bewusst so gebaut, dass er remote und solo trägt
(weniger Pair-Choreografie, mehr geführte Demo + Diskussion); Tag 2 bleibt
Hackathon-Spirit, aber remote über Google Meet — die 2er-Teams pairen über
Breakout-Räume statt am gemeinsamen Tisch, Trainer unterstützt per
Screen-Share statt im Raum herumzugehen, und die Teilnehmenden schreiben den
Code selbst in ihren eigenen Repos.

## Didaktisches Prinzip: Erfahrung vor Theorie

Nach der Formel für gutes Erklären in vier Schritten: **jeder Erklärblock
startet mit Erfahrung, nicht mit Konzept.** Vier Schritte pro Block:

1. **Hook über Erfahrung** — die Gruppe erlebt live etwas (meist: eine Lücke
   oder ein Fehlverhalten von Claude Code ohne den zu lernenden Baustein),
   bevor irgendein Begriff fällt. Erzeugt eine Neugier-Lücke.
2. **Mechanismus** — Schritt für Schritt Ursache-Wirkung aufbauen, die Gruppe
   entdeckt den Baustein mit, statt ihn präsentiert zu bekommen.
3. **Der befriedigende Klick** — die Auflösung ist anders, als die Gruppe
   erwartet hätte. Der Twist.
4. **Klein enden** — ein kleiner Witz, eine Beobachtung, ein praktischer Tipp.
   Keine große inspirierende Botschaft.

Beide Agenda-Dateien sind entlang dieser vier Schritte pro Übungsblock
strukturiert (Abschnitte "Hook" / "Mechanismus" / "Twist" / "Abschluss" statt
linearer Anleitung).

## Leitmotiv (durchgehend über beide Tage)

> Human-in-the-loop rausnehmen geht — aber nur, wenn die Kontrolle durch
> deterministische Gates ersetzt wird. Gates sind Hooks, Tests, Standards.
> Ohne Standards keine Gates. Ohne Gates keine Autonomie.

Läuft nie als eigener Foliensatz oder als benanntes Konzept vor der Gruppe —
transportiert sich über die Mechanik der Übungen selbst (Rules vs. Hooks,
Review-Rework-Converge-Loop, Plugin-Governance).

## Taktung (beide Tage)

7 Blöcke à 50–60 Minuten, 5–10 Minuten Pause nach jedem Block, 1h Mittag —
damit alle über den ganzen Tag fit und bei der Sache bleiben. 3 Blöcke
vormittags, 4 nachmittags:

| Block | Zeit | Dauer |
|---|---|---|
| 1 | 09:00–09:55 | 55 min |
| — | 09:55–10:00 | 5 min Pause |
| 2 | 10:00–10:50 | 50 min |
| — | 10:50–11:00 | 10 min Pause |
| 3 | 11:00–12:00 | 60 min |
| — | 12:00–13:00 | 60 min Mittag |
| 4 | 13:00–13:55 | 55 min |
| — | 13:55–14:00 | 5 min Pause |
| 5 | 14:00–14:50 | 50 min |
| — | 14:50–15:00 | 10 min Pause |
| 6 | 15:00–15:55 | 55 min |
| — | 15:55–16:00 | 5 min Pause |
| 7 | 16:00–17:00 | 60 min |

Die 4-Schritt-Übungsblöcke (Hook/Mechanismus/Twist/Abschluss) sind auf diese 7
Blöcke gemappt — teils 1:1 pro Block, teils über eine Pause hinweg gestreckt
(z. B. Pitfalls Tag 1: Hook+Mechanismus in Block 5, Pause als bewusst stehen
gelassene Neugier-Lücke, Twist+Abschluss erst in Block 6). Details je Tag in
`day-1-agenda.md` / `day-2-agenda.md`.

## Zeitplan für die Vorbereitung

Ziel: **erster vollständiger Workshop-Entwurf bis 24.07.2026**,
Workshop-Termin Tag 1 ist der 06.08.

## Warum diese Aufteilung

Die ursprüngliche Barista-Ablaufplanung sah vor: Tag 1 = gemeinsam Roadmap bauen,
Pitfalls & kritische Punkte durchgehen; Tag 2 = Hackathon → Starter Kit. Diese
Aufteilung bleibt erhalten, wird aber jetzt über zwei zeitlich getrennte Termine
statt zwei Kalendertage realisiert:

- **Tag 1** = Foundations (kompaktiert aus `day-1/` + `day-2-am/`) + Roadmap +
  Pitfalls. Endet mit dem Planner-Skill (die "Was"-Stufe der Pipeline) als
  Brücke zu Tag 2.
- **Tag 2** = Refine + Implement (aus `day-2-pm/`) + zwei neue Bausteine, die im
  Original fehlen (siehe unten) + Transfer-Hackathon gegen einen echten
  Barista-Repo-Ausschnitt statt des Calc-Sandkastens → Ergebnis ist das Starter
  Kit (Rules, Configs, Hooks, Skills, Repo zum Weiterarbeiten).

## Warum kompaktiert statt vollständig übernommen

Der Kunde hat für diesen Workshop **zwei Tage** freigegeben — weniger, als für
eine wirklich vollständige Foundation für die Factory im Original-Dreitage-
Format nötig wäre. Das reduziert die Zeit, die für langsames, sauberes
Fundament-Legen bleibt — wir kompensieren, wo möglich, über Kompaktierung
(paralleler statt sequenzieller Ablauf), nicht über Kürzung der Inhalte.

## Zwei Bausteine, die im Original-Repo fehlen und ergänzt werden müssen

**Update vom 18.08.2026 (Call mit dem Team):** das Team hat zwischenzeitlich
selbst einen MCP-Server als Marketplace-Ersatz gebaut — in der (falschen)
Annahme, ein Plugin-Marketplace biete kein Auto-Update. Für Block 2 an Tag 2
heißt das: keine leichte Demo mehr, sondern eine volle Session, die die
Annahme live widerlegt (Auto-Update-Beweis) und die MCP-Lösung sauber
einordnet (löst Zugriff, nicht Verhalten-Verteilung — beides bleibt nötig).
Details in `day-2-agenda.md`, Block 2.

1. **Marketplace-/Plugin-Mechanik** — im Original nur als Stretch-Erwähnung
   (`/skill-creator`-Demo), nicht als eigene Übung. Für Barista laut Björns
   Slack-Notiz früh relevant (heterogene Repo-Landschaft, viele Teams — Plugins
   als Weg, Konventionen wiederverwendbar zu verteilen statt in jedem Repo neu
   zu erfinden). Neuer Baustein für Tag 2 vormittags.
   **Wichtig:** Nils hat selbst noch nicht praktisch mit Plugin-/Marketplace-Mechanik
   gearbeitet — das ist Teil der eigenen Vorbereitung, nicht nur Material-Bau.
   Eigene Lernschleife (Doku lesen, selbst ein Mini-Plugin bauen) muss vor dem
   24.07.-Entwurf liegen, sonst fehlt die Substanz, um Fragen im Workshop live
   zu beantworten.
2. **Orchestration- / Review-Rework-Converge-Loop** — die bestehende
   Planner→Refine→Implement-Pipeline ist linear, ohne Rücksprung. Die heterogenen
   Standards des Teams + Agency-Code-Altlasten brauchen eher einen Loop, der
   nach Implement einen Review-Schritt einzieht, der bei Bedarf zurück zu
   Refine schickt, statt stur weiterzulaufen. Neuer Baustein für Tag 2
   nachmittags, direkt im Anschluss an Implement.

## Rollen

- **Nils** — Lead, Tag 1 solo, Tag 2 solo bis Block 6 (15:00).
- **Kamil** — steigt an Tag 2 ab Block 6 (15:00) ein, übernimmt den
  Eval-Block aus eigener Erfahrung (hat Evals in seiner eigenen Factory
  bereits gebaut).
- **Björn** — nicht Teil von Tag 2, hat aber die ursprüngliche
  Ersteinschätzung zum Kunden geliefert (technisch heterogen,
  Material-Anforderungen).
- Ein weiterer H&W-Kollege gibt vor Fertigstellung noch eine Feedback-Runde
  zum Material.

## Dateien

- `day-1-agenda.md` — 06.08., remote, Nils solo.
- `day-2-agenda.md` — 21.08.2026, remote, Nils solo, Kamil ab Block 6.
- `glossary.md` — Begriffs-Vorbesprechung vor dem Workshop.
- `exercises/day-2/02-refine/`, `03-implement/`, `04-review/` —
  Übungsgerüste für den Hackathon-Nachmittag, `04-review` ohne
  Original-Vorbild (siehe Punkt 2 unten).
