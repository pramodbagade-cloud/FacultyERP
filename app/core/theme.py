"""
FacultyERP
Theme Manager
-------------

Handles application appearance.
"""

import customtkinter as ctk


class ThemeManager:
    """Application theme manager."""

    def __init__(self):
        self.appearance_mode = "Light"
        self.color_theme = "blue"

    def apply(self):
        """Apply application theme."""

        ctk.set_appearance_mode(self.appearance_mode)
        ctk.set_default_color_theme(self.color_theme)

    def set_dark(self):
        self.appearance_mode = "Dark"
        self.apply()

    def set_light(self):
        self.appearance_mode = "Light"
        self.apply()