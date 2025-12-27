# PPTX - PowerPoint Presentations Skill

Presentation creation with layouts and animations.

## Overview

Work with PowerPoint using python-pptx.

**API Keys Required:** None

## Installation

```bash
pip install python-pptx
```

## Key Features

- Create presentations
- Multiple layouts
- Text formatting
- Images and charts
- Animations
- Speaker notes

## Code Example

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

# Title slide
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Project Presentation"
subtitle.text = "Your Name"

# Content slide
bullet_slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(bullet_slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = 'Key Points'
tf = body_shape.text_frame
tf.text = 'Point 1'

p = tf.add_paragraph()
p.text = 'Point 2'
p.level = 0

prs.save('presentation.pptx')
```

## When to Use

- Pitch decks
- Presentations
- Professional slides
