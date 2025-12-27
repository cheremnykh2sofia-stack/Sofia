# XLSX - Excel Spreadsheets Skill

Comprehensive spreadsheet creation, editing, and analysis.

## Overview

Work with Excel files using openpyxl and pandas.

**API Keys Required:** None

## Installation

```bash
pip install openpyxl pandas
```

## Key Features

- Create and edit spreadsheets
- Formulas and calculations
- Data analysis and pivot tables
- Charts and visualization
- Conditional formatting
- Data validation

## Code Example

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active
ws.title = "Data"

# Add headers
headers = ["Name", "Age", "City"]
ws.append(headers)

# Style headers
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill(start_color="4472C4", fill_type="solid")

# Add data
ws.append(["Alice", 25, "NYC"])
ws.append(["Bob", 30, "LA"])

# Add formula
ws["D1"] = "Average Age"
ws["D2"] = "=AVERAGE(B2:B3)"

wb.save("data.xlsx")
```

## When to Use

- Financial models
- Data analysis dashboards
- Roadmaps with formulas
- Any Excel operations
