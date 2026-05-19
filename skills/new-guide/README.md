# New Guide Skill

**Version:** 1.0.0
**Purpose:** Scaffold deployment guides and runbooks with appropriate complexity

---

## Overview

The new-guide skill creates structured documentation that adapts to your needs:

- **Simple guides** (single file) - For focused procedures under ~15 steps
- **Complex guides** (multi-file) - For deployments with multiple phases, backups, monitoring

The skill researches existing patterns in your workspace before creating anything.

## Installation

```bash
# Clone repo and copy skill
git clone https://github.com/edwardhallam/claude-skills.git /tmp/claude-skills && \
cp -r /tmp/claude-skills/skills/new-guide/latest ~/.claude/skills/new-guide && \
rm -rf /tmp/claude-skills
```

## Usage

```
Create a deployment guide for [AppName]
```

```
Scaffold a guide for setting up Prometheus monitoring
```

```
New guide for configuring Cloudflare Tunnel
```

## Output Formats

### Simple Format

Single file for focused procedures:

```
docs/[topic]/[guide-title].md
```

### Complex Format

Multi-file structure for full deployments:

```
docs/[platform]/[app-name]/
├── STATUS.md              ← Operational dashboard
└── Guide/
    ├── 1. Overview.md
    ├── 2. Deploy Application.md
    ├── 3. Configure Backups.md
    └── 4. Post-Deployment.md
```

## How It Works

1. **Research** - Searches for related guides in your workspace
2. **Assess** - Determines simple vs complex format based on scope
3. **Locate** - Chooses output directory based on purpose
4. **Create** - Scaffolds files using workspace conventions
5. **Verify** - Flags if existing guides may need updates

## Conventions

All generated guides follow these standards:

- `- [ ]` checkboxes for actionable steps
- Code blocks with language specifiers
- Verification steps after major operations
- Obsidian callouts (`> [!important]`, `> [!warning]`)

## Templates

See [latest/references/templates.md](./latest/references/templates.md) for the full template library.

---

## License

MIT License - See [LICENSE](../../LICENSE) for details.
