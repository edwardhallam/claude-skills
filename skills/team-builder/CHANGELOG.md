# Changelog

All notable changes to the team-builder skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0.0] - 2025-10-19

### Added

- **MANDATORY test-engineer requirement** - test-engineer is now required in every team (no exceptions)
- **"REQUIRED: Core Team Members" section** - Explicit documentation of mandatory agents at top of skill
- **Development Philosophy section** - New section emphasizing "Ship Fast, Iterate Continuously" approach
- **Vertical-slice guidance** - Step 2C now provides concrete examples of vertical slicing vs horizontal layering
- **Enhanced TEAM-SETUP.md template** - Rewritten with 3 phases (MVP Fast, Validate Real Usage, Iterate Vertical Slices)
- **Failure validation example** - Shows what a FAILED task looks like when test-engineer is missing
- **Deploy-fast messaging** - Emphasis on getting to production in DAYS, not weeks
- **Key Principles** in TEAM-SETUP.md - 5 core tenets of iterative development
- **Vertical slice example** - Concrete comparison showing 3 iterations vs horizontal layers

### Changed

- **Step 2: Determine the Team** - Restructured into 2A (Core-Required), 2B (Project-Specific), 2C (Vertical Slicing)
- **Step 6: Summarize** - Added explicit validation checkboxes and failure messaging
- **Best Practices section** - Renamed to "Vertical Slice Iterative Development (MANDATORY APPROACH)"
- **Agent selection priority** - test-engineer and documentation-writer listed FIRST as absolutely required
- **Workflow description** - Updated to emphasize "Build that ONE complete feature (vertical slice)"
- **Output examples** - Updated to show test-engineer as "REQUIRED - NO EXCEPTIONS"

### Impact

- **test-engineer mentions:** 10+ throughout the skill (up from ~3 in v2)
- **vertical slice mentions:** 11 throughout the skill (new in v3)
- **deploy fast mentions:** 6+ emphasizing quick production deployment
- **Line count:** 603 lines (up from 522 in v2)
- **File size:** 8.4KB (up from 7.1KB)

### Migration Notes

**From v2 to v3:**
- No breaking changes - this is additive guidance
- All teams will now ALWAYS include test-engineer
- Stronger emphasis on vertical slicing and fast deployment
- No configuration changes required for existing projects

---

## [2.0.0] - 2025-10-17

### Added

- **test-engineer agent** - Added with `[ALWAYS INCLUDE]` tags
- **Iterative development workflow** - Basic 3-phase workflow in TEAM-SETUP.md
- **Test-driven development guidance** - Emphasis on testing at every stage
- **documentation-writer as required** - Marked as always-include alongside test-engineer

### Changed

- **Team composition** - test-engineer added to all recommended teams
- **TEAM-SETUP.md template** - Added iterative workflow section
- **Agent templates** - Updated test-engineer template with CI/CD integration
- **Best practices** - Added iterative development philosophy section

### Impact

- **Line count:** 522 lines (up from ~400 in v1)
- **New agent templates:** test-engineer added to library
- **Workflow focus:** Shifted from waterfall to iterative

### Migration Notes

**From v1 to v2:**
- Existing teams should add test-engineer manually
- TEAM-SETUP.md should be updated with iterative workflow guidance

---

## [1.0.0] - Earlier

### Added

- Initial release of team-builder skill
- Core agent templates (infrastructure-architect, devops-engineer, backend-developer, frontend-developer, etc.)
- Plugin mapping for AITMPL and Wshobson sources
- Basic team creation workflow
- `.claude/` directory structure creation
- TEAM-SETUP.md template

### Features

- Project discovery (asking clarifying questions)
- Agent recommendation based on project type
- Configuration file generation
- Installation commands for plugins
- Minimal output constraint (<500 lines, <10 files)

---

## Version Comparison

### v3.0.0 vs v2.0.0

| Feature | v2.0.0 | v3.0.0 |
|---------|--------|--------|
| test-engineer | Recommended ([ALWAYS INCLUDE]) | **MANDATORY** (skill fails if missing) |
| Vertical slicing | Not mentioned | **Emphasized** (11 mentions) |
| Deploy timeline | Not specified | **Days to production** (explicit target) |
| Failure examples | None | **Added** (missing test-engineer example) |
| TEAM-SETUP.md | Basic 3-phase | **Enhanced** with Key Principles |
| Validation | Basic checklist | **Explicit** failure criteria |
| Line count | 522 | 603 (+15.5%) |

### v2.0.0 vs v1.0.0

| Feature | v1.0.0 | v2.0.0 |
|---------|--------|--------|
| test-engineer | Not included | **Added** ([ALWAYS INCLUDE]) |
| Iterative workflow | Not documented | **Added** (3-phase) |
| Testing emphasis | Minimal | **Significant** (test-driven) |
| documentation-writer | Optional | **Required** |
| Line count | ~400 | 522 (+30%) |

---

## Roadmap

### Future Considerations

**v3.x (Patch releases):**
- Bug fixes
- Documentation improvements
- Additional agent templates
- Plugin mapping updates

**v4.0 (Major release - TBD):**
- Potential features under consideration:
  - AI-powered agent selection (analyze codebase to recommend agents)
  - Team composition templates for common project types
  - Integration with package managers for easier installation
  - Agent performance metrics and recommendations
  - Multi-skill composition (team-builder + other skills)

**Community Requests:**
- Additional agent templates for specific domains (ML, mobile, embedded)
- Support for other plugin sources beyond AITMPL and Wshobson
- Custom team templates (save/load team configurations)

---

## Breaking Changes

### v3.0.0
- **None** - All changes are additive/behavioral

### v2.0.0
- **None** - All changes are additive

### v1.0.0
- Initial release (no breaking changes)

---

## Upgrade Instructions

### Upgrading to v3.0.0

1. Download [team-builder-v3.0.0.zip](./releases/team-builder-v3.0.0.zip)
2. Extract to `~/.claude/skills/team-builder/` (replacing v2)
3. Restart Claude Code
4. No project configuration changes required

**Existing projects:** Your current `.claude/` configurations will continue to work. Consider adding test-engineer if not already present.

### Upgrading to v2.0.0

1. Download team-builder-v2.0.0.zip
2. Extract to `~/.claude/skills/team-builder/` (replacing v1)
3. Restart Claude Code
4. Update existing projects to add test-engineer agent

---

## Deprecations

**None** - All versions maintain backward compatibility

---

## Known Issues

### v3.0.0
- None reported

### v2.0.0
- test-engineer was recommended but not enforced (fixed in v3)

### v1.0.0
- No testing agent included (fixed in v2)
- No iterative workflow guidance (fixed in v2)

---

## Credits

**Maintainer:** [@edwardhallam](https://github.com/edwardhallam)

**Philosophy:** Inspired by iterative development practices, vertical slice architecture, test-driven development, and DevOps culture.

**Framework:** Built following Anthropic's [skill creation framework](https://docs.claude.com/en/docs/claude-code).

---

## Links

- **Repository:** [github.com/edwardhallam/claude-skills](https://github.com/edwardhallam/claude-skills)
- **Documentation:** [README.md](./README.md)
- **Examples:** [examples.md](./examples.md)
- **Issues:** [GitHub Issues](https://github.com/edwardhallam/claude-skills/issues)

---

[3.0.0]: https://github.com/edwardhallam/claude-skills/releases/tag/v3.0.0
[2.0.0]: https://github.com/edwardhallam/claude-skills/releases/tag/v2.0.0
[1.0.0]: https://github.com/edwardhallam/claude-skills/releases/tag/v1.0.0
