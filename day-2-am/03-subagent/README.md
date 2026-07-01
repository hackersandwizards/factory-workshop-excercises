# Day 2 AM · Exercise 03 — Subagent

**Slot:** 10:45–11:30 · 45 minutes

## Concept

A subagent runs in an **isolated context** (its own conversation). It does the heavy lifting (lots of reading, lots of code) and returns only a **summary** to the main run. You save context tokens in the main conversation.

Skill = on-demand Markdown in the current context. Subagent = explicitly delegated to an isolated context.

## Frontmatter — what you can configure

```yaml
---
name: codebase-explorer
description: Use when the user wants to understand where a concept lives in the code
tools: Read, Grep, Glob, Bash
model: claude-sonnet-4-6
---
```

| Field | Purpose |
|------|-------|
| `tools` | Whitelist — the subagent can use only these |
| `model` | Haiku for routine work, Sonnet/Opus for hard problems |
| `description` | Activation key (same as a skill) |

## Goal

A subagent for a recurring workflow from your stack. Define the output contract.

## Suggestions

1. **`codebase-explorer`** — *"find every place where X happens and summarize"*
2. **`test-runner-and-summarizer`** — run `npm test`, parse, short report
3. **`dependency-analyzer`** — read `package.json` plus the lock file, summarize outdated packages and risks
4. **`legacy-code-explainer`** — read an old file, modern commentary (C++/Java legacy)
5. **`pr-diff-summarizer`** — `git diff main...HEAD`, structured summary

## Steps

1. Create `.claude/agents/<your-name>.md`
2. Frontmatter with `name`, `description`, `tools` (whitelist!), `model`
3. Body: role + workflow + output contract + rules
4. Trigger from the main context: `@<name>` or via the Task tool
5. Verify: output under 400 words, summary plus findings, structured

## Verify

- The subagent runs and returns a summary
- The output is more compact than the material it read (context protection!)
- The tools whitelist prevents unwanted side effects

## Stretch

- Model tuning: Haiku vs Sonnet — does it feel different?
- Compose several subagents: `@explorer` → `@summarizer`

## Bridge to the next exercise

Day 2 AM 04 — Hooks: subagents are soft boundaries (prompt-based). Hooks are hard boundaries (shell exit code, unavoidable).

Day 2 PM: what you just built becomes `@refine` — same job, isolated context, the plan lands in a bean.

## Solution

The reference solution lives on branch **`solution/day-2-am-03-subagent`** (kept off
`main` so it stays out of Claude's context) — two subagents under
`solution/.claude/agents/`: `codebase-explorer.md` (read-only discovery) and
`pr-diff-summarizer.md` (structured diff summary). Try it yourself first, then compare:

```bash
git checkout solution/day-2-am-03-subagent   # inspect solution/.claude/agents/…
git checkout main                            # back to your work
git show solution/day-2-am-03-subagent:day-2-am/03-subagent/solution/.claude/agents/codebase-explorer.md
```
