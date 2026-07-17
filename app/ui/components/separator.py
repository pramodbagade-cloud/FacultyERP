"""
Separator
"""

import customtkinter as ctk

from app.core.constants import Colors


class Separator(ctk.CTkFrame):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            height=1,
            fg_color=Colors.BORDER,
            **kwargs
        )