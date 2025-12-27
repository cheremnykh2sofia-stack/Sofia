---
description: "Security review of changes"
argument-hint: "[file path or PR number]"
---

Security review of changes.

**Checks:**
- OWASP Top 10 vulnerabilities
- SQL injection
- XSS vulnerabilities
- Authentication/Authorization issues
- Secret exposure
- Dependency vulnerabilities

**Output:**
- Security score
- Vulnerability list by severity
- Recommendations
- Compliance status

**Example:**
```
/security-review src/
/security-review 123
```

Please perform security review for: $ARGUMENTS
