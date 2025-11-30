# AI Bot - Professional Installer Setup Guide

## 🎯 Overview

AI Bot now includes a complete professional installation system with:
- **Interactive Setup Wizard** - Beautiful GUI for easy installation
- **Automatic Dependency Installation** - All requirements installed automatically
- **Wikipedia Download** - Select language and auto-download offline data
- **Password Protection** - Secure your installation
- **Desktop Shortcuts** - Quick access to the application
- **Standalone Executable** - Create a .exe for easy distribution

---

## 📦 Installation Methods

### Method 1: Quick Install (Easiest)

**For end users - just run the installer:**

```batch
REM Run the installation batch file
install.bat
```

This will:
1. Check for Python installation
2. Install all dependencies (PyQt5, requests, Pillow, etc.)
3. Generate application icons
4. Launch the interactive setup wizard
5. Create configuration and password

### Method 2: Command Line Installation

```bash
# Install dependencies first
pip install -r requirements.txt

# Run installer directly
python installer.py
```

### Method 3: Manual Installation

```bash
# Install dependencies
pip install PyQt5 requests Pillow

# Generate icons
python create_icon.py

# Run the app launcher (shows setup if needed)
python app_launcher.py
```

---

## 🔧 What the Installer Does

### Step 1: Welcome Screen
- Shows project information
- Explains what will be installed
- Gathers user consent

### Step 2: Language Selection
```
Available Languages:
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Russian (ru)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
```

### Step 3: Installation Location
- Users can browse and select install directory
- Default: `C:\Users\[Username]\AI Bot`

### Step 4: Installation Summary
- Shows installation details
- Option to create desktop shortcut
- "Install" button to proceed
  
  Additional options available in the installer:
  - Choose between a Full Wikipedia download (downloads the entire pages-articles dump for the selected language; very large) or a Sample (downloads a limited number of articles for testing).
  - Optionally store the Wikipedia dumps on an external USB drive: browse to the USB, authenticate it (the installer writes a small marker file to confirm write access), and the extractor will write the dump directly to the USB to save internal disk space.

### Step 5: Installation Progress
- Real-time progress bar
- Status messages
- Detailed installation log
- Installs:
  - Application files
  - Python dependencies
  - Wikipedia database

### Step 6: Password Setup
- Create secure password (minimum 8 characters)
- Confirm password
- Password is hashed with SHA-256
- Used to protect search history

### Step 7: Completion
- Success message
- Installation path displayed
- Ready to launch

---

## 🎨 Professional Icons

The installer creates professional AI-themed icons:

### Main Application Icon
- **Size**: 256x256 PNG
- **Format**: Also saved as .ICO for Windows
- **Design**: Neural network pattern with AI theme
- **Colors**: Blue gradient to purple background
- **Features**: 
  - Animated neural nodes
  - Lightning bolt (AI energy)
  - Gold center core
  - "AI" text branding

### Installer Icon
- **Size**: 256x256 PNG
- **Design**: Installation folder with checkmark
- **Colors**: Green to blue gradient
- **Purpose**: Desktop shortcut and Start menu

---

## 🚀 Building Standalone Executable

### Create a Single .EXE File

```bash
# Build executable
python build_executable.py
```

This creates:
- **Output**: `dist/AIBot.exe`
- **Size**: ~150-200 MB
- **Includes**: All dependencies bundled
- **No Installation Required**: Just run the .exe

### Create Professional Windows Installer

Requirements:
- InnoSetup (free download: https://jrsoftware.org/)

Steps:
1. Build the executable first: `python build_executable.py`
2. Open InnoSetup
3. Open the script: `setup.iss`
4. Click "Compile"
5. Creates installer: `dist/AI_Bot_Setup.exe`

---

## 📋 File Structure After Installation

```
C:\Users\[Username]\AI Bot\
├── run_ai_bot.py          (GUI launcher)
├── app_launcher.py         (With login check)
├── cli_interface.py        (CLI launcher)
├── config.json             (Settings + password hash)
├── data/
│   ├── wiki_dumps/         (Raw per-language dump output)
│   │   └── <lang>/articles/*.txt
│   ├── wikipedia.db        (Offline sqlite database created from dumps)
│   └── [other data files]
├── ai_bot/
│   ├── core/
│   │   └── ai_engine.py
│   ├── modules/
│   │   ├── web_search.py
│   │   └── wikipedia_offline.py
│   └── gui/
│       ├── main_window.py
│       ├── icon.png
│       └── icon.ico
└── requirements.txt
```

---

## 🔐 Security Features

### Password Protection
- Hashed with SHA-256
- Stored in config.json
- Required on every startup
- Minimum 8 characters

### Secure Installation
- Password validated before access
- Search history encrypted
- Configuration file protected

---

## ❌ Uninstalling AI Bot

There are three ways to uninstall AI Bot depending on how it was installed:

1) If you installed with the Windows installer (InnoSetup):
  - Open Control Panel → Programs & Features (or Settings → Apps).
  - Select "AI Bot" and click Uninstall. The InnoSetup-registered uninstaller will remove application files and shortcuts.

