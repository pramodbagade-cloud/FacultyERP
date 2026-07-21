"""
FacultyERP
Application Controller
"""

import customtkinter as ctk

from app.core.config import AppConfig
from app.core.theme import ThemeManager
from app.core.database import DatabaseManager
from app.core.logger import AppLogger

from app.ui.login.login_window import LoginWindow


class FacultyERP:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title(
            f"{AppConfig.APP_NAME} {AppConfig.VERSION}"
        )

        self.root.geometry(
            f"{AppConfig.WINDOW_WIDTH}x{AppConfig.WINDOW_HEIGHT}"
        )

        self.root.minsize(
            AppConfig.MIN_WIDTH,
            AppConfig.MIN_HEIGHT
        )

        AppLogger.initialize()

        DatabaseManager.initialize()

        theme_manager = ThemeManager()

        theme_manager.load_settings()

    def run(self):

        LoginWindow(self.root)

        self.root.mainloop()