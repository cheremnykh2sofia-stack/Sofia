---
description: "Generate complete CRUD API for a resource"
argument-hint: "[framework] [resource-name]"
---

Generate complete CRUD API for a resource with best practices.

**Supported Frameworks:** FastAPI, Django REST, Express, NestJS, Gin, Actix, Spring Boot, Laravel, Rails

**Arguments:**
- $1: Framework (fastapi, django, express, nestjs, etc.)
- $2: Resource name (users, products, orders, etc.)

**Generated Files:**
- Model/Entity with fields
- Schema/DTO (Pydantic, Zod, etc.)
- CRUD Service layer
- Router/Controller
- Routes registration
- Unit & integration tests
- Database migrations

**Example:**
```
/generate-api fastapi users
/generate-api nestjs products
/generate-api django orders
```

**Output Structure:**
```
src/
├── models/{resource}.py
├── schemas/{resource}.py
├── services/{resource}_service.py
├── routers/{resource}.py
└── tests/test_{resource}.py
```

Please generate CRUD API for: $ARGUMENTS
