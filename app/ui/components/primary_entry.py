"""
Primary Entry
"""

import customtkinter as ctk

from app.core.constants import Fonts, Dimensions


class PrimaryEntry(ctk.CTkEntry):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            width=Dimensions.ENTRY_WIDTH,
            height=40,
            font=Fonts.LABEL,
            corner_radius=8,
            **kwargs
        )