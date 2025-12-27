# DOCX - Word Documents Skill

Document creation, editing, and analysis with formatting preservation.

## Overview

Work with Word documents using python-docx.

**API Keys Required:** None

## Installation

```bash
pip install python-docx
```

## Key Features

- Create and edit documents
- Formatting (bold, italic, headings)
- Tables and lists
- Images
- Headers and footers
- Table of contents

## Code Example

```python
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Add title
title = doc.add_heading('Project Requirements Document', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add section
doc.add_heading('1. Overview', level=1)
doc.add_paragraph('This document describes...')

# Add table
table = doc.add_table(rows=2, cols=3)
table.style = 'Light Grid Accent 1'

hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Feature'
hdr_cells[1].text = 'Priority'
hdr_cells[2].text = 'Status'

doc.save('document.docx')
```

## When to Use

- PRDs and technical specs
- Reports and contracts
- Professional documents
