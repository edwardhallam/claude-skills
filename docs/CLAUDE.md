# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **skill-creation project** focused on maintaining and improving the **team-builder** skill for Claude Code. The project follows Anthropic's skill creation framework to build high-quality, reusable skills that extend Claude's capabilities.

**Primary Goal**: Create and refine the team-builder skill, which assembles specialized AI development teams using Claude Code agents.

## Repository Structure

```
skill-creator/
├── CLAUDE.md                          # This file (previously claude.md - lowercase)
├── ITERATIVE-WORKFLOW-GUIDE.md        # Reference: Iterative development philosophy
├── ITERATIVE-DEVELOPMENT-UPDATE.md    # Reference: Test-driven development updates
├── files.zip                          # Distribution package
└── Skill versions/
    └── team-builderv2.zip            # Latest packaged skill version
```

**Key Files:**
- `ITERATIVE-WORKFLOW-GUIDE.md` - Core philosophy for how team-builder teams should work (MVP → Deploy → Test → Iterate)
- `ITERATIVE-DEVELOPMENT-UPDATE.md` - Documents the shift to test-driven iterative development
- `Skill versions/team-builderv2.zip` - Contains the actual skill:
  - `team-builder/SKILL.md` (~17KB) - Main skill instructions
  - `team-builder/references/plugin-mapping.md` - Maps agent types to installation commands

## Core Philosophy

### The Team-Builder Principle

**❌ Problem**: Skills that over-scaffold (creating PRDs, deployment guides, scripts, documentation)
**✅ Solution**: Team-builder creates ONLY the team structure. The agents do the work.

**Critical Constraint**: Total output must be <500 lines across <10 files

### Iterative Development Workflow

```
Build MVP → Deploy Early → Test Continuously → Iterate Based on Real Usage
```

**Always Include in Teams:**
- `documentation-writer` - Creates lean PRDs and specs
- `test-engineer` - Tests at every stage (added in recent update)

## Working with Skills in This Repository

### Skill Location

The actual team-builder skill files are inside `Skill versions/team-builderv2.zip`:
```bash
# Extract to view/edit
unzip "Skill versions/team-builderv2.zip" -d /tmp/team-builder-work
```

### Skill Structure

```
team-builder/
├── SKILL.md                    # Main instructions (must be <500 lines)
│   ├── YAML frontmatter (name, description)
│   └── Markdown body
└── references/
    └── plugin-mapping.md       # Agent → installation command mapping
```

### Editing the Skill

When modifying the team-builder skill:

1. **Extract the skill**:
   ```bash
   cd "Skill versions"
   unzip -o team-builderv2.zip -d .
   ```

2. **Edit `team-builder/SKILL.md`** or reference files

3. **Validate total line count** (must be <500 lines for SKILL.md):
   ```bash
   wc -l team-builder/SKILL.md
   ```

4. **Repackage the skill**:
   ```bash
   cd team-builder
   zip -r ../team-builderv2-new.zip .
   ```

5. **Replace old version** and update distribution:
   ```bash
   mv ../team-builderv2-new.zip ../team-builderv2.zip
   ```

### Testing Changes

After making changes to the skill:

1. **Read the updated SKILL.md** to verify changes
2. **Check line count** - SKILL.md must stay under 500 lines
3. **Validate constraints**:
   - No instructions to create PRDs, deployment guides, or scripts
   - Emphasizes minimal output (<500 lines total, <10 files)
   - Includes iterative development workflow
   - Always includes test-engineer and documentation-writer

4. **Test conceptually** by asking: "If team-builder used this updated version, would it create only team structure, or would it over-scaffold?"

## Key Learnings from Past Development

### Critical Insight: Minimal Team Setup

**Initial versions** created too much upfront content (17 files, 8000+ lines):
- PRD.md
- deployment-guide.md
- troubleshooting.md
- Scripts and automation
- Architecture documentation

**Final version** creates ONLY team structure (5-10 files, 300-500 lines):
- Agent definitions in `.claude/agents/`
- Installation commands
- Minimal setup guide (TEAM-SETUP.md)

### Design Principles

1. **No Bias** - Don't predetermine what agents should build
2. **Minimal Output** - Under 500 lines total across all files
3. **Clear Constraints** - Explicitly state what NOT to create
4. **Progressive Disclosure** - Create structure first, let agents create artifacts when engaged

## Team-Builder Agent Categories

### Infrastructure Projects
- infrastructure-architect
- devops-engineer
- security-engineer
- documentation-writer (always)
- test-engineer (always)

### Web Development Projects
- backend-developer
- frontend-developer
- fullstack-developer
- database-architect
- quality-engineer
- documentation-writer (always)
- test-engineer (always)
- code-reviewer (recommended)

## Installation Command Formats

The skill generates installation commands in two formats:

