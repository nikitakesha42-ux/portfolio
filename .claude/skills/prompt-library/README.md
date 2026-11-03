# Prompt Library — Claude Code skills

Generated from `assets/prompts.json` by `scripts/build-skills.py`.

## Install

Symlink (recommended — edits to the JSON flow through automatically after a rebuild):

```bash
ln -s "$(pwd)/.claude/skills/prompt-library" ~/.claude/skills/prompt-library
```

Or copy a snapshot:

```bash
mkdir -p ~/.claude/skills && cp -R .claude/skills/prompt-library ~/.claude/skills/
```

## Use

In Claude Code, invoke a phase with its slash command:

- `/ux-research` — UX Research (12 prompts)
- `/writing` — Writing (4 prompts)
- `/design-systems` — Design Systems (4 prompts)
- `/prototyping` — Prototyping (6 prompts)
- `/design-engineering` — Design Engineering (7 prompts)

Pick a phase, Claude asks where you are, then runs the matching RTCCF prompt file.

## Rebuild

```bash
python3 scripts/build-skills.py --clean   # fresh rebuild from prompts.json
```