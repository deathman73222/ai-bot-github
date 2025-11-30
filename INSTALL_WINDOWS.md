# Quick Installation Guide for Windows

## Step 1: Download or Clone the Repository
```
git clone https://github.com/deathman73222/ai-bot-github.git
cd ai-bot-github
```

## Step 2: Run the Setup Script
Simply **double-click** `run_ai_bot.bat`

This will:
1. Create a Python virtual environment (if not exists)
2. Install all required packages
3. Launch the AI Bot application

## Step 3: First Launch
The GUI will open with:
- A search box at the top
- Mode selector (Hybrid/Online/Offline)
- Results panel on the right
- Search history on the left

## Quick Usage
1. Type your question: "What is Python?"
2. Click "Search" or press Enter
3. See results from online or offline sources

## Features
✅ Search the internet with DuckDuckGo (no API key needed)
✅ Search offline Wikipedia data
✅ Automatically switch between modes
✅ View search history
✅ Completely free and open source

## Troubleshooting
- If the app doesn't open, make sure Python 3.7+ is installed
- If DuckDuckGo doesn't work, check your internet connection
- Switch to "Offline Only" mode to use local Wikipedia data

## Advanced: Manual Setup
If `run_ai_bot.bat` doesn't work:

```powershell
# Open PowerShell in the ai-bot-github folder
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run_ai_bot.py
```

---
Need help? Check README.md for detailed documentation!
