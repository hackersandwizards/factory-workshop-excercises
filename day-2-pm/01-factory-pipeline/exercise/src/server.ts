import { Hono } from 'hono';
import { serveStatic } from 'hono/bun';
import { readFile, writeFile, rename } from 'node:fs/promises';
import { join } from 'node:path';
import { randomUUID } from 'node:crypto';

const NOTES_PATH = join(import.meta.dir, '..', 'data', 'notes.json');

interface Note {
  id: string;
  title: string;
  body: string;
  tags: string[];
  createdAt: string;
}

async function loadNotes(): Promise<Note[]> {
  const raw = await readFile(NOTES_PATH, 'utf8');
  return JSON.parse(raw) as Note[];
}

async function saveNotes(notes: Note[]): Promise<void> {
  const tmp = `${NOTES_PATH}.tmp`;
  await writeFile(tmp, JSON.stringify(notes, null, 2), 'utf8');
  await rename(tmp, NOTES_PATH);
}

const app = new Hono();

app.get('/api/notes', async (c) => {
  const notes = await loadNotes();
  return c.json(notes);
});

app.get('/api/notes/:id', async (c) => {
  const id = c.req.param('id');
  const notes = await loadNotes();
  const note = notes.find((n) => n.id === id);
  if (!note) return c.json({ error: 'not found' }, 404);
  return c.json(note);
});

app.post('/api/notes', async (c) => {
  const body = await c.req.json<{ title: string; body: string; tags?: string[] }>();
  if (!body.title || !body.body) {
    return c.json({ error: 'title and body required' }, 400);
  }
  const note: Note = {
    id: randomUUID(),
    title: body.title,
    body: body.body,
    tags: body.tags ?? [],
    createdAt: new Date().toISOString(),
  };
  const notes = await loadNotes();
  notes.push(note);
  await saveNotes(notes);
  return c.json(note, 201);
});

app.delete('/api/notes/:id', async (c) => {
  const id = c.req.param('id');
  const notes = await loadNotes();
  const next = notes.filter((n) => n.id !== id);
  if (next.length === notes.length) return c.json({ error: 'not found' }, 404);
  await saveNotes(next);
  return c.json({ ok: true });
});

app.get('/health', (c) => c.json({ ok: true }));

app.use('/*', serveStatic({ root: './public' }));

const port = Number(process.env.PORT ?? 3000);

export default {
  port,
  fetch: app.fetch,
};

console.log(`factory-starter listening on http://localhost:${port}`);
