#!/usr/bin/env bash
# Block any tool call that touches .env or .env.* files.
# Reads JSON from stdin (Claude Code passes tool_name + tool_input).
# Exit 2 = block.

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name // ""')

is_env_basename() {
  local base
  base=$(basename "$1")
  [[ "$base" =~ ^\.env(\..+)?$ ]]
}

case "$TOOL" in
  Bash)
    CMD=$(echo "$INPUT" | jq -r '.tool_input.command // ""')
    # Match .env / .env.<ext> as a token (handles spaces, quotes, globs, pipes, redirects).
    if echo "$CMD" | grep -qE '(^|[[:space:]/"'\''=])\.env(\.[a-zA-Z0-9_-]+)?($|[[:space:]"'\''|;&><*?\)])'; then
      echo "Blocked: Bash command touches .env file. Use environment variables or 1Password." >&2
      exit 2
    fi
    ;;
  Read|Edit|Write|NotebookEdit)
    P=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.notebook_path // ""')
    if [ -n "$P" ] && is_env_basename "$P"; then
      echo "Blocked: $TOOL on .env file ($P). Use environment variables or 1Password." >&2
      exit 2
    fi
    ;;
  Glob)
    PAT=$(echo "$INPUT" | jq -r '.tool_input.pattern // ""')
    if echo "$PAT" | grep -qE '\.env(\.|$|\*)'; then
      echo "Blocked: Glob pattern targets .env files ($PAT)." >&2
      exit 2
    fi
    ;;
  Grep)
    P=$(echo "$INPUT" | jq -r '.tool_input.path // ""')
    G=$(echo "$INPUT" | jq -r '.tool_input.glob // ""')
    if echo "$P $G" | grep -qE '\.env(\.|$|\*|[[:space:]])'; then
      echo "Blocked: Grep targets .env files." >&2
      exit 2
    fi
    ;;
esac

exit 0
