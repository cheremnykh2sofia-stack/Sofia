# Kimi Deep Reasoning Skill

Kimi K2 for deep reasoning and code analysis (262K context).

## Overview

Use Kimi K2 model for complex reasoning tasks with 262K context window.

**API Key Required:** `KIMI_API_KEY`

## Models

| Model | Context | Description |
|-------|---------|-------------|
| kimi-k2-thinking | 262K | Reasoning, deep analysis, SWE-bench 65.8% |
| kimi-k2-thinking-turbo | 262K | Faster, cheaper |
| moonshot-v1-128k | 128K | Standard model |

## Installation

```bash
pip install openai  # OpenAI-compatible API
```

## Code Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-kimi-key",
    base_url="https://api.moonshot.cn/v1"
)

resp = client.chat.completions.create(
    model="kimi-k2-thinking",
    messages=[{"role": "user", "content": "Analyze this algorithm..."}],
    temperature=0.3
)

print(resp.choices[0].message.content)
```

## When to Use

- Complex algorithmic problems
- Large codebase analysis (262K context!)
- Deep debugging
- Mathematical reasoning
- Multi-step problem solving

## Advantages

- **262K context** - Analyze entire modules
- **SWE-bench 65.8%** - Top-tier coding performance
- **Deep reasoning** - Step-by-step analysis
- **Multi-language** - Chinese and English
