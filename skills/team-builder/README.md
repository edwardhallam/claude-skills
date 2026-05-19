# Team Builder Skill

**Version:** 3.0.0
**Type:** Workflow Skill
**Purpose:** Assemble specialized AI development teams using Claude Code agents

---

## Overview

The team-builder skill helps you create the perfect AI development team for your project. It analyzes your project requirements and assembles a team of specialized agents (backend, frontend, DevOps, testing, etc.) configured for iterative development.

**What it does:**
- Recommends the right agents for your project type
- Creates `.claude/agents/` configuration files
- Provides installation commands for Claude Code plugins
- Sets up an iterative development workflow (MVP → Test → Deploy → Iterate)

**What it does NOT do:**
- Create PRDs or product requirements (your documentation-writer agent does this)
- Write deployment guides or scripts (your DevOps agent handles this)
- Build project artifacts (your development agents do the work)

---

## Key Features

### ✅ Mandatory Test-Driven Development

Every team includes a **test-engineer** agent (no exceptions). This ensures:
- Quality assurance from day one
- Testing at every stage (not just at the end)
- Validation of assumptions
- Automated test suites

### 🔄 Vertical-Slice Iterative Workflow

Teams are configured for modern iterative development:
1. **Build MVP** - Smallest working version of ONE feature
2. **Test Thoroughly** - Validate immediately
3. **Deploy Fast** - Target: Days to production, not weeks
4. **Iterate Continuously** - Build → Test → Deploy → Learn → Repeat

**Vertical Slicing:** Build complete features (UI → API → DB → Tests) one at a time, not horizontal layers (all backend, then all frontend).

### 🎯 Smart Agent Selection

Based on your project description, team-builder recommends:
- **Infrastructure projects:** infrastructure-architect, devops-engineer, test-engineer, documentation-writer
- **Web applications:** fullstack/backend/frontend developers, test-engineer, documentation-writer, code-reviewer
- **Security-critical:** Adds security-engineer
- **Data-heavy:** Adds database-architect

### 📦 Minimal Output

Team-builder creates ONLY the team structure:
- 5-10 files total
- Under 500 lines of configuration
- No over-scaffolding or pre-written artifacts

---

## Installation

### Method 1: Quick Install (Recommended)

```bash
# Download and extract in one command
curl -L https://github.com/edwardhallam/claude-skills/raw/main/skills/team-builder/releases/team-builder-v3.0.0.zip -o /tmp/team-builder.zip && \
unzip /tmp/team-builder.zip -d ~/.claude/skills/ && \
rm /tmp/team-builder.zip
```

### Method 2: Manual Download

1. Download [team-builder-v3.0.0.zip](./releases/team-builder-v3.0.0.zip)
2. Extract to `~/.claude/skills/`:
   ```bash
   unzip team-builder-v3.0.0.zip -d ~/.claude/skills/
   ```

### Method 3: Clone Repository

```bash
# Clone the repository
git clone https://github.com/edwardhallam/claude-skills.git

# Copy to Claude Code skills directory
cp -r claude-skills/skills/team-builder/latest ~/.claude/skills/team-builder
```

### Verify Installation

```bash
# Start Claude Code
claude

# Check available skills
/skills

# You should see "team-builder" in the list
```

---

## Usage

### Basic Usage

1. Start Claude Code in your project directory:
   ```bash
   cd /path/to/your-project
   claude
   ```

2. Invoke the team-builder skill:
   ```
   Use the team-builder skill to create a team for [describe your project]
   ```

### Example Invocations

**Infrastructure Project:**
```
Use team-builder to create a team for monitoring my Proxmox homelab with Prometheus and Grafana
```

**Web Application:**
```
Use team-builder to create a team for a task management SaaS application with React and Node.js
```

**API Development:**
```
Use team-builder to assemble a team for building a RESTful API with authentication and PostgreSQL
```

**Simple Project:**
```
Use team-builder to create a minimal team for a static site generator
```

### What Happens Next

1. **Team-builder asks clarifying questions** (1-3 questions about your project)
2. **Recommends a specialized team** (3-7 agents based on complexity)
3. **Creates configuration files:**
   ```
   your-project/
   └── .claude/
       ├── agents/
       │   ├── [agent-name].md  (for each agent)
       │   └── ...
       ├── commands/
       ├── settings.json
       └── TEAM-SETUP.md
   ```
4. **Provides installation commands** for plugins (AITMPL and Wshobson formats)
5. **Sets up iterative workflow** in TEAM-SETUP.md

---

## Team Composition

