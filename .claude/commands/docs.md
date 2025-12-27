---
description: "Generate documentation from code with examples"
argument-hint: "[file path or module]"
---

Generate comprehensive documentation from code with examples.

**Generated:**
- API reference with all endpoints
- Request/response examples
- Constructor and method documentation
- Usage examples with code
- Type information
- Error handling documentation

**Formats:**
- Markdown
- OpenAPI/Swagger
- Notion pages (if MCP configured)

**Example:**
```
/docs src/api/
/docs src/services/user_service.py
/docs .  # Entire project
```

Please generate documentation for: $ARGUMENTS
