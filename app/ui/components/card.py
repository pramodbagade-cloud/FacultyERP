"""
FacultyERP
Card Component
--------------

Reusable card container.
"""

import customtkinter as ctk

from app.core.constants import Colors, Dimensions


class Card(ctk.CTkFrame):
    """Reusable card."""

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            fg_color=Colors.CARD,
            corner_radius=Dimensions.BORDER_RADIUS,
            border_width=1,
            border_color=Colors.BORDER,
            **kwargs
        )