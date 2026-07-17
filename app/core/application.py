"""
FacultyERP Application Controller
---------------------------------

Responsible for:

1. Initializing the application
2. Loading configuration
3. Initializing database
4. Loading theme
5. Opening Login Window
"""

import customtkinter as ctk

from app.core.config import AppConfig
from app.core.theme import ThemeManager
from app.core.database import DatabaseManager

from app.ui.login.login_window import LoginWindow


class FacultyERPApplication:
    """Main application controller."""

    def __init__(self):

        # Appearance
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        # Load configuration
        self.config = AppConfig()

        # Theme
        self.theme = ThemeManager()

        # Database
        self.database = DatabaseManager()

    def run(self):
        """Launch the application."""

        login = LoginWindow(self)

        login.mainloop()