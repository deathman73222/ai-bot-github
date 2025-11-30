# Troubleshooting Guide

## Common Issues and Solutions

### 1. Application Won't Start

#### Issue: "Python not found" or "python is not recognized"
**Solution:**
- Download Python from https://www.python.org/downloads/
- During installation, CHECK the box: "Add Python to PATH"
- Restart your computer
- Try again

#### Issue: Blank window opens and closes immediately
**Solution:**
```powershell
# Open PowerShell and run:
cd C:\Users\rabin\OneDrive\Documents\GitHub\ai-bot-github
python run_ai_bot.py
```
This will show you the actual error message.

#### Issue: "No module named PyQt5"
**Solution:**
```powershell
pip install PyQt5 --upgrade
```

---

### 2. Search Not Working

#### Issue: Online search returns no results
**Solutions:**
1. Check internet connection: Open browser and visit google.com
2. DuckDuckGo might be temporarily down
3. Try a simpler query (e.g., "Python" instead of "Python 3.11 features")
4. Switch to "Offline Only" mode to use local Wikipedia

#### Issue: "No internet connection" message
**Solutions:**
- This is expected if you're offline
- Switch to "Offline Only" mode
- Or use "Hybrid" mode which falls back to offline automatically

#### Issue: Searches are very slow
**Solutions:**
1. DuckDuckGo might be slow - try again
2. Your internet might be slow - run a speed test
3. Switch to "Offline Only" for instant results

---

### 3. Offline Database Issues

#### Issue: "Wikipedia offline database not initialized"
**Solution:**
```powershell
# The app should auto-initialize. If not:
python
>>> from ai_bot.modules.wikipedia_offline import WikipediaOffline
>>> wiki = WikipediaOffline()
>>> wiki.setup_database()
>>> exit()
```

#### Issue: Offline search not working even after initialization
**Solutions:**
1. Check if database file exists: `data/wikipedia/wikipedia.db`
2. If not, delete the data folder and restart app
3. The app will recreate it with sample data

#### Issue: Want to load custom Wikipedia dump
**Solution:**
```python
# In Python:
from ai_bot.modules.wikipedia_offline import WikipediaOffline

wiki = WikipediaOffline()
wiki.setup_database("path/to/wikipedia_dump.json")
```

---

### 4. GUI Issues

#### Issue: Window appears very small or very large
**Solution:**
- Edit `config.json` and change `window_width` and `window_height`

#### Issue: Text is too small or too large
**Solution:**
- Edit `config.json` and change `font_size` (value in pixels)

#### Issue: GUI is unresponsive during search
**Solution:**
This is normal - the app uses threading. Wait for search to complete. If it hangs for >30 seconds:
1. Click the X to close
2. Try again with a simpler query

#### Issue: Results won't display
**Solutions:**
1. Click "Clear" button
2. Try a new search
3. Check if offline database exists

---

### 5. Installation Issues

#### Issue: "pip is not recognized"
**Solution:**
```powershell
# Use Python's pip module directly:
python -m pip install -r requirements.txt
```

#### Issue: Virtual environment won't activate
**Solution (Windows PowerShell):**
```powershell
# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try:
.\venv\Scripts\Activate.ps1
```

#### Issue: Requirements installation fails
**Solution:**
```powershell
# Upgrade pip first:
python -m pip install --upgrade pip

# Then try again:
pip install -r requirements.txt --upgrade
```

---

### 6. Performance Issues

#### Issue: App is very slow
**Solutions:**
1. **First launch** - Takes longer to initialize. This is normal.
2. **Large Wikipedia dump** - Slower searches. Consider using smaller dump.
3. **Old computer** - Reduce search frequency, give it time
4. **Disk space** - If <1GB free, app might slow down

#### Issue: High memory usage
**Solutions:**
1. Close other applications
2. Restart the app
3. Reduce cache size in `config.json`: set `cache_size_mb` to 50
4. Clear history: Press "Clear" button

---

### 7. Data and History

#### Issue: Search history is lost
**Solutions:**
1. History is saved in `data/search_history.json`
2. If file is deleted, history is gone
3. Make backups of important searches

