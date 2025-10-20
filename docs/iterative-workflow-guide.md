# Iterative Development Workflow - Quick Guide

## The New Team-Builder Philosophy

```
┌─────────────────────────────────────────────────────────┐
│  Ship Fast → Test Thoroughly → Iterate Continuously    │
└─────────────────────────────────────────────────────────┘
```

## Core Team (ALWAYS Included)

```
📝 documentation-writer  ←  Required: Lean PRD, specs
🧪 test-engineer        ←  Required: Test at every stage
```

## Standard 3-Phase Workflow

### Phase 1: MVP (Minimum Viable Product)
```
┌──────────────────────────────────────────────────────┐
│ 1. 📝 documentation-writer                           │
│    └─→ Create lean PRD (core features only)         │
│                                                       │
│ 2. 💻 Development Agents                             │
│    └─→ Build minimal working version                │
│                                                       │
│ 3. 🧪 test-engineer                                  │
│    └─→ Create basic test suite                      │
│                                                       │
│ 4. 🚀 devops-engineer                                │
│    └─→ Deploy to staging/production                 │
└──────────────────────────────────────────────────────┘
         Time to first deployment: FAST ⚡
```

### Phase 2: Validate & Test
```
┌──────────────────────────────────────────────────────┐
│ 1. 🧪 test-engineer                                  │
│    └─→ Run tests, identify issues                   │
│                                                       │
│ 2. 👀 code-reviewer                                  │
│    └─→ Review code quality                          │
│                                                       │
│ 3. 🔧 Development Agents                             │
│    └─→ Fix CRITICAL issues only                     │
└──────────────────────────────────────────────────────┘
         Get real feedback quickly 📊
```

### Phase 3: Iterate
```
┌──────────────────────────────────────────────────────┐
│ Based on real usage/testing, identify next priority │
│                                                       │
│ ┌──────────────────────────────────┐                │
│ │  Build → Test → Deploy → Learn  │ ←─── Repeat    │
│ └──────────────────────────────────┘                │
└──────────────────────────────────────────────────────┘
         Continuous improvement 🔄
```

## Example: Infrastructure Project

### Channels DVR on Docker

**Team Created:**
```
├── 📝 documentation-writer
├── 🏗️  infrastructure-architect
├── 🚀 devops-engineer
└── 🧪 test-engineer
```

**Iteration 1 - MVP:**
```
Day 1:
  📝 Create lean PRD: "Basic DVR with local storage"
  🏗️  Design: Docker container + volume mounts
  🚀 Deploy: docker-compose.yml with basic config
  🧪 Test: Container starts, records one channel
  ✅ DEPLOYED!
```

**Iteration 2 - Improve:**
```
Week 1:
  📝 Update: "Add network storage"
  🏗️  Design: NFS mount architecture
  🚀 Deploy: Add NFS mount to compose
  🧪 Test: Recording to NFS works
  ✅ DEPLOYED!
```

**Iteration 3 - Scale:**
```
Month 1:
  📝 Update: "Optimize for multiple streams"
  🏗️  Design: Resource allocation strategy
  🚀 Deploy: Tune container resources
  🧪 Test: Multi-stream performance
  ✅ DEPLOYED!
```

## Example: Web Application

### Task Management SaaS

**Team Created:**
```
├── 📝 documentation-writer
├── 🔙 backend-developer
├── 🎨 frontend-developer
├── 🚀 devops-engineer
├── 🧪 test-engineer
└── 👀 code-reviewer
```

**Iteration 1 - MVP:**
```
Week 1:
  📝 Lean PRD: "CRUD tasks + auth"
  🔙 Build: REST API (4 endpoints)
  🎨 Build: Simple task list UI
  🧪 Test: Integration tests for CRUD
  🚀 Deploy: Staging environment
  ✅ DEPLOYED!
```

**Iteration 2 - Feedback:**
```
Week 2:
  Based on usage: "Users want due dates"
  🔙 Add: Due date field + API
  🎨 Add: Date picker
  🧪 Test: Date handling
  🚀 Deploy: Production
  ✅ DEPLOYED!
```

**Iteration 3 - Enhance:**
```
Week 3:
  Based on usage: "Users want collaboration"
  🔙 Add: Share tasks endpoint
  🎨 Add: User selection UI
  🧪 Test: Permission tests
  👀 Review: Security check
  🚀 Deploy: Production
  ✅ DEPLOYED!
```

## Comparison

