"""
Form Label
"""

import customtkinter as ctk

from app.core.constants import Fonts, Colors


class FormLabel(ctk.CTkLabel):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            font=Fonts.LABEL,
            text_color=Colors.TEXT,
            anchor="w",
            **kwargs
        )