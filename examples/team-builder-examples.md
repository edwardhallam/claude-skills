# Team Builder Examples

Real-world examples of using the team-builder skill for different project types.

---

## Table of Contents

1. [Example 1: Homelab Infrastructure](#example-1-homelab-infrastructure)
2. [Example 2: Full-Stack Web Application](#example-2-full-stack-web-application)
3. [Example 3: API-Only Backend Service](#example-3-api-only-backend-service)
4. [Example 4: Simple Static Site](#example-4-simple-static-site)
5. [Example 5: Security-Critical Application](#example-5-security-critical-application)
6. [Example 6: Data-Heavy Analytics Platform](#example-6-data-heavy-analytics-platform)

---

## Example 1: Homelab Infrastructure

### Project: Proxmox Monitoring with Prometheus and Grafana

**Scenario:** You want to monitor your Proxmox homelab (multiple VMs, containers, storage) using Prometheus for metrics collection and Grafana for visualization.

### Invocation

```
Use team-builder to create a team for monitoring my Proxmox homelab with Prometheus and Grafana
```

### Team-Builder Questions

**Q1:** "What project are you building?"
**A:** "Monitoring system for Proxmox homelab with Prometheus and Grafana"

**Q2:** "Is this primarily infrastructure deployment or custom development?"
**A:** "Infrastructure deployment with some custom dashboard configuration"

### Team Created

```
/Users/edwardhallam/proxmox-monitoring/
└── .claude/
    ├── agents/
    │   ├── infrastructure-architect.md    (~80 lines)
    │   ├── devops-engineer.md             (~85 lines)
    │   ├── test-engineer.md               (~90 lines) ✅ REQUIRED
    │   └── documentation-writer.md        (~75 lines) ✅ REQUIRED
    ├── commands/
    ├── settings.json                      (~15 lines)
    └── TEAM-SETUP.md                      (~55 lines)

Total: 6 files, ~400 lines
```

### Installation Commands Provided

**AITMPL:**
```bash
npx claude-code-templates@latest \
  --agent infrastructure/infrastructure-architect \
  --agent infrastructure/devops-engineer \
  --agent quality/test-engineer \
  --agent documentation/technical-writer \
  --yes
```

**Wshobson:**
```bash
/plugin marketplace add wshobson/agents
/plugin install infrastructure-design@wshobson-agents
/plugin install devops-automation@wshobson-agents
/plugin install quality-assurance@wshobson-agents
/plugin install code-documentation@wshobson-agents
```

### Iterative Workflow

#### Phase 1: MVP (Week 1)

**Goal:** Get basic monitoring running in production ASAP

```bash
# Day 1-2: Plan
documentation-writer, create a lean PRD for MVP monitoring:
  - Prometheus collecting Proxmox metrics
  - Grafana with ONE dashboard showing CPU, RAM, disk
  - Docker-based deployment

# Day 3-4: Build
infrastructure-architect, design the monitoring stack architecture

devops-engineer, create docker-compose.yml for Prometheus + Grafana with basic Proxmox integration

# Day 5: Test
test-engineer, create tests to verify:
  - Containers start successfully
  - Prometheus scrapes Proxmox metrics
  - Grafana dashboard displays data

# Day 6: Deploy
devops-engineer, deploy to production Proxmox host

# Day 7: Validate
test-engineer, run smoke tests on production
✅ DEPLOYED - Basic monitoring live!
```

**MVP Output:**
- `docker-compose.yml` with Prometheus + Grafana
- Basic Prometheus config scraping Proxmox
- One Grafana dashboard (CPU, RAM, disk)
- Basic smoke tests
- Total: ~200 lines of code

#### Phase 2: Validate (Week 2)

```bash
# Run tests
test-engineer, validate production monitoring:
  - Are all metrics being collected?
  - Are there gaps in data?
  - Are thresholds appropriate?

# Gather feedback
[Look at dashboards in real usage]
Issues found:
  - Need disk I/O metrics
  - Want alerts for high CPU
  - Dashboard refresh rate too slow

# Document learnings
documentation-writer, update docs with findings
```

#### Phase 3: Iterate (Week 3+)

**Iteration 1 - Add Disk I/O:**
```bash
infrastructure-architect, design disk I/O metric collection
devops-engineer, implement disk I/O scraping + dashboard panel
test-engineer, test disk I/O metrics accuracy
✅ DEPLOYED
```

**Iteration 2 - Add Alerting:**
```bash
devops-engineer, configure Alertmanager for high CPU alerts
test-engineer, test alert triggering and notifications
✅ DEPLOYED
```

**Iteration 3 - Dashboard Improvements:**
```bash
infrastructure-architect, review dashboard performance
devops-engineer, optimize refresh rates and add filters
test-engineer, verify performance improvements
✅ DEPLOYED
```

### Results

- **Week 1:** Basic monitoring in production
- **Week 2:** Validated and refined
- **Week 3-4:** Added 3 complete features based on real usage
- **Total time:** 1 month to full-featured monitoring (vs. 3-6 months planning upfront)

---

## Example 2: Full-Stack Web Application

### Project: Task Management SaaS

**Scenario:** Building a task management SaaS application with user authentication, real-time updates, and team collaboration features using React (frontend) and Node.js/PostgreSQL (backend).

### Invocation

```
Use team-builder to create a team for a task management SaaS application with React frontend, Node.js backend, PostgreSQL database, and real-time collaboration
```

### Team-Builder Questions

**Q1:** "What project are you building?"
**A:** "Task management SaaS with React and Node.js"

**Q2:** "What are the key features?"
**A:** "User auth, task CRUD, real-time updates, team collaboration"

### Team Created

```
/Users/edwardhallam/taskmanager-saas/
└── .claude/
    ├── agents/
    │   ├── fullstack-developer.md         (~95 lines)
    │   ├── backend-developer.md           (~90 lines)
    │   ├── frontend-developer.md          (~85 lines)
    │   ├── database-architect.md          (~80 lines)
    │   ├── test-engineer.md               (~90 lines) ✅ REQUIRED
    │   ├── documentation-writer.md        (~75 lines) ✅ REQUIRED
    │   ├── code-reviewer.md               (~80 lines)
    │   └── devops-engineer.md             (~85 lines)
    ├── commands/
    ├── settings.json                      (~20 lines)
    └── TEAM-SETUP.md                      (~60 lines)

Total: 10 files, ~760 lines
```

### Installation Commands Provided

**AITMPL:**
```bash
npx claude-code-templates@latest \
  --agent development-team/fullstack-developer \
  --agent development-team/backend-developer \
  --agent development-team/frontend-developer \
  --agent data/database-architect \
  --agent quality/test-engineer \
  --agent documentation/technical-writer \
  --agent quality/code-reviewer \
  --agent infrastructure/devops-engineer \
  --yes
```

### Iterative Workflow

#### Phase 1: MVP (Week 1)

**Goal:** Ship ONE complete feature - Auth + Basic Task CRUD

```bash
# Day 1: Plan
documentation-writer, create lean PRD for MVP:
  Feature 1: User authentication (signup, login, logout)
  Feature 2: Basic task CRUD (create, read, update, delete)
  Feature 3: Simple UI (task list, add form)
  Out of scope: Teams, sharing, real-time, notifications

# Day 2-3: Build Database + Backend
database-architect, design schema for users and tasks tables

backend-developer, implement:
  - User auth API (signup, login, JWT)
  - Task CRUD endpoints
  - Database migrations

# Day 3-4: Build Frontend
frontend-developer, implement:
  - Login/signup forms
  - Task list view
  - Add/edit task forms

# Day 4: Integrate
fullstack-developer, connect frontend to backend API
  - Auth flow end-to-end
  - Task operations working

# Day 5: Test
test-engineer, create test suite:
  - Unit tests for auth logic
  - Integration tests for API endpoints
  - E2E tests for critical user flows

code-reviewer, review MVP code for quality and security

# Day 6: Deploy
devops-engineer, deploy to staging:
  - Docker containers for frontend and backend
  - PostgreSQL database
  - Basic CI/CD pipeline

# Day 7: Validate and Deploy to Production
test-engineer, run full test suite on staging
devops-engineer, deploy to production
✅ DEPLOYED - Users can sign up and manage their tasks!
```

**MVP Output:**
- Auth system (signup, login, JWT)
- 4 API endpoints (create, read, update, delete tasks)
- Simple React UI (task list + forms)
- PostgreSQL schema (users, tasks tables)
- Test suite (20+ tests)
- CI/CD pipeline
- Total: ~2000 lines of code

#### Phase 2: Validate (Week 2)

```bash
# Test with real users
test-engineer, monitor production:
  - Auth flow working?
  - Any errors or edge cases?
  - Performance issues?

# Gather feedback
[Early users provide feedback]
Findings:
  ✅ Auth works great
  ✅ Task CRUD is functional
  ❌ Users want due dates
  ❌ No way to organize tasks (tags, projects)
  ❌ UI is too basic

# Fix critical issues
backend-developer, fix API error handling
frontend-developer, improve error messages
test-engineer, add tests for edge cases
✅ DEPLOYED (fixes)
```

#### Phase 3: Iterate (Weeks 3-6)

**Iteration 1 - Due Dates (Vertical Slice):**
```bash
# Week 3
documentation-writer, add "due dates" to PRD

database-architect, add due_date column to tasks table

backend-developer, update API:
  - Add due_date field to create/update endpoints
  - Add filtering by due date

frontend-developer, add UI:
  - Date picker in task forms
  - Sort/filter by due date
  - Highlight overdue tasks

test-engineer, test due date functionality
code-reviewer, review code
devops-engineer, deploy
✅ DEPLOYED - Complete due date feature!
```

**Iteration 2 - Task Organization (Vertical Slice):**
```bash
# Week 4
database-architect, design projects/tags schema

backend-developer, implement:
  - Projects API (CRUD)
  - Tags API (CRUD)
  - Task-project and task-tag relationships

frontend-developer, implement:
  - Project sidebar navigation
  - Tag management UI
  - Filter tasks by project/tag

test-engineer, comprehensive testing
✅ DEPLOYED - Task organization feature!
```

**Iteration 3 - Real-Time Updates (Vertical Slice):**
```bash
# Week 5-6
backend-developer, implement WebSocket server with Socket.io

frontend-developer, add real-time subscriptions:
  - Tasks update live when other users make changes
  - Show "user is editing" indicators

test-engineer, test real-time edge cases
devops-engineer, scale backend for WebSocket connections
✅ DEPLOYED - Real-time collaboration!
```

### Results

- **Week 1:** MVP in production (auth + basic tasks)
- **Week 2:** Validated, fixed issues
- **Week 3:** Due dates feature
- **Week 4:** Organization (projects, tags)
- **Week 5-6:** Real-time collaboration
- **Total time:** 6 weeks to full-featured SaaS (vs. 6+ months waterfall approach)

---

## Example 3: API-Only Backend Service

### Project: RESTful API for E-commerce

**Scenario:** Building a backend API for an e-commerce platform (products, orders, payments) that will be consumed by web and mobile clients.

### Invocation

```
Use team-builder for a RESTful API backend service for e-commerce with product catalog, orders, and payment processing
```

### Team Created

```
/Users/edwardhallam/ecommerce-api/
└── .claude/
    ├── agents/
    │   ├── backend-developer.md           (~90 lines)
    │   ├── database-architect.md          (~85 lines)
    │   ├── test-engineer.md               (~90 lines) ✅ REQUIRED
    │   ├── documentation-writer.md        (~75 lines) ✅ REQUIRED
    │   ├── security-engineer.md           (~85 lines)
    │   ├── code-reviewer.md               (~80 lines)
    │   └── devops-engineer.md             (~85 lines)
    ├── commands/
    ├── settings.json                      (~15 lines)
    └── TEAM-SETUP.md                      (~55 lines)

Total: 9 files, ~660 lines
```

### Iterative Workflow

#### Phase 1: MVP (Week 1)

**Vertical Slice - Product Catalog ONLY**

```bash
# Day 1: Plan
documentation-writer, create lean PRD:
  MVP: Product catalog API (list products, get product details)
  Out of scope: Orders, payments, cart, users

# Day 2-3: Build
database-architect, design products schema

backend-developer, implement:
  - GET /products (list with pagination)
  - GET /products/:id (product details)
  - Basic validation and error handling

# Day 4: Test
test-engineer, create API tests:
  - Integration tests for endpoints
  - Load tests (can handle 1000 req/sec?)

security-engineer, security review (SQL injection, etc.)

# Day 5: Document and Deploy
documentation-writer, create API documentation (OpenAPI/Swagger)
devops-engineer, deploy to production
✅ DEPLOYED - Product catalog live!
```

#### Phase 2: Iterate

**Iteration 1 - User Orders:**
```bash
database-architect, design orders schema
backend-developer, implement orders API
test-engineer, test order workflows
✅ DEPLOYED
```

**Iteration 2 - Payment Integration:**
```bash
backend-developer, integrate Stripe API
security-engineer, review payment security
test-engineer, test payment flows
✅ DEPLOYED
```

### Results

- **Week 1:** Product catalog API live
- **Week 2-3:** Orders + Payments
- **Total:** 3 weeks to production API (vs. 2-3 months building all features upfront)

---

## Example 4: Simple Static Site

### Project: Portfolio Website Generator

**Scenario:** Building a simple static site generator for personal portfolios (markdown content → HTML).

### Invocation

```
Use team-builder for a minimal team to build a static site generator for portfolios
```

### Team Created

```
/Users/edwardhallam/portfolio-generator/
└── .claude/
    ├── agents/
    │   ├── fullstack-developer.md         (~85 lines)
    │   ├── test-engineer.md               (~80 lines) ✅ REQUIRED
    │   └── documentation-writer.md        (~70 lines) ✅ REQUIRED
    ├── commands/
    ├── settings.json                      (~10 lines)
    └── TEAM-SETUP.md                      (~45 lines)

Total: 5 files, ~290 lines
```

**Note:** Small team (3 agents) because it's a simple project.

### Iterative Workflow

**Iteration 1 (Week 1):** Parse markdown + generate HTML
**Iteration 2 (Week 2):** Add templates + styling
**Iteration 3 (Week 3):** Deploy command + GitHub Pages integration

---

## Example 5: Security-Critical Application

### Project: Healthcare Patient Portal

**Scenario:** Building a patient portal for healthcare records (HIPAA compliance required).

### Invocation

```
Use team-builder for a healthcare patient portal with strict security requirements (HIPAA compliance)
```

### Team Created

**Team includes security-engineer** (due to "strict security requirements" and "HIPAA"):

```
/Users/edwardhallam/patient-portal/
└── .claude/
    ├── agents/
    │   ├── backend-developer.md
    │   ├── frontend-developer.md
    │   ├── database-architect.md
    │   ├── security-engineer.md           ← Added due to security focus
    │   ├── test-engineer.md               ✅ REQUIRED
    │   ├── documentation-writer.md        ✅ REQUIRED
    │   ├── code-reviewer.md
    │   └── devops-engineer.md
    ├── commands/
    ├── settings.json
    └── TEAM-SETUP.md

Total: 10 files
```

### Workflow Emphasis

**security-engineer involved at EVERY phase:**

```bash
# Phase 1: MVP
security-engineer, review architecture for HIPAA compliance
[build MVP]
security-engineer, security audit before deployment
test-engineer, penetration testing

# Phase 2: Iterate
[add feature]
security-engineer, review new feature for security issues
[deploy]
```

---

## Example 6: Data-Heavy Analytics Platform

### Project: Business Intelligence Dashboard

**Scenario:** Building an analytics platform with complex SQL queries, data transformations, and visualization (processing millions of records).

### Invocation

```
Use team-builder for a business intelligence dashboard with complex data processing and visualizations
```

### Team Created

**Team includes database-architect** (due to "complex data processing"):

```
/Users/edwardhallam/bi-dashboard/
└── .claude/
    ├── agents/
    │   ├── backend-developer.md
    │   ├── frontend-developer.md
    │   ├── database-architect.md          ← Added due to data-heavy
    │   ├── test-engineer.md               ✅ REQUIRED
    │   ├── documentation-writer.md        ✅ REQUIRED
    │   ├── code-reviewer.md
    │   └── devops-engineer.md
    ├── commands/
    ├── settings.json
    └── TEAM-SETUP.md

Total: 9 files
```

### Workflow

**database-architect leads data design:**

```bash
# Phase 1: MVP
database-architect, design data warehouse schema (star/snowflake)
database-architect, optimize queries for millions of records
backend-developer, implement ETL pipeline
frontend-developer, build ONE dashboard
test-engineer, test query performance
✅ DEPLOYED - ONE working dashboard

# Phase 2: Iterate
[Add more dashboards based on user needs]
```

---

## Common Patterns

### Pattern 1: Start Small

All examples follow: **Minimal MVP → Deploy → Learn → Iterate**

### Pattern 2: Vertical Slicing

Every iteration builds ONE complete feature:
- Database schema changes
- Backend API
- Frontend UI
- Tests
- Deployment

**NOT:** All database → All backend → All frontend → Tests

### Pattern 3: Test at Every Stage

test-engineer validates at EVERY phase:
- After MVP
- Before each deployment
- After each iteration

### Pattern 4: Team Size Scales with Complexity

- **Simple projects:** 3-4 agents
- **Medium projects:** 5-7 agents
- **Complex projects:** 7-9 agents

### Pattern 5: Specialists Added as Needed

- **security-engineer:** When security is critical (healthcare, finance)
- **database-architect:** When data is complex (analytics, large-scale)
- **researcher:** When using novel technologies

---

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Building Everything Upfront

**Bad:**
```
Week 1-4: Build all features
Week 5: Test everything
Week 6: Deploy
Result: Users wanted different features
```

**Good:**
```
Week 1: MVP → Deploy
Week 2-6: Iterate based on real usage
Result: Built exactly what users need
```

### ❌ Anti-Pattern 2: Horizontal Layering

**Bad:**
```
Iteration 1: All database schema
Iteration 2: All backend APIs
Iteration 3: All frontend UI
Iteration 4: Tests
```

**Good:**
```
Iteration 1: ONE feature (DB → API → UI → Tests) → Deploy
Iteration 2: NEXT feature (DB → API → UI → Tests) → Deploy
```

### ❌ Anti-Pattern 3: Skipping Tests

**Bad:**
```
Build features → Deploy → Find bugs in production
```

**Good:**
```
Build feature → Test feature → Deploy → Confidence!
```

---

## Tips for Success

### 1. Be Specific in Your Invocation

**Vague:** "Use team-builder for a web app"
**Better:** "Use team-builder for a task management SaaS with React, Node.js, and real-time collaboration"

### 2. Answer Clarifying Questions Thoughtfully

Team-builder asks 1-3 questions. Provide:
- Project type (infrastructure vs. web app vs. API)
- Key technologies
- Critical requirements (security, scale, performance)

### 3. Start with Minimal Team

You can always add agents later. Start small:
- Core team (test-engineer + documentation-writer) ✅
- 1-2 specialists based on project type

### 4. Customize Agents After Creation

Edit `.claude/agents/*.md` files to:
- Add project-specific knowledge
- Customize behavior
- Add tools or remove restrictions

### 5. Follow the Iterative Workflow

The TEAM-SETUP.md provides 3-phase workflow. Follow it:
- Phase 1: MVP FAST
- Phase 2: Validate
- Phase 3: Iterate

---

## Next Steps

1. **[Install team-builder](../skills/team-builder/README.md#installation)**
2. **Try an example** similar to your project
3. **Customize your team** after creation
4. **Start iterating** - Build → Test → Deploy → Learn

---

**Questions?** [Open an issue](https://github.com/edwardhallam/claude-skills/issues) or check the [documentation](../skills/team-builder/README.md).
