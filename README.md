# Sofia - Claude Code SuperConfig

> Ultimate configuration for Claude Code with MCP servers, agents, skills, and memory system.

**Version:** 1.0
**Last Updated:** 2025-12-27

---

## Содержание

- [Быстрый старт](#быстрый-старт)
- [Возможности](#возможности)
- [Структура проекта](#структура-проекта)
- [MCP Серверы](#mcp-серверы)
- [Команды](#команды)
- [Агенты](#агенты)
- [Skills](#skills)
- [Memory System](#memory-system)
- [Установка](#установка)
- [Использование](#использование)

---

## Быстрый старт

1. **Клонировать репозиторий:**
   ```bash
   git clone https://github.com/cheremnykh2sofia-stack/Sofia.git
   cd Sofia
   ```

2. **Настроить переменные окружения:**
   ```bash
   cp .env.example .env
   # Отредактируйте .env и добавьте свои API ключи
   ```

3. **Установить зависимости (опционально):**
   ```bash
   pip install chromadb sentence-transformers  # Для memory system
   ```

4. **Готово!** Claude Code автоматически загрузит конфигурацию из `.claude/`

---

## Возможности

### 🎯 20 MCP Серверов

Интеграции с внешними сервисами:
- **Context7** - Актуальная документация библиотек
- **GitHub** - Управление репозиториями, issues, PRs
- **Linear** - Project management
- **Slack** - Командная коммуникация
- **Notion** - База знаний
- **Sentry** - Мониторинг ошибок
- **Figma** - Design files
- **PostgreSQL/SQLite** - Базы данных
- **Docker** - Container management
- **Playwright/Puppeteer** - Browser automation
- **Replicate** - 1000+ AI моделей
- И многие другие...

### 🤖 7+ Ключевых Агентов

Специализированные субагенты для разных задач:

**Strategic Tier (Opus 4.5):**
- **Orchestrator** - Мастер-координатор для сложных проектов
- **Software Architect** - Архитектурное проектирование
- **Senior Developer** - Разработка features (Python, async, Telegram)
- **Code Reviewer** - Ревью безопасности и качества
- **DevOps Engineer** - CI/CD, deployment, infrastructure
- **QA Engineer** - Тестирование и качество

**Kimi K2 Tier:**
- **Kimi Senior Coder** - Сложные алгоритмы (SWE-bench 65.8%)

### ⚡ 10+ Команд

Slash-команды для частых задач:
- `/init-project [stack] [name]` - Инициализация проекта
- `/code-review [path]` - Комплексное code review
- `/kimi-review [path]` - Глубокое ревью с Kimi K2
- `/deploy [env]` - Deployment в staging/production
- `/test [type]` - Запуск тестов
- `/ai-search [query]` - Поиск с Perplexity AI
- `/docs [path]` - Генерация документации
- `/sprint-planning [sprint]` - Sprint planning
- `/memory-search [query]` - Поиск в памяти
- `/memory-learn [content]` - Сохранение знаний

### 🧠 Memory System

Долгосрочная память на основе векторного поиска:
- Semantic search с ChromaDB
- Автоматическое сохранение знаний
- Категоризация (technical, tools, workflow, preference, etc.)
- Поиск по релевантности

### 🎨 Skills

Специализированные навыки:
- **Gemini 3 Pro** - Генерация изображений, текста, видео
- **Memory System** - Работа с долгосрочной памятью
- И множество других...

---

## Структура проекта

```
Sofia/
├── .claude/                    # Claude Code конфигурация
│   ├── settings.json          # Основная конфигурация
│   ├── commands/              # Slash команды
│   │   ├── init-project.md
│   │   ├── code-review.md
│   │   ├── kimi-review.md
│   │   ├── deploy.md
│   │   ├── test.md
│   │   ├── ai-search.md
│   │   ├── docs.md
│   │   ├── sprint-planning.md
│   │   ├── memory-search.md
│   │   └── memory-learn.md
│   ├── agents/                # Субагенты
│   │   ├── orchestrator.md
│   │   ├── senior-developer.md
│   │   ├── code-reviewer.md
│   │   ├── devops-engineer.md
│   │   ├── qa-engineer.md
│   │   ├── kimi-senior-coder.md
│   │   └── software-architect.md
│   ├── skills/                # Навыки
│   │   ├── gemini-3-pro.md
│   │   └── memory-system/
│   ├── memory/                # Memory storage
│   │   ├── vector_db/
│   │   └── knowledge_base.md
│   ├── logs/                  # Логи
│   └── templates/             # Шаблоны
├── tools/                     # Утилиты
│   └── vector_memory.py       # Memory system script
├── .env.example               # Пример переменных окружения
├── .gitignore
├── README.md                  # Этот файл
└── test_example.py            # Тестовый файл

```

---

## MCP Серверы

### Что такое MCP?

Model Context Protocol (MCP) - это протокол для подключения внешних сервисов к Claude Code.

### Настроенные серверы (20)

#### 1. Context7
**Возможности:** Актуальная документация библиотек
**API Key:** Не требуется
**Команда:** `mcp__context7__get-library-docs`

#### 2. GitHub
**Возможности:** Repos, issues, PRs, code search
**API Key:** `GITHUB_TOKEN`
**Команды:** `mcp__github__create-pull-request`, `mcp__github__search-code`

#### 3. Memory
**Возможности:** Персистентная память между сессиями
**API Key:** Не требуется

#### 4. PostgreSQL/SQLite
**Возможности:** Работа с базами данных
**Команды:** Выполнение SQL запросов, схема БД

#### 5. Playwright/Puppeteer
**Возможности:** Browser automation, screenshots, testing
**API Key:** Не требуется

Полный список и описания см. в `.claude/settings.json`.

---

## Команды

### Разработка

```bash
# Инициализация нового проекта
/init-project fastapi my-api

# Генерация API
/generate-api fastapi users

# Code review
/code-review src/api/

# Глубокое ревью с Kimi K2
/kimi-review src/
```

### Тестирование

```bash
# Запуск всех тестов
/test

# Только unit тесты
/test unit

# E2E тесты
/test e2e
```

### Deployment

```bash
# Deploy в staging
/deploy staging

# Deploy в production
/deploy production
```

### Исследование

```bash
# AI-powered search
/ai-search "best practices for FastAPI authentication 2025"

# Генерация документации
/docs src/api/
```

### Memory

```bash
# Сохранить знание
/memory-learn technical: Always use parameterized queries for SQL

# Поиск в памяти
/memory-search "authentication patterns"
```

---

## Агенты

### Когда использовать каких агентов?

| Задача | Агент | Модель |
|--------|-------|--------|
| Координация сложного проекта | Orchestrator | Opus 4.5 |
| Архитектурное проектирование | Software Architect | Opus 4.5 |
| Разработка features | Senior Developer | Opus 4.5 |
| Code review | Code Reviewer | Opus 4.5 |
| CI/CD и deployment | DevOps Engineer | Opus 4.5 |
| Тестирование | QA Engineer | Opus 4.5 |
| Сложные алгоритмы | Kimi Senior Coder | Kimi K2 |

### Пример использования Orchestrator

```
Используй Orchestrator для координации создания новой фичи:
1. Software Architect - дизайн архитектуры
2. Senior Developer - имплементация
3. Code Reviewer - ревью
4. QA Engineer - тесты
5. DevOps Engineer - deployment
```

---

## Skills

### Gemini 3 Pro

Генерация изображений, текста, видео:

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

# Генерация изображения (ТОЛЬКО .jpg!)
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Futuristic cyberpunk workspace",
    config=types.GenerateContentConfig(response_modalities=['Image'])
)

with open("image.jpg", "wb") as f:
    f.write(response.candidates[0].content.parts[0].inline_data.data)
```

### Memory System

```bash
# Сохранить знание
python tools/vector_memory.py save "Use pytest for testing" "technical"

# Поиск
python tools/vector_memory.py search "testing frameworks"

# Статистика
python tools/vector_memory.py stats
```

---

## Memory System

### Установка

```bash
pip install chromadb sentence-transformers
```

### Использование

#### Через Python

```python
from tools.vector_memory import VectorMemory

memory = VectorMemory()

# Сохранить
memory.save("Always validate user input", "technical")

# Поиск
results = memory.search("security practices")

# Статистика
stats = memory.stats()
```

#### Через командную строку

```bash
# Сохранить
python tools/vector_memory.py save "Content here" "technical"

# Поиск
python tools/vector_memory.py search "query here"

# Статистика
python tools/vector_memory.py stats
```

#### Через slash-команды

```
/memory-learn technical: Use async/await for I/O operations
/memory-search "async patterns"
/memory-stats
```

### Категории памяти

- `technical` - Технические паттерны и learnings
- `tools` - Использование инструментов
- `workflow` - Workflow паттерны
- `preference` - Предпочтения пользователя
- `project` - Project-specific knowledge
- `decision` - Важные решения
- `code` - Code snippets
- `error` - Решения ошибок

---

## Установка

### Требования

- Claude Code CLI
- Node.js (для MCP серверов)
- Python 3.11+ (опционально, для memory system)

### Шаги установки

1. **Клонировать репозиторий:**
   ```bash
   git clone https://github.com/cheremnykh2sofia-stack/Sofia.git
   cd Sofia
   ```

2. **Настроить переменные окружения:**
   ```bash
   cp .env.example .env
   # Отредактируйте .env
   ```

3. **Установить зависимости для memory system (опционально):**
   ```bash
   pip install chromadb sentence-transformers
   ```

4. **Проверить конфигурацию:**
   ```bash
   ls -la .claude/
   # Должны быть: settings.json, commands/, agents/, skills/
   ```

---

## Использование

### Базовые команды

```bash
# Инициализация проекта
/init-project fastapi my-service

# Code review
/code-review src/

# Деплой
/deploy staging

# Тесты
/test

# AI поиск
/ai-search "FastAPI best practices"
```

### Работа с агентами

Агенты автоматически вызываются через Orchestrator или напрямую через Task tool.

### Работа с памятью

```bash
# Сохранить важное знание
/memory-learn technical: Используй Pydantic для валидации в FastAPI

# Поискать релевантную информацию
/memory-search "валидация данных"
```

---

## API Keys

Получить API ключи можно здесь:

- **Anthropic:** https://console.anthropic.com/
- **Gemini:** https://ai.google.dev/
- **GitHub:** https://github.com/settings/tokens
- **Linear:** https://linear.app/settings/api
- **Slack:** https://api.slack.com/apps
- **Notion:** https://www.notion.so/my-integrations
- **Perplexity:** https://www.perplexity.ai/settings/api

Добавьте их в `.env` файл (не коммитьте `.env` в git!).

---

## Безопасность

### Hooks

Настроены safety hooks для предотвращения опасных команд:

```json
"PreToolUse": [
  {
    "matcher": "Bash(rm -rf)",
    "hooks": [{"type": "command", "command": "echo 'BLOCKED: Dangerous command' && exit 2"}]
  }
]
```

### Secrets

- Никогда не коммитьте `.env` файл
- Используйте `.env.example` как template
- API ключи должны быть в переменных окружения

---

## Расширение

### Добавление новых команд

Создайте файл в `.claude/commands/`:

```markdown
---
description: "Your command description"
argument-hint: "[args]"
---

Your command prompt here.

Use $1, $2, etc. for arguments.
Use $ARGUMENTS for all arguments.
```

### Добавление новых агентов

Создайте файл в `.claude/agents/`:

```markdown
---
description: "Agent description"
model: "claude-opus-4-5-20251101"
---

# Agent Name

You are a **Agent Name** specializing in...

## Role
...

## Expertise
...
```

### Добавление новых skills

Создайте папку в `.claude/skills/` с README.md.

---

## Лицензия

MIT

---

## Благодарности

Основано на **Claude Code SuperConfig** by Жемал Хамидун (@Jemal_Hamidun).

---

## Поддержка

Для вопросов и issue:
https://github.com/cheremnykh2sofia-stack/Sofia/issues

---

**Готово к использованию! 🚀**

Запустите Claude Code в этой директории и начните использовать все возможности конфигурации.
