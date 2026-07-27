# Tag 1 — 06.08.2026, remote, Nils solo

**Format:** Remote, 9:00–17:00 (Europe/Berlin), Nils aus Thailand zugeschaltet,
Björn im Urlaub — kein Co-Trainer vor Ort. Entsprechend weniger Pair-Programming-
Choreografie, mehr geführte Demo + Diskussion, Hands-on nur bei der einen
Übung, die wirklich trägt.

**Taktung:** 7 Blöcke à 50–60 Minuten mit 5–10 Minuten Pause dazwischen, 1h
Mittag. Details siehe `README.md` (Abschnitt „Taktung"). Gilt für beide
Workshop-Tage gleich.

| Block | Zeit | Dauer | Inhalt |
|---|---|---|---|
| 1 | 09:00–09:55 | 55 min | Kickoff + Foundations: Hook + Mechanismus |
| — | 09:55–10:00 | 5 min | Pause |
| 2 | 10:00–10:50 | 50 min | Foundations: Twist + Abschluss · Rules & Hooks Kurzdemo |
| — | 10:50–11:00 | 10 min | Pause |
| 3 | 11:00–12:00 | 60 min | Hands-on: Planner-Skill |
| — | 12:00–13:00 | 60 min | Mittag |
| 4 | 13:00–13:55 | 55 min | Roadmap-Workshop |
| — | 13:55–14:00 | 5 min | Pause |
| 5 | 14:00–14:50 | 50 min | Pitfalls, Teil 1 (Hook + Mechanismus) |
| — | 14:50–15:00 | 10 min | Pause |
| 6 | 15:00–15:55 | 55 min | Pitfalls, Teil 2 (Twist + Abschluss) |
| — | 15:55–16:00 | 5 min | Pause |
| 7 | 16:00–17:00 | 60 min | Recap + Ausblick Tag 2 · Wrap-up |

**Ziel des Tages:** Team versteht die Bausteine (Skill/Rule/Hook/Subagent), hat
selbst einen Planner-Skill gebaut, und wir haben gemeinsam eine Roadmap +
Pitfall-Liste für die Factory erarbeitet. Tag 1 endet auf der "Was"-Stufe der
Pipeline (Planner) — Tag 2 baut "Wie" (Refine/Implement) obendrauf.

**Herkunft:** kompaktiert aus `day-1/` (Foundations) + `day-2-am/`
(Customization-Atome) des Original-Repos. Pirate-Beispiele durch Barista-nahe
Beispiele ersetzt, um näher an der echten Arbeitsrealität des Teams zu bleiben.

---

## Block 1 · 09:00–09:55 · Kickoff + Foundations (Hook + Mechanismus)

**Kickoff (~15 min):** kurzer Rahmen — warum heute, was am Ende des Tages
steht, was Tag 2 bringt (Termin dafür idealerweise heute grob fixieren). Kurze
Runde: was läuft heute schon an Agent-Nutzung im Team, wo hakt's?

**Foundations, Hook (~10 min):** Claude Code in einem leeren Ordner ohne jede
Konfig starten und live eine Barista-nahe Aufgabe stellen (z. B. "schreib eine
Commit-Message für diesen Diff" oder "beschreibe diesen PR"). Ergebnis ist
generisch, trifft keine Team-Konvention. Die Gruppe sieht die Lücke, bevor ein
Begriff fällt.

**Foundations, Mechanismus (~30 min):** Schritt für Schritt CLAUDE.md ergänzen,
neu starten, Effekt zeigen. Dann denselben Effekt als Skill bauen (on-demand
statt immer an). Dann als Rule (scoped per Glob). Die Gruppe sieht bei jedem
Schritt, was sich ändert — sie leitet die drei Mechaniken selbst her, statt sie
präsentiert zu bekommen. Durchgängiges Beispiel über alle drei Schritte:
Commit-Message-Konvention (Type/Scope/Body/Ref) — läuft wie Björns Piraten-
Beispiel dreimal durch, nur mit Barista-Bezug statt Piraten-Sprache. Übungen:
`exercises/day-1/00-commit-claude-md/`, `01-commit-skill/`.

Beim Skill-Bau **beiläufig, ohne es zu benennen**: zwei Versionen der
SKILL.md-Beschreibung gegeneinander laufen lassen — eine mit Schritt-für-
Schritt-Instruktionen ("1. Öffne Datei X. 2. Ersetze Y durch Z. 3. …"), eine
mit Zweck + Kontext + Randbedingungen statt fixer Schritte. Dann eine Aufgabe
stellen, bei der eine Annahme nicht stimmt (z. B. die erwartete Datei existiert
unter anderem Pfad). Die instruktionslastige Version hakt oder rät falsch
weiter, die zweckbeschriebene passt sich an. Kein Etikett, keine Folie dazu —
läuft als Teil der normalen Skill-Bau-Demo mit, wird erst im Twist unten
aufgegriffen.

## Pause · 09:55–10:00

## Block 2 · 10:00–10:50 · Foundations (Twist + Abschluss) · Rules & Hooks Kurzdemo

**Foundations, Twist (~10 min):** Erwartung wäre "mehr Kontext ist immer
besser" — und, aus der Skill-Vergleichsdemo eben mitgenommen, "genauere
Instruktionen sind immer besser". Auflösung zu beidem: CLAUDE.md lädt bei
**jeder** Nachricht, egal ob relevant — das kostet permanent Tokens und
Aufmerksamkeit. Eine CLAUDE.md in einem Unterordner **überschreibt** die
übergeordnete, sie ergänzt sie nicht. Und die zweckbeschriebene Skill-Version
war robuster, nicht trotz, sondern **wegen** der fehlenden Schritt-für-Schritt-
Genauigkeit — sie lässt dem Modell die Urteilsfähigkeit, für die man es
eigentlich einsetzt. Bei einer Repo-Landschaft mit vielen Teams und Standards
wie bei Barista heißt das doppelt: falsch platzierte Configs **und** zu enge
Instruktionen brechen leise, nicht laut.

**Foundations, Ergänzung — Command + Prompting-Modi (~5 min, kurzer Nebensatz):**
Kontrast zum eben gebauten Skill: ein **Command** wird über `/name`
aufgerufen — als Datei entweder unter `.claude/commands/<name>.md` oder
unter `.claude/skills/<name>/SKILL.md` (beide Formen erzeugen denselben
Aufruf und verhalten sich technisch identisch, Skills sind der aktuell
empfohlene Nachfolger). **Wichtig, hier korrigiert:** nicht der Ordner
macht daraus "nur der Mensch darf triggern" — standardmäßig können beide
Formen auch vom Modell automatisch ausgelöst werden. Wer das ausschließen
will, setzt explizit `disable-model-invocation: true` im Frontmatter.
Faustregel aus der Trainer-Base-Card `slash-commands`: „Wenn du einen
Prompt öfter als zweimal eingibst, mach ihn zum Command." Passend dazu
(Card `effective-prompting`): Regular-, Thinking- und Plan-Modus sind Teil
desselben Zweck-statt-Instruktion-Gedankens — wann lohnt sich lautes
Nachdenken, wann reicht der Normalmodus. Kein eigener Übungspunkt, nur
Erwähnung — siehe `glossary.md` für die vollständige Definition.

**Foundations, Abschluss (~5 min):** "Willkommen im Club der Leute, die jetzt
jede Woche eine CLAUDE.md suchen, die sich heimlich in einen Unterordner
geschlichen hat."

**Rules & Hooks Kurzdemo (~35 min):** aus `day-2-am/02-rules` +
`day-2-am/04-env-block-hook`, als Demo statt Einzelübung.

- *Rule-Einstieg:* `exercises/day-1/02-commit-rule/` — knüpft direkt an die
  Commit-Konvention aus Block 1 an, diesmal per-Pfad gescoped (Scope `api`
  vs. `frontend`). Klärt nebenbei, warum eine Rule nicht "Commit-Konvention,
  dritte Variante" ist, sondern auf *Ort im Repo* statt *Aktion* reagiert —
  Begründung steht in der Übungs-README, muss hier nicht wiederholt werden.
- *Hook:* Claude Code bitten, `.env` zu lesen ("nur um zu prüfen, ob die
  Variable korrekt gesetzt ist") — es tut es klaglos, wenn kein Hook existiert.
- *Mechanismus:* Rule als weiche Leitplanke zeigen (Kontext, aber umgehbar),
  dann Hook als harte Leitplanke (Exit-Code, nicht umgehbar) live nachrüsten.
- *Twist:* Erwartung wäre "eine Anweisung in der CLAUDE.md, niemals .env zu
  lesen, reicht doch". Auflösung: eine Prompt-Anweisung ist eine Bitte, kein
  Zwang — der Agent kann sie in einem langen Kontext vergessen oder
  wegrationalisieren. Nur der Hook mit Exit-Code ist wirklich hart. Wer mag,
  testet das live gegen die eigene `.env`-Konvention.
- *Ergänzung (Card `permissions-security`, kurzer Nebensatz):* Hooks sind die
  harte Leitplanke, aber die alltägliche Steuerung läuft über
  Allow-/Deny-Permissions — bewusst konfigurieren statt „YOLO-Mode" (alles
  erlauben). Gerade relevant, wenn das Team hofft, den Agenten möglichst
  autonom laufen zu lassen (siehe Dark-Factory-Punkt im Glossar) — Berechtigungen
  sind der Ort, an dem sich diese Autonomie bewusst statt zufällig
  dosieren lässt.
- *Abschluss:* "Der Unterschied zwischen 'bitte nicht' und 'geht technisch
  nicht' ist meistens der Unterschied zwischen Incident und Nicht-Incident."

## Pause · 10:50–11:00

## Block 3 · 11:00–12:00 · Hands-on: Planner-Skill

Statt der Original-Zweiteilung (`day-2-am/01-planning-skill` generisch, dann
`day-2-pm/01-planner-rework` mit Bean-Anbindung getrennt an einem anderen Tag)
bauen wir hier **direkt den Planner mit Bean-Anbindung** — das spart einen
Umbauschritt und bringt sofort den echten Baustein der Pipeline.

**Hook:** Claude Code ohne Planner direkt eine größere, mehrschrittige Aufgabe
geben ("baue Feature X komplett um"). Es rennt los, trifft eigene Annahmen,
ändert vermutlich die falschen Dateien zuerst. Die Gruppe erlebt den
Kontrollverlust live, bevor über Planning gesprochen wird.

**Mechanismus:** Den Planner-Skill schrittweise aufbauen, 4★-Subset — Kontext
explorieren · eine Frage pro Nachricht · 2–3 Alternativen vor Konvergenz ·
Self-Review vor Abschluss. Nach jedem Mechanik-Schritt kurz zurück zum
Hook-Beispiel: was wäre jetzt anders gelaufen?

- Hard rule: nur "Was", keine Pfade/Signaturen — die kommen erst in Refine (Tag 2).
- Jeder wählt eine Planungs-Domäne aus dem eigenen Stack (z. B.
  `migration-planner`, `refactor-planner`).
- Test: `/planner <eigene Aufgabe>` → Bean entsteht mit High-Level-Plan.
- Übung: `exercises/day-1/03-planner/` — kein Copy-Paste-Startpunkt, die
  SKILL.md entsteht live; `HINTS.md` dort enthält Checkliste + Snippet-
  Template. Enthält auch die Trigger-Entscheidung `disable-model-invocation:
  true` (Begründung: Bean-Seiteneffekt + Dialog-Charakter sollen bewusst
  angestoßen werden, nicht beiläufig vom Modell ausgelöst).

**Twist:** Erwartung wäre "ein Planungsschritt macht den Agenten langsamer,
weil er erstmal fragt statt loszulegen". Auflösung: das Gegenteil — der Bean
als Datei-Vertrag macht die nächsten Pipeline-Schritte (Refine, Implement)
günstiger und schneller, weil sie nicht neu explorieren müssen. Die Investition
zahlt sich nicht in der einzelnen Aufgabe aus, sondern über die ganze Pipeline.

**Abschluss:** "Ironischerweise ist der Agent, der zuerst am meisten
nachfragt, am Ende der, der am wenigsten nervt."

## Mittag · 12:00–13:00

## Block 4 · 13:00–13:55 · Roadmap-Workshop

**Ausgangspunkt:** Nordstern aus der Konzeptionsphase mit PO und Eng-Lead,
Termin vom 27.07. Das ist eine Diskussionsgrundlage auf Leads-Ebene, keine
beschlossene Sache — die Aufgabe hier ist, sie mit dem ganzen Barista-Team zu
validieren und zu konkretisieren, nicht sie zu verkünden. Bewusst auf 55
Minuten fokussiert (Kernzielbild + Top-Meilensteine) statt erschöpfend —
Detailtiefe kommt in der Mentoring-Phase.

**Rahmen (~5 min):** kurz teilen, was PO und Eng-Lead skizziert haben — als
Diskussionsgrundlage einführen, nicht als Ergebnis verkünden.

**Zielbild validieren (~15 min):** Dark-Factory-Vision vorstellen (Ticket-rein,
Lösung-raus als Endziel, aber phasiert erreicht — erst mentored collaborative
mode für komplexe Aufgaben, dann volle Autonomie für "bread and butter" wie
Dependency-Updates). Team-Reaktion einholen: deckt sich das mit eurer eigenen
Wahrnehmung? Was fehlt aus eurer Sicht?

**Meilensteine konkretisieren (~20 min):** entlang der vier Hebel aus der
Konzeptionsphase, offene Fragen ans Team statt Vortrag:

- *Pilot-Team:* Barista **ist** das Pilot-Produktteam — bereits vor der
  Konzeptionsphase geklärt, keine offene Suche. Fokus hier nicht "wer",
  sondern "wie": was heißt "mit ihnen zusammen bauen, nicht für sie" für die
  nächsten Wochen ganz konkret?
- *Standardisierung:* Spring Boot/Nuxt als Ziel-Stack, Single-Service-Repos
  statt Monorepo. Bewusst offen ansprechen, wo das wehtut (Legacy-Ktor,
  proprietäre Auth) — bei diesem Team keine Beschönigung.
- *Jira-Workflow:* interaktiver Refinement-Schritt für präzise Sub-Tickets.
  **Direkte Brücke zu Block 3** — der Planner-Skill von heute Vormittag ist
  exakt dieser Mechanismus im Kleinen.
- *Phasierte Automatisierung:* mentored → autonom — wo im Team zuerst
  ansetzen? "Bread and butter" zuerst, nicht die komplexen Fälle.

**Rollen-Wandel ansprechen (~10 min):** neue Engpässe durch Erfolg
(Code-Review, Product-Ownership-Kapazität), Richtung "Product Engineer" als
mögliche Rollen-Verschmelzung. Offen diskutieren, nicht vorentscheiden — passt
inhaltlich als Vorgeschmack auf Block 5/6 (Pitfalls) am Nachmittag.

**Nächste Schritte festhalten (~5 min):** aus der Konzeptionsphase bereits
klar benannt — Barista klärt Standardisierungsanforderungen im Team. Hier im
Workshop konkretisieren: wer treibt das, bis wann, wie wird's sichtbar
gemacht.

## Pause · 13:55–14:00

## Block 5 · 14:00–14:50 · Pitfalls, Teil 1 (Hook + Mechanismus)

Zwei Stufen desselben Musters, nicht zwei getrennte Themen: wenn niemand
explizit entscheidet, entscheidet trotzdem etwas — nur nicht mehr das Team.
Erst im Kleinen (Konventionen), dann im Großen (Architektur/Produkt). Ziel
ist nicht, das direkt zu benennen — das Team soll selbst draufkommen, was auf
dem Spiel steht, statt es präsentiert zu bekommen. Genau das macht ihnen
später begreifbar, warum sie Entscheidungshoheit nicht aufgeben wollen: Coden
kann ein Agent gut, Architektur im Blick behalten und Herr über das Produkt
bleiben ist eine andere Frage.

**Stufe 1 — Hook + Mechanismus (~15 min):** Team bringt ein eigenes
Repo-Beispiel mit widersprüchlichen Konventionen mit (in der Einladung vorher
erbitten). Gemeinsam nachvollziehen, wie/warum sich der Agent für eine
Konvention entscheidet (Auflösungsreihenfolge, Scope) — offene Fragen ans
Team, kein Vortrag. Dient als Aufwärmung auf ungefährlicher Skala, bevor
Stufe 2 dasselbe Muster mit echtem Gewicht zeigt.

**Stufe 2 — Live-Demo (~30 min):** einem Agenten live eine größere,
architektonisch relevante Aufgabe komplett autonom geben — kein Planner, kein
Checkpoint, über mindestens zwei Services/Komponenten hinweg ("zieh das
komplett durch"). Ergebnis muss lauffähig/plausibel sein, sonst dient
"der Code ist doch nicht gut" als Ausweg und das eigentliche Thema geht
unter. Danach gemeinsam auswerten: welche Entscheidungen sind dabei gefallen,
die eigentlich dem Team gehört hätten (Kopplung, Ort der Logik, gewähltes
Pattern, Scope)? Jede:r nennt eine Stelle, an der er/sie anders entschieden
hätte.

*Live-Demo-Setup:* Rabatt-Code beim Checkout, Cart-Service +
Pricing-Service (zwei fiktive, unabhängige Stubs) — Auftrag, Ablauf und
die Entscheidungspunkte, auf die zu achten ist, stehen in
`live-demos/checkout-discount/README.md`. Kein Teilnehmer-Exercise, reines
Trainer-Material.

Block endet bewusst **vor** der Auflösung — die Pause bis Block 6 lässt die
Neugier-Lücke stehen.

## Pause · 14:50–15:00

## Block 6 · 15:00–15:55 · Pitfalls, Teil 2 (Twist + Abschluss)

**Twist (zweistufig):** "Man könnte denken, das Problem ist der Agent." Löst
sich zuerst auf der kleinen Stufe auf (Konventionen aus Block 5 — der Agent
macht nur sichtbar, was zwischen den Teams nie geklärt wurde). Dann auf der
großen Stufe (die Live-Demo): dasselbe Muster, nur mit Architektur-/
Produktentscheidungen statt Namenskonventionen. Bei einer echten Dark Factory
(voll autonom, Ticket-rein/Lösung-raus) passiert das nicht nur einmal am
Nachmittag, sondern bei jedem Ticket, in jedem Repo — Entropie ist dann keine
Frage von Code-Qualität (der Agent codet gut), sondern davon, wer die
Entscheidungshoheit behält. Rückverweis auf Block 3: der Planner mit seinem
STOP-Gate bei den Alternativen ("Wahl des Ansatzes ist Pflicht-Gate, keine
Rückfrage, die sich wegoptimieren lässt") ist genau die Antwort auf dieses
Problem — kein Zufall, dass das Team das schon vormittags selbst gebaut hat.
Genau hier fließen auch die Agile-Manifest-Werte unterschwellig ein.

**Abschluss (~5 min):** bewusst klein halten — Beobachtung, kein Appell.
Möglicher Satz: "Ein Agent, der gut codet, ist kein Problem. Einer, der
Entscheidungen trifft, die euch gehören, schon — auch wenn der Code sauber
ist."

## Pause · 15:55–16:00

## Block 7 · 16:00–17:00 · Recap + Ausblick Tag 2 · Wrap-up

**Recap + Ausblick (~30 min):** was macht Refine (Was → Wie), was macht
Implement (Wie → Branch/Code), was ist neu gegenüber dem, was das Team kennt
(Orchestration/Review-Rework-Converge, Marketplace/Plugin). Kein Deep-Dive —
Vorfreude wecken, nicht vorwegnehmen.

**Wrap-up (~30 min):** offene Fragen, Termin Tag 2 fixieren (falls noch nicht
vormittags passiert), wer bringt was zu Tag 2 mit (echter Repo-Ausschnitt für
den Transfer-Hackathon).

**Einordnung zum Schluss (kurzer Nebensatz):** Barista ist bewusst das erste
Team, das das ausprobiert — nicht das einzige, das es je tun wird. Was hier
entsteht, ist später auch Beweismaterial für das nächste Team, das
onboardet. Nicht ausführen, nur als Perspektive stehen lassen.

---

## Voraussetzung

Wie im Original-Repo: Harness läuft bei allen vorher (Claude Code installiert,
Setup getestet) — das ist Bedingung aus der Konzeptionsphase, nicht Teil des
Tages selbst.
