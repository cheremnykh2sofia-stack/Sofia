# Deepgram STT Skill

Audio transcription with nova-2 model.

## Overview

Speech-to-text transcription using Deepgram API.

**API Key Required:** `DEEPGRAM_API_KEY`

## Models

| Model | Accuracy | Speed |
|-------|----------|-------|
| nova-3 | 54.2% WER reduction | Fast |
| nova-3-medical | Medical terminology | Fast |
| flux-general-en | Real-time voice agents | Ultra-fast |

## Installation

```bash
pip install deepgram-sdk
```

## Code Example

```python
import httpx

DEEPGRAM_API_KEY = "your-key"
headers = {"Authorization": f"Token {DEEPGRAM_API_KEY}"}

with open("audio.mp3", "rb") as f:
    resp = httpx.post(
        "https://api.deepgram.com/v1/listen?model=nova-3&language=ru",
        headers=headers,
        content=f.read()
    )

transcript = resp.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
print(transcript)
```

## Features

- 36+ languages
- Real-time streaming
- Diarization (speaker detection)
- Punctuation and formatting
- Custom vocabulary

## When to Use

- Audio transcription
- Meeting recordings
- Voice command processing
- Subtitle generation
