# ElevenLabs TTS Skill

Text-to-speech with voice cloning and sound effects.

## Overview

High-quality speech synthesis using ElevenLabs API.

**API Key Required:** `ELEVENLABS_API_KEY`

## Models

| Model | Latency | Use Case |
|-------|---------|----------|
| eleven_flash_v2_5 | 75ms | Real-time |
| eleven_turbo_v2_5 | 300ms | General |
| eleven_multilingual_v2 | 600ms | Best quality |

## Installation

```bash
pip install elevenlabs
```

## Code Example

```python
import httpx

ELEVENLABS_API_KEY = "your-key"
headers = {"xi-api-key": ELEVENLABS_API_KEY}

# Get voices
voices_resp = httpx.get("https://api.elevenlabs.io/v1/voices", headers=headers)
voice_id = voices_resp.json()["voices"][0]["voice_id"]

# Generate speech
payload = {
    "text": "Hello, world!",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
}

resp = httpx.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    headers=headers,
    json=payload
)

with open("speech.mp3", "wb") as f:
    f.write(resp.content)
```

## Features

- 29+ languages
- Voice cloning
- Sound effects
- Voice design
- Projects (long-form)

## When to Use

- High-quality TTS
- Voice cloning
- Audiobook narration
- Sound effects generation
