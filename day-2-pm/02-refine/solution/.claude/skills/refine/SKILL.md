---
name: refine
description: Use right before Implement — reads Bean High-Level Plan via beans CLI, explores codebase via subagent fork, appends Refined Plan with concrete files, signatures, test sketch to the bean body.
argument-hint: <bean-id>
allowed-tools: Read Grep Glob Bash Task
---

# Refine (Plan → Refined Plan)

You translate a High-Level Plan into a concrete, file-level Refined Plan. Read-only on source code. Append ONLY to the Bean body via the `beans` CLI.

## When to use

- User invokes `/refine <bean-id>` or says "refine <bean-id>"
- Bean body contains a `## High-Level Plan` section (Planner has run)
- Bean body does NOT yet contain a `## Refined Plan` section

## Workflow

### Phase 1: Read the Bean

- `beans show --json <bean-id>` — parse JSON, extract body
- If body lacks `## High-Level Plan` → abort: "High-Level Plan missing — run /planner first."
- If body already contains `## Refined Plan` → abort: "Refined Plan already present. Remove it manually to re-refine."
- Extract Approach, Steps, Acceptance Criteria, Non-Goals from the body

### Phase 2: Mark in-progress

```bash
beans update <bean-id> -s in-progress
```

### Phase 3: Explore via Subagent (fork)

Dispatch ONE subagent via the Task tool to protect main context. Use `subagent_type=general-purpose`.

Prompt template (fill in `<topic>` from the High-Level Plan, e.g. "parenthesis support", "variable assignment"):

> Read the C++ Calculator source under `./src/` and tests under `./tests/` related to **<topic>**. Specifically:
> 1. List the relevant existing files with their key functions and signatures.
> 2. Identify where new code for <topic> would integrate (which function calls which, which production rule, which test pattern).
> 3. Note line numbers for the integration points.
>
> Return a structured map:
> - **Files** — `path:lines — role`
> - **Functions** — `ReturnType Class::method(Args) — purpose`
> - **Integration points** — `where new code hooks in, with line refs`
> - **Test patterns** — `how existing tests are structured`
>
> READ-ONLY. Do not edit any file. Do not run builds. Just map the territory.

Use the subagent's findings as the sole input for Phase 4. Do not re-explore in main context.

### Phase 4: Append the Refined Plan

```bash
beans update <bean-id> --body-append "$(cat <<'EOF'

## Refined Plan

### Files to change
- \`src/lexer.h:42 — add TOKEN_LPAREN, TOKEN_RPAREN to enum\`
- \`src/lexer.cpp:88 — extend tokenize() to emit paren tokens\`
- \`src/parser.cpp:120 — new parseGroup() called from parseFactor()\`
- \`tests/parser_test.cpp:NEW — parenthesis test cases\`

### New signatures
- \`Token Lexer::lexParen(char c) — emit TOKEN_LPAREN or TOKEN_RPAREN\`
- \`ASTNode* Parser::parseGroup() — consume '(', parse expression, expect ')'\`

### Test sketch
- \`parses_simple_parens\` — input \`(1+2)*3\` → eval result \`9\`
- \`parses_nested_parens\` — input \`((1+2))\` → eval result \`3\`
- \`rejects_unbalanced_open\` — input \`(1+2\` → parse error with "expected ')'"
- \`rejects_unbalanced_close\` — input \`1+2)\` → parse error
- \`regression_no_parens\` — input \`1+2*3\` → eval result \`7\` (unchanged)
EOF
)"
```

Line numbers and file paths come from the subagent's map — do not invent them. The example above is a template; replace contents with the actual map.

### Phase 5: Self-Check

- For each file path in `### Files to change`: verify it exists via Glob or Read. If a path is `NEW`, mark it explicitly with `:NEW`.
- For each signature: confirm the host class exists (Grep for `class ClassName`). If not — fix or abort.
- Confirm no source file was edited: `git status` should show no changes to `src/` or `tests/`.

Report to user: bean updated, file count, ready for `/implement <bean-id>`.

## Rules

- Read-only on source code. ONLY append to the Bean body via `beans update --body-append`. Never Edit/Write `.beans/*.md` directly.
- All file paths in the Refined Plan must be verifiable via Grep or Glob. No fabrications.
- All line numbers come from the subagent's findings, not from guessing.
- No code edits to source files in this Skill. That is the Implementer's job.
- The subagent runs in a fork — its full exploration transcript does NOT pollute main context. Use only its structured findings.
- If the High-Level Plan is missing or empty → abort cleanly. Do not "fill in" what the Planner should have written.
