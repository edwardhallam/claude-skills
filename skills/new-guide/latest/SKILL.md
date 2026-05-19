---
name: new-guide
description: Scaffolds guides and runbooks. Use when user asks to create a deployment guide, how-to guide, setup documentation, or runbook. Automatically determines appropriate format (simple single-file or complex multi-file) based on scope.
---

# Guide Scaffolding Skill

This skill creates structured guides, adapting format to match complexity.

## When to Use

Trigger when user says things like:
- "Create a guide for X"
- "Scaffold a deployment guide for X"
- "New guide for [AppName]"
- "Create documentation for setting up X"
- "Write a how-to for X"

## Execution Strategy

This skill adapts to available tooling. Check for subagents before starting:

```
1. Check .claude/agents/ directory (or run /agents) for available subagents
2. Identify agents matching needed capabilities
3. Delegate to agents when available, otherwise execute inline
```

### Capability Matching

| Phase | Capability Needed | Agent Characteristics | Fallback |
|-------|-------------------|----------------------|----------|
| Research | Read-only codebase analysis | `disallowedTools` includes Write/Edit; description mentions "research", "patterns", or "existing" | Inline Glob, Grep, Read |
| Vendor verification | Web search and fetch | Tools include WebSearch, WebFetch | Inline WebSearch, WebFetch |
| Writing | Documentation creation | Tools include Write, Edit; description mentions "documentation", "guides", or "writing" | Inline Write tool |

### Delegation Benefits

When suitable agents exist:
- **Isolated context** - Research doesn't consume main conversation tokens
- **Specialized prompts** - Agents have domain-specific instructions
- **Parallel execution** - Multiple research tasks can run simultaneously

### No Agents Available

If no subagents match needed capabilities, execute all phases inline using standard tools. This skill is fully functional without subagents.

## Step 0: Research Existing Patterns

**Before creating any files**, research existing guides and verify technical content.

### Delegation Check

Per the Execution Strategy above:
1. Check for a **read-only research agent** (description mentions "research", "patterns", or "existing"; has `disallowedTools: Write, Edit`)
2. If found → delegate research tasks to that agent
3. If not found → execute research inline as described below

### Research Tasks (inline or delegated)

1. **Search for related guides:**
   - Use Glob/Grep to find guides for similar services (e.g., if creating a Mailgun guide, search for existing Mailgun configurations)
   - Check the workspace's docs, runbooks, and operations folders for relevant
     patterns
   - Look for guides that configure the same tools or services

2. **What to learn from existing guides:**

   | Copy from existing guides | Verify independently |
   |---------------------------|---------------------|
   | Format and structure | Current vendor UI paths |
   | Callout style and placement | Latest best practices |
   | Checkbox granularity | New features or options |
   | Verification patterns | Security recommendations |
   | Section ordering | Deprecated settings |
   | Lessons learned / gotchas | - |

3. **When to deviate from existing guides:**
   - Vendor has released new recommended approach
   - Existing guide has a known issue or workaround that's been fixed
   - New guide covers a different use case requiring different steps
   - Security best practices have evolved

   When deviating, flag potential updates to the reference guide for user review.

4. **Web service accuracy:**
   - Web service UIs change frequently; existing guides represent "last known working" configuration
   - Always include verification steps so users can confirm they're in the right place
   - If UI paths have changed significantly, flag potential reference guide updates for user review

**Reference guide discovery by topic:**
| Topic | Search For | Use for |
|-------|------------|---------|
| Best practices | `best-practices`, `standards`, `policy` | Policies, patterns, standards to follow |
| Secrets management | `.env.example`, `secrets`, `key rotation` | Environment file pattern, key rotation |
| DNS and tunnels | `dns`, `tunnel`, `reverse proxy` | DNS record format, ingress, verification flow |
| Email delivery | `smtp`, `mail`, `email infrastructure` | MTA config, per-server setup pattern |
| Updates | `unattended upgrades`, `release tracking`, `dependency updates` | Fleet-wide update conventions |
| Backups | `backup`, `restore`, `retention` | Storage lifecycle, backup script patterns |

## Step 1: Assess Complexity

Before creating any files, evaluate the guide requirements:

### Simple Format (single file)

Use when ALL of these are true:
- Single, focused task or procedure
- Fewer than ~15 actionable steps
- No new infrastructure provisioning
- No ongoing maintenance requirements
- Can be completed in one session

### Complex Format (multi-file)

