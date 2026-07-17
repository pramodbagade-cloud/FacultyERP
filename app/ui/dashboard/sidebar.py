"""
FacultyERP
Sidebar
--------
"""

import customtkinter as ctk
from tkinter import messagebox

from app.core.session import Session

from app.ui.departments.department_window import DepartmentWindow


class Sidebar:
    """Left Navigation Panel"""

    def __init__(self, parent, dashboard):

        self.parent = parent

        self.dashboard = dashboard

        self.width = 270

        self.build()

    # ==========================================================
    # BUILD
    # ==========================================================

    def build(self):

        self.frame = ctk.CTkScrollableFrame(

            self.parent,

            width=self.width,

            corner_radius=0

        )

        self.frame.grid(

            row=0,

            column=0,

            sticky="ns"

        )

        self.frame.grid_propagate(False)

        self.build_title()

        self.build_dashboard()

        self.build_academic_masters()

        self.build_academics()

        self.build_student_mentoring()

        self.build_course_file()

        self.build_accreditation()

        self.build_portfolios()

        self.build_administration()

        self.build_system()

    # ==========================================================
    # TITLE
    # ==========================================================

    def build_title(self):

        ctk.CTkLabel(

            self.frame,

            text="FacultyERP",

            font=("Segoe UI",22,"bold")

        ).pack(

            pady=(15,0)

        )

        ctk.CTkLabel(

            self.frame,

            text="Teaching, Assessment\n& Accreditation",

            justify="center"

        ).pack(

            pady=(0,20)

        )

    # ==========================================================
    # DASHBOARD
    # ==========================================================

    def build_dashboard(self):

        ctk.CTkButton(

            self.frame,

            text="🏠 Dashboard",

            anchor="w",

            command=self.dashboard.workspace.show_home

        ).pack(

            fill="x",

            padx=10,

            pady=(0,10)

        )