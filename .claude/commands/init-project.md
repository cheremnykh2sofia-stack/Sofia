---
description: "Initialize new project with full automation"
argument-hint: "[stack] [project-name]"
---

Initialize a new project with comprehensive setup.

**Supported Stacks:**
- **Backend:** fastapi, django, flask, express, nestjs, gin
- **Frontend:** react, nextjs, vue, nuxt, svelte
- **Full-stack:** mern, t3, django-react
- **Bots:** telegram-bot

**Arguments:**
- $1: Stack type (e.g., fastapi, react, telegram-bot)
- $2: Project name

**Actions to perform:**
1. Create project structure with best practices
2. Install all dependencies
3. Set up linting/formatting (ESLint, Prettier, Black, Ruff)
4. Configure git hooks (pre-commit, husky)
5. Set up database connection (if applicable)
6. Create testing framework
7. Generate CI/CD pipeline (GitHub Actions)
8. Create Docker configuration
9. Generate .env files with examples
10. Create README with documentation

**Example:**
```
/init-project fastapi my-api-service
/init-project nextjs my-frontend
/init-project telegram-bot assistant-bot
```

Please initialize the project with the specified stack and name.
