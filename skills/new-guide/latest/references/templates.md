# Templates

Use these templates when scaffolding guides.

---

## Simple Guide Template

Use for single-file guides (fewer than ~15 steps, no ongoing maintenance).

```markdown
# [Guide Title]

> [One-line description of what this guide accomplishes]

## Prerequisites

- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

## Steps

### [Step Group 1]

- [ ] Step description

```bash
# Command with context
command here
```

- [ ] Verify: [verification step]

### [Step Group 2]

- [ ] Step description
- [ ] Step description

## Verification

- [ ] [Final verification that guide objective is met]

## Troubleshooting

| Issue | Solution |
|-------|----------|
| [Common issue] | [Solution] |
```

---

# Complex Guide Templates

Use for multi-file guides (new deployments, multiple phases, ongoing maintenance).

---

## Overview & Planning Template

Only include when guide requires architectural decisions or significant planning.

```markdown
# Overview & Planning

**Next:** [[2. {NextPhase}]]

---

## Project Overview

[Brief description of what we're deploying and why]

## Architecture

[ASCII diagram or description of the target architecture]

```
┌─────────────────────────────────────────┐
│              [Component]                 │
└─────────────────────────────────────────┘
```

## Key Decisions

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Compute | [Choice] | [Why] |
| Database | [Choice] | [Why] |

## Prerequisites

- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]
- [ ] Access to [required accounts/systems]

## Resource Requirements

- **CPU**: X cores
- **RAM**: X GB
- **Storage**: X GB

---

**Next:** [[2. {NextPhase}]]
```

---

## Generic Phase Template

```markdown
# [Phase Name]

**Previous:** [[{N-1}. {PrevPhase}]]

---

## Overview

[Brief description of what this phase accomplishes]

## Steps

### [Step Group 1]

- [ ] Step description

```bash
# Command with context
command here
```

- [ ] Verify step completed:

```bash
# Verification command
```

### [Step Group 2]

> [!note] Context
> Helpful information about this section

- [ ] Step description
- [ ] Step description

> [!warning] Caution
> Warning about potential issues

## Verification

- [ ] [Verification step 1]
- [ ] [Verification step 2]

---

**Next:** [[{N+1}. {NextPhase}]]
```

---

## Post-Deployment Template

Only include when guide has multiple phases requiring final verification.

```markdown
# Post-Deployment

**Previous:** [[{N-1}. {PrevPhase}]]

---

## Verify Functionality

- [ ] [Core functionality check 1]
- [ ] [Core functionality check 2]
- [ ] [Integration check if applicable]

## Check Logs for Errors

- [ ] Check application logs:

```bash
# Log viewing command
```

- [ ] Check system logs:

```bash
sudo journalctl -u [service] -f
```

<!-- CONDITIONAL: Only include if backups were configured -->
## Run First Backup

- [ ] Execute backup:

```bash
# Backup command
```

- [ ] Verify backup completed successfully

<!-- CONDITIONAL: Only include if deploying to tracked infrastructure -->
## Update Inventory

- [ ] Update the workspace's infrastructure inventory with:
  - Hostname, IP, OS, resources
  - All installed software and versions
  - Running services and ports
  - Any tunnel or ingress details

## Monitor Initial Period

- [ ] Watch for errors over 24-48 hours
- [ ] Monitor resource usage: `htop`, `df -h`
- [ ] Verify scheduled tasks are running

---

**Next:** [[{N}. Ongoing Maintenance]]
```

---

## Ongoing Maintenance Template

Only include when service requires regular upkeep.

```markdown
# Ongoing Maintenance

**Previous:** [[{N-1}. Post-Deployment]]

---

## Daily Tasks

- [ ] Check service status
- [ ] Review error logs

## Weekly Tasks

- [ ] Verify backups completed
- [ ] Check disk usage
- [ ] Review security updates

## Monthly Tasks

- [ ] Apply security patches
- [ ] Review and rotate logs
- [ ] Test backup restoration

## Updating [AppName]

```bash
# 1. Backup first
# backup command

# 2. Stop services
# stop command

# 3. Update
# update commands

# 4. Restart services
# start command

# 5. Verify
# verification command
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| [Common issue] | [Cause] | [Solution] |

## Useful Commands

```bash
# Service status
# Log viewing
# Resource monitoring
```
```

---

## STATUS.md Template (Complex Guides Only)

Create alongside `Guide/` directory for complex guides. STATUS.md serves as an operational dashboard - tracking deployment state, providing quick commands, and maintaining changelog.

```markdown
# [Service Name] Status

Last verified: [DATE or "Not yet deployed"]

## Architecture

[Description or ASCII diagram of target architecture]

```
┌─────────────────────────────────────────┐
│              [Component]                 │
└─────────────────────────────────────────┘
```

## Configuration Summary

| Component | Setting | Value | Status |
|-----------|---------|-------|--------|
| [Component] | [Setting] | [Value] | 📋 Planned |

Status indicators: 📋 Planned → 🔄 In Progress → ✅ Deployed

## Deployment Guide

See `Guide/` for full deployment instructions:
1. [[Guide/1. Phase Name|Phase Name]]
2. [[Guide/2. Phase Name|Phase Name]]

## Quick Commands

\`\`\`bash
# Verify service status
[placeholder - add verification commands during deployment]

# View logs
[placeholder - add log commands during deployment]

# Test functionality
[placeholder - add test commands during deployment]
\`\`\`

## Configuration Files

| File | Purpose |
|------|---------|
| [path] | [purpose] |

## Troubleshooting

See [[Guide/X. Phase|Phase - Troubleshooting]] for common issues.

<!-- OPTIONAL: Include if service has known issues or gotchas -->
## Known Issues

| Issue | Workaround | Reference |
|-------|------------|-----------|
| [Issue description] | [Workaround] | [Link if applicable] |

## Changelog

### [DATE]
- Initial scaffold created
```

> [!note] STATUS File Updates
> STATUS.md is scaffolded with placeholder content. Update during/after deployment:
> - Fill in Architecture section with actual design
> - Update Configuration Summary as components are deployed
> - Add Quick Commands as they're discovered
> - Add Changelog entries for each deployment session
