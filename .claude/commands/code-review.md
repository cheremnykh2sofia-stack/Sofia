---
description: "Comprehensive code review with security and quality checks"
argument-hint: "[file path or PR number]"
---

Perform comprehensive code review checking all aspects.

**Arguments:**
- $1: File path, directory, or PR number

**Checks Performed:**
1. **Readability** - Naming, formatting, comments
2. **Architecture** - SOLID principles, patterns, coupling
3. **Functionality** - Logic correctness, edge cases
4. **Security** - OWASP Top 10, injection, XSS, auth flaws
5. **Performance** - Complexity analysis, bottlenecks, memory
6. **Tests** - Coverage, quality, edge cases
7. **Dependencies** - Versions, vulnerabilities
8. **Documentation** - Docstrings, README
9. **Git practices** - Commit messages, branch naming

**Output Format:**
- Code quality score (1-10)
- Detailed checklists for each category
- Specific recommendations with code examples
- Approval/Request changes decision

**Example:**
```
/code-review src/api/users.py
/code-review src/services/
/code-review 123  # PR number
```

Please review the code at: $ARGUMENTS
