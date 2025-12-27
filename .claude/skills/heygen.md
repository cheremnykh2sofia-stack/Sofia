# HeyGen Video Avatars Skill

AI avatar video generation for talking heads and presentations.

## Overview

Create videos with AI avatars using HeyGen API.

**API Key Required:** `HEYGEN_API_KEY`

## Features

| Feature | Description |
|---------|-------------|
| AI Avatars | 100+ ready avatars |
| Custom Avatar | Clone your face |
| Voice Cloning | Clone your voice |
| Text-to-Video | Text → video with avatar |
| Multi-language | 40+ languages |
| Lip Sync | Perfect lip synchronization |

## Code Example

```python
import httpx

HEYGEN_API_KEY = "your-key"
headers = {"X-Api-Key": HEYGEN_API_KEY}

payload = {
    "video_inputs": [{
        "character": {
            "type": "avatar",
            "avatar_id": "josh_lite3_20230714",
            "avatar_style": "normal"
        },
        "voice": {
            "type": "text",
            "input_text": "Hello! Welcome to our demo.",
            "voice_id": "voice_id_here"
        },
        "background": {"type": "color", "value": "#FFFFFF"}
    }],
    "dimension": {"width": 1920, "height": 1080}
}

resp = httpx.post(
    "https://api.heygen.com/v2/video/generate",
    headers=headers,
    json=payload
)
video_id = resp.json()["data"]["video_id"]

# Check status
status = httpx.get(
    f"https://api.heygen.com/v1/video_status.get?video_id={video_id}",
    headers=headers
)
```

## When to Use

- AI avatar videos
- Personalized messages
- Training videos
- Marketing content
