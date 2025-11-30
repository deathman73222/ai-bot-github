# AI Bot Quick Reference

## 🚀 Start the App

### Windows (Easiest)
Double-click: `run_ai_bot.bat`

### Windows (Command Line)
```powershell
python run_ai_bot.py
```

### macOS/Linux
```bash
bash run_ai_bot.sh
```

### Command Line Version
```powershell
python cli_interface.py
```

---

## 📖 Search Modes

| Mode | Online | Offline | When to Use |
|------|--------|---------|------------|
| **Hybrid** | ✅ First | ✅ Fallback | **Recommended** - Best of both |
| **Online** | ✅ Only | ❌ | Current events, latest info |
| **Offline** | ❌ | ✅ Only | No internet, privacy, speed |

---

## 🔍 Search Tips

### Simple Searches
```
"Python" → Results about Python programming
"climate change" → Information about climate change
"quantum computing" → Facts about quantum computers
```

### Advanced Searches
```
"machine learning" + "deep learning" → More specific
"artificial intelligence 2025" → Tend to use Online mode
```

### Best Results
- Use common terms
- 2-3 words typically work best
- Specific topics work better than vague queries

---

## 🎯 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Search |
| `Ctrl+A` | Select all (search box) |
| `Ctrl+C` | Copy (results) |
| Click item | View from history |

---

## 📊 File Locations

```
Project Root: C:\Users\rabin\OneDrive\Documents\GitHub\ai-bot-github\

Important Files:
├── run_ai_bot.bat          ← Double-click to start
├── run_ai_bot.py           ← Python entry point
├── cli_interface.py        ← Command line version
├── config.json             ← Settings
└── data/
    └── wikipedia/
        └── wikipedia.db    ← Offline database
```

---

## ⚙️ Configuration

Edit `config.json` to customize:

```json
"search": {
  "default_mode": "hybrid",     // Start mode
  "timeout_seconds": 10,         // Wait time for searches
  "cache_size_mb": 100           // How much to cache
}
```

---

## 🛠️ Installation Quick Check

```powershell
# Should show version (e.g., Python 3.9.0)
python --version

# Should not error
pip list | Select-String PyQt5

# Should work
python -c "from ai_bot.core.ai_engine import AIEngine"
```

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| App won't start | `python run_ai_bot.py` in terminal to see error |
| No online results | Check internet, try simpler query |
| Slow searches | Wait 10 seconds, try again, or use offline |
| GUI won't respond | Wait for search to finish (max 15 sec) |
| Database errors | Delete `data/wikipedia/wikipedia.db` and restart |
| Import errors | `pip install -r requirements.txt --upgrade` |

---

## 📚 Help Files

- **README.md** - Full documentation
- **GETTING_STARTED.md** - Setup guide
- **INSTALL_WINDOWS.md** - Windows-specific
- **TROUBLESHOOTING.md** - Problem solving
- **This file** - Quick reference

---

## 💾 Important Commands

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install packages
pip install -r requirements.txt

# Update packages
pip install -r requirements.txt --upgrade

# Run app
python run_ai_bot.py

# Run CLI version
python cli_interface.py

# Check Python
python --version

# List installed packages
pip list
```

---

## 🌐 Search Engines Used

- **Online**: DuckDuckGo (Free, no API key needed)
- **Offline**: Wikipedia (Local SQLite database)

---

## 📖 Python Code Usage

### Simple Search
```python
from ai_bot.core.ai_engine import AIEngine
from ai_bot.modules.web_search import WebSearcher
from ai_bot.modules.wikipedia_offline import WikipediaOffline

engine = AIEngine()
searcher = WebSearcher()
wiki = WikipediaOffline()

result = engine.process_query("Python", searcher.search, wiki.search)
print(result['response'])
```

### Change Mode
```python
engine.set_mode('offline')  # Or 'online' or 'hybrid'
```

### Access History
```python
history = engine.get_history(limit=5)
for item in history:
    print(item['query'])
```

---

## 🎓 Learning Resources

### For Python Beginners
- Search "Python tutorial" for getting started
- Check local Wikipedia articles

### For Advanced Users
- Modify `ai_bot/core/ai_engine.py` for custom logic
- Add new search providers in `ai_bot/modules/`
- Customize GUI in `ai_bot/gui/main_window.py`

---

## 📊 Performance Specs

| Operation | Time |
|-----------|------|
| App startup | 2-5 seconds |
| Online search | 2-8 seconds |
| Offline search | < 1 second |
| Database creation | First run only |
| Cache lookup | < 100ms |

---

## 🔐 Privacy & Security

✅ **No cloud storage** - Runs 100% locally
✅ **No tracking** - No analytics sent
✅ **No accounts** - No registration needed
✅ **Open source** - See all code
✅ **Free** - No hidden costs

---

## 📱 System Requirements

- Windows, macOS, or Linux
- Python 3.7+
- 2GB RAM
- 500MB disk space
- (Optional) Internet connection

---

## 🎯 Pro Tips

1. **Use Hybrid mode** - Automatic fallback for reliability
2. **Clear cache regularly** - Keep responses fresh
3. **Pin frequently used searches** - Copy to notes
4. **Try offline mode** - Lightning fast responses
5. **Combine modes** - Test different modes for comparison

---

## 🆘 Emergency Commands

If app crashes:
```powershell
# Force quit and restart
taskkill /F /IM python.exe
python run_ai_bot.py
```

If database is corrupted:
```powershell
# Delete and recreate
Remove-Item data/wikipedia/wikipedia.db
python run_ai_bot.py  # Will recreate automatically
```

---

## 📞 Support Channels

1. Check TROUBLESHOOTING.md
2. Review error messages
3. Check GitHub Issues
4. Read source code (it's well commented!)

---

## 🚀 Next Steps After Installation

1. ✅ Run the app
2. ✅ Try 3-5 searches
3. ✅ Switch between modes
4. ✅ Test offline functionality
5. ✅ Check search history
6. ✅ Explore settings in config.json

---

**Remember**: This is a free, open-source project. It's built to be simple, reliable, and to work offline!

**Happy Searching! 🔍**
