---
name: learn
description: Teaches Claude something new by routing it to the appropriate memory file. Use when the user wants Claude to remember a preference, pattern, or rule. Analyzes the learning and determines whether it belongs in CLAUDE.md, tool-standards.md, best-practices.md, or a rules file. Can also update or remove existing learnings, and evolves the memory architecture when needed.
---

# Learn Skill

This skill routes new knowledge to the appropriate location in the memory architecture, and maintains the architecture itself as it evolves.

## When to Use

Trigger when user says things like:

**Add (default)**:
- "Remember that we prefer X"
- "I want Claude to always do X"
- "Use X instead of Y"
- "We have a new [system/service/VM]"
- "From now on, do X"
- "Learn this: ..."

**Update**:
- "Update the preference for X to Y"
- "Change the rule about X"
- "We no longer use X, we use Y instead"
- "/learn update: TypeScript is now required, not just preferred"

**Remove**:
- "Forget about X"
- "Remove the rule about X"
- "We no longer need the X preference"
- "/learn remove: pnpm preference"

---

## Step 1: Parse the Learning

Identify:

1. **Operation**: Add (default), Update, or Remove
2. **The fact/rule/preference** being taught
3. **Category indicators**:
   - Tool/language names → Tool preference
   - "always", "never", "Claude should" → Claude behavior
   - System/VM/service names → DevOps context
   - "security", "policy", "standard" → Best practice
   - "when deploying", "before deployment" → Deployment rule
   - "in guides", "documentation" → Documentation rule
   - "when working on [path]", "for [filetype] files" → Path-specific
4. **Scope** if any (all projects, specific paths, specific systems)

---

## Step 2: Determine Destination

### Categorization Table

| Category | Detection Patterns | Destination | Section Hint |
|----------|-------------------|-------------|--------------|
| **Tool preference** | Tool/language/framework names, "use X", "prefer X" | `DevOps/tool-standards.md` | Match language/purpose |
| **Claude behavior** | "always", "never", "when you", "Claude should" | `CLAUDE.md` | "Claude Responsibilities" |
| **DevOps context** | VM names, service names, infrastructure details | `.claude/rules/devops-context.md` | Match system type |
| **Best practice** | "security", "policy", "standard", operational requirement | `DevOps/best-practices.md` | Match topic or "Future Sections" |
| **Deployment rule** | "before deploying", "pre-deployment", infrastructure workflow | `.claude/rules/infrastructure.md` | "Pre-Deployment Checklist" |
| **Documentation rule** | "in guides", "when documenting", writing conventions | `.claude/rules/guide-creation.md` | "Guide Conventions" |
| **Path-specific rule** | "when working on X", "for Y files", scoped to file types | `.claude/rules/[topic].md` | Create if needed |
| **Complex workflow** | Multi-step procedure, reusable process | `.claude/skills/[name]/skill.md` | Create new skill |

### Ambiguous Cases

If category is unclear, ask the user using AskUserQuestion:

```
I want to remember: '[learning]'

This could be:
1. A tool preference (stored in tool-standards.md)
2. A Claude behavior (stored in CLAUDE.md)
3. A best practice (stored in best-practices.md)

Which fits best, or should I create a new rules file?
```

---

## Step 3: Read Target File

Read the target file to:
1. Understand existing structure and formatting
2. Find the appropriate section
3. Match the style (bullet points, tables, etc.)

For **Update/Remove** operations:
- Search for existing content matching the learning
- If not found, report and ask user for clarification

---

## Step 4: Preview Change

Always show the user what will change before applying:

### Add Preview
```
📍 File: DevOps/tool-standards.md
📍 Section: ## JavaScript/TypeScript Runtime

I'll add:

+ | **TypeScript** | Preferred | Use for all new projects; JavaScript only for legacy |

Confirm? (yes/no)
```

### Update Preview
```
📍 File: DevOps/tool-standards.md
📍 Section: ## JavaScript/TypeScript Runtime

Current:
| **TypeScript** | Preferred | Use for all new projects |

Change to:
| **TypeScript** | Required | Mandatory for all new projects; no exceptions |

Confirm? (yes/no)
```

