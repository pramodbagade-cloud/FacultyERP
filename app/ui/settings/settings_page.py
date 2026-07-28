"""
FacultyERP
Settings Window
---------------

Personal configuration window for FacultyERP.
"""

import customtkinter as ctk
from tkinter import messagebox
from app.ui.academic_masters.academic_masters_window import AcademicMastersWindow
from app.ui.settings.appearance_window import AppearanceWindow


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

        for widget in self.parent.winfo_children():
            widget.destroy()

        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self.parent)

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

        # ======================================================
        # HEADER
        # ======================================================

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

        # ======================================================
        # FIRST ROW
        # ======================================================

        # ------------------------------------------------------
        # MY PROFILE
        # ------------------------------------------------------

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
            text="Personal Information\nDesignation\nDepartment",
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
            pady=(10, 20)
        )

        # ------------------------------------------------------
        # MY TEACHING PORTFOLIO
        # ------------------------------------------------------

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
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self.portfolio_card,
            text="My Teaching Portfolio",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.portfolio_card,
            text="Notes\nLesson Plans\nCourse Files\nProjects",
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
            pady=(10, 20)
        )

        # ------------------------------------------------------
        # ACADEMIC MASTERS
        # ------------------------------------------------------

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
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
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
            pady=(10, 20)
        )
                # ======================================================
        # SECOND ROW
        # ======================================================

        # ------------------------------------------------------
        # FACULTY CONNECT
        # ------------------------------------------------------

        self.faculty_connect_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.faculty_connect_card.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.faculty_connect_card,
            text="📩",
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self.faculty_connect_card,
            text="Faculty Connect",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.faculty_connect_card,
            text="Intra-Mail\nWhatsApp\nNews & Notices\nAddress Diary",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.faculty_connect_card,
            text="Open",
            command=self.open_faculty_connect
        ).pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

        # ------------------------------------------------------
        # APPLICATION
        # ------------------------------------------------------

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
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
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
            pady=(10, 20)
        )

        # ------------------------------------------------------
        # APPEARANCE
        # ------------------------------------------------------

        self.appearance_card = ctk.CTkFrame(
            self.container,
            corner_radius=12
        )

        self.appearance_card.grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.appearance_card,
            text="🎨",
            font=("Segoe UI Emoji", 36)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            self.appearance_card,
            text="Appearance",
            font=self.heading_font
        ).pack()

        ctk.CTkLabel(
            self.appearance_card,
            text="Light / Dark\nThemes\nPrimary Color",
            justify="center",
            font=self.normal_font
        ).pack(
            pady=8
        )

        ctk.CTkButton(
            self.appearance_card,
            text="Open",
            command=self.open_appearance
        ).pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )
            # ==========================================================
    # CARD ACTIONS
    # ==========================================================

    def open_profile(self):

        self.placeholder("My Profile")

    def open_teaching_portfolio(self):

        messagebox.showinfo(
            "FacultyERP",
            "My Teaching Portfolio\n\n"
            "Coming Soon\n\n"
            "This module will become the faculty member's personal teaching repository.\n\n"
            "• Subjects Taught\n"
            "• Lecture Notes\n"
            "• PPTs\n"
            "• Lesson Plans\n"
            "• Course Files\n"
            "• Lab Manuals\n"
            "• Practical Files\n"
            "• Question Banks\n"
            "• Previous Year Question Papers\n"
            "• Assignments\n"
            "• Mini & Major Projects\n"
            "• Teaching Innovations\n"
            "• Student Achievements"
        )

    def open_academic_masters(self):

        AcademicMastersWindow(self.parent)

    def open_faculty_connect(self):

        messagebox.showinfo(
            "FacultyERP",
            "Faculty Connect\n\n"
            "Coming Soon\n\n"
            "Communication platform for faculty members.\n\n"
            "• Intra-Mail\n"
            "• WhatsApp Connect\n"
            "• News & Notices\n"
            "• Address Diary"
        )

    def open_application(self):

        self.placeholder("Application")

    def open_appearance(self):

        AppearanceWindow(self.parent)

    # ==========================================================
    # PLACEHOLDER
    # ==========================================================

    def placeholder(self, module):

        messagebox.showinfo(
            "FacultyERP",
            f"{module}\n\nModule will be implemented in a future release."
        )
        