### AITMPL Format
```bash
npx claude-code-templates@latest \
  --agent development-team/backend-developer \
  --agent infrastructure/devops-engineer \
  --yes
```

### Wshobson Format
```bash
/plugin marketplace add wshobson/agents
/plugin install backend-development@wshobson-agents
```

Mappings are maintained in `team-builder/references/plugin-mapping.md`

## Common Tasks

### Viewing the Current Skill

```bash
# Extract and read
unzip -o "Skill versions/team-builderv2.zip" -d /tmp
cat /tmp/team-builder/SKILL.md
```

### Updating Agent Definitions

Agent templates are defined in `team-builder/SKILL.md` under the "Agent Template Library" section. To add/modify agents:

1. Extract the skill
2. Edit the agent template in SKILL.md
3. Ensure format follows:
   ```markdown
   ### agent-name

   **Description for Claude**: [When to invoke this agent]

   **Template**:
   ```markdown
   ---
   name: agent-name
   description: [Brief description]
   model: sonnet
   tools: Read, Write, Edit, Bash, Grep, Glob
   ---

   # Agent Name

   [Role and capabilities]
   ```
4. Validate, repackage, test

### Updating Plugin Mappings

Edit `team-builder/references/plugin-mapping.md` to add new plugin mappings or update existing ones.

### Reviewing Iterative Workflow

Reference `ITERATIVE-WORKFLOW-GUIDE.md` for the 3-phase workflow:
1. **Phase 1: MVP** - Build minimum viable product
2. **Phase 2: Validate & Test** - Run tests, identify issues
3. **Phase 3: Iterate** - Fix → Deploy → Learn → Repeat

## Quality Checklist

Before packaging any skill updates:

- [ ] SKILL.md is under 500 lines
- [ ] YAML frontmatter has name and description
- [ ] Description is specific and includes key terms
- [ ] No auxiliary documentation (README, INSTALLATION_GUIDE, etc.)
- [ ] Constraints are explicit (what NOT to create)
- [ ] Includes test-engineer and documentation-writer as required agents
- [ ] Iterative development workflow is emphasized
- [ ] Agent templates follow standard format
- [ ] Plugin mappings are current

## Skill Creation Framework Reference

While this repository focuses on team-builder, it follows general skill-creation principles:

### Context Window Economy
- **Metadata** (name + description): Always loaded (~100 words)
- **SKILL.md body**: Loaded when triggered (<500 lines)
- **Bundled resources**: Loaded as needed by Claude

### Skill Types
- **Workflow skills**: Multi-step procedures (like team-builder)
- **Tool integration skills**: Working with specific formats (PDF, XLSX, etc.)
- **Domain expertise skills**: Company knowledge, schemas, APIs

### Progressive Disclosure
Skills load in three levels:
1. Metadata → Always in context
2. SKILL.md → When skill triggers
3. Resources → As needed

## Development Workflow

When working on skill improvements:

1. **Identify need** - Real project or user feedback
2. **Review current version** - Extract and read SKILL.md
3. **Plan changes** - What needs to be added/removed/changed?
4. **Implement** - Edit skill files
5. **Validate** - Check line count, constraints, format
6. **Package** - Create new zip
7. **Test** - Conceptually validate output would be minimal
8. **Document** - Update reference files if needed

## Important Notes

### File Naming
- The project root previously had `claude.md` (lowercase)
- Standard is `CLAUDE.md` (uppercase) for Claude Code
- Both exist currently - CLAUDE.md is the authoritative version

### Version Control
- This is NOT a git repository (no .git directory)
- Version control is manual via "Skill versions/" directory
- When updating team-builder, create new version or replace existing

### External Dependencies
- Team-builder references external plugin repositories:
  - `npx claude-code-templates@latest` (AITMPL)
  - `wshobson/agents` marketplace
- Plugin mappings must stay current with these sources

## Success Metrics

### Team-Builder Quality
- ✅ Output under 500 lines total
- ✅ Under 10 files created
- ✅ No PRDs/guides/scripts
- ✅ Clear agent descriptions
- ✅ Working installation commands

### Skill Quality
- ✅ SKILL.md under 500 lines
- ✅ Specific description with key terms
- ✅ Tested and validated
- ✅ No auxiliary documentation
- ✅ Follows context window economy principles

## Related Documentation

**In this repository**:
- `ITERATIVE-WORKFLOW-GUIDE.md` - 3-phase iterative development workflow
- `ITERATIVE-DEVELOPMENT-UPDATE.md` - Test-driven development changes

**In skill archives**:
- `team-builder/SKILL.md` - Main skill instructions
- `team-builder/references/plugin-mapping.md` - Agent installation mappings

**External**:
- Claude Code Documentation: https://docs.claude.com/en/docs/claude-code
- Anthropic API Docs: https://docs.anthropic.com
