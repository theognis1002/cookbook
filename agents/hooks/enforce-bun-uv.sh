#!/bin/bash

if [ "$CLAUDE_TOOL_NAME" != "Bash" ]; then
  exit 0
fi

command="$CLAUDE_TOOL_INPUT_command"

if echo "$command" | grep -qE '\b(npm|yarn|pnpm)\b'; then
  echo '{"decision":"block","reason":"Use bun instead of npm/yarn/pnpm."}'
  exit 0
fi

if echo "$command" | grep -qE '\b(pip|pip3|python -m pip|python3 -m pip)\b'; then
  echo '{"decision":"block","reason":"Use uv instead of pip/pip3."}'
  exit 0
fi

exit 0
