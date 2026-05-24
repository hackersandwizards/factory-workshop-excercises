---
id: bean-002
title: Tag-Filter UI + Backend
status: todo
type: feature
scope: fullstack
---

# Tag-Filter UI + Backend

## Description

User soll Notes nach Tags filtern können. Backend: `GET /api/notes` akzeptiert `?tag=foo` Query-Param. Frontend: Dropdown mit allen Tags der vorhandenen Notes plus "Alle". Auswahl filtert die angezeigten Notes.

## Checklist

### Backend

- [ ] `GET /api/notes` akzeptiert `?tag=<tag>` Query-Parameter
- [ ] Mehrere Tags: `?tag=foo&tag=bar` (AND-Logik — Note muss beide haben) ODER `?tag=foo,bar` (OR-Logik). Entscheide und dokumentiere.
- [ ] Ohne Query: alle Notes wie bisher
- [ ] Unbekannte Tags: leere Liste, kein 404

### Frontend

- [ ] Dropdown über Note-Liste, zeigt alle einzigartigen Tags der Notes plus "Alle"
- [ ] Auswahl ruft `loadNotes()` mit Filter neu
- [ ] "Alle" oder leer = kein Filter
- [ ] Tag-Liste aktualisiert sich, wenn Note hinzugefügt oder gelöscht wird

## Definition of Done

- [ ] Backend-Endpoint funktioniert mit `curl ?tag=workshop`
- [ ] Frontend zeigt Dropdown, Filter funktioniert
- [ ] Bestehende POST/DELETE-Funktionen laufen weiter
- [ ] Linting / Type-Check grün

## Open Questions

- Tag-Logik: AND oder OR bei mehreren Tags? Entscheide im Refine.
- Sortierung des Dropdowns: alphabetisch? Nach Häufigkeit? Entscheide im Refine.
