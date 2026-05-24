---
name: refine
description: Refine a bean — generate an Implementation Plan in the bean body. Usage /refine <bean-id>
---

Launch `@refine` for bean `$ARGUMENTS`.

Use the Agent tool:
- `subagent_type: refine`
- `description: "Refine bean $ARGUMENTS"`
- `prompt: "Refine bean $ARGUMENTS. Read .beans/$ARGUMENTS--*.md (use Glob if exact filename unknown), explore codebase, write the Implementation Plan to the bean body."`

After the agent returns:
- Show the file path of the updated bean
- Print "Plan ready. Run `/implement $ARGUMENTS` when reviewed."
