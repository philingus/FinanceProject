# PocketBudget Analyzer

**CPS 3320: Python Programming**  
**Project 1**  
**Phil Combatir**  
**Professor: Yulia Kumar**  
**Kean University**

---

## Overview

PocketBudget Analyzer is a lightweight Python tool that helps users gain clear insights into their personal spending. Given a simple CSV export from any bank or credit-card platform, it will:

- Ingest transaction data and parse dates  
- Fill or standardize missing categories  
- Apply a rule-based engine to assign categories (Groceries, Travel, Utilities, etc.)  
- Compute monthly summaries and overall category totals  
- Generate two visualizations: a line chart of monthly trends and a pie chart of spending breakdown  
- Expose everything through a single command-line interface

This approach prioritizes transparency and ease of use. The full source code lives here, and a 50-transaction dummy dataset demonstrates how quickly you can see your spending patterns.

---

## Getting Started

### Prerequisites

- Python 3.8 or newer  
- `pip` package manager

### Installation

```bash
git clone https://github.com/philingus/FinanceProject.git
cd FinanceProject

# create and activate a virtual environment
python3 -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows PowerShell
# .\venv\Scripts\Activate.ps1

pip install -r requirements.txt
