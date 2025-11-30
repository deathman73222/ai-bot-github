"""Main entry point for AI Bot application.

Launches the graphical user interface for the AI Bot hybrid search engine.
"""
from ai_bot.gui.main_window import main
import sys
import os

# Add parent directory to path for module imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    main()
