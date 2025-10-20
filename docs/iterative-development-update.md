# Team-Builder Skill Update: Test-Driven Iterative Development

## Changes Made

I've updated the team-builder skill to emphasize **test-driven iterative development** with a "ship fast, iterate" philosophy.

## Key Updates

### 1. Test Engineer Now Required

**test-engineer is now ALWAYS included** in every team:

**Before:**
- Optional specialist
- Only mentioned for web projects

**After:**
- **[CRITICAL - ALWAYS INCLUDE]** tag
- Core team member alongside documentation-writer
- Included in all project types

### 2. New Test Engineer Agent Template

Created comprehensive test-engineer agent with:
- Proactive involvement at every stage
- Test automation and CI/CD focus
- Support for iterative development cycles
- Infrastructure and application testing

```markdown
---
name: test-engineer
description: Test strategy, test automation, quality assurance, and validation. 
Use for creating tests, CI/CD testing, and ensuring code quality. 
PROACTIVELY involved at every stage.
model: sonnet
tools: Read, Write, Edit, Bash, Grep, Glob
---
```

### 3. Iterative Development Philosophy

Added explicit guidance throughout:

**Core Philosophy:**
```
Build MVP → Deploy Early → Test Continuously → Iterate Based on Real Usage
```

**Development Workflow:**
1. documentation-writer: Create lean, focused PRD
2. Development agents: Build MVP (not perfection!)
3. test-engineer: Create test suite
4. devops-engineer: Deploy to staging/production
5. **Iterate**: Fix → Test → Deploy → Repeat

### 4. Updated TEAM-SETUP.md Template

Now includes **Iterative Development Workflow** section:

```markdown
## Iterative Development Workflow

This team is designed for rapid iteration:

**Phase 1 - MVP (Minimum Viable Product)**
1. documentation-writer: Create lean PRD focused on core functionality
2. [relevant dev agents]: Build minimal working version
3. test-engineer: Create basic test suite
4. devops-engineer: Deploy to staging/production

**Phase 2 - Validate & Test**
1. test-engineer: Run tests, identify issues
2. code-reviewer: Review code quality
3. Fix critical issues only

**Phase 3 - Iterate**
1. Based on real usage/testing, identify next priority
2. Repeat cycle: build → test → deploy → learn
3. Continuously improve

**Key Principle:** Ship fast, test thoroughly, iterate continuously. 
Don't aim for perfection in v1.
```

### 5. Revised Team Recommendations

**Infrastructure Projects (Now):**
- infrastructure-architect
- devops-engineer
- test-engineer **[ALWAYS INCLUDE]**
- documentation-writer **[ALWAYS INCLUDE]**
- security-engineer [if needed]

**Web Development Projects (Now):**
- backend-developer
- frontend-developer
- test-engineer **[ALWAYS INCLUDE]**
- documentation-writer **[ALWAYS INCLUDE]**
- code-reviewer [recommended]
- database-architect [if data-heavy]

### 6. Updated Best Practices

**New priority order:**
1. **Core team (ALWAYS)**:
   - documentation-writer
   - test-engineer

2. **Development agents** (project-specific)
   
3. **Specialists** (as needed)

**Iterative Development Principles:**
- Start with MVP: Build the simplest thing that works
- Deploy early: Get something running quickly
- Test continuously: test-engineer involved at every stage
- Iterate based on real usage: Learn from production
- Avoid over-engineering: Ship fast, improve later

## Example Team Output

### Before (Old Approach)
```
channels-dvr-setup/.claude/agents/
├── infrastructure-architect.md
├── devops-engineer.md
└── documentation-writer.md

Focus: Complete solution upfront
```

### After (New Iterative Approach)
```
channels-dvr-setup/.claude/agents/
├── infrastructure-architect.md
├── devops-engineer.md
├── test-engineer.md              ← ALWAYS INCLUDED
└── documentation-writer.md       ← ALWAYS INCLUDED

Focus: MVP → Deploy → Test → Iterate
```

## Why This Matters

### Traditional Approach (What we're avoiding):
1. Perfect planning upfront
2. Build complete feature set
3. Test everything at the end
4. Deploy when "ready"
5. ❌ Slow, risky, often over-engineered

