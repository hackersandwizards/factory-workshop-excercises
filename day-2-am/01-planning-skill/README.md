# Day 2 AM · Exercise 01 — Planning Skill

**Slot:** 09:00–10:10 · 70 minutes

## Goal

Build your own planning skill that implements a **4-mechanic subset** of `obra/superpowers/brainstorming`. The output is a **Markdown plan file** at `.plans/<task>.md` — the bean-file form that recurs throughout the PM Factory.

## Teaching pattern: Demo → Deconstruct → Reconstruct

| Phase | What | Duration |
|-------|-----|-------|
| Demo | Trainer walks through the `obra/superpowers/brainstorming` SKILL.md on GitHub | 10min |
| Deconstruct | Group discussion: what do we see? Extract the 8 mechanics | 10min |
| Reconstruct | Your own planning skill with `/skill-creator`, 4★ subset | 25min |
| Share-out | Check the description and file output with your neighbor | 5min |

The rest is buffer plus the transition into Rules.

## Reference skill

`https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md`

**Inspiration, not a template.** Build your own tailored suit.

## The 8 mechanics

| Mechanic | What it does | |
|----------|----------------|---|
| **Explore project context** | Recon before asking — no blind plan | ★ |
| **One question per message** | Explicit decision points | ★ |
| **2-3 alternatives before converging** | Force the trade-off | ★ |
| **Self-review (guardrail)** | Check before finalizing the plan | ★ |
| Spec → file, not conversation | The file is the contract | |
| Hard approval gate | Plan and execute kept separate | |
| Explicit constraints / non-goals | Prevent scope creep | |
| Repeatable routine | Process > inspiration | |

★ = mandatory subset for the exercise. See the rest now, add them later.

Build checklist: [`exercise/HINTS.md`](exercise/HINTS.md).

## Steps (Reconstruct)

1. Choose a general planner or a planner for a specific planning domain from your own stack:
   - `refactor-planner`, `migration-planner`, `test-coverage-planner`, `feature-planner`
2. Start `/skill-creator` — an interview flow through frontmatter plus body
3. `name` + `description` (the description is the activation key)
4. Workflow body with the **mandatory 4★ subset**: Explore context · One question per message · 2-3 approaches · Self-review
5. Output path: the skill writes the plan to `.plans/<task>.md`
6. Test: enter the trigger phrase → does the skill activate? → does it actually write the `.md` file?

## Verify

- The description triggers for the right tasks, not for the wrong ones
- A neighbor reads the description and understands when to trigger it
- The 4★ mechanics are recognizable in the workflow
- The output lands as a file in `.plans/`, not just in the conversation

## Stretch

- Add the remaining 4 mechanics (approval gate, constraints, etc.)
- Test the skill with several trigger phrases and tune the activation
- Define your own subagent type via `.claude/agents/<name>.md` and reference it in the skill via `agent:`

## Bridge to PM

A Markdown file in `.plans/` = **the bean-file form**. The PM Factory uses file-as-contract between agents — the planning skill is the first step toward a multi-agent pipeline.

## Solution

A generic reference skill in `solution/`:
- [`planner/SKILL.md`](solution/.claude/skills/planner/SKILL.md) — domain-agnostic, 4★ subset plus an externalize phase

Build it yourself first. Then compare how the subset is mapped out.
