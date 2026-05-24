---
id: bean-001
title: PATCH-Endpoint für Note-Update
status: todo
type: feature
scope: backend
---

# PATCH-Endpoint für Note-Update

## Description

Aktuell kann man Notes erstellen (POST), löschen (DELETE) und auslesen (GET / GET-by-id). Was fehlt: Notes editieren ohne komplett zu löschen und neu zu erstellen.

Endpoint `PATCH /api/notes/:id` soll partielles Update unterstützen — `title`, `body`, `tags` jeweils einzeln oder kombiniert. Felder, die nicht im Request-Body kommen, bleiben unverändert. `id` und `createdAt` sind unveränderlich.

## Checklist

- [ ] `PATCH /api/notes/:id` Route in `src/server.ts`
- [ ] Validierung: mindestens ein Feld muss im Body sein (sonst 400)
- [ ] 404 wenn Note-ID nicht existiert
- [ ] Frontend-Edit-UI **NICHT** Teil dieser Bean — nur Backend
- [ ] `data/notes.json` atomar geschrieben (Pattern wie bei DELETE / POST)

## Definition of Done

- [ ] Backend-Endpoint funktioniert (manuell mit `curl` verifiziert)
- [ ] Existierende POST/DELETE/GET-Tests laufen weiter (falls Tests existieren — falls nicht, manuell verifiziert)
- [ ] Linting / Type-Check grün
- [ ] PR-Branch gepushed

## Manual Verify

```bash
# Note erstellen
curl -X POST http://localhost:3000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","body":"Original","tags":["a"]}'
# → speichere ID

# Nur Body updaten
curl -X PATCH http://localhost:3000/api/notes/<ID> \
  -H "Content-Type: application/json" \
  -d '{"body":"Updated"}'
# → title und tags bleiben, body ist neu

# Nur Tags updaten
curl -X PATCH http://localhost:3000/api/notes/<ID> \
  -H "Content-Type: application/json" \
  -d '{"tags":["x","y"]}'
# → title und body bleiben

# Leerer Body
curl -X PATCH http://localhost:3000/api/notes/<ID> \
  -H "Content-Type: application/json" -d '{}'
# → 400

# Unbekannte ID
curl -X PATCH http://localhost:3000/api/notes/no-such-id \
  -H "Content-Type: application/json" -d '{"title":"x"}'
# → 404
```
