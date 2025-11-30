"""Enhanced app launcher with startup wizard check.

This is the main entry point that checks if installation is complete
and shows password login if needed.
"""
import sys
import os
import json
import hashlib
from pathlib import Path

from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class LoginDialog(QDialog):
    """Password login dialog."""

    def __init__(self):
        """Initialize login dialog."""
        super().__init__()
        self.setWindowTitle("AI Bot - Login")
        self.setGeometry(100, 100, 400, 200)
        self.authenticated = False

        layout = QVBoxLayout()

        # Title
        title = QLabel("AI Bot Login")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title)

        # Password input
        layout.addWidget(QLabel("Enter your password:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.returnPressed.connect(self.verify_password)
        layout.addWidget(self.password_input)

        # Buttons
        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.verify_password)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def verify_password(self):
        """Verify password."""
        password = self.password_input.text()

        if not password:
            QMessageBox.warning(self, "Error", "Please enter your password")
            return

        # Read stored password hash
        config_file = Path.home() / "AI Bot" / "config.json"
        if not config_file.exists():
            QMessageBox.critical(self, "Error", "Configuration not found")
            return

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)

            password_hash = hashlib.sha256(
                password.encode()
            ).hexdigest()

            if password_hash == config.get("password_hash"):
                self.authenticated = True
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Incorrect password")
                self.password_input.clear()
        except Exception as exc:  # pylint: disable=broad-except
            QMessageBox.critical(self, "Error", f"Failed to verify: {exc}")


def check_first_run():
    """Check if this is first run, show installer if needed."""
    config_file = Path.home() / "AI Bot" / "config.json"

    if not config_file.exists():
        # First run - show installer
        from installer import AIBotInstaller
        app = QApplication(sys.argv)
        installer = AIBotInstaller()
        installer.show()
        sys.exit(app.exec_())


def main():
    """Main entry point."""
    # Check installation
    check_first_run()

    # Show login if password is set
    app = QApplication(sys.argv)

    config_file = Path.home() / "AI Bot" / "config.json"
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)

        if "password_hash" in config:
            login = LoginDialog()
            if login.exec_() != QDialog.Accepted:
                sys.exit(0)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Warning: Could not read config: {exc}")

    # Launch main application
    from ai_bot.gui.main_window import AIBotGUI
    window = AIBotGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
