"""Create desktop shortcut for AI Bot on Windows.

Run this once to create a convenient desktop shortcut.
"""
import os
from pathlib import Path

try:
    from win32com.client import Dispatch
except ImportError:
    print("Installing pywin32...")
    os.system("pip install pywin32")
    from win32com.client import Dispatch


def create_desktop_shortcut() -> bool:
    """Create a Windows desktop shortcut for AI Bot.

    Returns:
        True if shortcut was created successfully, False otherwise.
    """
    # Get paths
    script_dir = Path(__file__).parent.absolute()
    desktop = Path.home() / "Desktop"
    shortcut_path = desktop / "AI Bot.lnk"

    # Batch file path
    batch_file = script_dir / "run_ai_bot.bat"

    if not batch_file.exists():
        print(f"Error: {batch_file} not found!")
        return False

    try:
        # Create shortcut using Windows COM
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.TargetPath = str(batch_file)
        shortcut.WorkingDirectory = str(script_dir)
        icon_path = str(script_dir / "ai_bot" / "gui" / "icon.ico")
        shortcut.IconLocation = icon_path
        shortcut.Description = "AI Bot - Hybrid Search Engine"
        shortcut.save()

        print(f"✓ Desktop shortcut created: {shortcut_path}")
        return True

    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error creating shortcut: {exc}")
        print("\nManual workaround:")
        print(f"1. Right-click on {batch_file}")
        print("2. Select 'Send to' > 'Desktop (create shortcut)'")
        return False


if __name__ == "__main__":
    print("AI Bot - Desktop Shortcut Creator")
    print("=" * 50)
    create_desktop_shortcut()
    print("Done!")
