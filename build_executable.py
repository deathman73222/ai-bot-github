"""Build AI Bot as standalone Windows executable.

Creates a self-contained .exe file using PyInstaller.
"""
import os
import sys
import subprocess
from pathlib import Path


def build_executable() -> bool:
    """Build the AI Bot executable.

    Returns:
        True if build successful, False otherwise.
    """
    # Check if PyInstaller is installed
    try:
        import PyInstaller as pi  # noqa: F401
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "PyInstaller", "pywin32"
        ])

    project_dir = Path(__file__).parent
    icon_path = project_dir / "ai_bot" / "gui" / "icon.ico"

    # Create icon if it doesn't exist
    if not icon_path.exists():
        print("Creating icon...")
        try:
            from create_icon import create_ai_bot_icon
            create_ai_bot_icon()
        except Exception as exc:  # pylint: disable=broad-except
            print(f"Warning: Could not create icon: {exc}")

    print("\nBuilding AI Bot executable...")
    print("This may take a few minutes...\n")

    # PyInstaller command
    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=AIBot",
        f"--icon={icon_path}",
        "--add-data=requirements.txt:.",
        "--add-data=config.json:.",
        f"--distpath={project_dir}/dist",
        f"--buildpath={project_dir}/build",
        f"--specpath={project_dir}/build",
        str(project_dir / "run_ai_bot.py")
    ]

    try:
        subprocess.run(pyinstaller_cmd, check=True)
        print("\n✓ Build successful!")
        print(f"✓ Executable created: {project_dir}/dist/AIBot.exe")
        print("\nYou can now distribute this file to users.")
        return True
    except subprocess.CalledProcessError as exc:
        print(f"\n❌ Build failed: {exc}")
        return False


def build_installer() -> None:
    """Build an installer package."""
    print("\n" + "="*60)
    print("AI Bot Installer Package Builder")
    print("="*60 + "\n")

    project_dir = Path(__file__).parent

    # First build the executable
    if not build_executable():
        return

    print("\n✓ AI Bot executable is ready for distribution!")
    print("\nTo create a professional installer:")
    print("  1. Install InnoSetup from https://jrsoftware.org/")
    print("  2. Use the provided .iss script to create installer")
    print("  3. This will create a Windows installer package")


if __name__ == "__main__":
    try:
        build_installer()
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error: {exc}")
        sys.exit(1)
