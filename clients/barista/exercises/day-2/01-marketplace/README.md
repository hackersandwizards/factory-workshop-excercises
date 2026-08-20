# Day 2 · Exercise 01 — Marketplace: the auto-update proof

**Slot:** Block 2, 10:00–10:50 · **Trainer-led live demo, not a participant
exercise.** Purpose: run through this skeleton yourself beforehand
(rehearsal), then demo it live on Friday.

## Why this exercise exists

The team built their own MCP server as a marketplace replacement — on the
assumption that a plugin marketplace offers no auto-update. That's wrong.
This skeleton is the deterministic, live-demoable proof of the opposite,
without depending on the random background timer.

## Concept

Two different auto-update defaults probably explain the misunderstanding:

- **Official Anthropic marketplaces:** auto-update **on** by default.
- **Third-party or local/self-built marketplaces** (like the one in this
  skeleton): auto-update **off** by default — toggle under `/plugin` →
  Marketplaces → "Enable auto-update".

Anyone who only ever experimented with their own/local marketplace and
never flipped that toggle would never see an auto-update happen on its own
— and could easily conclude "the feature doesn't exist" instead of "my
default is off". That's most likely what happened to the team.

**That's why this exercise deliberately does not show the automatic
background path** (up to a 10-minute random delay — unusable for a live
demo), but the **manual, deterministic** path instead, which always works
immediately regardless of the toggle.

## The skeleton

```
exercise/demo-marketplace/
├── .claude-plugin/
│   └── marketplace.json                              ← marketplace manifest
└── plugins/
    └── commit-convention/
        ├── .claude-plugin/
        │   └── plugin.json                            ← plugin manifest
        └── skills/
            └── commit-convention/
                └── SKILL.md                            ← Day 1 example, reused
```

Deliberately not a toy example: the plugin distributes exactly the
commit-message convention (Type/Scope/Body/Ref) the team already built
themselves on Day 1 (`exercises/day-1/01-commit-skill/`, purpose variant)
— recognition value instead of a new example.

## Walkthrough (for rehearsing and for the live demo)

1. **Show the baseline.** In the target repo (or an empty test folder):
   ```bash
   /plugin marketplace add ./exercise/demo-marketplace
   /plugin install commit-convention@barista-demo-marketplace
   ```
   Briefly show the skill is now there (`/plugin` → Installed).

2. **Demonstrate the before-state.** Ask Claude Code for a commit message
   for some diff — shows the current `SKILL.md` wording in action.

3. **Change the source.** In
   `exercise/demo-marketplace/plugins/commit-convention/skills/commit-convention/SKILL.md`,
   change something visible (e.g. extend the `description` line or reword
   the body hint), and **bump the version in `plugin.json`**
   (`1.0.0` → `1.0.1`) — without a version bump the effect can look
   ambiguous; with one it's unambiguous.

4. **Forced refresh, no waiting:**
   ```bash
   /plugin marketplace update barista-demo-marketplace
   /reload-plugins
   ```
   `/reload-plugins` can invalidate the prompt cache for plugins that ship
   MCP servers (warning, `--force` if needed) — not relevant for this pure
   skill plugin, but worth having mentioned once.

5. **Show the after-state.** Ask for a commit message again — the change is
   there, without anyone touching the skill file in the target repo by
   hand.

## Verify (run through this completely before Friday)

- [ ] `/plugin marketplace add ./exercise/demo-marketplace` runs without error
- [ ] `/plugin install commit-convention@barista-demo-marketplace` installs visibly
- [ ] Skill is usable (a commit-message request shows the Day 1 convention)
- [ ] Change to `SKILL.md` + version bump in `plugin.json`
- [ ] `/plugin marketplace update barista-demo-marketplace` + `/reload-plugins` show the change — **without waiting for the background timer**
- [ ] `/plugin` → Marketplaces tab shows the auto-update toggle (off by default, since it's a local marketplace) — see this once deliberately before it's a live surprise

## Edge cases, ready to answer live

- **Version constraints:** a plugin can declare a dependency on another
  plugin via a semver range (`~2.1.0`). Auto-update fetches the highest
  version *within* the range, not necessarily the latest — prevents a
  dependency from silently breaking.
- **Session isolation:** an already-running session stays on the state from
  session start until `/reload-plugins` or a restart — no update pulls the
  rug out mid-work.
- **No version field set?** Claude Code falls back to the git commit SHA as
  the version for auto-update purposes.
- **Cross-marketplace dependencies:** locked by default (security
  boundary), must be explicitly allowed in `marketplace.json`.
- **Offline machine:** no permanent drift — the next online check just
  catches up automatically.
- **Errors surface visibly** in the `/plugin` "Errors" tab, not hidden in a
  log — no silent breakage.
- **Name conflict — corrected, verify before repeating the old claim:**
  marketplace skills are **always namespaced** (`/plugin-name:skill-name`),
  local skills stay unnamespaced (`/skill-name`) — a same-named local skill
  and marketplace skill **coexist without collision**, by design. (What
  *can* silently shadow, per a GitHub issue rather than official docs: a
  plugin skill overriding a **built-in** slash command of the same name —
  a different scenario, treat with appropriate caution if it comes up.)
  This is the twist at the end of Block 2 — the collision fear is unfounded.

## Bridge

The same mechanism carries the rest of the day: Refine, Implement, and
Review (Block 4–5) get built this afternoon in a way that could later be
distributed through this same marketplace skeleton — as of today, the
difference between "built once in your own repo" and "usable by the whole
team" is just a `marketplace.json` entry.

## Solution

No solution branch — this skeleton *is* already the finished, working
version. No solution-lockdown `CLAUDE.md` in this folder, because there's
nothing to hide here: this is trainer rehearsal material, not a participant
puzzle.
