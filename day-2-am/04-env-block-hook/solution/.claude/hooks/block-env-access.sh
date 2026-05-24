#!/usr/bin/env bash
# Block any Bash command that reads .env or .env.* files.
# Reads JSON from stdin (Claude Code passes tool_input as JSON).
# Exit 2 = block the tool call.

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""' 2>/dev/null || echo "")

if echo "$COMMAND" | grep -qE '\.env(\.[a-z]+)?(\s|$|\||;|&|>|<)'; then
  echo "Blocked: command tries to access .env file. Use environment variables or 1Password instead." >&2
  exit 2
fi

exit 0
