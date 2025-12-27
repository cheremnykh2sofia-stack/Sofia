---
description: "Systematic bug processing and prioritization"
argument-hint: "[bug ID or description]"
---

Systematic bug processing and prioritization.

**Steps:**
1. Gather information
2. Reproduce the issue
3. Severity classification (P0-P3)
4. Impact analysis
5. Root cause investigation
6. Fix strategy
7. Communication plan
8. Prevention measures

**Priority Levels:**
| Level | Description | Response Time |
|-------|-------------|---------------|
| P0 | Critical, system down | Immediate |
| P1 | Major feature broken | < 4 hours |
| P2 | Feature degraded | < 1 day |
| P3 | Minor issue | < 1 week |

**Example:**
```
/bug-triage "Users can't login after password reset"
/bug-triage BUG-456
```

Please triage bug: $ARGUMENTS
