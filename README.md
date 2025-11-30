# AI Bot - Professional Hybrid Search Engine

A powerful desktop application that combines **online web search** with **offline Wikipedia functionality** for free, unrestricted access to information.

## 🎯 Features

✅ **Hybrid Search Mode** - Automatically switches between online and offline sources
✅ **Online Search** - Uses DuckDuckGo API (completely free, no API key needed)
✅ **Offline Wikipedia** - Works without internet using local Wikipedia dumps
✅ **Professional GUI** - Beautiful PyQt5 interface with dark/light themes
✅ **Search History** - Keeps track of recent queries with encryption
✅ **Multiple Modes** - Switch between Hybrid, Online-only, and Offline-only modes
✅ **Password Protection** - Secure your installation and search history
✅ **Multi-Language Support** - Wikipedia available in 10+ languages
✅ **No Subscriptions** - Completely free and open-source
✅ **Professional Installer** - Interactive setup wizard for easy installation

## 💻 System Requirements

### Minimum
- **OS**: Windows 7+, macOS 10.14+, or Linux
- **Python**: 3.7+ (only if running from source)
- **RAM**: 2GB
- **Disk Space**: 500MB - 3GB
- **Internet**: Required for online search and initial setup

### Recommended
- **OS**: Windows 10+, macOS 11+, or Linux (Ubuntu 20.04+)
- **Python**: 3.9+
- **RAM**: 4GB+
- **Disk Space**: 5GB+
- **Internet**: Broadband connection

---

## 🚀 Quick Installation

### Option 1: Standalone Executable (Easiest)

**For Windows users - no Python required:**

1. Download: `AI_Bot_Setup.exe`
2. Run the installer
3. Follow the setup wizard
4. Create your password
5. Start searching!

### Option 2: Interactive Installation Wizard

**Windows with Python installed:**

```batch
REM Run the installer batch file
install.bat
```

This will:
- Automatically detect Python
- Install all dependencies
- Generate application icons
- Launch interactive setup wizard
- Create password protection
- Optionally create desktop shortcut

### Option 3: Manual Installation

**For developers or advanced users:**

```bash
# 1. Clone the repository
git clone https://github.com/deathman73222/ai-bot-github.git
cd ai-bot-github

# 2. Create virtual environment (optional but recommended)
python -m venv venv

# Windows:
.\venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app launcher (will show setup wizard on first run)
python app_launcher.py
```

---

## 🎨 First Run Setup

When you launch AI Bot for the first time, you'll see the **Interactive Setup Wizard** with:

1. **Welcome Screen** - Project overview
2. **Language Selection** - Choose Wikipedia language
   - English, Spanish, French, German, Italian
   - Portuguese, Russian, Chinese, Japanese, Korean
3. **Installation Location** - Select where to install
4. **Installation Summary** - Confirm settings
5. **Automatic Installation** - Downloads and configures everything
6. **Password Setup** - Create a secure password (8+ characters)
7. **Completion** - Ready to use!

---

## ▶️ Running AI Bot

### Launch Options

**GUI Application (Recommended):**
```bash
python run_ai_bot.py
# or
python app_launcher.py  # Shows login screen
```

**Command Line Interface:**
```bash
python cli_interface.py
```

**Standalone Executable (Windows):**
```bash
# If you have AIBot.exe
AIBot.exe
```

---

## 🔍 Usage Guide

### Online Search
1. Select "Hybrid" or "Online Only" mode
2. Enter your search query
3. Results appear instantly from DuckDuckGo

### Offline Search
1. Select "Offline Only" or "Hybrid" mode
2. Enter your search query
3. Search your local Wikipedia database

### Hybrid Mode (Recommended)
- First tries online search
- Automatically falls back to offline if no internet
- Best of both worlds!

### View Search History
- Click "Search History" to see previous queries
- Click any history item to view details
- Search history is encrypted and password-protected

---

## 🔐 Security Features

- **Password Protected** - Secure login on startup
- **Encrypted History** - Search history is encrypted
- **Local Processing** - All data stays on your computer
- **No Tracking** - No telemetry or data collection
- **Open Source** - Code is transparent and auditable

---

## 🛠️ Advanced Options

### Add Additional Wikipedia Languages

Edit `config.json`:
```json
{
  "language": "en",
  "additional_languages": ["es", "fr", "de"],
  ...
}
```

Then re-run the installer to download additional Wikipedia dumps.

### Create Portable Installation

```bash
# Build standalone executable
python build_executable.py

# Creates: dist/AIBot.exe
```

### Create Professional Installer

Requirements: [InnoSetup](https://jrsoftware.org/)

```bash
# 1. Build executable first
python build_executable.py

# 2. Open setup.iss in InnoSetup
# 3. Click "Compile"
# 4. Creates: dist/AI_Bot_Setup.exe
```

---

## 📋 Project Structure

```
ai-bot-github/
├── ai_bot/                    # Main application
│   ├── core/
│   │   └── ai_engine.py      # Query routing logic
│   ├── modules/
│   │   ├── web_search.py     # DuckDuckGo integration
│   │   └── wikipedia_offline.py  # Local Wikipedia
│   └── gui/
│       ├── main_window.py    # PyQt5 interface
│       ├── icon.png          # Application icon
│       └── icon.ico          # Windows icon
├── installer.py              # Installation wizard
├── app_launcher.py           # Login + launcher
├── create_icon.py            # Icon generator
├── build_executable.py       # Executable builder
├── install.bat               # Windows installer batch
├── setup.iss                 # InnoSetup installer script
├── requirements.txt          # Python dependencies
├── config.json               # Configuration file
├── cli_interface.py          # Command-line interface
├── run_ai_bot.py            # GUI launcher
└── README.md                 # This file
```

---

## 🔧 Troubleshooting

### "Python not found"
**Solution**: Install Python from https://www.python.org/ (check "Add Python to PATH")

### "Module not found" errors
**Solution**: Install dependencies: `pip install -r requirements.txt`

### "PyQt5 import failed"
**Solution**: Install PyQt5: `pip install PyQt5 --upgrade`

### "Cannot create shortcut"
**Solution**: Run installer with admin privileges on Windows

### Forgot password
**Solution**: Delete `config.json` in your installation folder and reinstall

For more help, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📚 Documentation

- **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** - Detailed installation instructions
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Getting started guide
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Architecture overview
- **[PYLINT_COMPLIANCE.md](PYLINT_COMPLIANCE.md)** - Code quality standards
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure code meets Pylint standards
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

- **DuckDuckGo** - Free online search API
- **MediaWiki** - Wikipedia data source
- **PyQt5** - GUI framework
- **Python Community** - Awesome language and libraries

---

## 🎯 Roadmap

### Completed ✅
- [x] Core search engine
- [x] Online search integration
- [x] Offline Wikipedia support
- [x] PyQt5 GUI
- [x] CLI interface
- [x] Professional installer
- [x] Password protection
- [x] Search history
- [x] Code quality (Pylint compliance)

### Planned 🔄
- [ ] Additional languages
- [ ] Search result filtering
- [ ] Advanced query syntax
- [ ] Browser integration
- [ ] Custom themes
- [ ] Search analytics

---

## 💬 Support

### Getting Help
1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Review [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)
3. Search existing GitHub issues
4. Create a new issue with details

---

## 🎉 Thank You

Thank you for using AI Bot! We hope it helps you find the information you need, whenever and wherever you need it.

**Happy Searching!** 🔍

---

**AI Bot v1.0** | Professional Hybrid Search Engine | Open Source | Free Forever

*Made with ❤️ for knowledge seekers everywhere*
