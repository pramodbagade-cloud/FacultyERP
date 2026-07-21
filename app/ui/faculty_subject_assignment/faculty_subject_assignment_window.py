"""
FacultyERP
Faculty Subject Assignment Window
---------------------------------
"""

import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from app.services.faculty_subject_assignment_service import (
    FacultySubjectAssignmentService
)
from app.services.department_service import DepartmentService
from app.services.course_service import CourseService
from app.services.subject_service import SubjectService
from app.services.faculty_service import FacultyService


class FacultySubjectAssignmentWindow(ctk.CTkToplevel):
    """Faculty Subject Assignment Management."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        super().__init__(parent)

        self.title(
            "Faculty Subject Assignment"
        )

        self.geometry(
            "1450x780"
        )

        self.minsize(
            1300,
            720
        )

        self.transient(parent)

        self.grab_set()

        # ======================================================
        # CURRENT RECORD
        # ======================================================

        self.assignment_id = None

        # ======================================================
        # MASTER DATA
        # ======================================================

        self.departments = []

        self.courses = []

        self.subjects = []

        self.faculty = []

        # ======================================================
        # VARIABLES
        # ======================================================

        self.department_var = ctk.StringVar()

        self.course_var = ctk.StringVar()

        self.semester_var = ctk.StringVar(
            value="1"
        )

        self.subject_var = ctk.StringVar()

        self.faculty_var = ctk.StringVar()

        self.academic_year_var = ctk.StringVar()

        self.division_var = ctk.StringVar()

        self.batch_var = ctk.StringVar(
            value="Full"
        )

        self.workload_var = ctk.StringVar(
            value="0"
        )

        self.active_var = ctk.IntVar(
            value=1
        )

        # ======================================================
        # BUILD WINDOW
        # ======================================================

        self.create_widgets()

        self.initialize()
            # ==========================================================
    # CREATE WIDGETS
    # ==========================================================

    def create_widgets(self):

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )

        # ======================================================
        # TITLE
        # ======================================================

        title = ctk.CTkLabel(

            self,

            text="Faculty Subject Assignment",

            font=("Segoe UI", 24, "bold")

        )

        title.grid(

            row=0,

            column=0,

            sticky="w",

            padx=15,

            pady=(10, 5)

        )

        # ======================================================
        # FORM FRAME
        # ======================================================

        self.form_frame = ctk.CTkFrame(
            self
        )

        self.form_frame.grid(

            row=1,

            column=0,

            sticky="nsew",

            padx=10,

            pady=5

        )

        for column in range(6):

            self.form_frame.grid_columnconfigure(

                column,

                weight=1

            )

        # ======================================================
        # BUTTON FRAME
        # ======================================================

        self.button_frame = ctk.CTkFrame(
            self
        )

        self.button_frame.grid(

            row=2,

            column=0,

            sticky="ew",

            padx=10,

            pady=(5, 0)

        )

        # ======================================================
        # GRID FRAME
        # ======================================================

        self.grid_frame = ctk.CTkFrame(
            self
        )

        self.grid_frame.grid(

            row=3,

            column=0,

            sticky="nsew",

            padx=10,

            pady=(5, 10)

        )

        self.grid_frame.grid_rowconfigure(
            0,
            weight=1
        )

        self.grid_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # ======================================================
        # ROW 1
        # ======================================================

        ctk.CTkLabel(

            self.form_frame,

            text="Department"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5,

            sticky="w"

        )

        self.department_combo = ctk.CTkComboBox(

            self.form_frame,

            variable=self.department_var,

            values=[],

            width=220

        )

        self.department_combo.grid(

            row=0,

            column=1,

            padx=5,

            pady=5,

            sticky="ew"

        )

        ctk.CTkLabel(

            self.form_frame,

            text="Course"

        ).grid(

            row=0,

            column=2,

            padx=5,

            pady=5,

            sticky="w"

        )

        self.course_combo = ctk.CTkComboBox(

            self.form_frame,

            variable=self.course_var,

            values=[],

            width=220

        )

        self.course_combo.grid(

            row=0,

            column=3,

            padx=5,

            pady=5,

            sticky="ew"

        )

        ctk.CTkLabel(

            self.form_frame,

            text="Semester"

        ).grid(

            row=0,

            column=4,

            padx=5,

            pady=5,

            sticky="w"

        )

        self.semester_combo = ctk.CTkComboBox(

            self.form_frame,

            variable=self.semester_var,

            values=[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8"
            ],

            width=120

        )

        self.semester_combo.grid(

            row=0,

            column=5,

            padx=5,

            pady=5,

            sticky="ew"

        )
                # ======================================================
        # ROW 2
        # ======================================================

        ctk.CTkLabel(
            self.form_frame,
            text="Subject"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.subject_combo = ctk.CTkComboBox(
            self.form_frame,
            variable=self.subject_var,
            values=[],
            width=220
        )

        self.subject_combo.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.form_frame,
            text="Faculty"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.faculty_combo = ctk.CTkComboBox(
            self.form_frame,
            variable=self.faculty_var,
            values=[],
            width=220
        )

        self.faculty_combo.grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.form_frame,
            text="Academic Year"
        ).grid(
            row=1,
            column=4,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.academic_year_combo = ctk.CTkComboBox(
            self.form_frame,
            variable=self.academic_year_var,
            values=[],
            width=120
        )

        self.academic_year_combo.grid(
            row=1,
            column=5,
            padx=5,
            pady=5,
            sticky="ew"
        )

        # ======================================================
        # ROW 3
        # ======================================================

        ctk.CTkLabel(
            self.form_frame,
            text="Division"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.division_combo = ctk.CTkComboBox(
            self.form_frame,
            variable=self.division_var,
            values=[],
            width=220
        )

        self.division_combo.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.form_frame,
            text="Batch"
        ).grid(
            row=2,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.batch_entry = ctk.CTkEntry(
            self.form_frame,
            textvariable=self.batch_var
        )

        self.batch_entry.grid(
            row=2,
            column=3,
            padx=5,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.form_frame,
            text="Workload (Hrs/Week)"
        ).grid(
            row=2,
            column=4,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.workload_entry = ctk.CTkEntry(
            self.form_frame,
            textvariable=self.workload_var,
            width=120
        )

        self.workload_entry.grid(
            row=2,
            column=5,
            padx=5,
            pady=5,
            sticky="ew"
        )

        # ======================================================
        # ROW 4
        # ======================================================

        ctk.CTkLabel(
            self.form_frame,
            text="Remarks"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="nw"
        )

        self.remarks_text = ctk.CTkTextbox(
            self.form_frame,
            height=80
        )

        self.remarks_text.grid(
            row=3,
            column=1,
            columnspan=3,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        self.active_checkbox = ctk.CTkCheckBox(
            self.form_frame,
            text="Active",
            variable=self.active_var
        )

        self.active_checkbox.grid(
            row=3,
            column=4,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.form_frame.grid_rowconfigure(
            3,
            weight=1
        )
                # ======================================================
        # BUTTONS
        # ======================================================

        self.new_button = ctk.CTkButton(
            self.button_frame,
            text="New",
            width=120
        )

        self.new_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="Save",
            width=120
        )

        self.save_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.update_button = ctk.CTkButton(
            self.button_frame,
            text="Update",
            width=120
        )

        self.update_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.delete_button = ctk.CTkButton(
            self.button_frame,
            text="Delete",
            width=120
        )

        self.delete_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Clear",
            width=120
        )

        self.clear_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        # ======================================================
        # TREEVIEW
        # ======================================================

        columns = (
            "Faculty",
            "Department",
            "Course",
            "Semester",
            "Subject",
            "Academic Year",
            "Division",
            "Batch",
            "Workload",
            "Status"
        )

        self.tree = ttk.Treeview(
            self.grid_frame,
            columns=columns,
            show="headings",
            height=18
        )

        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

        self.tree.column(
            "Faculty",
            width=220,
            anchor="w"
        )

        self.tree.column(
            "Department",
            width=150,
            anchor="w"
        )

        self.tree.column(
            "Course",
            width=170,
            anchor="w"
        )

        self.tree.column(
            "Semester",
            width=80,
            anchor="center"
        )

        self.tree.column(
            "Subject",
            width=220,
            anchor="w"
        )

        self.tree.column(
            "Academic Year",
            width=120,
            anchor="center"
        )

        self.tree.column(
            "Division",
            width=90,
            anchor="center"
        )

        self.tree.column(
            "Batch",
            width=100,
            anchor="center"
        )

        self.tree.column(
            "Workload",
            width=100,
            anchor="center"
        )

        self.tree.column(
            "Status",
            width=90,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            self.grid_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_tree_select
        )
            # ==========================================================
    # LOAD DEPARTMENTS
    # ==========================================================

    def load_departments(self):

        self.departments = DepartmentService.get_departments()

        values = [
            department.department_name
            for department in self.departments
        ]

        self.department_combo.configure(
            values=values
        )

        if values:

            self.department_var.set(
                values[0]
            )

    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):

        self.courses = CourseService.get_courses()

        values = [
            course.course_name
            for course in self.courses
        ]

        self.course_combo.configure(
            values=values
        )

        if values:

            self.course_var.set(
                values[0]
            )

    # ==========================================================
    # LOAD SUBJECTS
    # ==========================================================

    def load_subjects(self):

        self.subjects = SubjectService.get_subjects()

        values = [
            subject.subject_name
            for subject in self.subjects
        ]

        self.subject_combo.configure(
            values=values
        )

        if values:

            self.subject_var.set(
                values[0]
            )

    # ==========================================================
    # LOAD FACULTY
    # ==========================================================

    def load_faculty(self):

        self.faculty = FacultyService.get_faculty()

        values = []

        for faculty in self.faculty:

            values.append(
                f"{faculty.first_name} "
                f"{faculty.last_name}"
            )

        self.faculty_combo.configure(
            values=values
        )

        if values:

            self.faculty_var.set(
                values[0]
            )

    # ==========================================================
    # LOAD ACADEMIC YEARS
    # ==========================================================

    def load_academic_years(self):

        values = [
            "2026-2027"
        ]

        self.academic_year_combo.configure(
            values=values
        )

        self.academic_year_var.set(
            values[0]
        )

    # ==========================================================
    # LOAD DIVISIONS
    # ==========================================================

    def load_divisions(self):

        values = [
            "A",
            "B",
            "C"
        ]

        self.division_combo.configure(
            values=values
        )

        self.division_var.set(
            values[0]
        )
            # ==========================================================
    # LOAD ASSIGNMENTS
    # ==========================================================

    def load_assignments(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        assignments = FacultySubjectAssignmentService.get_assignments()

        for row in assignments:

            status = "Active"

            if row[12] == 0:

                status = "Inactive"

            self.tree.insert(

                "",

                "end",

                iid=str(row[0]),

                values=(

                    row[2],      # Faculty

                    row[3],      # Department

                    row[4],      # Course

                    row[5],      # Semester

                    row[7],      # Subject

                    row[8],      # Academic Year

                    row[9],      # Division

                    row[10],     # Batch

                    row[11],     # Workload

                    status

                )

            )

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_fields(self):

        self.assignment_id = None

        if self.departments:

            self.department_var.set(

                self.departments[0].department_name

            )

        if self.courses:

            self.course_var.set(

                self.courses[0].course_name

            )

        self.semester_var.set("1")

        if self.subjects:

            self.subject_var.set(

                self.subjects[0].subject_name

            )

        if self.faculty:

            self.faculty_var.set(

                f"{self.faculty[0].first_name} "
                f"{self.faculty[0].last_name}"

            )

        self.academic_year_var.set(

            "2026-2027"

        )

        self.division_var.set("A")

        self.batch_var.set("Full")

        self.workload_var.set("0")

        self.active_var.set(1)

        self.remarks_text.delete(

            "1.0",

            "end"

        )

        self.tree.selection_remove(

            self.tree.selection()

        )

    # ==========================================================
    # NEW
    # ==========================================================

    def new_assignment(self):

        self.clear_fields()
            # ==========================================================
    # GET DEPARTMENT ID
    # ==========================================================

    def get_department_id(self):

        department_name = self.department_var.get()

        for department in self.departments:

            if department.department_name == department_name:

                return department.department_id

        return 0

    # ==========================================================
    # GET COURSE ID
    # ==========================================================

    def get_course_id(self):

        course_name = self.course_var.get()

        for course in self.courses:

            if course.course_name == course_name:

                return course.course_id

        return 0

    # ==========================================================
    # GET SUBJECT ID
    # ==========================================================

    def get_subject_id(self):

        subject_name = self.subject_var.get()

        for subject in self.subjects:

            if subject.subject_name == subject_name:

                return subject.subject_id

        return 0

    # ==========================================================
    # GET FACULTY ID
    # ==========================================================

    def get_faculty_id(self):

        faculty_name = self.faculty_var.get()

        for faculty in self.faculty:

            full_name = (
                f"{faculty.first_name} "
                f"{faculty.last_name}"
            )

            if full_name == faculty_name:

                return faculty.faculty_id

        return 0

    # ==========================================================
    # GET ACADEMIC YEAR ID
    # ==========================================================

    def get_academic_year_id(self):

        #
        # Temporary implementation.
        # Replace after AcademicYear module is developed.
        #

        return 1

    # ==========================================================
    # GET DIVISION ID
    # ==========================================================

    def get_division_id(self):

        division = self.division_var.get()

        mapping = {

            "A": 1,

            "B": 2,

            "C": 3

        }

        return mapping.get(

            division,

            0

        )
        # ==========================================================
    # SAVE ASSIGNMENT
    # ==========================================================

    def save_assignment(self):

        try:

            workload = float(

                self.workload_var.get().strip()

                if self.workload_var.get().strip()

                else "0"

            )

        except ValueError:

            messagebox.showerror(

                "Error",

                "Invalid workload hours."

            )

            return

        success, message = FacultySubjectAssignmentService.add_assignment(

            faculty_id=self.get_faculty_id(),

            department_id=self.get_department_id(),

            course_id=self.get_course_id(),

            semester=int(self.semester_var.get()),

            subject_id=self.get_subject_id(),

            academic_year_id=self.get_academic_year_id(),

            division_id=self.get_division_id(),

            batch_name=self.batch_var.get().strip(),

            workload_hours=workload,

            remarks=self.remarks_text.get(

                "1.0",

                "end"

            ).strip(),

            is_active=self.active_var.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.load_assignments()

            self.clear_fields()

        else:

            messagebox.showerror(

                "Error",

                message
            )

    # ==========================================================
    # BIND EVENTS
    # ==========================================================

    def bind_events(self):

        self.new_button.configure(

            command=self.new_assignment

        )

        self.save_button.configure(

            command=self.save_assignment

        )

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def initialize(self):

        self.bind_events()
            # ==========================================================
    # TREEVIEW SELECT
    # ==========================================================

    def on_tree_select(self, event):

        selection = self.tree.selection()

        if not selection:

            return

        self.assignment_id = int(
            selection[0]
        )

        assignment = FacultySubjectAssignmentService.get_assignment(
            self.assignment_id
        )

        if assignment is None:

            return

        self.department_var.set(
            self.get_department_name(
                assignment.department_id
            )
        )

        self.course_var.set(
            self.get_course_name(
                assignment.course_id
            )
        )

        self.semester_var.set(
            str(
                assignment.semester
            )
        )

        self.subject_var.set(
            self.get_subject_name(
                assignment.subject_id
            )
        )

        self.faculty_var.set(
            self.get_faculty_name(
                assignment.faculty_id
            )
        )

        self.academic_year_var.set(
            "2026-2027"
        )

        if assignment.division_id == 1:

            self.division_var.set("A")

        elif assignment.division_id == 2:

            self.division_var.set("B")

        else:

            self.division_var.set("C")

        self.batch_var.set(
            assignment.batch_name
        )

        self.workload_var.set(
            str(
                assignment.workload_hours
            )
        )

        self.remarks_text.delete(
            "1.0",
            "end"
        )

        self.remarks_text.insert(
            "1.0",
            assignment.remarks
        )

        self.active_var.set(
            assignment.is_active
        )

    # ==========================================================
    # LOOKUP NAME METHODS
    # ==========================================================

    def get_department_name(
        self,
        department_id
    ):

        for department in self.departments:

            if department.department_id == department_id:

                return department.department_name

        return ""

    def get_course_name(
        self,
        course_id
    ):

        for course in self.courses:

            if course.course_id == course_id:

                return course.course_name

        return ""

    def get_subject_name(
        self,
        subject_id
    ):

        for subject in self.subjects:

            if subject.subject_id == subject_id:

                return subject.subject_name

        return ""

    def get_faculty_name(
        self,
        faculty_id
    ):

        for faculty in self.faculty:

            if faculty.faculty_id == faculty_id:

                return (
                    f"{faculty.first_name} "
                    f"{faculty.last_name}"
                )

        return ""
        # ==========================================================
    # UPDATE ASSIGNMENT
    # ==========================================================

    def update_assignment(self):

        if self.assignment_id is None:

            messagebox.showwarning(

                "Warning",

                "Please select an assignment."

            )

            return

        try:

            workload = float(

                self.workload_var.get().strip()

                if self.workload_var.get().strip()

                else "0"

            )

        except ValueError:

            messagebox.showerror(

                "Error",

                "Invalid workload hours."

            )

            return

        success, message = FacultySubjectAssignmentService.update_assignment(

            assignment_id=self.assignment_id,

            faculty_id=self.get_faculty_id(),

            department_id=self.get_department_id(),

            course_id=self.get_course_id(),

            semester=int(self.semester_var.get()),

            subject_id=self.get_subject_id(),

            academic_year_id=self.get_academic_year_id(),

            division_id=self.get_division_id(),

            batch_name=self.batch_var.get().strip(),

            workload_hours=workload,

            remarks=self.remarks_text.get(

                "1.0",

                "end"

            ).strip(),

            is_active=self.active_var.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.load_assignments()

            self.clear_fields()

        else:

            messagebox.showerror(

                "Error",

                message

            )

    # ==========================================================
    # DELETE ASSIGNMENT
    # ==========================================================

    def delete_assignment(self):

        if self.assignment_id is None:

            messagebox.showwarning(

                "Warning",

                "Please select an assignment."

            )

            return

        if not messagebox.askyesno(

            "Confirm",

            "Delete selected assignment?"

        ):

            return

        success, message = FacultySubjectAssignmentService.delete_assignment(

            self.assignment_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.load_assignments()

            self.clear_fields()

        else:

            messagebox.showerror(

                "Error",

                message

            )

    # ==========================================================
    # UPDATE BUTTON EVENTS
    # ==========================================================

    def bind_events(self):

        self.new_button.configure(

            command=self.new_assignment

        )

        self.save_button.configure(

            command=self.save_assignment

        )

        self.update_button.configure(

            command=self.update_assignment

        )

        self.delete_button.configure(

            command=self.delete_assignment

        )

        self.clear_button.configure(

            command=self.clear_fields

        )
        