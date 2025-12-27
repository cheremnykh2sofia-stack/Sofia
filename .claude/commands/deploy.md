---
description: "Deploy application to staging or production"
argument-hint: "[staging / production / local]"
---

Universal deployment command with comprehensive checks and automation.

**Arguments:**
- $1: Environment (staging, production, local)

**Pre-deploy Checks:**
- Tests passing
- Linting clean
- Environment variables set
- Database backups (production only)
- Git status clean

**Deployment Steps:**
1. Build application
2. Run test suite
3. Build Docker image
4. Push to registry
5. Deploy to environment
6. Run database migrations
7. Health checks
8. Smoke tests

**Post-deploy:**
- Verification
- Monitoring setup
- Smoke tests
- Log monitoring

**Example:**
```
/deploy staging
/deploy production
/deploy local
```

Please deploy to: $ARGUMENTS