2) If you installed from source or want to run our uninstaller manually:
  - Use the provided `uninstall.bat` (Windows) located in the repository or installation folder. Run it and follow the prompts.
  - Alternatively run the Python uninstaller:

```powershell
python uninstall.py
```

  - These scripts will remove the installation folder, desktop and Start Menu shortcuts (if present) and optionally attempt to uninstall Python packages listed in `requirements.txt`.

3) If you stored Wikipedia dumps on an external USB drive:
  - The uninstaller will not automatically delete files on external drives unless you explicitly point it to the external path. To remove the dumps from a USB, run the uninstaller and provide the USB path when prompted.

Notes and safety:
- Always close AI Bot before uninstalling. If files are in use, the uninstaller may not remove them. Reboot and run the uninstaller again if necessary.
- The `uninstall.py` and `uninstall.bat` scripts are interactive and ask for confirmation before deleting anything.
- If you used the InnoSetup installer, prefer the Control Panel uninstall as it handles registry and uninstaller entries more cleanly.

---

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 7 or later
- **Python**: 3.7 or higher (if not using .exe)
- **RAM**: 2 GB
- **Storage**: 1-3 GB (depending on Wikipedia downloads)
- **Internet**: Required for initial setup and online searches

### Recommended
- **OS**: Windows 10 or later
- **Python**: 3.9 or higher
- **RAM**: 4 GB+
- **Storage**: 5+ GB
- **Internet**: Always on for best experience

---

## 🌍 Wikipedia Language Support

During installation, choose your primary language for offline data:

| Language | Code | Size | Details |
|----------|------|------|---------|
| English | en | ~800 MB | Complete Wikipedia |
| Spanish | es | ~500 MB | Español |
| French | fr | ~600 MB | Français |
| German | de | ~700 MB | Deutsch |
| Italian | it | ~400 MB | Italiano |
| Portuguese | pt | ~300 MB | Português |
| Russian | ru | ~600 MB | Русский |
| Chinese | zh | ~300 MB | 中文 |
| Japanese | ja | ~250 MB | 日本語 |
| Korean | ko | ~150 MB | 한국어 |

**Note**: Additional languages can be added after installation

---

## 🔄 First Run Experience

### On First Run:
1. Installer wizard launches
2. User selects language and location
3. Dependencies automatically installed
4. Icons generated
5. Password created
6. Application launched

### On Subsequent Runs:
1. Login prompt (with password)
2. Main application launches
3. Ready to search

---

## 🛠️ Troubleshooting

### Issue: Python not found
```
❌ Error: Python is not installed or not in PATH
```
**Solution**: Install Python from https://www.python.org/ and check "Add Python to PATH"

### Issue: PyQt5 installation fails
```
⚠️ Warning: Could not install PyQt5
```
**Solution**: Run manually: `pip install PyQt5 -upgrade`

### Issue: Icon generation fails
**Solution**: Pillow library not installed. Run: `pip install Pillow`

### Issue: Password forgotten
**Solution**: Delete config.json and reinstall

---

## 📝 Configuration File

After installation, `config.json` contains:

```json
{
  "language": "en",
  "install_path": "C:\\Users\\User\\AI Bot",
  "version": "1.0",
  "first_run": false,
  "password_hash": "sha256_hash_of_password",
  "wikipedia_dumps": {
    "en": {"downloaded": true, "size": 850000000}
  }
}
```

---

## 🎯 For Developers

### Creating Portable Distribution

```bash
# 1. Build executable
python build_executable.py

# 2. Create installer (requires InnoSetup)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup.iss

# 3. Results:
#    - dist/AIBot.exe (portable)
#    - dist/AI_Bot_Setup.exe (installer)
```

### Customizing Installation

Edit `installer.py`:
- Change colors and styling
- Add/remove installation steps
- Modify language list
- Customize welcome message

---

## ✅ Verification Checklist

After successful installation, verify:

- ✅ Icons generated (check `ai_bot/gui/`)
- ✅ Desktop shortcut created (if selected)
- ✅ Password set in config.json
- ✅ Can login with password
- ✅ Application launches successfully
- ✅ Can search online and offline
- ✅ Search history stored

---

## 🚀 Next Steps

1. **Run the Application**:
   ```bash
   python run_ai_bot.py
   ```

2. **Test Online Search**:
   - Make sure you have internet connection
   - Try searching for something

3. **Test Offline Search**:
   - Go to "Offline Only" mode
   - Wikipedia data will be queried locally

4. **Create Shortcuts**:
   - Use create_shortcut.py for additional shortcuts
   - Pin application to Start menu

---

## 📞 Support

For issues or questions:
1. Check TROUBLESHOOTING.md
2. Review log files in installation directory
3. Visit project GitHub: https://github.com/yourusername/ai-bot-github

---

## 📜 License

See LICENSE file in installation directory

---

**AI Bot Installation Guide** | Professional Setup System | v1.0
