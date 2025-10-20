# Claude Skills

A collection of high-quality skills for [Claude Code](https://claude.com/claude-code) that extend Claude's capabilities for software development and infrastructure management.

## Overview

This repository contains reusable skills that follow Anthropic's skill creation framework. These skills are designed to help developers build better software faster by providing specialized AI agents for different development tasks.

## Available Skills

### [Team Builder](./skills/team-builder/) (v3.0.0) ⭐

**Assembles specialized AI development teams using Claude Code agents.**

The team-builder skill helps you create the perfect AI development team for your project by:
- Identifying the right specialized agents for your needs
- Creating the `.claude/` configuration structure
- Providing ready-to-run installation commands
- Setting up an iterative development workflow

**Best for:**
- Homelab infrastructure projects (Proxmox, Docker, MCP Servers)
- Full-stack web development
- Any project needing multiple specialized AI agents

**Key Features:**
- Mandatory test-driven development (includes test-engineer)
- Vertical-slice iterative workflow (MVP → Deploy → Test → Iterate)
- Deploy-first mentality (days to production, not weeks)
- Smart agent selection based on project type

[**→ Full Documentation**](./skills/team-builder/README.md) | [**→ Download Latest**](./skills/team-builder/releases/team-builder-v3.0.0.zip) | [**→ Examples**](./examples/team-builder-examples.md)

---

## Quick Start

### Installation

**Method 1: Download and Install (Recommended)**

```bash
# Download the latest release
curl -L https://github.com/edwardhallam/claude-skills/raw/main/skills/team-builder/releases/team-builder-v3.0.0.zip -o /tmp/team-builder.zip

# Extract to Claude Code skills directory
unzip /tmp/team-builder.zip -d ~/.claude/skills/

# Clean up
rm /tmp/team-builder.zip
```

**Method 2: Clone Repository**

```bash
# Clone the repository
git clone https://github.com/edwardhallam/claude-skills.git

# Copy the skill to Claude Code
cp -r claude-skills/skills/team-builder/latest ~/.claude/skills/team-builder
```

### Usage

Once installed, use the skill in Claude Code:

```bash
# Start Claude Code
claude

# Use the team-builder skill
Use the team-builder skill to create a team for [describe your project]
```

**Example:**
```
Use the team-builder skill to create a team for a task management web app with React and Node.js
```

Claude will:
1. Ask clarifying questions about your project
2. Recommend a specialized team of 3-7 agents
3. Create the `.claude/agents/` configuration
4. Provide installation commands for plugins
5. Set up an iterative development workflow

---

## Why Use These Skills?

### 🎯 **Focused Expertise**
Each agent specializes in specific domains (backend, DevOps, infrastructure, testing) providing expert-level guidance.

### 🚀 **Faster Development**
Pre-configured workflows and team structures help you start building immediately without planning overhead.

### ✅ **Quality Built-In**
Mandatory test-engineer ensures quality assurance is part of every project from day one.

### 🔄 **Iterative by Design**
Emphasizes vertical slicing and rapid deployment: Build MVP → Test → Deploy → Iterate.

### 📚 **Well-Documented**
Comprehensive guides for installation, usage, and real-world examples.

---

## Documentation

- **[Team Builder Documentation](./skills/team-builder/README.md)** - Complete guide to using the team-builder skill
- **[Usage Examples](./examples/team-builder-examples.md)** - Real-world scenarios and workflows
- **[Iterative Workflow Guide](./docs/iterative-workflow-guide.md)** - Philosophy behind the iterative development approach
- **[Development Updates](./docs/iterative-development-update.md)** - Recent changes to the iterative workflow
- **[Version 3 Changes](./docs/team-builder-v3-changes.md)** - What's new in team-builder v3

---

## Project Structure

```
claude-skills/
├── skills/
│   └── team-builder/          # Team-builder skill
│       ├── latest/            # Current version (browseable)
│       ├── releases/          # Downloadable versions
│       ├── README.md          # Skill documentation
│       └── CHANGELOG.md       # Version history
├── docs/                      # Supporting documentation
├── examples/                  # Usage examples
└── README.md                  # This file
```

---

## Example Projects

### Infrastructure: Proxmox Monitoring

**Input:**
```
Use team-builder to create a team for monitoring my Proxmox homelab with Prometheus and Grafana
```

**Output:** Creates a 4-agent team
- infrastructure-architect (system design)
- devops-engineer (deployment, containers)
- test-engineer (validation, smoke tests)
- documentation-writer (PRDs, runbooks)

**Workflow:** MVP (basic monitoring) → Test → Deploy → Iterate (add dashboards, alerts)

[**→ See Full Example**](./examples/team-builder-examples.md#example-1-homelab-infrastructure)

### Web App: Task Management SaaS

**Input:**
```
Use team-builder to create a team for a task management SaaS application with authentication and real-time updates
```

**Output:** Creates a 6-7 agent team
- fullstack-developer (vertical slices)
- backend-developer (API, database)
- frontend-developer (UI/UX)
- test-engineer (test automation)
- documentation-writer (PRDs, API docs)
- code-reviewer (code quality)
- devops-engineer (deployment)

**Workflow:** MVP (auth + CRUD) → Test → Deploy → Iterate feature-by-feature

[**→ See Full Example**](./examples/team-builder-examples.md#example-2-full-stack-web-application)

---

## Philosophy

These skills follow a modern iterative development philosophy:

```
Build MVP → Deploy Early → Test Continuously → Iterate Based on Real Usage
```

**NOT:** Build everything perfectly → Test at end → Deploy when "ready"

**YES:** Build smallest working version → Test immediately → Deploy FAST → Iterate

### Key Principles

1. **Vertical Slices Over Horizontal Layers**
   - Build complete features (UI → API → DB → Tests) one at a time
   - Each iteration is fully deployable

2. **Test-Driven from Day 1**
   - test-engineer validates at every stage
   - Quality is built-in, not bolted-on

3. **Deploy to Production Quickly**
   - Target: Days to first deployment, not weeks
   - Learn from real usage, not assumptions

4. **Iterate Continuously**
   - Small, frequent deployments
   - Build → Test → Deploy → Learn → Repeat

[**→ Full Workflow Guide**](./docs/iterative-workflow-guide.md)

---

## Requirements

- **Claude Code** - Download from [claude.com/claude-code](https://claude.com/claude-code)
- **Git** (optional) - For cloning the repository
- **curl/wget** (optional) - For downloading releases

---

## Version History

- **v3.0.0** (October 19, 2025) - Mandatory test-engineer + vertical-slice iterative development
- **v2.0.0** (October 17, 2025) - Added test-engineer with always-include tags
- **v1.0.0** (Earlier) - Initial team-builder skill

[**→ Full Changelog**](./skills/team-builder/CHANGELOG.md)

---

## Contributing

This repository is currently maintained by [@edwardhallam](https://github.com/edwardhallam). Contributions, issues, and feature requests are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## Support

- **Issues:** [GitHub Issues](https://github.com/edwardhallam/claude-skills/issues)
- **Documentation:** [Team Builder Docs](./skills/team-builder/README.md)
- **Examples:** [Usage Examples](./examples/team-builder-examples.md)

---

## Acknowledgments

Built following Anthropic's [skill creation framework](https://docs.claude.com/en/docs/claude-code) for Claude Code.

**Philosophy inspired by:**
- Iterative development practices
- Vertical slice architecture
- Test-driven development
- DevOps culture

---

**Ready to build your AI development team?** [Get Started →](./skills/team-builder/README.md)