### Core Team (Always Included)

Every team MUST include:

1. **test-engineer** - Quality assurance, validation, test automation
2. **documentation-writer** - PRDs, specs, API documentation

These are non-negotiable. If a team doesn't include these, the skill has failed.

### Project-Specific Agents

**Infrastructure Projects:**
- infrastructure-architect (system design, architecture decisions)
- devops-engineer (deployment, CI/CD, containers)
- security-engineer (optional, for security-critical projects)

**Web Development Projects:**
- fullstack-developer (recommended for vertical slicing)
  - OR backend-developer + frontend-developer (if specialized skills needed)
- database-architect (for data-heavy applications)
- code-reviewer (strongly recommended for all dev projects)

**Specialists:**
- researcher (technology evaluation, troubleshooting novel problems)
- security-engineer (security audits, access control)
- quality-engineer (comprehensive QA beyond testing)

### Team Sizes

- **Small projects:** 3-4 agents (core team + 1-2 specialists)
- **Medium projects:** 4-6 agents (core team + multiple specialists)
- **Large/complex projects:** 6-8 agents (core team + full specialist coverage)

---

## Workflow After Setup

### Phase 1: Build MVP (Days, Not Weeks)

```bash
# 1. Start with documentation
documentation-writer, create a lean PRD for the MVP functionality

# 2. Build the minimal working version
[Use your development agents to build ONE core feature]

# 3. Create tests
test-engineer, write tests for the MVP

# 4. Deploy
devops-engineer, help me deploy this to staging
```

**Target:** Get something working in production in DAYS, not weeks.

### Phase 2: Validate & Test

```bash
# 5. Run tests
test-engineer, run all tests and identify any issues

# 6. Review code
code-reviewer, review the MVP code for quality issues

# 7. Fix critical issues only
[Fix blockers, not nice-to-haves]
```

**Focus:** Fix what's broken, don't gold-plate.

### Phase 3: Iterate (Vertical Slices)

```bash
# 8. Plan next feature
Based on usage, what's the next priority feature?

# 9. Build complete feature
[Build ONE feature: UI → API → DB → Tests]

# 10. Deploy immediately
devops-engineer, deploy this feature to production

# 11. Repeat
```

**Key:** Build complete, deployable features one at a time.

---

## Configuration

### Agent Templates

Each agent is defined in a markdown file with YAML frontmatter:

```markdown
---
name: backend-developer
description: Backend API development, database design, and server-side logic. Use for API design, database work, and backend implementation.
model: sonnet
tools: Read, Write, Edit, Bash, Grep, Glob
---

# Backend Developer

You are an expert backend developer specialized in API design...
```

### Customization

After team-builder creates your team, you can:

1. **Edit agent files** in `.claude/agents/` to customize behavior
2. **Add custom commands** in `.claude/commands/`
3. **Modify settings** in `.claude/settings.json`
4. **Add/remove agents** as your project evolves

---

## Examples

### Example 1: Homelab Infrastructure

**Project:** Proxmox monitoring with Prometheus and Grafana

**Team Created:**
- infrastructure-architect
- devops-engineer
- test-engineer ✅
- documentation-writer ✅

**Iteration 1 (Week 1):**
- Build: Basic Prometheus + Grafana in Docker
- Test: Verify containers start and collect metrics
- Deploy: docker-compose up on production server
- Learn: What metrics matter most?

**Iteration 2 (Week 2):**
- Build: Custom dashboards for critical metrics
- Test: Dashboard queries work correctly
- Deploy: Update Grafana configuration
- Learn: What alerts do we need?