Use when ANY of these are true:
- Deploying a new application or service
- Creating new VMs, containers, or cloud resources
- Configuring multiple integrated services
- Requires backup or monitoring setup
- Has ongoing maintenance procedures
- More than 15 steps across multiple phases

## Step 2: Determine Output Location

| Purpose | Location |
|---------|----------|
| Cloud/VM deployment | `docs/[platform]/[app-name]/` or the workspace's existing deployment-docs area |
| Self-hosted infrastructure | `docs/infrastructure/[app-name]/` or the workspace's existing infrastructure area |
| Best practice implementation | `docs/best-practices/[topic-slug]/` |
| Project-specific | `Projects/[ProjectName]/guides/` |
| Educational | `Education/[Topic]/` |
| General purpose | Ask user for preferred location |

## Step 3: Determine Inventory Requirements

**Include inventory steps ONLY when:**
- Deploying to Proxmox VMs or LXC containers
- Deploying to AWS, GCP, or other cloud instances tracked in inventory
- Installing software that exposes ports on tracked infrastructure

**Inventory location:** use the workspace's existing infrastructure inventory
file, if one exists.

**Skip inventory steps when:**
- Local development guides
- Third-party/SaaS configuration
- Educational or theoretical guides
- Infrastructure not tracked in the inventory

## Step 4: Select Phases (Complex Format Only)

All phases are OPTIONAL. Select only what's needed:

| Phase | Include When |
|-------|-------------|
| Overview & Planning | Complex deployments with architectural decisions |
| Infrastructure/VM Setup | Creating new VMs or cloud resources |
| Networking Configuration | Custom networking, VPCs, tunnels |
| Install Dependencies | Software prerequisites needed |
| Deploy Application | Core application deployment |
| Configure Reverse Proxy | Public-facing services |
| Configure Authentication | OAuth, SSO, user management |
| Configure Backups | Data persistence requirements |
| Configure Monitoring | Production services |
| Post-Deployment | Multi-step deployments needing verification |
| Ongoing Maintenance | Services requiring regular upkeep |

## Step 5: Create Files

### Delegation Check

Per the Execution Strategy above:
1. Check for a **documentation writing agent** (tools include Write, Edit; description mentions "documentation", "guides", or "writing")
2. If found → delegate file creation to that agent with context from Steps 0-4
3. If not found → create files inline as described below

### Simple Format

Create single file at chosen location: `[Guide Title].md`

Use template from [templates.md](references/templates.md) - Simple Guide Template

### Complex Format

Create structure:
```
[AppName]/
├── STATUS.md              ← Operational dashboard (scaffolded with placeholders)
└── Guide/
    ├── 1. [First Phase].md
    ├── 2. [Second Phase].md
    └── ...
```

**Files to create:**
1. **STATUS.md** - Use template from [templates.md](references/templates.md) - STATUS.md Template
   - Scaffold with placeholder content
   - Update during/after deployment with actual values
2. **Guide/ files** - Use templates from [templates.md](references/templates.md) - Complex Guide Templates

## Conventions (All Formats)

1. **Checklists**: Use `- [ ]` for every actionable step
2. **Code blocks**: Always specify language
3. **Verification**: Include verification after major operations
4. **Callouts** (Obsidian syntax):
   - `> [!important]` for critical steps
   - `> [!note]` for helpful context
   - `> [!warning]` for dangerous operations

## Complex Format Additional Conventions

1. **File naming**: `[N]. [Phase Name].md` (numbered sequentially)
2. **Navigation**: Start each file with `**Previous:** [[X]]` and end with `**Next:** [[Y]]`

## Templates

See [references/templates.md](references/templates.md) for markdown templates.

## Reference Examples

**Simple guides:**
- `docs/cloud/setup/lock-down-ssh.md`

**Complex guides (validated through deployment):**
- `docs/application-migration/` - Full application deployment with email, backups, and DNS
- `docs/email-infrastructure/` - Multi-server infrastructure with DNS and MTA config
- `docs/unattended-upgrades/` - Fleet-wide configuration
- `docs/cloud-app/` - Setup guide with multiple phases
- `docs/best-practices/remove-hardcoded-secrets/` - Best-practice implementation with multi-host deployment

> [!important] Reference Guides for Format, Verify Content Independently
> When creating a new guide that overlaps with an existing one (e.g., Mailgun setup, Cloudflare DNS):
> 1. **Read existing guides** for format, structure, and lessons learned
> 2. **Verify technical content** against current vendor documentation
> 3. **Flag potential updates** to reference guides for user review if they appear outdated
