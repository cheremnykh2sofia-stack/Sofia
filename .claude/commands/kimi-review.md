---
description: "Deep code review using Kimi K2 (262K context, SWE-bench 65.8%)"
argument-hint: "[file path or directory]"
model: "kimi-k2-thinking"
---

Deep code review using Kimi K2 specialized SWE model with 262K context window.

**Advantages over regular code-review:**
- 262K context window - can analyze entire modules
- Deep reasoning about security implications
- Algorithm complexity analysis
- Architectural pattern validation
- SWE-bench 65.8% accuracy

**Checks:**
- **Security** - SQL injection, XSS, auth flaws, OWASP Top 10
- **Performance** - Algorithm complexity (Big-O), N+1 queries, memory leaks
- **Code Quality** - SOLID principles, design patterns, DRY
- **Best Practices** - Error handling, logging, type hints

**Output Format:**
```json
{
  "overall_score": 7.5,
  "security": {"score": 8, "issues": [...]},
  "performance": {"score": 7, "issues": [...]},
  "quality": {"score": 8, "issues": [...]},
  "recommendations": [...],
  "code_fixes": [...]
}
```

**Example:**
```
/kimi-review src/services/
/kimi-review app/api/endpoints/
```

Please perform deep code review using Kimi K2 for: $ARGUMENTS
