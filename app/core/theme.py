"""
FacultyERP
Theme Manager
-------------
"""

import customtkinter as ctk

from app.repositories.app_settings_repository import AppSettingsRepository


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

        self.appearance_mode = (
            AppSettingsRepository.get_setting(
                "appearance_mode"
            )
            or "Light"
        )

        self.current_theme = (
            AppSettingsRepository.get_setting(
                "theme_name"
            )
            or "Professional Blue"
        )

    # ==========================================================
    # APPLY
    # ==========================================================

    def apply(self):

        ctk.set_appearance_mode(
            self.appearance_mode
        )

        ctk.set_default_color_theme(
            self.THEMES.get(
                self.current_theme,
                "blue"
            )
        )

    # ==========================================================
    # LOAD SETTINGS
    # ==========================================================

    def load_settings(self):

        self.appearance_mode = (
            AppSettingsRepository.get_setting(
                "appearance_mode"
            )
            or "Light"
        )

        self.current_theme = (
            AppSettingsRepository.get_setting(
                "theme_name"
            )
            or "Professional Blue"
        )

        self.apply()

    # ==========================================================
    # SAVE SETTINGS
    # ==========================================================

    def save_settings(self):

        AppSettingsRepository.set_setting(

            "appearance_mode",

            self.appearance_mode

        )

        AppSettingsRepository.set_setting(

            "theme_name",

            self.current_theme

        )

    # ==========================================================
    # AVAILABLE THEMES
    # ==========================================================

    def get_available_themes(self):

        return list(
            self.THEMES.keys()
        )

    # ==========================================================
    # CURRENT THEME
    # ==========================================================

    def get_current_theme(self):

        return self.current_theme

    # ==========================================================
    # SET THEME
    # ==========================================================

    def set_theme(

        self,

        theme

    ):

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