### ❌ Traditional "Waterfall" Approach
```
Months 1-2: Complete planning
Month 3:    Build all features
Month 4:    Test everything
Month 5:    Deploy
Month 6:    Discover users wanted something different
```
**Result:** 6 months to first deployment, may not match needs

### ✅ Iterative Approach (New Default)
```
Week 1:  MVP deployed
Week 2:  First improvements deployed
Week 3:  More features deployed
Week 4:  Refined based on real usage
```
**Result:** 1 week to first deployment, continuously improved

## Key Principles

### 1. **Start Small**
```
❌ "Build complete monitoring suite with:
    - 50+ dashboards
    - All possible alerts
    - Historical data analysis
    - ML anomaly detection"

✅ "Build basic monitoring:
    - CPU, RAM, Disk
    - Simple alert if down
    - 1 dashboard"
    
    (Then iterate!)
```

### 2. **Test Early**
```
❌ Write all code → Test at end

✅ Write feature → Test feature → Deploy feature
```

### 3. **Deploy Often**
```
❌ Wait until "perfect" (never happens)

✅ Deploy when working, even if minimal
```

### 4. **Learn from Reality**
```
❌ Guess what users need → Build guesses

✅ Deploy basics → See what's actually used → Build that
```

## Team Size for Iterative Development

### Minimum Viable Team (3-4 agents)
```
📝 documentation-writer  ← Required
🧪 test-engineer        ← Required
💻 1-2 specialists      ← Project specific
```

**Example:**
- Proxmox setup: doc-writer + test-engineer + devops-engineer + infrastructure-architect

### Standard Team (4-6 agents)
```
📝 documentation-writer  ← Required
🧪 test-engineer        ← Required
💻 2-4 specialists      ← Based on needs
```

**Example:**
- Web app: doc-writer + test-engineer + backend-dev + frontend-dev + devops + code-reviewer

### Large Team (6-8 agents)
```
📝 documentation-writer  ← Required
🧪 test-engineer        ← Required
💻 4-6 specialists      ← Full stack
```

**Example:**
- Complex SaaS: doc-writer + test-engineer + backend + frontend + database + devops + security + code-reviewer

## Testing Throughout Development

```
┌─────────────────────────────────────────────────────┐
│              test-engineer's Role                    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Phase 1 (MVP):        Create basic test suite      │
│  Phase 2 (Validate):   Run tests, find issues       │
│  Phase 3 (Iterate):    Add tests for new features   │
│                                                      │
│  Continuous:           Test automation in CI/CD     │
│                        Smoke tests for deployments  │
│                        Performance monitoring       │
└─────────────────────────────────────────────────────┘
```

## Decision Framework

### When to Deploy?
```
✅ Deploy when:
- Core functionality works
- Basic tests pass
- Critical issues are fixed

❌ Don't wait for:
- All possible features
- Perfect optimization
- Every edge case handled
```

### What to Build Next?
```
✅ Priority based on:
- Real usage patterns
- User feedback
- Critical bugs
- Actual pain points

❌ Don't build:
- "Might need" features
- "Cool to have" ideas
- Over-optimizations
- Speculative additions
```

## Success Metrics

### Traditional Approach
- Time to first deployment: **Months**
- Features delivered: **Many** (some unused)
- Defects found: **Late** (expensive to fix)

### Iterative Approach
- Time to first deployment: **Days/Weeks**
- Features delivered: **Fewer** (all validated)
- Defects found: **Early** (cheap to fix)

## Commands to Get Started

### 1. Create Team
```bash
# In Claude chat
Use the team-builder skill to create a team for [your project]
```

### 2. Start Iteration
```bash
# In Claude Code
claude

# Phase 1: MVP
documentation-writer, create a lean PRD for MVP functionality

# Build MVP with relevant agents
[build minimum working version]

# Phase 2: Test
test-engineer, create basic test suite for MVP

# Phase 3: Deploy
devops-engineer, help deploy this to staging
```

### 3. Iterate
```bash
# After each deployment
test-engineer, run all tests and identify issues

# Fix critical issues
[fix only critical problems]

# Plan next iteration
Based on usage, what should we add next?
```

## Remember

```
┌─────────────────────────────────────────────┐
│                                             │
│   Perfect is the enemy of shipped          │
│                                             │
│   Ship fast → Test thoroughly →            │
│   Iterate continuously                      │
│                                             │
└─────────────────────────────────────────────┘
```

🚀 **Start with MVP, not perfection**
🧪 **Test at every stage, not at the end**
📦 **Deploy early and often, not when "ready"**
🔄 **Iterate based on reality, not assumptions**

---

**Your team-builder now creates teams optimized for this workflow!**
