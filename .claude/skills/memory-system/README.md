# Memory System Skill

Long-term memory and knowledge management for Claude Code using vector search.

## Overview

Implements semantic search and persistent knowledge storage using ChromaDB.

## Components

1. **Vector Memory** - ChromaDB for semantic search
2. **Knowledge Base** - Text-based knowledge storage
3. **Auto-Learning** - Automatic knowledge extraction

## Installation

```bash
pip install chromadb sentence-transformers
```

## Setup

The memory system automatically stores data in `~/.claude/memory/`.

```
~/.claude/memory/
├── vector_db/          # ChromaDB storage
└── knowledge_base.md   # Text-based knowledge
```

## Usage

### Save Knowledge

```bash
python tools/vector_memory.py save "Always use parameterized queries" "technical"
python tools/vector_memory.py save "Preferred stack: FastAPI + React" "preference"
```

### Search Memory

```bash
python tools/vector_memory.py search "authentication patterns"
python tools/vector_memory.py search "database" "technical"
```

### View Statistics

```bash
python tools/vector_memory.py stats
```

## Content Types

- `technical` - Technical learnings and patterns
- `tools` - Tool usage and configurations
- `workflow` - Workflow patterns
- `preference` - User preferences
- `project` - Project-specific knowledge
- `decision` - Important decisions
- `code` - Code snippets
- `error` - Error solutions

## Auto-Learning

Configure Claude to automatically save important knowledge:

```markdown
## AUTO-LEARNING

After each session, automatically save:

1. **Fixed errors:**
   python tools/vector_memory.py save "Error X solved with Y" "technical"

2. **New tools/patterns:**
   python tools/vector_memory.py save "Use Z for W" "tools"

3. **User decisions:**
   python tools/vector_memory.py save "Chose X because Y" "decision"
```

## Commands

Use slash commands for easy access:

- `/memory-learn [category]: [content]` - Save knowledge
- `/memory-search [query]` - Search memory
- `/memory-stats` - View statistics

## Example Workflow

```python
# After fixing a bug
memory.save(
    "SQL injection fixed by using parameterized queries with SQLAlchemy",
    content_type="technical"
)

# Later, searching for solutions
results = memory.search("SQL security")
# Returns the saved solution with relevance score
```

## Benefits

- **Persistent Knowledge:** Survives across sessions
- **Semantic Search:** Find relevant information even with different wording
- **Automatic Learning:** Build knowledge base over time
- **Context Retention:** Remember project decisions and patterns

Always save important learnings to build a comprehensive knowledge base.