### Remove Preview
```
📍 File: DevOps/tool-standards.md
📍 Section: ## Package Managers

I'll remove:
- | pnpm | Preferred | Faster than npm |

Confirm? (yes/no)
```

---

## Step 5: Apply Change

After confirmation:
1. Make the edit using the Edit tool
2. Confirm what was learned and where:
   ```
   ✓ Learned! Added TypeScript preference to tool-standards.md
   ```

---

## Step 6: Architecture Review

After every change, perform a quick health check on the memory architecture.

### Review Triggers

| Condition | Action |
|-----------|--------|
| Target file >150 lines | Suggest splitting into focused files |
| 3+ learnings in same new category | Propose creating dedicated rules file |
| Learning doesn't fit existing files | Propose new file or architecture expansion |
| New pattern of categorization emerged | Propose updating this skill's categorization logic |
| New file created | Update CLAUDE.md Key References if appropriate |

### Architecture Health Checks

1. **File size**: Check line count of modified file
2. **Categorization gaps**: Did this learning reveal a missing category?
3. **Pattern emergence**: Are we seeing a new type of learning that needs its own home?
4. **Skill evolution**: Should the categorization table in this skill be updated?

### Proposing Architecture Changes

If the review identifies needed changes:

```
📋 Architecture Review

I noticed:
- `.claude/rules/devops-context.md` is now 160 lines
- We've added 4 Python-related learnings recently

Recommendations:
1. Split devops-context.md into focused files
2. Create `.claude/rules/python.md` for Python-specific rules
3. Update this skill's categorization table

Apply these architecture improvements? (yes/no/skip)
```

### Self-Modification

When new categories emerge, update this skill's categorization table:

```
📋 Skill Self-Update

New category detected: "Python development"

I'll add to this skill's categorization table:

+ | **Python rules** | "Python", "type hints", "pytest", "ruff", ".py files" | `.claude/rules/python.md` |

Confirm skill update? (yes/no)
```

---

## Formatting Guidelines

Match the target file's existing style:

| File | Typical Format |
|------|----------------|
| `tool-standards.md` | Tables with Tool/Status/Notes columns |
| `CLAUDE.md` | Bullet points with **bold** labels |
| `devops-context.md` | Mix of tables and bullet points |
| `best-practices.md` | Sections with ### Policy headers |
| `.claude/rules/*.md` | Bullet points, checklists |

---

## Memory Architecture Reference

Current structure (check for updates):

```
workspace/
├── CLAUDE.md                              # Claude behavioral instructions
├── DevOps/
│   ├── best-practices.md                  # Operational standards/policies
│   └── tool-standards.md                  # Preferred development tools
└── .claude/
    ├── rules/
    │   ├── devops-context.md              # Always-loaded DevOps awareness
    │   ├── infrastructure.md              # Deployment rules (globs: DevOps/**)
    │   └── guide-creation.md              # Guide conventions
    ├── agents/                            # Specialized subagents
    └── skills/
        ├── learn/                         # This skill
        └── new-guide/                     # Guide scaffolding
```

---

## Examples

### Example 1: Tool Preference

**User**: "Use TypeScript whenever possible"

**Analysis**:
- Operation: Add
- Keyword: "TypeScript" (language)
- Pattern: "use X" → Tool preference
- Destination: `DevOps/tool-standards.md`

### Example 2: Claude Behavior

**User**: "Always ask before deleting files"

**Analysis**:
- Operation: Add
- Keyword: "always" → Behavior
- Destination: `CLAUDE.md`
- Section: Claude Responsibilities

### Example 3: New System

**User**: "We have a new VM called Analytics running Grafana"

**Analysis**:
- Operation: Add
- Keyword: "VM" → DevOps context
- Destination: `.claude/rules/devops-context.md`
- Section: VMs on Proxmox

### Example 4: Update Existing

**User**: "TypeScript is now required, not just preferred"

**Analysis**:
- Operation: Update
- Target: Find existing TypeScript entry
- Destination: `DevOps/tool-standards.md`

### Example 5: Path-Specific (New File)

**User**: "When working on Python files, always use type hints"

**Analysis**:
- Operation: Add
- Pattern: "when working on X" → Path-specific
- Destination: `.claude/rules/python.md` (create new)
- Include globs frontmatter: `**/*.py`
