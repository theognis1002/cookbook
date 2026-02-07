{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/enforce-bun-uv.sh"
          }
        ]
      }
    ]
  }
}
