"""
FacultyERP
Theme Manager
-------------
Application Theme Manager
UI Design Standards
"""

import customtkinter as ctk
from app.repositories.app_settings_repository import AppSettingsRepository


class UITheme:
    # ==========================================================
    # FONT FAMILY
    # ==========================================================
    FONT_FAMILY = "Segoe UI"

    # ==========================================================
    # FONTS
    # ==========================================================
    TITLE_FONT = (FONT_FAMILY, 24, "bold")
    HEADER_FONT = (FONT_FAMILY, 20, "bold")
    SECTION_FONT = (FONT_FAMILY, 16, "bold")
    LABEL_FONT = (FONT_FAMILY, 12)
    LABEL_BOLD_FONT = (FONT_FAMILY, 12, "bold")
    BUTTON_FONT = (FONT_FAMILY, 12)
    GRID_HEADER_FONT = (FONT_FAMILY, 12, "bold")
    STATUS_FONT = (FONT_FAMILY, 11)
    SMALL_FONT = (FONT_FAMILY, 10)

    # ==========================================================
    # STANDARD CONTROL SIZES
    # ==========================================================
    BUTTON_HEIGHT = 36
    ENTRY_WIDTH = 170
    COMBO_WIDTH = 170
    LARGE_COMBO_WIDTH = 260
    SMALL_BUTTON_WIDTH = 110
    MEDIUM_BUTTON_WIDTH = 150
    LARGE_BUTTON_WIDTH = 220

    # ==========================================================
    # STANDARD PADDING
    # ==========================================================
    WINDOW_PADDING = 15
    FRAME_PADDING = 10
    CONTROL_PADX = 10
    CONTROL_PADY = 8
    SECTION_SPACING = 15

    # ==========================================================
    # STANDARD WINDOW SIZES
    # ==========================================================
    SMALL_WINDOW = (900, 600)
    MEDIUM_WINDOW = (1200, 750)
    LARGE_WINDOW = (1500, 850)


class ThemeManager:
    """Application theme manager."""

    THEMES = {
        "Professional Blue": "blue",
        "NAAC Green": "green",
        "Midnight": "dark-blue"
    }

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================
    def __init__(self):
        self.appearance_mode = AppSettingsRepository.get_setting("appearance_mode") or "Light"
        self.current_theme = AppSettingsRepository.get_setting("theme_name") or "Professional Blue"

    # ==========================================================
    # APPLY
    # ==========================================================
    def apply(self):
        ctk.set_appearance_mode(self.appearance_mode)
        ctk.set_default_color_theme(self.THEMES.get(self.current_theme, "blue"))

    # ==========================================================
    # LOAD SETTINGS
    # ==========================================================
    def load_settings(self):
        self.appearance_mode = AppSettingsRepository.get_setting("appearance_mode") or "Light"
        self.current_theme = AppSettingsRepository.get_setting("theme_name") or "Professional Blue"
        self.apply()

    # ==========================================================
    # SAVE SETTINGS
    # ==========================================================
    def save_settings(self):
        AppSettingsRepository.set_setting("appearance_mode", self.appearance_mode)
        AppSettingsRepository.set_setting("theme_name", self.current_theme)

    # ==========================================================
    # AVAILABLE THEMES
    # ==========================================================
    def get_available_themes(self):
        return list(self.THEMES.keys())

    # ==========================================================
    # CURRENT THEME
    # ==========================================================
    def get_current_theme(self):
        return self.current_theme

    # ==========================================================
    # SET THEME
    # ==========================================================
    def set_theme(self, theme):
        if theme not in self.THEMES:
            return
        self.current_theme = theme
        self.save_settings()
        self.apply()

    # ==========================================================
    # SET LIGHT
    # ==========================================================
    def set_light(self):
        self.appearance_mode = "Light"
        self.save_settings()
        self.apply()

    # ==========================================================
    # SET DARK
    # ==========================================================
    def set_dark(self):
        self.appearance_mode = "Dark"
        self.save_settings()
        self.apply()

    # ==========================================================
    # GET APPEARANCE MODE
    # ==========================================================
    def get_appearance_mode(self):
        return self.appearance_mode

    # ==========================================================
    # RESET DEFAULTS
    # ==========================================================
    def reset_defaults(self):
        self.appearance_mode = "Light"
        self.current_theme = "Professional Blue"
        self.save_settings()
        self.apply()