### Iterative Approach (What we're enabling):
1. Lean PRD focused on MVP
2. Build minimal working version
3. Test continuously throughout
4. Deploy early and often
5. Learn from real usage
6. Iterate based on feedback
7. ✅ Fast, validated, right-sized solutions

## Usage Examples

### Example 1: Infrastructure Project
```
User: "Use team-builder to set up a team for Proxmox monitoring"

Team Created:
- infrastructure-architect (design system)
- devops-engineer (deploy containers)
- test-engineer (validate infrastructure) ← ALWAYS INCLUDED
- documentation-writer (runbooks) ← ALWAYS INCLUDED

Workflow:
1. Create lean PRD for basic monitoring
2. Build simple Prometheus + Grafana setup
3. Create smoke tests
4. Deploy and validate
5. Iterate: Add alerts, dashboards, etc.
```

### Example 2: Web Application
```
User: "Use team-builder for a task management SaaS"

Team Created:
- backend-developer (API)
- frontend-developer (UI)
- test-engineer (test automation) ← ALWAYS INCLUDED
- documentation-writer (API docs) ← ALWAYS INCLUDED
- code-reviewer (quality)

Workflow:
1. Create PRD for MVP: basic CRUD + auth
2. Build minimal API + simple UI
3. Write integration tests
4. Deploy to staging
5. Iterate: Add features based on usage
```

## Team Size Guidelines

**Small Projects (3-4 agents):**
- Minimum: documentation-writer + test-engineer + 1-2 specialists
- Example: doc-writer, test-engineer, devops-engineer

**Medium Projects (4-6 agents):**
- Core + development + specialists
- Example: doc-writer, test-engineer, backend-dev, frontend-dev, devops

**Large Projects (6-8 agents):**
- Full stack with multiple specialists
- Example: doc-writer, test-engineer, backend-dev, frontend-dev, db-architect, devops, security, code-reviewer

## Benefits of This Approach

### For Development Teams:
- ✅ Faster time to first deployment
- ✅ Reduced risk (small increments)
- ✅ Continuous validation through testing
- ✅ Learn from real usage, not assumptions
- ✅ Higher quality through continuous testing

### For Infrastructure Projects:
- ✅ Get basic setup working quickly
- ✅ Validate architecture decisions early
- ✅ Test each component as you go
- ✅ Iterate based on actual performance
- ✅ Catch issues before they compound

### For Maintenance:
- ✅ Test suite grows with features
- ✅ Easier to refactor with test coverage
- ✅ Faster debugging with good tests
- ✅ Confidence to iterate quickly

## Philosophy Summary

**Old Way:**
> "Let's plan everything perfectly, build it all, then test, then deploy"

**New Way:**
> "Let's build the simplest thing that could work, test it, deploy it, then iterate based on what we learn"

The team-builder now encourages and enables this modern, agile approach by:
1. Making test-engineer a required core team member
2. Providing iterative workflow guidance
3. Emphasizing MVP over perfection
4. Supporting continuous deployment

## Next Steps

1. **Download updated skill**: [team-builder.zip](computer:///mnt/user-data/outputs/team-builder.zip)
2. **Create a new team** with the iterative approach
3. **Notice the difference**:
   - test-engineer is always included
   - TEAM-SETUP.md has iterative workflow
   - Philosophy is baked into agent descriptions
4. **Follow the workflow**:
   - Lean PRD
   - MVP first
   - Test early
   - Deploy quickly
   - Iterate continuously

## Test the New Approach

Try it with your Proxmox monitoring project:

```
Use the team-builder skill to create a team for Proxmox monitoring.
Focus on getting basic monitoring deployed quickly.
```

Expected team:
- infrastructure-architect
- devops-engineer  
- test-engineer ← Now included automatically!
- documentation-writer

Then follow the iterative workflow:
1. "documentation-writer, create a lean PRD for MVP monitoring"
2. Build basic setup
3. "test-engineer, create validation tests"
4. Deploy
5. Iterate on improvements

Ship fast, test thoroughly, iterate continuously! 🚀
