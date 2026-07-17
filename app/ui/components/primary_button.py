"""
Primary Button
"""

import customtkinter as ctk

from app.core.constants import Colors, Fonts, Dimensions


class PrimaryButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            width=Dimensions.BUTTON_WIDTH,
            height=42,
            fg_color=Colors.PRIMARY,
            hover_color=Colors.PRIMARY_DARK,
            text_color="white",
            font=Fonts.BUTTON,
            corner_radius=8,
            **kwargs
        )