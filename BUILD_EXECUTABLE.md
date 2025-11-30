# Building Standalone Executables

This guide shows how to create a standalone `.exe` file for Windows or executable for other platforms.

## Prerequisites

Install PyInstaller:
```powershell
pip install pyinstaller
```

## Creating Windows Executable (.exe)

### Option 1: Simple (Recommended for First-Time)

```powershell
cd C:\Users\rabin\OneDrive\Documents\GitHub\ai-bot-github
pyinstaller --onefile --windowed --name "AI Bot" run_ai_bot.py
```

This creates: `dist/AI Bot.exe`

### Option 2: With Icon and Metadata

```powershell
# First, get/create an icon file (AI Bot Icon.ico)
pyinstaller --onefile `
    --windowed `
    --name "AI Bot" `
    --icon "icon.ico" `
    --add-data "ai_bot:ai_bot" `
    --add-data "data:data" `
    --add-data "config.json:." `
    run_ai_bot.py
```

### Option 3: Full Setup (with console fallback)

Create a file called `build_exe.py`:

```python
import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'run_ai_bot.py',
    '--onefile',
    '--windowed',
    '--name=AI Bot',
    '--icon=icon.ico',
    '--add-data=ai_bot:ai_bot',
    '--add-data=data:data',
    '--add-data=config.json:.',
    '--hidden-import=PyQt5',
    '--hidden-import=requests',
    '--collect-all=PyQt5',
])

print("Build complete! Executable in: dist/AI Bot.exe")
```

Then run:
```powershell
python build_exe.py
```

---

## Output Structure

After building, you'll have:
```
dist/
├── AI Bot.exe          ← Standalone executable
└── _internal/          ← Dependencies (don't delete)

build/                  ← Temporary files (can delete)
```

---

## Using the Executable

### First Run:
1. Create a folder: `C:\Program Files\AI Bot`
2. Copy `dist/` folder contents to `C:\Program Files\AI Bot\`
3. Double-click `AI Bot.exe`

### Create Desktop Shortcut:
1. Right-click `AI Bot.exe`
2. Select "Send to" > "Desktop (create shortcut)"
3. (Optional) Edit shortcut properties to customize

### Or run from Command Line:
```powershell
C:\Program Files\AI Bot\AI Bot.exe
```

---

## Advanced: Creating Installer

Install NSIS:
```powershell
choco install nsis  # If you have Chocolatey
```

Or download from: https://nsis.sourceforge.io/

Create installer script `installer.nsi`:

```nsis
; AI Bot Installer Script

!include "MUI2.nsh"

; Installer name
OutFile "AI-Bot-Installer.exe"
InstallDir "$PROGRAMFILES\AI Bot"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

; Files to install
Section "Install"
    SetOutPath "$INSTDIR"
    File /r "dist\*.*"
    
    ; Create Start Menu shortcut
    CreateDirectory "$SMPROGRAMS\AI Bot"
    CreateShortcut "$SMPROGRAMS\AI Bot\AI Bot.lnk" "$INSTDIR\AI Bot.exe"
    CreateShortcut "$SMPROGRAMS\AI Bot\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    
    ; Create Desktop shortcut
    CreateShortcut "$DESKTOP\AI Bot.lnk" "$INSTDIR\AI Bot.exe"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\*.*"
    RMDir /r "$INSTDIR"
    Delete "$DESKTOP\AI Bot.lnk"
    RMDir /r "$SMPROGRAMS\AI Bot"
SectionEnd
```

Build installer:
```powershell
makensis installer.nsi
```

Output: `AI-Bot-Installer.exe`

---

## Troubleshooting Build Issues

### Issue: "Module not found"
**Solution**: Add to PyInstaller command:
```powershell
--hidden-import=module_name
```

### Issue: Executable is very large (>200MB)
This is normal with PyQt5. To reduce:
```powershell
pyinstaller --onefile --windowed --noupx run_ai_bot.py
```

### Issue: "cannot import name 'QXxx'"
**Solution**: Add:
```powershell
--collect-all=PyQt5
```

### Issue: Offline data not included
**Solution**: Add to command:
```powershell
--add-data "data:data"
```

---

## macOS Executable

```bash
pyinstaller --onefile --windowed --name "AI Bot" run_ai_bot.py
```

Output: `dist/AI Bot.app`

To create DMG (installer):
```bash
pip install create-dmg
create-dmg "dist/AI Bot.app"
```

---

## Linux Executable

```bash
pyinstaller --onefile --windowed --name "ai-bot" run_ai_bot.py
```

Output: `dist/ai-bot`

To create AppImage:
```bash
pip install AppImage
```

---

## Distribution Checklist

Before distributing your executable:

- [ ] Tested on target OS
- [ ] All dependencies included
- [ ] Config files included
- [ ] Data directory included
- [ ] Icon present
- [ ] Version number updated
- [ ] README included
- [ ] License included
- [ ] Works without internet (offline mode)

---

## Portable Version

To create a portable USB version:

1. Build executable: `pyinstaller --onefile run_ai_bot.py`
2. Copy to USB:
   - `dist/AI Bot.exe` (or executable)
   - `config.json`
   - `data/` folder
   - `README.md`
   - `QUICK_REFERENCE.md`

3. Users can run directly from USB without installation

---

## Performance Optimization

For faster startup:

```powershell
pyinstaller --onefile `
    --windowed `
    --noupx `
    --optimize=2 `
    run_ai_bot.py
```

---

## Code Signing (Optional, for Distribution)

To sign your executable:
```powershell
# Generate certificate (requires resources)
# Then sign:
signtool sign /f certificate.pfx /p password /t http://timestamp.server AI Box.exe
```

---

## Version Management

Before building, update version in:
- `ai_bot/__init__.py`: `__version__ = "1.1.0"`
- `setup.py`: `version="1.1.0"`

Then build with version tag:
```powershell
pyinstaller --version-file=version.txt --onefile run_ai_bot.py
```

---

## Distribution Methods

### Method 1: Direct Download
- Host `AI-Bot-Installer.exe` on GitHub Releases
- Users download and run

### Method 2: GitHub Actions
Automate builds - see `.github/workflows/build.yml`

### Method 3: Chocolatey Package
- Create Chocolatey package for easy install
- `choco install ai-bot`

### Method 4: Windows Store
- Contact Microsoft Store for listing
- Advanced deployment method

---

## Verification After Build

```powershell
# Check executable details
wmic datafile where name="C:\\Path\\AI Bot.exe" get Description

# Check file size
Get-Item "dist/AI Bot.exe" | Select-Object Length

# Test execution
& "dist/AI Bot.exe"  # Should launch without errors
```

---

## Cleanup After Build

```powershell
# Remove build artifacts
Remove-Item build -Recurse
Remove-Item dist -Recurse  # Optional - contains your executable!
Remove-Item *.spec

# Keep dist/ for distribution
```

---

## Next Steps

1. Build executable: `pyinstaller --onefile --windowed run_ai_bot.py`
2. Test thoroughly on clean Windows installation
3. Create installer (optional)
4. Distribute via GitHub, website, or installer
5. Collect user feedback

---

**Ready to deploy? You now have a standalone application! 🚀**
