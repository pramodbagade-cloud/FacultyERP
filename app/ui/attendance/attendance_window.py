"""
FacultyERP
Attendance Window
-----------------

Daily attendance management.
"""

import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


class AttendanceWindow:
    """Attendance Module."""

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def __init__(
        self,
        parent,
        subject_name="Heat Transfer",
        semester="V",
        lecture_no=1,
        topic="Introduction"
    ):

        self.parent = parent

        self.subject_name = subject_name

        self.semester = semester

        self.lecture_no = lecture_no

        self.topic = topic

        self.title_font = ("Segoe UI", 24, "bold")

        self.heading_font = ("Segoe UI", 16, "bold")

        self.normal_font = ("Segoe UI", 12)

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
                # ==========================================================
        # HEADER
        # ==========================================================

        self.header_frame = ctk.CTkFrame(
            self.container,
            corner_radius=10
        )

        self.header_frame.pack(
            fill="x",
            padx=10,
            pady=(10, 15)
        )

        ctk.CTkLabel(
            self.header_frame,
            text="📋 Attendance",
            font=self.title_font
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            self.header_frame,
            text=f"Subject : {self.subject_name}",
            font=self.heading_font
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=20
        )

        ctk.CTkLabel(
            self.header_frame,
            text=f"Semester : {self.semester}",
            font=self.normal_font
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=20,
            pady=(0, 15)
        )

        #
        # Lecture Information
        #

        self.info_frame = ctk.CTkFrame(
            self.container
        )

        self.info_frame.pack(
            fill="x",
            padx=10,
            pady=(0, 15)
        )

        #
        # Date
        #

        ctk.CTkLabel(
            self.info_frame,
            text="Date"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.lbl_date = ctk.CTkLabel(
            self.info_frame,
            text="15-Jul-2026"
        )

        self.lbl_date.grid(
            row=0,
            column=1,
            padx=10,
            sticky="w"
        )

        #
        # Lecture No
        #

        ctk.CTkLabel(
            self.info_frame,
            text="Lecture"
        ).grid(
            row=0,
            column=2,
            padx=(40, 10),
            sticky="w"
        )

        self.lbl_lecture = ctk.CTkLabel(
            self.info_frame,
            text=str(self.lecture_no)
        )

        self.lbl_lecture.grid(
            row=0,
            column=3,
            padx=10,
            sticky="w"
        )


        #
        # Topic
        #

        ctk.CTkLabel(
            self.info_frame,
            text="Topic"
        ).grid(
            row=1,
            column=0,
            padx=15,
            pady=(0, 15),
            sticky="w"
        )

        self.lbl_topic = ctk.CTkLabel(
            self.info_frame,
            text=self.topic
        )

        self.lbl_topic.grid(
            row=1,
            column=1,
            columnspan=3,
            sticky="w",
            padx=10
        )
                # ==========================================================
        # ATTENDANCE TOOLBAR
        # ==========================================================

        self.toolbar = ctk.CTkFrame(
            self.container
        )

        self.toolbar.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        self.mark_all_var = ctk.BooleanVar(value=True)

        self.mark_all = ctk.CTkCheckBox(
            self.toolbar,
            text="Mark All Present",
            variable=self.mark_all_var,
            command=self.mark_all_present
        )

        self.mark_all.pack(
            side="left",
            padx=15,
            pady=12
        )

        self.search_entry = ctk.CTkEntry(
            self.toolbar,
            width=220,
            placeholder_text="Search Student..."
        )

        self.search_entry.pack(
            side="right",
            padx=15,
            pady=10
        )
                # ==========================================================
        # STUDENT LIST
        # ==========================================================

        self.student_frame = ctk.CTkScrollableFrame(
            self.container,
            height=420
        )

        self.student_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0,15)
        )

        #
        # Column Heading
        #

        ctk.CTkLabel(
            self.student_frame,
            text="Roll",
            font=self.heading_font,
            width=60
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        ctk.CTkLabel(
            self.student_frame,
            text="Student Name",
            font=self.heading_font,
            width=300
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="w"
        )

        ctk.CTkLabel(
            self.student_frame,
            text="Present",
            font=self.heading_font
        ).grid(
            row=0,
            column=2,
            padx=20,
            pady=10
        )

        #
        # Temporary Student Data
        #

        self.student_checks = []

        dummy_students = [

            ("01", "Amit S. Patil"),

            ("02", "Neha R. Joshi"),

            ("03", "Rahul P. Shinde"),

            ("04", "Pooja M. Pawar"),

            ("05", "Rohan V. Jadhav")

        ]

        for row, student in enumerate(dummy_students, start=1):

            roll, name = student

            ctk.CTkLabel(

                self.student_frame,

                text=roll,

                width=60

            ).grid(

                row=row,

                column=0,

                padx=10,

                pady=6,

                sticky="w"

            )

            ctk.CTkLabel(

                self.student_frame,

                text=name,

                anchor="w",

                width=300

            ).grid(

                row=row,

                column=1,

                padx=10,

                pady=6,

                sticky="w"

            )

            var = ctk.BooleanVar(value=True)

            chk = ctk.CTkCheckBox(

                self.student_frame,

                text="",

                variable=var

            )

            chk.grid(

                row=row,

                column=2,

                padx=20,

                pady=6

            )

            self.student_checks.append(var)
                    # ==========================================================
        # SUMMARY
        # ==========================================================

        self.summary_frame = ctk.CTkFrame(
            self.container
        )

        self.summary_frame.pack(
            fill="x",
            padx=10,
            pady=(0, 15)
        )

        self.lbl_present = ctk.CTkLabel(
            self.summary_frame,
            text="Present : 5",
            font=("Segoe UI", 13, "bold")
        )

        self.lbl_present.pack(
            side="left",
            padx=20,
            pady=12
        )

        self.lbl_absent = ctk.CTkLabel(
            self.summary_frame,
            text="Absent : 0",
            font=("Segoe UI", 13, "bold")
        )

        self.lbl_absent.pack(
            side="left",
            padx=20
        )

        self.lbl_percentage = ctk.CTkLabel(
            self.summary_frame,
            text="Attendance : 100 %",
            font=("Segoe UI", 13, "bold")
        )

        self.lbl_percentage.pack(
            side="right",
            padx=20
        )

        # ==========================================================
        # SAVE BUTTON
        # ==========================================================

        self.save_button = ctk.CTkButton(
            self.container,
            text="💾 Save Attendance",
            height=45,
            font=("Segoe UI", 16, "bold"),
            command=self.save_attendance
        )

        self.save_button.pack(
            pady=(0, 20)
        )
            # ==========================================================
    # SAVE ATTENDANCE
    # ==========================================================

    def save_attendance(self):

        present = 0

        absent = 0

        for student in self.student_checks:

            if student.get():

                present += 1

            else:

                absent += 1

        messagebox.showinfo(

            "Attendance",

            f"Attendance Saved\n\n"

            f"Present : {present}\n"

            f"Absent : {absent}"

        )
        
