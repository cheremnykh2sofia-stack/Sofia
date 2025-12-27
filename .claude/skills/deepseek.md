# DeepSeek Code Skill

DeepSeek models for code generation and reasoning.

## Overview

Use DeepSeek for code tasks (OpenAI-compatible API).

**API Key Required:** `DEEPSEEK_API_KEY`

## Models

- **deepseek-chat** - Universal, dialogs
- **deepseek-reasoner** - Reasoning, R1-like

## Code Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-deepseek-key",
    base_url="https://api.deepseek.com"
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Write a function to..."}],
    temperature=0.7
)

print(resp.choices[0].message.content)
```

## When to Use

- Code generation
- Code explanation
- Refactoring suggestions
- Algorithm implementation
