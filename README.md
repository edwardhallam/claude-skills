# Claude Skills

A public collection of skills for Claude Code.

## Operations Baseline

| Field | Value |
| --- | --- |
| Repo type | `public-skill-pack` |
| Template baseline | `public-skill-pack-v1` |
| Runtime | Local Claude Code skill installation |
| Deploy path | None; pushes run validation only |
| CI check | `validate` |
| Failure notification | `CI Failure Email` via Resend to `edwardhallam@fastmail.com` |
| Renovate | Extends `edwardhallam/renovate-config`; Dependency Dashboard issue #1 |
| Visibility | Public; no private agent files or internal runbook links |

## Available Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [team-builder](./skills/team-builder/) | Assembles specialized AI development teams using Claude Code agents | [→ Install](#team-builder) |
| [learn](./skills/learn/) | Basic Claude Code Memory Management | [→ Install](#learn) |
| [new-guide](./skills/new-guide/) | Obsidian-friendly guide/runbook creation | [→ Install](#new-guide) |

---

## Installation

### team-builder

Assembles specialized AI development teams for your projects.

```bash
# Download and install
curl -L https://github.com/edwardhallam/claude-skills/raw/main/skills/team-builder/releases/team-builder-v3.0.0.zip -o /tmp/team-builder.zip && \
unzip /tmp/team-builder.zip -d ~/.claude/skills/ && \
rm /tmp/team-builder.zip
```

**Usage:**
```
Use team-builder to create a team for [describe your project]
```

[Full documentation →](./skills/team-builder/README.md)

---

### learn

A modular memory system designed for Claude Code with a DevOps/Dev/Obsidian Knowledge Base focus.

```bash
# Clone repo and copy skill
git clone https://github.com/edwardhallam/claude-skills.git /tmp/claude-skills && \
cp -r /tmp/claude-skills/skills/learn/latest ~/.claude/skills/learn && \
rm -rf /tmp/claude-skills
```

**Usage:**
```
Remember that we prefer TypeScript over JavaScript
```

[Full documentation →](./skills/learn/README.md)

---

### new-guide

Scaffolds Obsidian-friendly development/deployment guides and runbooks

```bash
# Clone repo and copy skill
git clone https://github.com/edwardhallam/claude-skills.git /tmp/claude-skills && \
cp -r /tmp/claude-skills/skills/new-guide/latest ~/.claude/skills/new-guide && \
rm -rf /tmp/claude-skills
```

**Usage:**
```
Create a deployment guide for [AppName]
```

[Full documentation →](./skills/new-guide/README.md)

---

## Verify Installation

```bash
# Start Claude Code
claude

# Check available skills
/skills

# You should see your installed skills listed
```

## Development

```bash
scripts/verify.sh
```

The verifier checks skill metadata, local markdown links, release archives, and
public-repo hygiene.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
