"""
Secondary Button
"""

import customtkinter as ctk

from app.core.constants import Fonts, Colors


class SecondaryButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            fg_color="transparent",
            hover=False,
            text_color=Colors.PRIMARY,
            font=Fonts.SMALL,
            border_width=0,
            **kwargs
        )