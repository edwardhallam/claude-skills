# Plugin Mapping Guide

Quick reference for matching project types to recommended plugins.

## Infrastructure Projects

### Core Team (Always Include)
- **infrastructure-architect** - Architecture and design
  - AITMPL: `--agent infrastructure/system-architect`
  - Wshobson: `/plugin install infrastructure-automation@wshobson-agents`

- **devops-engineer** - Deployment and automation
  - AITMPL: `--agent infrastructure/devops-engineer`
  - Wshobson: `/plugin install devops-automation@wshobson-agents`

- **documentation-writer** - Runbooks and docs
  - AITMPL: `--agent documentation/technical-writer`
  - Wshobson: `/plugin install code-documentation@wshobson-agents`

### Specialists (Add as Needed)
- **security-engineer** - Security and compliance
  - AITMPL: `--agent security/security-engineer`
  - Wshobson: `/plugin install security-scanning@wshobson-agents`

---

## Web Development Projects

### Core Team (Always Include)
- **backend-developer** - API and server logic
  - AITMPL: `--agent development-team/backend-developer`
  - Wshobson: `/plugin install backend-development@wshobson-agents`

- **frontend-developer** - UI and client logic
  - AITMPL: `--agent development-team/frontend-developer`
  - Wshobson: `/plugin install frontend-mobile-development@wshobson-agents`

- **documentation-writer** - API docs and PRD
  - AITMPL: `--agent documentation/technical-writer`
  - Wshobson: `/plugin install code-documentation@wshobson-agents`

### Specialists (Add as Needed)
- **database-architect** - Schema and optimization
  - AITMPL: `--agent database/database-architect`

- **quality-engineer** - Testing and QA
  - AITMPL: `--agent testing/qa-engineer`
  - Wshobson: `/plugin install unit-testing@wshobson-agents`

- **devops-engineer** - Deployment
  - AITMPL: `--agent infrastructure/devops-engineer`
  - Wshobson: `/plugin install devops-automation@wshobson-agents`

---

## Hybrid Projects (Infrastructure + Development)

### Recommended Team
1. infrastructure-architect
2. devops-engineer
3. backend-developer (if APIs needed)
4. security-engineer
5. documentation-writer

---

## Installation Examples

### Small Project (3-4 agents)
```bash
# AITMPL
npx claude-code-templates@latest \
  --agent infrastructure/devops-engineer \
  --agent infrastructure/system-architect \
  --agent documentation/technical-writer \
  --yes

# Wshobson
/plugin marketplace add wshobson/agents
/plugin install devops-automation@wshobson-agents
/plugin install infrastructure-automation@wshobson-agents
/plugin install code-documentation@wshobson-agents
```

### Medium Project (5-6 agents)
```bash
# AITMPL
npx claude-code-templates@latest \
  --agent development-team/backend-developer \
  --agent development-team/frontend-developer \
  --agent infrastructure/devops-engineer \
  --agent testing/qa-engineer \
  --agent documentation/technical-writer \
  --yes
```

### Large Project (7+ agents)
```bash
# AITMPL
npx claude-code-templates@latest \
  --agent development-team/backend-developer \
  --agent development-team/frontend-developer \
  --agent database/database-architect \
  --agent infrastructure/devops-engineer \
  --agent security/security-engineer \
  --agent testing/qa-engineer \
  --agent documentation/technical-writer \
  --yes
```

---

## Project Type Quick Match

**"Proxmox + Docker setup"** → infrastructure-architect, devops-engineer, documentation-writer

**"React + FastAPI app"** → backend-developer, frontend-developer, database-architect, documentation-writer

**"Channels DVR setup"** → infrastructure-architect, devops-engineer, documentation-writer

**"Full-stack SaaS"** → backend-developer, frontend-developer, database-architect, devops-engineer, security-engineer, quality-engineer, documentation-writer

**"API service"** → backend-developer, database-architect, devops-engineer, documentation-writer

**"Static website"** → frontend-developer, devops-engineer, documentation-writer
