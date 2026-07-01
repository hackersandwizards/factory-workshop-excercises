# Day 2 PM · Exercise 03 — Implement (Refined Plan → Code on a Branch)

**Slot:** ~60 minutes · Phase 3 of the Factory pipeline

## Goal

Build an `implement` skill that takes a bean's Refined Plan section, creates a feature branch, implements + builds + tests + commits each step individually, and finally writes an Implementation Log into the bean. Never merge, never push.

> **Your sandbox + build commands.** Wherever this README says `../sandbox`, use your language's folder. The build/test gate in Phase 3 differs per language — your `implement` skill must use the row for the sandbox you're in:
>
> | Lang | Sandbox | Build | Test |
> |------|---------|-------|------|
> | C++ | `../sandbox` | `cmake --build build` | `ctest --test-dir build` |
> | Java | `../sandbox-java` | `mvn -q compile` | `mvn -q test` |
> | Python | `../sandbox-python` | _(none)_ | `python3 -m unittest` |
>
> Bean IDs carry your prefix (`sandbox-` / `jsandbox-` / `pysandbox-`); `sandbox-dy91` below is an example.

## Prerequisites

- The sandbox calculator for your language is built and its tests pass green
- The `beans` CLI is installed. The bean from Exercise 02 has a `## Refined Plan` in its body, status `in-progress`.
- Your language toolchain is installed (C++: `cmake`+`ctest` · Java: JDK 21 + Maven · Python: 3.9+)
- `git status` in your sandbox is clean, HEAD is on `main`

## Task

Detailed hints + build checklist + expected bugs: `exercise/HINTS.md`. Skeleton: `exercise/.claude/skills/.gitkeep` — an empty starting point, the skill is built from scratch.

1. Copy `exercise/.claude/` into the sandbox: `cp -r exercise/.claude ../sandbox/`. Then `mkdir ../sandbox/.claude/skills/implement && touch ../sandbox/.claude/skills/implement/SKILL.md`.
2. Frontmatter: `name: implement`, `argument-hint: <bean-id>`, `model: claude-sonnet-4-6`, `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`.
3. Phase 1 (Preflight): parse `beans show --json <bean-id>`, extract the `## Refined Plan`. Check the working tree is clean. Check HEAD == `main`. If not → abort with a clear message.
4. Phase 2 (Branch): generate a slug from the bean's `title` field. Create the branch `feat/<bean-id>-<slug>`. If it already exists → abort.
5. Phase 3 (Loop): per `### Files to change` entry: edit → build → test (use your language's commands from the table above). If red: max 2 fix attempts, then abort. If green: commit with a descriptive message.
6. Phase 4 (Log): `beans update <bean-id> --body-append "..."` with the branch name, a list of commit SHAs + descriptions, and the final test status.
7. Phase 5 (Status): if green → `beans update <bean-id> -s completed` + append `## Summary of Changes`. If red → status stays `in-progress`, append notes.
8. Hard rules: never commit to `main`, never `git push`, never `git merge`. Tests must be green before every commit. Never edit `.beans/*.md` directly.

## Self-Check

- `git branch` in your sandbox shows `feat/<bean-id>-parenthesis-support` (or similar)
- `git log feat/<bean-id>-...` shows several small commits, one per logical step
- `main` is unchanged (`git log main` contains no new commits)
- Tests are green (`ctest --test-dir build` / `mvn -q test` / `python3 -m unittest`)
- `beans show <bean-id>` shows status `completed`, a `## Implementation Log` with branch + commits + status, and a `## Summary of Changes`
- For an artificially broken step (e.g. a deliberately wrong Refined Plan) → the skill stops after 2 attempts, writes `aborted-tests-red` into the log, status stays `in-progress`, and it does not ruin the codebase

## Solution Comparison

After the exercise, compare your skill with `solution/.claude/skills/implement/SKILL.md`. Pay attention to: the preflight guards (clean tree, on main), the 2-attempt limit, the exact Implementation Log schema, and the branch-naming logic. What is worded more defensively than in yours?

## Learning Goals

- Hard constraints in skills: "never X" must be stated clearly, checkably, and unambiguously
- Test-driven implementation loop: build/test/commit per step is a safety pattern
- Fail loud instead of fail silent: a clean abort with state in the log beats "somehow done"
- End-to-end pipeline: Planner → Refine → Implement as a factory that carries a bean from idea to branch — without the main conversation ever seeing the code
