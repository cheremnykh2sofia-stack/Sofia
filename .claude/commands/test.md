---
description: "Run comprehensive test suite with coverage"
argument-hint: "[test type: unit/integration/e2e/all]"
---

Run comprehensive test suite with coverage reporting.

**Arguments:**
- $1: Test type (unit, integration, e2e, all) - default: all

**Test Types:**
- **unit** - Unit tests only (fast)
- **integration** - Integration tests
- **e2e** - End-to-end tests (slow)
- **all** - All test types

**Features:**
- Coverage reporting (target: 80%+)
- Parallel execution for speed
- Detailed failure reports
- Performance metrics
- Test result summary

**Example:**
```
/test
/test unit
/test integration
/test e2e
```

Please run tests: $ARGUMENTS
