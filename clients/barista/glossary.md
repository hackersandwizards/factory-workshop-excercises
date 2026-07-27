# Glossar — Begriffs-Vorbesprechung

Zweck: vor dem Workshop mit dem technischen Lead durchgehen, ob wir bei den zentralen
Begriffen dasselbe meinen — und wo ggf. noch vertieft werden muss, bevor wir
die Agenda final festzurren (Ziel-Entwurf 24.07., siehe `README.md`).

**Wie benutzen:** Begriff für Begriff durchgehen. Bei jedem: passt die
Kurzdefinition zum Verständnis des Teams? Wenn nein/unsicher → in der letzten
Spalte notieren. Ergebnis entscheidet, ob ein Begriff in der Agenda mehr Zeit
braucht (z. B. eigener Hook-Absatz statt Kurzdemo) oder ob er als bekannt
vorausgesetzt werden kann (Zeit sparen für Tieferes).

Die Spalte „Wo im Workshop" verweist auf die aktuelle Planung
(`day-1-agenda.md` / `day-2-agenda.md`) — zeigt, wie viel Tiefe jeder Begriff
aktuell bekommt.

## Geltungsbereich — warum eine eigene Spalte

Nicht jeder Begriff hier ist AI-allgemeingültig. Manche sind modell-/tool-
unabhängige Konzepte, manche sind Claude-Code-Produktfeatures, manche sind
ein konkretes Drittanbieter-Tool, das Björn für sein Übungs-Repo gewählt hat,
und manche haben wir selbst für diesen Workshop geprägt. Das ist bei Barista
nicht nebensächlich: laut Discovery-Call läuft bei euch **Cursor und Claude
Code parallel** — ein Begriff, der nur ein Claude-Code-Feature beschreibt
(z. B. „Skill"), übersetzt sich nicht 1:1 in Cursor, auch wenn das
zugrundeliegende Konzept dort in anderer Form existiert. Genau das lohnt sich,
im Vorgespräch zu klären: gilt das, was wir zeigen, für euren ganzen Stack oder
nur für den Claude-Code-Teil davon?

Kennzeichnung in der Spalte „Geltungsbereich":

- **Allgemein** — modell-/tool-unabhängiges KI- oder Software-Engineering-Konzept
- **Claude Code** — Anthropic-Produktfeature; Konzept oft übertragbar, konkrete Mechanik nicht
- **Tool** — konkretes Drittanbieter-Tool, hier nur exemplarisch gewählt
- **H&W/Björn** — unsere eigene Begriffsprägung aus dem Trainingsmaterial, kein Industriestandard
- **Workshop-neu** — unser eigener Vorschlag für diesen Workshop, existiert im Original-Material noch nicht
- **Kunde/Branche** — im Discovery-Call verwendeter Begriff bzw. ein aufkommender Szene-Begriff ohne feste Norm

## Modell & Kern-Vokabular

| Begriff | Geltungsbereich | Kurzdefinition | Wo im Workshop | Offene Klärungsfragen |
|---|---|---|---|---|
| Modell (LLM) | Allgemein | Das Sprachmodell selbst (z. B. Claude) — sagt nur Tokens vorher, hat kein Gedächtnis über die Session hinaus, keinen Zugriff auf irgendwas ohne Werkzeuge. | Vorausgesetzt, wird nicht extra erklärt | |
| Agent | Allgemein | Modell + Harness — das Modell plus alles, was drumherum gebaut ist, damit es zuverlässig etwas bewirken kann (Tools, Kontext, Leitplanken). „Agent = Model + Harness" (Formulierung aus Fowler/Osmani, siehe unten). | Tag 1, Block 1 (Kickoff/Foundations) | |
| Prompt | Allgemein | Die Eingabe an das Modell — kann Instruktion, Frage, Zweck-/Kontextbeschreibung sein. | Durchgängig, nicht extra thematisiert | |
| Context / Context Window | Allgemein | Alles, was das Modell bei einer Anfrage tatsächlich „sieht" (Prompt + geladene Dateien + Tool-Ergebnisse + Verlauf), begrenzt auf eine feste Größe (Context Window). Wird bei jeder Nachricht neu befüllt. | Tag 1, Block 1 (CLAUDE.md-Kosten-Argument im Twist) | |
| Token | Allgemein | Kleinste Verarbeitungseinheit für das Modell (grob: Wortstück). Kosten- und Kontext-Budget werden in Tokens gemessen. | Beiläufig (CLAUDE.md-Twist: „lädt bei jeder Nachricht, kostet Tokens") | |
| Prompt Engineering vs. Context Engineering vs. Harness Engineering | Allgemein (aufkommend) | Drei verwandte, oft verwechselte Ebenen: Prompt Engineering = wie eine einzelne Anfrage formuliert ist; Context Engineering = was insgesamt im Context Window landet; Harness Engineering = die gesamte Infrastruktur um das Modell (siehe unten). „Harness Engineering" ist branchenweit im Umlauf (Fowler, Osmani u. a.), aber noch kein gefestigter Standardbegriff. | Tag 1, Block 1 (Rahmenbegriff) | |

## Harness-Bausteine

| Begriff | Geltungsbereich | Kurzdefinition | Wo im Workshop | Offene Klärungsfragen |
|---|---|---|---|---|
| Harness | Allgemein | Alles, was um das Modell gebaut wird, damit ein verlässlicher Agent daraus wird: Prompts/CLAUDE.md, Skills, Tools/MCP, Hooks, Sandbox, Orchestrierung, Observability. Deckt sich mit dem Begriff, den Barista im Discovery-Call selbst benutzt hat. | Rahmenbegriff über beide Tage | |
| CLAUDE.md | Claude Code | Immer-an-Kontextdatei, wird bei **jeder** Session/Nachricht geladen, unabhängig von Relevanz. Hierarchisch: Unterordner-Datei überschreibt (nicht ergänzt) die übergeordnete. Cursor hat ein eigenes, anders funktionierendes Äquivalent (`.cursor/rules` bzw. Projekt-Regeln) — Konzept übertragbar, Datei/Mechanik nicht 1:1. | Tag 1, Block 1–2 (Foundations) | Gilt die Demo nur für den Claude-Code-Teil eures Stacks? |
| Skill (SKILL.md) | Claude Code | On-demand-Baustein — lädt nur, wenn die Beschreibung zur Aufgabe passt („activation key"). Bleibt sonst inaktiv, kostet dann auch keinen Kontext. Kein Cursor-Äquivalent mit derselben Mechanik. | Tag 1, Block 1–2 · Block 3 (Planner) | Baut ihr aktuell schon eigene Skills, oder wäre der Skill-Bau in Block 1 für alle komplett neu? Bestimmt, wie viel Tempo wir in der Demo vorlegen können. |
| Rule | Claude Code | Scoped-Baustein, lädt automatisch, wenn eine passende Datei im Spiel ist (`paths`-Frontmatter, Liste von Glob-Mustern). Weiche Leitplanke — im Kontext, aber prinzipiell umgehbar. Cursor hat mit `.cursor/rules` ein ähnliches, aber technisch eigenständiges Konzept (dort heißt das Frontmatter-Feld `globs` — Verwechslungsgefahr, siehe Klärungsbedarf). | Tag 1, Block 2 (Kurzdemo) | Läuft bei euch schon mal `.claude/rules/` mit dem falschen Feldnamen (`glob`/`globs` statt `paths`)? Live geprüft: mit `glob`/`globs` lädt die Rule immer, statt nur bei passender Datei — stiller Fehler, kein Fehlerhinweis. |
| Hook | Claude Code | Shell-Skript auf einem Tool-Event (z. B. PreToolUse). Nicht-Null-Exit blockiert den Tool-Call **hart** — der Agent kann das nicht wegargumentieren, anders als eine Prompt-Anweisung. | Tag 1, Block 2 (Kurzdemo) | |
| Subagent | Claude Code | Läuft in eigenem, isoliertem Kontext, macht die „schmutzige" Arbeit (viel Lesen/Suchen) und gibt nur eine Zusammenfassung zurück — schont den Hauptkontext. Das Konzept „Multi-Agent-Delegation" ist allgemein, diese konkrete Umsetzung (Task-Tool) ist Claude Code. | Tag 2, Block 1–2 (Refine) | |
| Command (Slash Command) | Claude Code | Über `/<name>` aufgerufener Baustein — als Datei entweder unter `.claude/commands/<name>.md` **oder** unter `.claude/skills/<name>/SKILL.md` (Skills sind der aktuell empfohlene, funktionsreichere Nachfolger; beide Formen erzeugen denselben `/<name>`-Aufruf und verhalten sich technisch identisch). **Korrigiert gegenüber Vorversion:** nicht der Ordner entscheidet, ob Mensch oder Modell auslöst — standardmäßig können **beide** Formen sowohl von Hand als auch automatisch vom Modell getriggert werden. Wer erzwingen will, dass wirklich nur der Mensch auslöst, setzt explizit `disable-model-invocation: true` im Frontmatter. | Aktuell **kein** eigener Übungspunkt in der Agenda — nur indirekt über den „Capability vs. Command"-Kontrast unten erwähnt. | Lohnt sich eine kurze Live-Gegenüberstellung im Skill-Bau-Block (Tag 1, Block 1), oder reicht die Erwähnung? |
| MCP / MCP-Server | Allgemein (offener Standard) | Protokoll, über das ein Agent mit externen Systemen spricht (Dateien, APIs, Tools). Ursprünglich von Anthropic, mittlerweile herstellerübergreifend adoptiert (u. a. OpenAI, Google) — eine der wenigen hier wirklich tool-unabhängigen Techniken. Bei Barista aktuell nur lokal, nicht aus der Cloud. | Nicht explizit im aktuellen Plan — Barista-Constraint aus Discovery-Call | Ist „nur lokaler MCP-Zugriff" eine bewusste Governance-Entscheidung oder eine technische Übergangslösung, die sich vor dem Workshop noch ändert? Welche MCP-Server (GitLab/Jira/Confluence) sind für Barista überhaupt relevant? |
| Tool / Tool-Whitelist | Allgemein | Eine konkrete Fähigkeit, die ein Agent aufrufen kann (Read, Bash, Edit, …). Bei Subagents typischerweise auf eine Whitelist eingeschränkt. | Tag 2, Block 1 (Refine: read-only) | |
| Guardrail | Allgemein | Sammelbegriff für alles, was Verhalten einschränkt — kann weich (Rule, Prompt-Hinweis) oder hart (Hook) sein. | Beiläufig (Rules-vs-Hooks-Twist) | |

## Pipeline & Prozess

| Begriff | Geltungsbereich | Kurzdefinition | Wo im Workshop | Offene Klärungsfragen |
|---|---|---|---|---|
| Bean | **Tool** (Drittanbieter) | Datei-Kontrakt zwischen den Pipeline-Stufen, verwaltet über die `beans`-CLI (github.com/hmans/beans) — ein konkretes, kleines Drittanbieter-Tool, das Björn für sein Übungs-Repo gewählt hat, **kein** AI-Industriestandard. Das dahinterliegende Prinzip (Plan/Status/Log als Datei statt als Gespräch) ist allgemein und ließe sich genauso mit einem Jira-Ticket, einem Linear-Issue oder einer einfachen Markdown-Datei umsetzen. | Tag 1, Block 3 (Planner) · Tag 2 durchgängig | Wollen wir bei `beans` bleiben, oder auf ein Tool umstellen, das näher an eurem Stack ist (Jira?) — oder das Prinzip ganz werkzeugneutral zeigen? |
| Planner / High-Level Plan | H&W/Björn | Erste Pipeline-Stufe in Björns Workshop-Repo: das „Was" — Beschreibung, Ansatz, Steps, Acceptance Criteria, keine Pfade/Signaturen. Das allgemeine Prinzip „erst planen, dann coden" ist branchenweit üblich, diese genaue Drei-Stufen-Aufteilung + Bean-Anbindung ist Björns spezifische Umsetzung. | Tag 1, Block 3 | |
| Refine / Refined Plan | H&W/Björn | Zweite Stufe: das „Wie" — Subagent erkundet die echte Codebase (read-only), liefert konkrete Pfade/Signaturen/Test-Skizze zurück in den Bean. | Tag 2, Block 1–2 | |
| Implement | H&W/Björn | Dritte Stufe: Branch anlegen, pro Schritt editieren/bauen/testen/committen. Nie auf main, nie push, nie merge. | Tag 2, Block 2–3 | |
| Acceptance Criteria (AC) | Allgemein | Klassischer Software-Engineering-Begriff, nicht KI-spezifisch. Im Plan festgehaltene Erfolgskriterien — Prüfmaßstab dafür, ob eine Umsetzung wirklich „fertig" ist, unabhängig davon, ob Tests grün sind. | Tag 2, Block 4 (Review-Twist) | |
| Orchestration | Allgemein | Koordination mehrerer Agenten/Subagenten über eine Aufgabe hinweg (wer macht was, in welcher Reihenfolge). | Tag 2, Block 4 (neuer Baustein) | |
| Review-Rework-Converge-Loop | **Workshop-neu** | Rücksprung-Mechanik nach Implement, die wir für Barista neu entwerfen — existiert im Original-Übungsrepo noch nicht. Prüft gegen die Acceptance Criteria (nicht nur gegen Tests) und schickt bei Bedarf zurück zu Refine. | Tag 2, Block 4 (muss noch gebaut werden) | |
| Human-in-the-loop | Allgemein | Grad, in dem ein Mensch zwischen den Pipeline-Stufen freigeben/eingreifen muss, statt dass der Agent durchläuft. Barista zeigte im Discovery-Call wenig Begeisterung dafür — guter Punkt, um gemeinsam zu klären, wo genau die Grenze liegen soll. | Durchgehendes Thema, nicht als eigener Block | |
| Dark Factory | Kunde/Branche | Zielbild vollständig autonomer Coding-Agenten ohne laufenden Human-in-the-loop. Im Discovery-Call verwendeter Ausdruck; in der Branche ein aufkommender, aber nicht formal genormter Begriff. | Nicht als eigener Block — sollte in der Klärung „wie schnell/wie autonom" mitschwingen | |

## Verteilung & Skalierung

| Begriff | Geltungsbereich | Kurzdefinition | Wo im Workshop | Offene Klärungsfragen |
|---|---|---|---|---|
| Plugin | Claude Code | Bündel aus Skills/Rules/Hooks, das sich als Einheit installieren lässt — Konventionen einmal pflegen, in vielen Repos ausrollen. Konkrete Mechanik ist ein Claude-Code-Feature; das allgemeine Prinzip „Plugin-System" gibt es in vielen Tools unter anderem Namen. | Tag 2, Block 5–6 (neuer Baustein, muss noch gebaut werden) | Braucht ihr das auch für den Cursor-Teil eures Stacks — und wenn ja, wie würde das dort aussehen? |
| Marketplace | Claude Code | Verzeichnis/Registry, aus dem Plugins installiert werden — der Verteilweg für Plugins über Teams/Repos hinweg. | Tag 2, Block 5–6 (neuer Baustein) | |
| Skill-Registry | Allgemein (DevOps-Begriff) | Aus der Plattform-Engineering-/DevOps-Welt geliehen, nicht KI-spezifisch: zentrale Übersicht, welche Skills/Capabilities im Unternehmen überhaupt existieren — Vorstufe zu einem echten Marketplace. | Nicht im aktuellen Plan — evtl. als Ausblick relevant | |
| Paved Road | Allgemein (DevOps-Begriff) | Der „vorgezeichnete", unterstützte Weg, etwas zu tun (Gegenteil von „jedes Team erfindet es neu") — Grundidee hinter der Plugin-/Marketplace-Übung. | Beiläufig (Plugin-Hook: Copy-Paste-Problem) | |
| Starter Kit | Workshop-neu | Kein Fachbegriff, nur unser Name für das konkrete Ergebnis von Tag 2: Rules, Configs, Hooks, Skills, Repo zum Weiterentwickeln — bewusst **mit** dem Team gebaut, nicht mitgebracht. | Tag 2, Block 6–7 (Transfer-Hackathon) | |

## Konzepte / Denkmodelle

| Begriff | Geltungsbereich | Kurzdefinition | Wo im Workshop | Offene Klärungsfragen |
|---|---|---|---|---|
| Guides vs. Sensors | Branche (Fowlers Prägung) | Zwei Kontrollrichtungen im Harness: Guides steuern vorab (CLAUDE.md/Skill/Rule), Sensors prüfen im Nachgang (Tests, Review-Agenten). Aus Martin Fowlers Artikel zu Harness Engineering — wird zunehmend zitiert, ist aber (noch) nicht der eine Industriestandard. | Rahmenbegriff über beide Tage | |
| Capability vs. Command | Claude Code (Mechanik) + H&W/Björn (Framing/Beispiel) | **Dreifach korrigiert gegenüber Vorversionen dieses Glossars** — es geht nicht darum, *wie* ein Skill geschrieben ist, sondern um zwei verschiedene Bausteine: **Command** = auf Zuruf per `/<name>`, **Capability** = ein Skill, den das Modell selbst einsetzt, wenn die Beschreibung zur Aufgabe passt. Neu (dritte Korrektur): der Unterschied liegt **nicht am Ordner** (`.claude/commands/` vs. `.claude/skills/`) — beide erzeugen denselben `/<name>`-Aufruf und sind standardmäßig **beides zugleich**, von Hand und automatisch auslösbar. Was eine Capability zum reinen Command macht, ist das Frontmatter-Feld `disable-model-invocation: true`. Björns Beispiel Conventional Commits bleibt gültig, nur die Begründung ändert sich: ein `/commit`-Skill **mit** `disable-model-invocation: true` triggert wirklich nur auf Zuruf; ein `commit-message`-Skill **ohne** dieses Feld triggert automatisch, sobald die Beschreibung passt — der Unterschied liegt am Flag, nicht am Verzeichnis. Nicht zu verwechseln mit „Purpose vs. Instructions" unten — das ist eine andere Achse (wie der *Inhalt* eines einzelnen Skills geschrieben ist, nicht welcher Baustein-Typ verwendet wird). Bewusst **nicht** Thema: vollständige Tour durch alle Cursor-Konfigurationsflächen, Werkzeug-Debatte ("welches Tool macht das am besten"), Bewertung der Repo-Maturity der Teilnehmer. | Tag 1, Block 1 (aktuell nur als Kontrast erwähnt, kein Hands-on für Command) | |
| Purpose- vs. instruktionsbasiertes Skill-/Prompt-Design | Allgemein (Praxiswissen, kein fester Fachbegriff) | Ob ein Skill/Prompt den Zweck + Randbedingungen beschreibt (Modell entscheidet den Weg selbst) oder starre Schritt-für-Schritt-Anweisungen gibt (bricht bei der ersten Abweichung von der Erwartung). Verbreitete Prompting-Praxis, aber nicht an einen Autor/ein Tool gebunden. | Tag 1, Block 1–2 (Skill-Vergleichsdemo) | |
| Spec-Driven Development (SDD) | Allgemein (Branchentrend 2025/26, u. a. GitHub Spec Kit, AWS Kiro — kein Einzeltool) | Statt direkt Code zu prompten, wird zuerst eine strukturierte, **versionierte** Spezifikation geschrieben (Outcomes, Scope, Constraints, offene Entscheidungen, Verifikationskriterien), aus der der Agent Code ableitet; die Spec bleibt lebendiges Dokument, oft CI/CD-geprüft. Nils' Ergänzung, zentral für Barista: Fokus muss auf dem **Warum** (Intent/Outcome) liegen, nicht nur dem **Was** (Feature-Liste) — dieselbe Achse wie „Purpose vs. Instructions" oben. Versionierung ist ein echter Pluspunkt (Nachvollziehbarkeit von Entscheidungen). **Aber:** je länger/umfassender eine Spec, desto länger kann der Agent am Stück unbeaufsichtigt laufen, ohne Checkpoint — das ist laut Nils/Björn **nicht** erstrebenswert. Deckt sich mit dem Grundgedanken hinter Planner→Refine→Implement (bewusst kleine, geprüfte Schritte) und dem neuen Review-Rework-Converge-Loop, statt eine große Spec zu schreiben und den Agenten lange allein laufen zu lassen. | Nicht als eigener Block — die Pipeline ist implizit die Antwort darauf, der Begriff selbst fällt aber nirgends namentlich | Schreibt ihr heute schon Specs vor dem Coden? Wie lang/detailliert — und lasst ihr den Agenten damit schon länger am Stück unbeaufsichtigt laufen? |
| Vibe Coding vs. Factory-Ansatz | gemischt: „Vibe Coding" Allgemein/Mainstream, „Factory" H&W-Kreis | „Vibe Coding" = mittlerweile breit etablierter Szene-Begriff für freies Drauflos-Prompten ohne Plan-Struktur. „Factory" als Gegenpol (Pipeline mit Plan/Refine/Implement-Disziplin) ist eher Vokabular aus unserem/Björns Umfeld, nicht allgemein genormt. Aus Nils' eigenem Benchmark: Factory schlägt vibe deutlich bei Kosten und Robustheit. | Nicht explizit benannt, aber die ganze Pipeline ist die Antwort auf „vibe" | |
| Konvergenz | Nils' eigener Befund | Beobachtung aus Nils' Benchmark, kein Fachbegriff: unterschiedliche Modelle/Methoden laufen unabhängig voneinander auf dieselbe grobe Pipeline-Struktur zu — ein Hinweis, dass Plan→Refine→Implement kein Show-Konzept ist, sondern sich technisch aufdrängt. | Guter Beleg für die Pitfalls-/Roadmap-Runde | |
| Non-Determinismus | Allgemein | Modelle liefern bei gleicher Eingabe nicht garantiert dasselbe Ergebnis — Grundbegründung dafür, warum überhaupt ein Harness (Guardrails, Tests, Review) nötig ist statt reinem Vertrauen. | Beiläufig, Grundannahme hinter allen Blöcken | |

## Fehlt noch etwas?

Diese Liste ist mein erster Wurf aus dem, was der Workshop-Plan bisher
berührt — nicht abschließend. Begriffe, die mir zusätzlich noch einfallen, die
aber aktuell in keinem Block explizit vorkommen und die ihr ggf. selbst
mitbringt: **Sandbox/Isolation** (Allgemein), **Observability/Logging für
Agent-Läufe** (Allgemein, DevOps-geliehen), **Model Routing** (Allgemein als
Konzept, bei euch konkret **LightLLM-Gateway** — Tool-spezifisch), **Eval/
Benchmark** (Allgemein — wie misst man, ob eine Änderung am Harness wirklich
besser ist). Wenn im Vorgespräch weitere Begriffe auftauchen, bei
denen ihr merkt „das meinen wir vielleicht nicht gleich" — einfach ergänzen,
das ist der Sinn der Übung.

Praktische Konsequenz aus der Geltungsbereich-Spalte: Alles, was als
**Claude Code** markiert ist, lohnt sich, im Vorgespräch kurz zu checken, ob es
1:1 fürs Team gilt oder ob es einen Cursor-Übersetzungs-Hinweis braucht. Alles
als **Tool** Markierte (aktuell nur „Bean") ist austauschbar — wert, vorab zu
entscheiden, ob `beans` als Lehrbeispiel taugt oder ob ein Barista-näheres
Tool (Jira?) weniger Verwirrung stiftet.
