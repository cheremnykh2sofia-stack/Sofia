---
description: "Search entire history and accumulated knowledge"
argument-hint: "[query] [--type code|error|learning]"
---

Search entire conversation history and accumulated knowledge using semantic search.

**Content Types:**
- `code` - Code snippets
- `error` - Error solutions
- `learning` - Learnings and insights
- `decision` - Decisions made
- `discussion` - Discussions
- `question` - Questions asked

**Output:**
- Search results with relevance score
- Date and type
- Topics and tags
- Content preview
- Links to original context

**Example:**
```
/memory-search "authentication" --type code
/memory-search "database optimization"
/memory-search "API design patterns" --type learning
```

Please search memory for: $ARGUMENTS
