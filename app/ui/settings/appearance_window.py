"""
FacultyERP
Appearance Settings
-------------------
Professional Appearance Configuration Window
"""

import customtkinter as ctk

from tkinter import colorchooser
from tkinter import messagebox

from app.core.theme import ThemeManager


class AppearanceWindow(ctk.CTkToplevel):
    """Appearance Settings Window."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.theme_manager = ThemeManager()

        self.title("Appearance Settings")

        self.geometry("900x600")

        self.minsize(
            900,
            600
        )

        self.transient(parent)

        self.grab_set()

        self.primary_color = "#2563EB"

        self.mode_var = ctk.StringVar(
            value=self.theme_manager.appearance_mode
        )

        self.theme_var = ctk.StringVar(
            value=self.theme_manager.get_current_theme()
        )

        self.build_ui()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        self.grid_rowconfigure(
            1,
            weight=1
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )

        # ======================================================
        # HEADER
        # ======================================================

        header = ctk.CTkFrame(
            self,
            corner_radius=10
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        header.grid_columnconfigure(
            0,
            weight=1
        )

        ctk.CTkLabel(
            header,
            text="Appearance Settings",
            font=("Segoe UI", 24, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(18, 5)
        )

        ctk.CTkLabel(
            header,
            text="Customize the appearance of FacultyERP.",
            font=("Segoe UI", 13)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(0, 18)
        )

        # ======================================================
        # CONTENT
        # ======================================================

        self.content = ctk.CTkFrame(self)

        self.content.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.content.grid_rowconfigure(
            0,
            weight=1
        )

        self.content.grid_columnconfigure(
            0,
            weight=1
        )

        self.content.grid_columnconfigure(
            1,
            weight=1
        )

        # ======================================================
        # LEFT PANEL
        # ======================================================

        self.left_panel = ctk.CTkFrame(
            self.content,
            corner_radius=10
        )

        self.left_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=20
        )

        # ------------------------------------------------------
        # APPEARANCE MODE
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.left_panel,
            text="Appearance Mode",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkRadioButton(
            self.left_panel,
            text="Light",
            variable=self.mode_var,
            value="Light"
        ).pack(
            anchor="w",
            padx=30,
            pady=5
        )

        ctk.CTkRadioButton(
            self.left_panel,
            text="Dark",
            variable=self.mode_var,
            value="Dark"
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

        # ------------------------------------------------------
        # THEME
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.left_panel,
            text="Application Theme",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 10)
        )

        self.theme_menu = ctk.CTkOptionMenu(
            self.left_panel,
            values=self.theme_manager.get_available_themes(),
            variable=self.theme_var,
            width=220
        )

        self.theme_menu.pack(
            padx=20,
            pady=(0, 20)
        )

        # ------------------------------------------------------
        # ACCENT COLOR
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.left_panel,
            text="Primary Accent Color",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 10)
        )

        self.color_preview = ctk.CTkFrame(
            self.left_panel,
            width=90,
            height=40,
            fg_color=self.primary_color,
            corner_radius=8
        )

        self.color_preview.pack(
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkButton(
            self.left_panel,
            text="Choose Color",
            width=180,
            command=self.pick_color
        ).pack(
            padx=20,
            pady=(0, 20)
        )

        info = (
            "• Select Light or Dark mode.\n"
            "• Choose the application theme.\n"
            "• Pick an accent color.\n"
            "• Click Apply to save."
        )

        ctk.CTkLabel(
            self.left_panel,
            text=info,
            justify="left",
            wraplength=240,
            font=("Segoe UI", 11)
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 20)
        )

        # ======================================================
        # RIGHT PREVIEW PANEL
        # ======================================================

        self.preview_panel = ctk.CTkFrame(
            self.content,
            corner_radius=10
        )

        self.preview_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=20
        )

        self.build_preview()
        self.create_button_bar()
            # ==========================================================
    # BUILD PREVIEW
    # ==========================================================

    def build_preview(self):

        ctk.CTkLabel(
            self.preview_panel,
            text="Live Preview",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        self.preview_window = ctk.CTkFrame(
            self.preview_panel,
            width=360,
            height=430,
            corner_radius=10
        )

        self.preview_window.pack(
            padx=20,
            pady=(0, 20),
            fill="both",
            expand=True
        )

        self.preview_window.pack_propagate(False)

        # ------------------------------------------------------
        # Preview Header
        # ------------------------------------------------------

        self.preview_header = ctk.CTkFrame(
            self.preview_window,
            height=55,
            fg_color=self.primary_color,
            corner_radius=0
        )

        self.preview_header.pack(
            fill="x"
        )

        self.preview_header.pack_propagate(False)

        ctk.CTkLabel(
            self.preview_header,
            text="FacultyERP",
            text_color="white",
            font=("Segoe UI", 18, "bold")
        ).pack(
            side="left",
            padx=20,
            pady=15
        )

        # ------------------------------------------------------
        # Preview Body
        # ------------------------------------------------------

        body = ctk.CTkFrame(
            self.preview_window,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True
        )

        # ------------------------------------------------------
        # Sidebar
        # ------------------------------------------------------

        self.preview_sidebar = ctk.CTkFrame(
            body,
            width=90,
            fg_color=self.primary_color,
            corner_radius=0
        )

        self.preview_sidebar.pack(
            side="left",
            fill="y"
        )

        self.preview_sidebar.pack_propagate(False)

        for item in (
            "Dashboard",
            "Faculty",
            "Subjects",
            "Students",
            "Reports"
        ):

            ctk.CTkLabel(
                self.preview_sidebar,
                text=item,
                text_color="white",
                font=("Segoe UI", 12)
            ).pack(
                anchor="w",
                padx=12,
                pady=10
            )

        # ------------------------------------------------------
        # Dashboard Area
        # ------------------------------------------------------

        dashboard = ctk.CTkFrame(
            body,
            fg_color="transparent"
        )

        dashboard.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        ctk.CTkLabel(
            dashboard,
            text="Dashboard",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            dashboard,
            text="Preview of current application appearance.",
            font=("Segoe UI", 11)
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        for title in (
            "Faculty",
            "Departments",
            "Courses"
        ):

            card = ctk.CTkFrame(
                dashboard,
                height=60,
                corner_radius=8
            )

            card.pack(
                fill="x",
                pady=8
            )

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14, "bold")
            ).pack(
                anchor="w",
                padx=15,
                pady=(10, 2)
            )

            ctk.CTkLabel(
                card,
                text="Sample information",
                font=("Segoe UI", 11)
            ).pack(
                anchor="w",
                padx=15
            )

    # ==========================================================
    # PICK COLOR
    # ==========================================================

    def pick_color(self):

        color = colorchooser.askcolor(
            color=self.primary_color
        )[1]

        if color is None:

            return

        self.primary_color = color

        self.color_preview.configure(
            fg_color=color
        )

        self.preview_header.configure(
            fg_color=color
        )

        self.preview_sidebar.configure(
            fg_color=color
        )
            # ==========================================================
    # APPLY THEME
    # ==========================================================

    def apply_theme(self):

        if self.mode_var.get() == "Dark":

            self.theme_manager.set_dark()

        else:

            self.theme_manager.set_light()

        self.theme_manager.set_theme(
            self.theme_var.get()
        )

        messagebox.showinfo(
            "FacultyERP",
            (
                "Appearance settings have been saved.\n\n"
                "Restart FacultyERP to apply the selected theme."
            )
        )

        self.destroy()

    # ==========================================================
    # CLOSE WINDOW
    # ==========================================================

    def close_window(self):

        self.destroy()

    # ==========================================================
    # BUTTON BAR
    # ==========================================================

    def create_button_bar(self):

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=2,
            column=0,
            sticky="e",
            padx=20,
            pady=(0, 20)
        )

        ctk.CTkButton(
            button_frame,
            text="Apply",
            width=120,
            command=self.apply_theme
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="Close",
            width=120,
            command=self.close_window
        ).pack(
            side="left"
        )
