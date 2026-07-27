# Live-Demo: Rabatt-Code beim Checkout (Block 5, Stufe 2)

Trainer-Material für Nils — kein Teilnehmer-Exercise, kein Solution-Branch,
kein CLAUDE.md mit Guardrails. Das ist Absicht: die Demo soll zeigen, was
ohne Planner und ohne Checkpoint passiert.

Ziel: dem Team live vorführen, dass ein Agent bei einer architektonisch
relevanten Aufgabe echte Entscheidungen trifft, die eigentlich dem Team
gehört hätten — nicht nur, dass er Code schreibt.

## Setup

Zwei kleine, unabhängige Services:

- `services/cart-service/` — Warenkorb + Checkout, berechnet aktuell nur
  die reine Artikelsumme.
- `services/pricing-service/` — Rabatt-Regeln + Gutschein-Validierung,
  funktioniert eigenständig, ist aber nicht mit dem Cart-Service verbunden.

Beide bewusst minimal (reines Python, keine echten HTTP-Server) — es geht
um die Architekturentscheidung, nicht um Infrastruktur-Ceremony.

## Live-Demo-Ablauf

1. Beide Services kurz zeigen (README + Code), 2–3 Minuten. Team soll
   verstehen: zwei getrennte, funktionierende Bausteine, keine Verbindung.
2. Agent live, komplett autonom, ohne Planner, ohne Checkpoint, folgenden
   Auftrag geben (wörtlich oder sinngemäß):

   > "Beim Checkout im Cart-Service sollen Rabatt-Codes berücksichtigt
   > werden können. Der Pricing-Service verwaltet die Rabatt-Regeln
   > bereits. Bau das komplett durch, End-to-End."

3. Laufen lassen, nicht eingreifen — auch wenn er Zwischenfragen stellt
   oder Annahmen trifft, kommentarlos zusehen.
4. Ergebnis gemeinsam auswerten (siehe Entscheidungspunkte unten).

## Entscheidungspunkte, auf die zu achten ist (nicht vorab zeigen)

Der Agent MUSS hier etwas entscheiden, es gibt keinen neutralen Default:

- **Kopplungsart:** ruft Cart-Service den Pricing-Service synchron auf
  (direkter Funktionsaufruf/Import, da beides im selben Repo liegt) — oder
  baut er eine sauberere Grenze (z. B. ein Interface/Protokoll), die auch
  über einen echten Netzwerk-Call hinweg funktionieren würde?
- **Source of Truth:** wo landet die eigentliche Rabatt-Validierung —
  bleibt sie im Pricing-Service, oder dupliziert der Agent Teile der Logik
  in den Cart-Service (z. B. weil das "einfacher" ist)?
- **Fehlerfall:** was passiert, wenn der Code ungültig ist oder
  `validate_coupon` `None` zurückgibt — bricht der Checkout ab, läuft er
  ohne Rabatt weiter, oder wirft der Agent eine Exception, die noch gar
  nicht vorgesehen war?
- **Vertrag/Schnittstelle:** übernimmt der Cart-Service das
  `DiscountRule`-Objekt direkt (enge Kopplung an die interne Struktur des
  Pricing-Service) oder definiert er sich einen eigenen, schmaleren
  Vertrag?
- **Testabdeckung:** schreibt der Agent Tests nur für den Erfolgsfall,
  oder auch für ungültige/abgelaufene Codes? Zeigt, wie viel er selbst als
  "fertig" definiert, ohne dass das Team das vorgegeben hat.

## Auswertung mit dem Team (Mechanismus, Block 5)

Nach dem Lauf: jede:r im Raum benennt eine Stelle, an der sie/er anders
entschieden hätte. Nicht bewerten, ob der Agent "gut" oder "schlecht"
entschieden hat — der Punkt ist, DASS entschieden wurde, ohne dass das
Team gefragt wurde. Block endet bewusst vor der Auflösung (siehe Agenda,
Block 6 Twist).

## Fallback

Falls der Agent unerwartet "sauber" entscheidet (z. B. weil er zufällig
das im Team bevorzugte Pattern trifft) und keine kontroverse Entscheidung
sichtbar wird: nachfragen, WARUM er sich so entschieden hat — meistens
zeigt die Begründung trotzdem eine unausgesprochene Annahme (z. B. "ich
habe angenommen, dass beide Services im selben Prozess laufen").
