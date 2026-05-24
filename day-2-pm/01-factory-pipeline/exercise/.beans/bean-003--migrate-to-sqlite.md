---
id: bean-003
title: Migration JSON → SQLite
status: todo
type: refactor
scope: backend
notes: "Data-Flow-Change. Refine sollte Behavioral Contract schreiben (Mynab-Pattern)."
---

# Migration JSON → SQLite

## Description

`data/notes.json` als File-DB skaliert nicht. Migration auf SQLite mit Bun's eingebautem `bun:sqlite`-Modul.

Anforderungen:

1. Neue SQLite-DB `data/notes.db`
2. Schema: `notes(id TEXT PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL, tags TEXT NOT NULL, created_at TEXT NOT NULL)` — `tags` als JSON-Array-String
3. Migration-Script `scripts/migrate-to-sqlite.ts`: liest existierende `notes.json`, schreibt in DB, lässt JSON-Datei als Backup liegen (`notes.json.bak`)
4. `src/server.ts` nutzt SQLite, nicht mehr JSON
5. API-Contract bleibt identisch (Frontend muss nicht angepasst werden)

## Checklist

- [ ] Schema-Datei oder inline-`CREATE TABLE IF NOT EXISTS` in `src/server.ts` Startup
- [ ] Migration-Script existiert und ist idempotent (mehrfach laufen lassen = same state)
- [ ] Alle existierenden IDs bleiben gleich
- [ ] `createdAt` bleibt erhalten (ISO-String)
- [ ] Tags-Roundtrip funktioniert (Array → JSON-String → Array)
- [ ] Health-Endpoint `/health` checkt jetzt DB-Erreichbarkeit
- [ ] `notes.json` wird umbenannt zu `notes.json.bak`, nicht gelöscht
- [ ] Atomare Writes nicht mehr nötig (SQLite-Transaktion ersetzt)

## Definition of Done

- [ ] Migration-Script läuft erfolgreich auf den 3 Seed-Notes
- [ ] Alle API-Endpoints funktionieren weiter (manuelles `curl`-Roundtrip)
- [ ] `notes.json.bak` existiert
- [ ] Linting / Type-Check grün

## Behavioral Contract

(Refine soll das ausfüllen — Behavioral Contract Pattern aus Mynab `~/Sources/mynab/.claude/agents/refine.md` Abschnitt 3.1.)

Erwartete Sub-Sections:
- Data Flow Trace — wo wird gelesen, wo geschrieben, wann Migration
- Field-Level Contracts — Tabellenfelder, Constraints
- Invariants — z.B. "IDs bleiben über Migration stabil"
- Old-to-New Mapping — Felder JSON → SQLite-Spalten
- Verification Scenario — Migration-Script läuft, Endpoints liefern gleichen Output wie vorher

## Open Questions

- Bei jeder Server-Startup `CREATE TABLE IF NOT EXISTS`, oder separate Migration-Step? Entscheide im Refine.
- Was passiert, wenn Migration läuft und User parallel writes macht? (lock? abort?) Entscheide im Refine.
- Bun's `bun:sqlite` API kennen — Refine sollte das prüfen.
