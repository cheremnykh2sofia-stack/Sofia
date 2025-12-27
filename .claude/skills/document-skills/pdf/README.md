# PDF Processing Skill

PDF manipulation for text extraction, creation, merging/splitting.

## Overview

Work with PDFs using pypdf and reportlab.

**API Keys Required:** None

## Installation

```bash
pip install pypdf pdfplumber reportlab
```

## Key Features

- Text and table extraction
- PDF creation
- Merge and split PDFs
- Form filling
- Metadata editing
- OCR support (with pytesseract)

## Code Example

### Extract Text

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

### Create PDF

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("output.pdf", pagesize=letter)
c.drawString(100, 750, "Hello World")
c.save()
```

### Merge PDFs

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()

for pdf_file in ["file1.pdf", "file2.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

writer.write("merged.pdf")
```

## When to Use

- PDF form filling
- Text extraction
- Document merging
- Report generation
