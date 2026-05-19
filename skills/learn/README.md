# Learn Skill

**Version:** 1.0.0
**Purpose:** Route new knowledge to the appropriate memory file in your workspace

---

## Overview

The learn skill teaches Claude new preferences, patterns, and rules by intelligently routing them to the right location in your workspace's memory architecture:

- **Tool preferences** → `tool-standards.md`
- **Claude behaviors** → `CLAUDE.md`
- **DevOps context** → `.claude/rules/devops-context.md`
- **Best practices** → `best-practices.md`
- **Path-specific rules** → `.claude/rules/[topic].md`

## Installation

```bash
# Clone repo and copy skill
git clone https://github.com/edwardhallam/claude-skills.git /tmp/claude-skills && \
cp -r /tmp/claude-skills/skills/learn/latest ~/.claude/skills/learn && \
rm -rf /tmp/claude-skills
```

## Usage

### Add a preference (default)

```
Remember that we prefer TypeScript over JavaScript
```

```
Use bun instead of npm for all new projects
```

```
We have a new VM called Analytics running Grafana
```

### Update an existing preference

```
TypeScript is now required, not just preferred
```

### Remove a preference

```
Remove the rule about pnpm
```

## How It Works

1. **Parse** - Identifies the operation (add/update/remove) and category
2. **Categorize** - Determines destination file based on keywords
3. **Preview** - Shows exactly what will change before applying
4. **Apply** - Makes the edit after user confirmation
5. **Review** - Checks architecture health (file sizes, patterns)

## Example Session

**User:** "Always ask before deleting files"

**Claude:**
```
📍 File: CLAUDE.md
📍 Section: Claude Responsibilities

I'll add:

+ - **Ask before deleting** - Always confirm before removing files

Confirm? (yes/no)
```

**User:** "yes"

**Claude:**
```
✓ Learned! Added deletion confirmation rule to CLAUDE.md
```

## Memory Architecture

The skill works with this standard structure:

```
workspace/
├── CLAUDE.md                    # Claude behavioral instructions
├── DevOps/
│   ├── best-practices.md        # Operational standards
│   └── tool-standards.md        # Preferred tools
└── .claude/
    └── rules/
        ├── devops-context.md    # Infrastructure context
        └── [topic].md           # Path-specific rules
```

---

## License

MIT License - See [LICENSE](../../LICENSE) for details.
