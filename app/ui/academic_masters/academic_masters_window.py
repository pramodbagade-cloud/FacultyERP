"""
FacultyERP
Academic Masters Window
-----------------------
"""

import customtkinter as ctk

from app.ui.departments.department_window import DepartmentWindow
from app.ui.course.course_window import CourseWindow
from app.ui.subject.subject_window import SubjectWindow
from app.ui.faculty.faculty_window import FacultyWindow
from app.ui.students.student_window import StudentWindow
from app.ui.academic_year.academic_year_window import AcademicYearWindow
from app.ui.semester.semester_window import SemesterWindow
from app.ui.division.division_window import DivisionWindow


class AcademicMastersWindow:
    """Academic Masters."""

    def __init__(self, parent):

        self.parent = parent

        self.title_font = ("Segoe UI", 24, "bold")

        self.heading_font = ("Segoe UI", 16, "bold")

        self.build_ui()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        #
        # Clear Workspace
        #

        for widget in self.parent.winfo_children():

            widget.destroy()

        #
        # Main Container
        #

        self.container = ctk.CTkFrame(
            self.parent
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        #
        # Header
        #

        header = ctk.CTkFrame(self.container)

        header.pack(
            fill="x",
            padx=10,
            pady=(10,20)
        )

        ctk.CTkLabel(
            header,
            text="🎓 Academic Masters",
            font=self.title_font
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,5)
        )

        ctk.CTkLabel(
            header,
            text="Manage all academic master data",
            font=("Segoe UI",12)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0,15)
        )

        #
        # Button Area
        #

        button_frame = ctk.CTkFrame(self.container)

        button_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        button_frame.grid_columnconfigure((0,1,2),weight=1)

        button_frame.grid_rowconfigure((0,1,2),weight=1)

        buttons = [

            "Departments",

            "Courses",

            "Subjects",

            "Faculty",

            "Students",

            "Academic Year",

            "Semesters",

            "Divisions"

        ]

        for index, text in enumerate(buttons):

            row = index // 3

            column = index % 3

            ctk.CTkButton(

                button_frame,

                text=text,

                height=80,

                font=("Segoe UI",16,"bold"),

                command=lambda t=text:self.open_module(t)

            ).grid(

                row=row,

                column=column,

                padx=15,

                pady=15,

                sticky="nsew"

            )

    # ==========================================================
    # OPEN MODULE
    # ==========================================================
        # ==========================================================
    # OPEN MODULE
    # ==========================================================

    def open_module(self, module):

        if module == "Departments":

            DepartmentWindow(

                self.parent

            )

            return

        elif module == "Courses":

            CourseWindow(

                self.parent

            )

            return

        elif module == "Subjects":

            SubjectWindow(

                self.parent

            )

            return

        elif module == "Faculty":

            FacultyWindow(

                self.parent

            )

            return

        elif module == "Students":

            StudentWindow(

                self.parent

            )

            return

        elif module == "Academic Year":

            AcademicYearWindow(

                self.parent

            )

            return

        elif module == "Semesters":

            SemesterWindow(

                self.parent

            )

            return

        
        elif module == "Divisions":

            DivisionWindow(
                self.parent
            )

            return