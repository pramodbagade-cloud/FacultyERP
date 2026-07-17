"""
Title Label
"""

import customtkinter as ctk

from app.core.constants import Fonts, Colors


class TitleLabel(ctk.CTkLabel):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            font=Fonts.TITLE,
            text_color=Colors.TEXT,
            **kwargs
        )