#### Issue: Cache is full
**Solution:**
```powershell
# Clear cache from GUI: Click "Clear" button
# Or manually delete:
# Delete: data/cache folder
```

---

### 8. Mode-Specific Issues

#### Hybrid Mode Issues
- If online search is slow, waits for timeout then falls back
- Timeout is set to 10 seconds in `config.json`
- Change to `online_timeout_seconds` to adjust

#### Online Mode Issues
- Requires internet connection
- If no internet, you'll get error message
- Solution: Switch to Hybrid or Offline mode

#### Offline Mode Issues
- Only searches local data
- Sample Wikipedia articles included
- To get more articles, download Wikipedia dump
- For current events, switch to Online mode

---

### 9. Advanced Troubleshooting

#### Enable Debug Mode
Edit `config.json`:
```json
"advanced": {
  "debug_mode": true
}
```

Then check logs in `logs/ai_bot.log`

#### Check Database Integrity
```python
import sqlite3
from pathlib import Path

db_path = Path("data/wikipedia/wikipedia.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM articles")
print(f"Articles in database: {cursor.fetchone()[0]}")
conn.close()
```

#### Rebuild Database
```python
from ai_bot.modules.wikipedia_offline import WikipediaOffline
import os

# Delete old database
if os.path.exists("data/wikipedia/wikipedia.db"):
    os.remove("data/wikipedia/wikipedia.db")

# Create new one
wiki = WikipediaOffline()
wiki.setup_database()
```

---

### 10. Still Not Working?

#### Try the CLI Version First
```powershell
python cli_interface.py
```

If CLI works but GUI doesn't, the issue is likely with PyQt5.

#### Reinstall Everything
```powershell
# Backup your searches first!

# Remove virtual environment
rmdir /s venv

# Remove cache
rmdir /s data\cache

# Start fresh
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt --force-reinstall

# Run
python run_ai_bot.py
```

#### Check Python Version
```powershell
python --version
```
Should be 3.7 or higher. If not, reinstall Python 3.9+

#### Test Individual Components
```python
# Test web search
from ai_bot.modules.web_search import WebSearcher
ws = WebSearcher()
print(ws.search("python"))

# Test offline search
from ai_bot.modules.wikipedia_offline import WikipediaOffline
wiki = WikipediaOffline()
print(wiki.search("artificial intelligence"))

# Test AI engine
from ai_bot.core.ai_engine import AIEngine
engine = AIEngine()
print(engine.process_query("test", ws.search, wiki.search))
```

---

## Getting Help

### Check These First:
1. README.md - General documentation
2. GETTING_STARTED.md - Quick start guide
3. INSTALL_WINDOWS.md - Windows-specific setup
4. This file - Troubleshooting

### Report Issues:
- GitHub Issues: https://github.com/deathman73222/ai-bot-github/issues
- Include:
  - Error message (copy-paste from console)
  - Python version: `python --version`
  - Operating system
  - Steps you took

### Quick Diagnostics Script
```python
import sys
import os
from pathlib import Path

print("=== AI Bot Diagnostics ===\n")

print(f"Python: {sys.version}")
print(f"OS: {sys.platform}")
print(f"Current directory: {os.getcwd()}")
print(f"Project exists: {Path('ai_bot').exists()}")

try:
    import PyQt5
    print(f"PyQt5: ✓ Installed")
except:
    print(f"PyQt5: ✗ Missing")

try:
    import requests
    print(f"requests: ✓ Installed")
except:
    print(f"requests: ✗ Missing")

db_path = Path("data/wikipedia/wikipedia.db")
print(f"Wikipedia DB: {'✓ Exists' if db_path.exists() else '✗ Missing'}")

print("\nIf all checks pass, the app should work!")
```

---

## Prevention Tips

1. **Keep requirements updated**: `pip install -r requirements.txt --upgrade`
2. **Back up your data**: Copy `data/` folder regularly
3. **Use Hybrid mode**: Fallback protection
4. **Monitor disk space**: Keep >500MB free
5. **Test before relying**: Use app for non-critical searches first

---

**Last Updated**: November 2025
**Questions?** Check the GitHub repository or create an issue!
