"""
FacultyERP
Settings Window
---------------

Personal configuration window for FacultyERP.
"""

import customtkinter as ctk
from tkinter import messagebox
from app.ui.academic_masters.academic_masters_window import AcademicMastersWindow


class SettingsWindow:
    """Settings Page."""

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.title_font = ("Segoe UI", 26, "bold")

        self.heading_font = ("Segoe UI", 18, "bold")

        self.normal_font = ("Segoe UI", 12)

        self.card_width = 260

        self.card_height = 170

        self.build_ui()

    # ==========================================================
    # BUILD USER INTERFACE
    # ==========================================================

    def build_ui(self):

        #
        # Clear Workspace
        #

        for widget in self.parent.winfo_children():

            widget.destroy()

        #
        # Configure Grid
        #

        self.parent.grid_rowconfigure(
            1,
            weight=1
        )

        self.parent.grid_columnconfigure(
            0,
            weight=1
        )

        #
        # Main Container
        #

        self.container = ctk.CTkFrame(
            self.parent
        )

        self.container.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.container.grid_columnconfigure(
            (0, 1, 2),
            weight=1,
            uniform="cards"
        )

        self.container.grid_rowconfigure(
            (1, 2),
            weight=1
        )
                # ==========================================================
        # HEADER
        # ==========================================================

        self.header_frame = ctk.CTkFrame(
            self.container,
            corner_radius=10
        )

        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            padx=10,
            pady=(10, 20)
        )

        self.header_frame.grid_columnconfigure(
            0,
            weight=1
        )

        ctk.CTkLabel(
            self.header_frame,
            text="⚙ Settings",
            font=self.title_font
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(18, 5)
        )

        ctk.CTkLabel(
            self.header_frame,
            text="Configure your FacultyERP workspace",
            font=("Segoe UI", 13)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=22,
            pady=(0, 18)
        )
                # ==========================================================
        # FIRST ROW
        # ==========================================================

        #
        # MY PROFILE
        #

        self.profile_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.profile_card.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.profile_card,
            text="👤",
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self.profile_card,
            text="My Profile",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.profile_card,
            text="Personal information\nDesignation\nDepartment",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.profile_card,
            text="Open",
            command=self.open_profile
        ).pack(
            fill="x",
            padx=20,
            pady=(10,20)
        )

        # ==========================================================
        # MY TEACHING PORTFOLIO
        # ==========================================================

        self.portfolio_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.portfolio_card.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.portfolio_card,
            text="📚",
            font=("Segoe UI Emoji",36)
        ).pack(
            pady=(20,5)
        )

        ctk.CTkLabel(
            self.portfolio_card,
            text="My Teaching Portfolio",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.portfolio_card,
            text="Subjects\nLabs\nProjects\nSeminars",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.portfolio_card,
            text="Open",
            command=self.open_teaching_portfolio
        ).pack(
            fill="x",
            padx=20,
            pady=(10,20)
        )

        # ==========================================================
        # ACADEMIC MASTERS
        # ==========================================================

        self.master_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.master_card.grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.master_card,
            text="🎓",
            font=("Segoe UI Emoji",36)
        ).pack(
            pady=(20,5)
        )

        ctk.CTkLabel(
            self.master_card,
            text="Academic Masters",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.master_card,
            text="Departments\nSubjects\nFaculty\nStudents",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.master_card,
            text="Open",
            command=self.open_academic_masters
        ).pack(
            fill="x",
            padx=20,
            pady=(10,20)
        )
                # ==========================================================
        # SECOND ROW
        # ==========================================================

        #
        # AI SETTINGS
        #

        self.ai_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.ai_card.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.ai_card,
            text="🤖",
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self.ai_card,
            text="AI Settings",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.ai_card,
            text="Prompts\nTemplates\nAI Preferences",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.ai_card,
            text="Open",
            command=self.open_ai_settings
        ).pack(
            fill="x",
            padx=20,
            pady=(10,20)
        )

        # ==========================================================
        # APPLICATION
        # ==========================================================

        self.application_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.application_card.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.application_card,
            text="⚙",
            font=("Segoe UI Emoji",36)
        ).pack(
            pady=(20,5)
        )

        ctk.CTkLabel(
            self.application_card,
            text="Application",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.application_card,
            text="Backup\nRestore\nTheme\nAbout",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.application_card,
            text="Open",
            command=self.open_application
        ).pack(
            fill="x",
            padx=20,
            pady=(10,20)
        )

        # ==========================================================
        # EMPTY CARD (Reserved for future)
        # ==========================================================

        self.empty_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.empty_card.grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.empty_card,
            text="Coming Soon",
            font=("Segoe UI",16,"bold")
        ).pack(
            expand=True
        )
        # ==========================================================
    # CARD ACTIONS
    # ==========================================================

    def open_profile(self):

        self.placeholder("My Profile")

    def open_teaching_portfolio(self):

        self.placeholder("My Teaching Portfolio")

    def open_academic_masters(self):

        AcademicMastersWindow(self.parent)

    def open_ai_settings(self):

        self.placeholder("AI Settings")

    def open_application(self):

        self.placeholder("Application")

    # ==========================================================
    # PLACEHOLDER
    # ==========================================================

    def placeholder(self, module):

        messagebox.showinfo(

            "FacultyERP",

            f"{module}\n\nModule will be implemented in the next phase."

        )

        