[**→ See Full Example**](./examples.md#example-1-homelab-infrastructure)

### Example 2: Web Application

**Project:** Task management SaaS with React and Node.js

**Team Created:**
- fullstack-developer (for vertical slicing)
- backend-developer
- frontend-developer
- test-engineer ✅
- documentation-writer ✅
- code-reviewer
- devops-engineer

**Iteration 1 (Week 1):**
- Build: User auth + basic task CRUD
- Test: Integration tests for auth and CRUD
- Deploy: Staging environment
- Learn: Is the UX intuitive?

**Iteration 2 (Week 2):**
- Build: Due dates feature (UI + API + DB + tests)
- Test: Date handling and validation
- Deploy: Production
- Learn: What's the next priority?

[**→ See Full Example**](./examples.md#example-2-full-stack-web-application)

---

## Troubleshooting

### Issue: Team-builder doesn't appear in `/skills`

**Solution:**
```bash
# Check installation path
ls ~/.claude/skills/team-builder/

# Should contain: SKILL.md and references/

# If not, re-extract the zip to the correct location
unzip team-builder-v3.0.0.zip -d ~/.claude/skills/
```

### Issue: "Skill not found" error

**Solution:**
1. Verify you're in a project directory (not the skills directory itself)
2. Restart Claude Code: `exit` then `claude`
3. Try the full invocation: `Use the team-builder skill to create a team for [project]`

### Issue: Wrong agents recommended

**Solution:**
Team-builder asks 1-3 clarifying questions. Provide specific details:
- **Project type:** Infrastructure vs. web app vs. API
- **Technologies:** Languages, frameworks, databases
- **Complexity:** MVP vs. production-ready vs. enterprise-scale

### Issue: Too many or too few agents

**Solution:**
After team creation, you can:
- **Add agents:** Manually create new `.md` files in `.claude/agents/`
- **Remove agents:** Delete agent files you don't need
- **Modify agents:** Edit existing agent files to change behavior

---

## Best Practices

### 1. Start Small

Begin with a minimal team (3-4 agents) and add specialists as needed.

**Good:** test-engineer + documentation-writer + devops-engineer + infrastructure-architect
**Not Good:** 10 agents with overlapping responsibilities

### 2. Always Include Core Team

Never skip test-engineer or documentation-writer. They're mandatory for a reason.

### 3. Use Vertical Slices

Build complete features (UI → API → DB → Tests) one at a time, not horizontal layers.

**Good:** Iteration 1: User login feature (complete) → Iteration 2: Profile page (complete)
**Not Good:** Iteration 1: All UI → Iteration 2: All API → Iteration 3: Tests

### 4. Deploy Early and Often

Don't wait for perfection. Deploy when it works, even if minimal.

**Target:** First deployment in days (MVP), then weekly or daily iterations.

### 5. Test Continuously

Engage test-engineer at EVERY phase, not just at the end.

- After building MVP: Create basic tests
- After each feature: Add feature tests
- Before each deploy: Run full test suite

---

## Advanced Usage

### Custom Agent Templates

You can add your own agent templates by creating `.md` files in `.claude/agents/`:

```markdown
---
name: ml-engineer
description: Machine learning model development, training, and deployment
model: opus
tools: Read, Write, Edit, Bash, Grep, Glob
---

# ML Engineer

You are an expert machine learning engineer...
```

### Project-Specific Workflows

Customize `TEAM-SETUP.md` after creation to add project-specific guidance:
- Local development setup
- Branch naming conventions
- Code review process
- Deployment procedures

### Integration with CI/CD

The team-builder workflow integrates naturally with CI/CD:
- test-engineer creates automated tests
- devops-engineer sets up CI/CD pipelines
- Tests run on every commit
- Deployments happen automatically when tests pass

---

## FAQ

**Q: Can I use this for non-development projects?**
A: Team-builder is optimized for software development and infrastructure projects. For other domains, you may need to customize the agents significantly.

**Q: Do I need to install plugins manually?**
A: Team-builder provides installation commands, but you run them yourself. This gives you control over what gets installed.

**Q: Can I share my team configuration with others?**
A: Yes! The `.claude/` directory can be committed to git. Others can clone your repo and get the same team setup.

**Q: What if I need an agent that's not in the templates?**
A: Create a custom agent file in `.claude/agents/` following the template format. You can also request additions via GitHub issues.

**Q: How do I update to a newer version?**
A: Download the new version and extract it to `~/.claude/skills/team-builder/`, replacing the old files. Existing project teams won't be affected.

---

## Version Information

**Current Version:** 3.0.0 (October 19, 2025)

**Key Changes in v3:**
- Mandatory test-engineer requirement (no exceptions)
- Vertical-slice iterative development emphasis
- Deploy-fast mentality (days to production)
- Enhanced workflow guidance in TEAM-SETUP.md

[**→ Full Changelog**](./CHANGELOG.md)

---

## Related Documentation

- **[Examples](./examples.md)** - Real-world usage scenarios
- **[Changelog](./CHANGELOG.md)** - Version history and changes

---

## Support

- **Issues:** [GitHub Issues](https://github.com/edwardhallam/claude-skills/issues)
- **Repository:** [claude-skills](https://github.com/edwardhallam/claude-skills)
- **Claude Code Docs:** [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code)

---

## License

MIT License - See [LICENSE](../../LICENSE) for details

---

**Ready to build your team?** [Download Now](./releases/team-builder-v3.0.0.zip) | [See Examples](./examples.md)
