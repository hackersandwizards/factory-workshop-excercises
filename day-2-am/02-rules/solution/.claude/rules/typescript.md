---
glob: "**/*.ts"
description: TypeScript code conventions — types stay typed, escapes are documented
---

# TypeScript Conventions

These rules apply to all `.ts` files in this project. When reading, writing, or reviewing TypeScript code, enforce all three conventions below.

## 1. No `any` without `// reason:` comment

`any` defeats the type system. If you must use it, document why on the same line or directly above.

```ts
// ❌ Bad
function process(input: any) { ... }

// ✅ Good — reason inline
function process(input: any) { // reason: external API has no schema, runtime-validated below
  ...
}

// ✅ Good — reason above
// reason: legacy callback boundary, narrowing happens in caller
type Handler = (data: any) => void;
```

When reviewing code: flag every `any` without a `reason:` comment. Suggest concrete typing or, if truly impossible, ask for the reason and add the comment.

## 2. No `// @ts-ignore` or `// @ts-expect-error` without `// reason:`

Type-checker suppressions hide real bugs. Every suppression must explain why it's safe.

```ts
// ❌ Bad
// @ts-ignore
foo.bar.baz;

// ✅ Good
// @ts-ignore reason: typings for X library are wrong upstream, see issue #4521
foo.bar.baz;
```

Prefer `@ts-expect-error` over `@ts-ignore` — it fails the build when the underlying issue is fixed.

## 3. No `console.log` outside test files

Production code uses a dedicated logger. `console.log` is allowed only in:
- Files matching `*.test.ts` or `*.spec.ts`
- Files under `scripts/` (one-off tooling)

```ts
// ❌ Bad (in src/)
console.log("user fetched", user);

// ✅ Good
logger.debug("user fetched", { userId: user.id });
```

When reviewing code: every `console.log` outside test/scripts should be replaced or removed.

## Enforcement style

When you spot a violation:
1. Name the rule (e.g. "Rule violation: `any` without `// reason:`")
2. Show the offending line with file path
3. Suggest the concrete fix
4. Do NOT auto-fix without asking — the developer may have context you don't
