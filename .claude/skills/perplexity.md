# Perplexity Research Skill

Research with web search and citations.

## Overview

Use Perplexity AI for research with real-time web search.

**API Key Required:** `PERPLEXITY_API_KEY`

## Model

- **sonar** - With citations and sources

## Code Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-pplx-key",
    base_url="https://api.perplexity.ai"
)

resp = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "Find information about..."}]
)

# Response includes citations in metadata
print(resp.choices[0].message.content)
```

## When to Use

- Web research
- Latest information
- Fact-checking
- Competitive analysis
- Technology research

Always check citations for source verification.
