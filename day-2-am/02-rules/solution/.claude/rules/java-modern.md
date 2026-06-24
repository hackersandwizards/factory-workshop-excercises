---
glob: "**/*.java"
---

# Modern Java Conventions

Enforce these when working with Java source.

## Types & Generics

- Always parameterize generics — no raw types (`List<Integer>`, never `List`)
- `var` for local variables where the right-hand side makes the type obvious
- Prefer immutable data: `record` for plain data carriers, `final` fields

## Equality & Null

- `.equals()` for object/string comparison — never `==` on references
- `Objects.equals(a, b)` when either side may be null
- `Optional<T>` for "maybe absent" return values instead of returning `null`

## Collections & Loops

- Enhanced `for (T x : items)` or streams — no C-style index loops when no index is needed
- Factory methods (`List.of(...)`, `Map.of(...)`) for small immutable collections
- No redundant constructors (`new String("x")`, `new Integer(1)`) — use literals / `valueOf`

## Class Design

- Fields `private`; expose behavior, not state — accessors only where needed
- `final` on classes/fields/params that should not change
- Constructor injection over field mutation

## Resources & Errors

- try-with-resources for anything `AutoCloseable`
- Never swallow exceptions silently — catch specific types, not bare `Exception`
