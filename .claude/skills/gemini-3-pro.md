# Gemini 3 Pro Skill

Full Gemini API suite for text, images, video, and audio generation.

## Overview

Access to Google's Gemini 3 Pro models for various AI tasks.

**API Key Required:** `GEMINI_API_KEY`

## Models Available

| Model | Capability | Context |
|-------|------------|---------|
| gemini-3-pro-preview | Text generation | 2M tokens |
| gemini-3-pro-image-preview | Image generation | - |
| veo-3.1-generate-preview | Video generation | - |
| gemini-tts-preview | Text-to-speech | - |
| gemini-stt-preview | Speech-to-text | - |

## Installation

```bash
pip install google-genai
```

## Image Generation

**IMPORTANT:** The model generates JPEG only, NOT PNG!

```python
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

# Generate image
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate image: Futuristic cyberpunk workspace with holographic screens",
    config=types.GenerateContentConfig(response_modalities=['Image'])
)

# SAVE AS .jpg ONLY!
with open("generated_image.jpg", "wb") as f:
    f.write(response.candidates[0].content.parts[0].inline_data.data)
```

## Text Generation

```python
response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="Explain quantum computing in simple terms"
)

print(response.text)
```

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| Using `google.generativeai` | Old SDK | Use `from google import genai` |
| Saving as .png | Model doesn't support PNG | Save as .jpg only |
| `response_modalities=['Text', 'Image']` | Wrong config | Use `['Image']` only |
| `gemini-pro-vision` model | Wrong model (for analysis) | Use `gemini-3-pro-image-preview` |

## Prompt Engineering for Images

Include these elements for best results:
- **Camera specs:** Sony A7R V, Canon EOS R5, Hasselblad X2D
- **Lenses:** 85mm f/1.4, 35mm f/1.8, 50mm f/1.2
- **Lighting:** Rembrandt, split, butterfly, loop
- **Film stocks:** Kodak Portra 400, Cinestill 800T

**Example:**
```
Photorealistic portrait, shot on Hasselblad X2D 100c,
100mm f/2.2 lens, Rembrandt lighting with soft key light,
Kodak Portra 800 film aesthetic, 8K resolution
```

## When to Use

- High-quality image generation
- Long-form text generation (2M context)
- Video generation with Veo
- Text-to-speech and speech-to-text

Always use the correct SDK and save images as JPEG.
