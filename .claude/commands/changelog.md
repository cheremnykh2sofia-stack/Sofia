---
description: "Auto-generate changelog from git commits and PRs"
argument-hint: "[version number]"
---

Auto-generate changelog from git commits and PRs.

**Process:**
1. Analyze git log since last tag
2. Fetch GitHub PR information
3. Categorize changes (Added, Changed, Fixed, etc.)
4. Format as Keep a Changelog
5. Generate release notes
6. Create GitHub release

**Output:**
- Updated CHANGELOG.md
- GitHub release with notes
- Categorized changes

**Example:**
```
/changelog v2.1.0
/changelog v1.0.0-beta.1
```

Please generate changelog for: $ARGUMENTS
