"""
FacultyERP
Faculty Subject Allocation Window
---------------------------------
"""

import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from app.services.faculty_subject_allocation_service import FacultySubjectAllocationService
from app.services.academic_year_service import AcademicYearService
from app.services.department_service import DepartmentService
from app.services.course_service import CourseService
from app.services.semester_service import SemesterService
from app.services.division_service import DivisionService
from app.services.subject_service import SubjectService
from app.services.faculty_service import FacultyService



class FacultySubjectAllocationWindow:
    """Faculty Subject Allocation Management."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.allocation_id = None

        self.academic_years = []
        self.departments = []
        self.courses = []
        self.semesters = []
        self.divisions = []
        self.subjects = []
        self.faculty = []

        self.academic_year_var = ctk.StringVar()
        self.department_var = ctk.StringVar()
        self.course_var = ctk.StringVar()
        self.semester_var = ctk.StringVar()
        self.division_var = ctk.StringVar()
        self.subject_var = ctk.StringVar()
        self.faculty_var = ctk.StringVar()
        self.batch_var = ctk.StringVar(value="Full")
        self.theory_hours_var = ctk.StringVar(value="0")
        self.practical_hours_var = ctk.StringVar(value="0")
        self.tutorial_hours_var = ctk.StringVar(value="0")
        self.workload_var = ctk.StringVar(value="0")
       
        self.class_teacher_var = ctk.IntVar(value=0)

        self.main_frame = None
        self.filter_frame = None
        self.content_frame = None
        self.left_frame = None
        self.right_frame = None

        self.academic_year_combo = None
        self.department_combo = None
        self.course_combo = None
        self.semester_combo = None
        self.division_combo = None
        self.subject_combo = None
        self.faculty_combo = None
        self.theory_value_label = None
        self.practical_value_label = None
        self.tutorial_value_label = None

        self.batch_combo = None
        self.theory_hours_entry = None
        self.practical_hours_entry = None
        self.tutorial_hours_entry = None
        self.workload_entry = None
        

        self.class_teacher_check = None
        self.remarks_text = None

        self.save_button = None
        self.update_button = None
        self.delete_button = None
        self.clear_button = None

        self.tree = None

        self.build_ui()
        self.load_master_data()
        self.bind_events()
        self.load_allocations()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        self.main_frame = ctk.CTkFrame(self.parent)

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.main_frame.grid_rowconfigure(
            2,
            weight=1
        )

        self.main_frame.grid_columnconfigure(
            0,
            weight=1
        )

        ctk.CTkLabel(
            self.main_frame,
            text="Faculty Subject Allocation",
            font=("Segoe UI",24,"bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=(10,15)
        )

        self.filter_frame = ctk.CTkFrame(
            self.main_frame
        )

        self.filter_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=10,
            pady=(0,10)
        )

        self.content_frame = ctk.CTkFrame(
            self.main_frame
        )

        self.content_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0,10)
        )

        self.content_frame.grid_rowconfigure(
            0,
            weight=1
        )

        self.content_frame.grid_columnconfigure(
            0,
            weight=0
        )

        self.content_frame.grid_columnconfigure(
            1,
            weight=1
        )
                # ==========================================================
        # FILTER FRAME
        # ==========================================================

        for column in range(10):
            self.filter_frame.grid_columnconfigure(column, weight=1)

        ctk.CTkLabel(
            self.filter_frame,
            text="Academic Year"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=10,
            sticky="w"
        )

        self.academic_year_combo = ctk.CTkComboBox(
            self.filter_frame,
            variable=self.academic_year_var,
            values=[]
        )

        self.academic_year_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Department"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=10,
            sticky="w"
        )

        self.department_combo = ctk.CTkComboBox(
            self.filter_frame,
            variable=self.department_var,
            values=[]
        )

        self.department_combo.grid(
            row=0,
            column=3,
            padx=5,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Course"
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=10,
            sticky="w"
        )

        self.course_combo = ctk.CTkComboBox(
            self.filter_frame,
            variable=self.course_var,
            values=[]
        )

        self.course_combo.grid(
            row=0,
            column=5,
            padx=5,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Semester"
        ).grid(
            row=0,
            column=6,
            padx=5,
            pady=10,
            sticky="w"
        )

        self.semester_combo = ctk.CTkComboBox(
            self.filter_frame,
            variable=self.semester_var,
            values=[]
        )

        self.semester_combo.grid(
            row=0,
            column=7,
            padx=5,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Division"
        ).grid(
            row=0,
            column=8,
            padx=5,
            pady=10,
            sticky="w"
        )

        self.division_combo = ctk.CTkComboBox(
            self.filter_frame,
            variable=self.division_var,
            values=[]
        )

        self.division_combo.grid(
            row=0,
            column=9,
            padx=5,
            pady=10,
            sticky="ew"
        )

        # ==========================================================
        # LEFT PANEL
        # ==========================================================

        self.left_frame = ctk.CTkFrame(
            self.content_frame,
            width=380
        )

        self.left_frame.grid(
            row=0,
            column=0,
            sticky="ns",
            padx=(0,10),
            pady=5
        )

        self.left_frame.grid_columnconfigure(
            1,
            weight=1
        )
        # ==========================================================
        # FACULTY
        # ==========================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Faculty"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=(15,5),
            sticky="w"
        )

        self.faculty_combo = ctk.CTkComboBox(
            self.left_frame,
            variable=self.faculty_var,
            values=[]
        )

        self.faculty_combo.grid(
            row=0,
            column=1,
            padx=10,
            pady=(15,5),
            sticky="ew"
        )

        # ==========================================================
        # SUBJECT
        # ==========================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Subject"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.subject_combo = ctk.CTkComboBox(
            self.left_frame,
            variable=self.subject_var,
            values=[],
            command=lambda _:self.on_subject_change()
        )

        self.subject_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=5,
            sticky="ew"
        )
        # ==========================================================
        # THEORY SECTION
        # ==========================================================

        theory_frame = ctk.CTkFrame(
            self.left_frame
        )

        theory_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=(15,5),
            sticky="ew"
        )

        theory_frame.grid_columnconfigure(
            1,
            weight=1
        )

        ctk.CTkLabel(
            theory_frame,
            text="THEORY",
            font=("Segoe UI",13,"bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=(8,2),
            sticky="w"
        )

        ctk.CTkLabel(
            theory_frame,
            text="Hours / Week"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=(0,8),
            sticky="w"
        )

        self.theory_value_label = ctk.CTkLabel(
            theory_frame,
            text="N/A",
            height=34,
            fg_color="#E5E5E5",
            corner_radius=6,
            font=("Segoe UI", 12, "bold")
        )

        self.theory_value_label.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0,8),
            sticky="ew"
        )

        # ==========================================================
        # PRACTICAL SECTION
        # ==========================================================

        practical_frame = ctk.CTkFrame(
            self.left_frame
        )

        practical_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="ew"
        )

        practical_frame.grid_columnconfigure(
            1,
            weight=1
        )

        ctk.CTkLabel(
            practical_frame,
            text="PRACTICAL",
            font=("Segoe UI",13,"bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=(8,2),
            sticky="w"
        )

        ctk.CTkLabel(
            practical_frame,
            text="Hours / Week"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.practical_value_label = ctk.CTkLabel(
            practical_frame,
            text="N/A",
            height=34,
            fg_color="#E5E5E5",
            corner_radius=6,
            font=("Segoe UI", 12, "bold")
        )

        self.practical_value_label.grid(
            row=1,
            column=1,
            padx=10,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(
            practical_frame,
            text="Batch"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=(0,8),
            sticky="w"
        )

        self.batch_combo = ctk.CTkComboBox(
            practical_frame,
            variable=self.batch_var,
            values=[
                "Batch A",
                "Batch B",
                "Batch C"
            ]
        )

        self.batch_combo.grid(
            row=2,
            column=1,
            padx=10,
            pady=(0,8),
            sticky="ew"
        )

        # ==========================================================
        # TUTORIAL SECTION
        # ==========================================================

        tutorial_frame = ctk.CTkFrame(
            self.left_frame
        )

        tutorial_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="ew"
        )

        tutorial_frame.grid_columnconfigure(
            1,
            weight=1
        )

        ctk.CTkLabel(
            tutorial_frame,
            text="TUTORIAL",
            font=("Segoe UI",13,"bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=(8,2),
            sticky="w"
        )

        ctk.CTkLabel(
            tutorial_frame,
            text="Hours / Week"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=(0,8),
            sticky="w"
        )
        self.tutorial_value_label = ctk.CTkLabel(
            tutorial_frame,
            text="N/A",
            height=34,
            fg_color="#E5E5E5",
            corner_radius=6,
            font=("Segoe UI", 12, "bold")
        )

        self.tutorial_value_label.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0,8),
            sticky="ew"
        )
        # ==========================================================
        # CLASS TEACHER
        # ==========================================================

        self.class_teacher_check = ctk.CTkCheckBox(
            self.left_frame,
            text="Class Teacher",
            variable=self.class_teacher_var
        )

        self.class_teacher_check.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=10,
            pady=(15,5),
            sticky="w"
        )

        # ==========================================================
        # REMARKS
        # ==========================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Remarks"
        ).grid(
            row=6,
            column=0,
            columnspan=2,
            padx=10,
            pady=(10,2),
            sticky="w"
        )

        self.remarks_text = ctk.CTkTextbox(
            self.left_frame,
            height=120
        )

        self.remarks_text.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=10,
            pady=(0,10),
            sticky="nsew"
        )

        # ==========================================================
        # LEFT PANEL LAYOUT
        # ==========================================================

        self.left_frame.grid_rowconfigure(
            7,
            weight=1
        )

        
        # ==========================================================
        # RIGHT PANEL
        # ==========================================================

        self.right_frame = ctk.CTkFrame(
            self.content_frame
        )

        self.right_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            pady=5
        )

        self.right_frame.grid_rowconfigure(
            1,
            weight=1
        )

        self.right_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # ==========================================================
        # BUTTON FRAME
        # ==========================================================

        button_frame = ctk.CTkFrame(
            self.right_frame
        )

        button_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=10
        )

        self.save_button = ctk.CTkButton(
            button_frame,
            text="Save",
            width=110,
            command=self.save_allocation
        )

        self.save_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.update_button = ctk.CTkButton(
            button_frame,
            text="Update",
            width=110,
            command=self.update_allocation
        )

        self.update_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            width=110,
            command=self.delete_allocation
        )

        self.delete_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            width=110,
            command=self.new_record
        )

        self.clear_button.pack(
            side="left",
            padx=5,
            pady=5
        )

        # ==========================================================
        # TREEVIEW FRAME
        # ==========================================================

        tree_frame = ctk.CTkFrame(
            self.right_frame
        )

        tree_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0,10)
        )

        tree_frame.grid_rowconfigure(
            0,
            weight=1
        )

        tree_frame.grid_columnconfigure(
            0,
            weight=1
        )


        columns = (
            "Academic Year",
            "Division",
            "Faculty",
            "Subject Code",
            "Subject",
            "Batch",
            "Theory",
            "Practical",
            "Tutorial",
            "Workload",
            "Status"
        )

        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            height=20
        )

        scrollbar_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            tree_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        column_widths = {
            "Academic Year": 100,
            "Division": 60,
            "Faculty": 180,
            "Subject Code": 120,
            "Subject": 340,
            "Batch": 70,
            "Theory": 70,
            "Practical": 80,
            "Tutorial": 70,
            "Workload": 80,
            "Status": 70
        }

        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=column_widths[column],
                minwidth=column_widths[column],
                stretch=(column == "Subject"),
                anchor="center"
            )

        self.tree.column(
            "Faculty",
            anchor="w"
        )

        self.tree.column(
            "Subject",
            anchor="w"
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_tree_select
        )

        self.update_hour_cards(
            0,
            0,
            0
        )

    # ==========================================================
    # UPDATE HOUR CARDS
    # ==========================================================

    def update_hour_cards(
        self,
        theory_hours,
        practical_hours,
        tutorial_hours
    ):

        if theory_hours > 0:

            self.theory_value_label.configure(
                text=f"{theory_hours} Hrs / Week",
                fg_color="#D5F5E3"
            )

        else:

            self.theory_value_label.configure(
                text="N/A",
                fg_color="#E5E5E5"
            )

        if practical_hours > 0:

            self.practical_value_label.configure(
                text=f"{practical_hours} Hrs / Week",
                fg_color="#D5F5E3"
            )

        else:

            self.practical_value_label.configure(
                text="N/A",
                fg_color="#E5E5E5"
            )

        if tutorial_hours > 0:

            self.tutorial_value_label.configure(
                text=f"{tutorial_hours} Hrs / Week",
                fg_color="#D5F5E3"
            )

        else:

            self.tutorial_value_label.configure(
                text="N/A",
                fg_color="#E5E5E5"
            )


    # ==========================================================
    # LOAD MASTER DATA
    # ==========================================================

    def load_master_data(self):

        self.load_academic_years()
        self.load_departments()
        self.load_faculty()

        if self.department_var.get():
            self.load_courses()

        if self.course_var.get():
            self.load_semesters()

        if self.semester_var.get():
            self.load_divisions()
            self.load_subjects()

    # ==========================================================
    # LOAD ACADEMIC YEARS
    # ==========================================================

    def load_academic_years(self):

        self.academic_years = AcademicYearService.get_academic_years()
        print("Academic Years :", self.academic_years)
        values = [
            year.academic_year
            for year in self.academic_years
        ]

        self.academic_year_combo.configure(
            values=values
        )

        if values:
            self.academic_year_var.set(values[0])

    # ==========================================================
    # LOAD DEPARTMENTS
    # ==========================================================

    def load_departments(self):

        self.departments = DepartmentService.get_departments()
        print("Departments :", self.departments)
        values = [
            department.department_name
            for department in self.departments
        ]

        self.department_combo.configure(
            values=values
        )

        if values:
            self.department_var.set(values[0])
            self.load_faculty()

    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):

        department_id = self.get_department_id()

        self.courses = CourseService.get_courses_by_department(
            department_id
        )

        values = [
            course.course_name
            for course in self.courses
        ]

        self.course_combo.configure(
            values=values
        )

        if values:
            self.course_var.set(values[0])
            self.load_semesters()
            self.load_divisions()
            self.load_subjects()
        else:
            self.course_var.set("")
            self.course_combo.configure(values=[])

    # ==========================================================
    # LOAD SEMESTERS
    # ==========================================================

    def load_semesters(self):

        self.semesters = SemesterService.get_semesters()

        values = [
            semester.semester_name
            for semester in self.semesters
        ]

        self.semester_combo.configure(
            values=values
        )

        if values:
            self.semester_var.set(values[0])
            self.load_divisions()
            self.load_subjects()
        else:
            self.semester_var.set("")
            self.semester_combo.configure(values=[])

    # ==========================================================
    # LOAD DIVISIONS
    # ==========================================================

    def load_divisions(self):

        course_id = self.get_course_id()
        academic_year_id = self.get_academic_year_id()
        semester_id = self.get_semester_id()

        self.divisions = DivisionService.get_divisions_by_course_year_semester(
            course_id,
            academic_year_id,
            semester_id
        )

        values = [
            division.division_name
            for division in self.divisions
        ]

        self.division_combo.configure(
            values=values
        )

        if values:
            self.division_var.set(values[0])
        else:
            self.division_var.set("")
            self.division_combo.configure(values=[])

    # ==========================================================
    # LOAD SUBJECTS
    # ==========================================================

    def load_subjects(self):

        department_id = self.get_department_id()

        course_id = self.get_course_id()

        semester_id = self.get_semester_id()
        print("========================================")
        print("Department ID :", department_id)
        print("Course ID     :", course_id)
        print("Semester ID   :", semester_id)
        print("========================================")

        if not department_id or not course_id or not semester_id:

            self.subjects = []

            self.subject_combo.configure(
                values=[]
            )

            self.subject_var.set("")

            return

        self.subjects = SubjectService.get_subjects_by_course_semester(
            course_id,
            semester_id
        )

        values = [
            subject.subject_name
            for subject in self.subjects
        ]

        self.subject_combo.configure(
            values=values
        )

        if values:

            self.subject_var.set(values[0])

            self.on_subject_change()

        else:

            self.subject_var.set("")
    # ==========================================================
    # LOAD FACULTY
    # ==========================================================

    def load_faculty(self):

        department_id = self.get_department_id()

        if department_id == 0:
            self.faculty = []
            self.faculty_combo.configure(values=[])
            self.faculty_var.set("")
            return

        self.faculty = FacultyService.get_faculty_by_department(
            department_id
        )

        values = [
            f"{faculty.first_name} {faculty.last_name}"
            for faculty in self.faculty
        ]

        self.faculty_combo.configure(
            values=values
        )

        if values:
            self.faculty_var.set(values[0])
        else:
            self.faculty_var.set("")
                
    # ==========================================================
    # LOOKUP METHODS
    # ==========================================================

    def get_academic_year_id(self):

        name = self.academic_year_var.get()

        for academic_year in self.academic_years:
            if academic_year.academic_year == name:
                return academic_year.academic_year_id

        return 0

    def get_department_id(self):

        name = self.department_var.get()

        for department in self.departments:
            if department.department_name == name:
                return department.department_id

        return 0

    def get_course_id(self):

        name = self.course_var.get()

        for course in self.courses:
            if course.course_name == name:
                return course.course_id

        return 0

    def get_semester_id(self):

        name = self.semester_var.get()

        for semester in self.semesters:
            if semester.semester_name == name:
                return semester.semester_id

        return 0

    def get_division_id(self):

        name = self.division_var.get()

        for division in self.divisions:
            if division.division_name == name:
                return division.division_id

        return 0

    def get_subject_id(self):

        name = self.subject_var.get()

        for subject in self.subjects:
            if subject.subject_name == name:
                return subject.subject_id

        return 0

    def get_faculty_id(self):

        name = self.faculty_var.get()

        for faculty in self.faculty:

            full_name = (
                f"{faculty.first_name} "
                f"{faculty.last_name}"
            )

            if full_name == name:
                return faculty.faculty_id

        return 0

    # ==========================================================
    # LOOKUP NAME METHODS
    # ==========================================================

    def get_academic_year_name(self, academic_year_id):

        for academic_year in self.academic_years:
            if academic_year.academic_year_id == academic_year_id:
                return academic_year.academic_year

        return ""

    def get_department_name(self, department_id):

        for department in self.departments:
            if department.department_id == department_id:
                return department.department_name

        return ""

    def get_course_name(self, course_id):

        for course in self.courses:
            if course.course_id == course_id:
                return course.course_name

        return ""

    def get_semester_name(self, semester_id):

        for semester in self.semesters:
            if semester.semester_id == semester_id:
                return semester.semester_name

        return ""

    def get_division_name(self, division_id):

        for division in self.divisions:
            if division.division_id == division_id:
                return division.division_name

        return ""

    def get_subject_name(self, subject_id):

        for subject in self.subjects:
            if subject.subject_id == subject_id:
                return subject.subject_name

        return ""

    def get_faculty_name(self, faculty_id):

        for faculty in self.faculty:
            if faculty.faculty_id == faculty_id:
                return f"{faculty.first_name} {faculty.last_name}"

        return ""

    # ==========================================================
    # CALCULATE WORKLOAD
    # ==========================================================

    def calculate_workload(self):

        try:
            theory = float(self.theory_hours_var.get() or 0)
        except ValueError:
            theory = 0

        try:
            practical = float(self.practical_hours_var.get() or 0)
        except ValueError:
            practical = 0

        try:
            tutorial = float(self.tutorial_hours_var.get() or 0)
        except ValueError:
            tutorial = 0

        total = theory + practical + tutorial

        if total == int(total):
            self.workload_var.set(str(int(total)))
        else:
            self.workload_var.set(f"{total:.1f}")

    def on_subject_change(self):
        selected_subject=self.subject_var.get().strip()
        for subject in self.subjects:
            if subject.subject_name.strip()==selected_subject:
                theory=subject.theory_hours or 0
                practical=subject.practical_hours or 0
                tutorial=subject.tutorial_hours or 0
                self.theory_hours_var.set(str(theory))
                self.practical_hours_var.set(str(practical))
                self.tutorial_hours_var.set(str(tutorial))
                self.update_hour_cards(theory,practical,tutorial)
                if practical>0:
                    self.batch_combo.configure(state="normal")
                    if self.batch_var.get()=="":
                        self.batch_var.set("Batch A")
                else:
                    self.batch_combo.configure(state="disabled")
                    self.batch_var.set("N/A")
                self.calculate_workload()
                return
        self.theory_hours_var.set("0")
        self.practical_hours_var.set("0")
        self.tutorial_hours_var.set("0")
        self.update_hour_cards(0,0,0)
        self.batch_combo.configure(state="disabled")
        self.batch_var.set("N/A")
    # ==========================================================
    # TREE SELECTION
    # ==========================================================
    def on_tree_select(self,event):
        selection=self.tree.selection()
        if not selection:
            return
        self.selected_allocation_id=int(selection[0])
        allocation=FacultySubjectAllocationService.get_by_id(self.selected_allocation_id)
        print("========================================")
        print("ALLOCATION")
        print("========================================")
        print("Columns :", allocation.keys())
        print(dict(allocation))
        print("========================================")
        print("========================================")
        if allocation is None:
            return
        allocation = dict(allocation)
        self.academic_year_var.set(self.get_academic_year_name(allocation["academic_year_id"]))

        print("Department from allocation =",allocation["department_id"])
        print("Department name =",self.get_department_name(allocation["department_id"]))
        print("Departments =",[(d.department_id,d.department_name) for d in self.departments])

        self.department_var.set(self.get_department_name(allocation["department_id"]))
        self.load_faculty()
        self.load_courses()
        self.course_var.set(self.get_course_name(allocation["course_id"]))
        self.load_semesters()
        self.semester_var.set(self.get_semester_name(allocation["semester_id"]))
        self.load_divisions()
        self.division_var.set(self.get_division_name(allocation["division_id"]))
        self.load_subjects()
        self.subject_var.set(self.get_subject_name(allocation["subject_id"]))
        self.faculty_var.set(self.get_faculty_name(allocation["faculty_id"]))
        self.batch_var.set(allocation["batch_name"])
        self.theory_hours_var.set(str(allocation["theory_hours"]))
        self.practical_hours_var.set(str(allocation["practical_hours"]))
        self.tutorial_hours_var.set(str(allocation["tutorial_hours"]))
        self.workload_var.set(str(allocation["workload_hours"]))
        self.update_hour_cards(allocation["theory_hours"],allocation["practical_hours"],allocation["tutorial_hours"])
        self.class_teacher_var.set(allocation["is_class_teacher"])
        self.remarks_text.delete("1.0","end")
        self.remarks_text.insert("1.0",allocation["remarks"] if allocation["remarks"] else "")
    # ==========================================================
    # SAVE
    # ==========================================================

    def save_allocation(self):
        faculty_id=self.get_faculty_id()
        subject_id=self.get_subject_id()
        academic_year_id=self.get_academic_year_id()
        division_id=self.get_division_id()
        if faculty_id==0:
            messagebox.showwarning("Validation","Please select Faculty.")
            return
        if subject_id==0:
            messagebox.showwarning("Validation","Please select Subject.")
            return
        if division_id==0:
            messagebox.showwarning("Validation","Please select Division.")
            return
        try:
            success,message=FacultySubjectAllocationService.add(
                faculty_id=faculty_id,
                subject_id=subject_id,
                academic_year_id=academic_year_id,
                division_id=division_id,
                batch_name=self.batch_var.get().strip(),
                theory_hours=float(self.theory_hours_var.get() or 0),
                practical_hours=float(self.practical_hours_var.get() or 0),
                tutorial_hours=float(self.tutorial_hours_var.get() or 0),
                is_class_teacher=self.class_teacher_var.get(),
                display_order=1,
                remarks=self.remarks_text.get("1.0","end").strip()
            )
            if success:
                messagebox.showinfo("Success",message)
                self.load_allocations()
                self.new_record()
            else:
                messagebox.showwarning("Validation",message)
        except Exception as ex:
            messagebox.showerror("Error",str(ex))
    # ==========================================================
    # UPDATE
    # ==========================================================

    def update_allocation(self):

        if self.selected_allocation_id is None:    

            messagebox.showwarning(
                "Warning",
                "Please select an allocation."
            )

            return

        try:

            FacultySubjectAllocationService.update(
                allocation_id=self.selected_allocation_id,
                faculty_id=self.get_faculty_id(),
                subject_id=self.get_subject_id(),
                academic_year_id=self.get_academic_year_id(),
                division_id=self.get_division_id(),
                batch_name=self.batch_var.get().strip(),
                theory_hours=float(self.theory_hours_var.get() or 0),
                practical_hours=float(self.practical_hours_var.get() or 0),
                tutorial_hours=float(self.tutorial_hours_var.get() or 0),
                is_class_teacher=self.class_teacher_var.get(),
                display_order=1,
                remarks=self.remarks_text.get(
                    "1.0",
                    "end"
                ).strip()
            )

            messagebox.showinfo(
                "Success",
                "Faculty Subject Allocation updated successfully."
            )

            self.load_allocations()

            self.tree.selection_set(str(self.selected_allocation_id))
            self.tree.focus(str(self.selected_allocation_id))

        except Exception as ex:

            messagebox.showerror(
                "Error",
                str(ex)
            )

    # ==========================================================
    # DELETE
    # ==========================================================

    def delete_allocation(self):

        if self.allocation_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an allocation."
            )

            return

        if not messagebox.askyesno(
            "Confirm",
            "Delete selected allocation?"
        ):

            return

        try:

            FacultySubjectAllocationService.delete(
                self.allocation_id
            )

            messagebox.showinfo(
                "Success",
                "Faculty Subject Allocation deleted successfully."
            )

            self.load_allocations()

            self.clear_fields()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                str(ex)
            )

    # ==========================================================
    # LOAD GRID
    # ==========================================================

    def load_allocations(self):

        self.tree.delete(
            *self.tree.get_children()
        )

        rows = FacultySubjectAllocationService.get_grid_data()

        for row in rows:

            status = "Active"

            if row[12] == 0:
                status = "Inactive"

            self.tree.insert(
                "",
                "end",
                iid=str(row[0]),
                values=(
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    status
                )
            )

    # ==========================================================
    # CLEAR FIELDS
    # ==========================================================

    def clear_fields(self):

        self.allocation_id = None

        self.batch_var.set("Full")
        self.theory_hours_var.set("0")
        self.practical_hours_var.set("0")
        self.tutorial_hours_var.set("0")
        self.workload_var.set("0")
        self.class_teacher_var.set(0)

        self.remarks_text.delete(
            "1.0",
            "end"
        )

        if self.faculty:
            self.faculty_var.set(
                f"{self.faculty[0].first_name} {self.faculty[0].last_name}"
            )

        if self.subjects:
            self.subject_var.set(
                self.subjects[0].subject_name
            )

        self.tree.selection_remove(
            self.tree.selection()
        )

        self.enable_new_mode()
    
    # ==========================================================
    # REFRESH FILTER DATA
    # ==========================================================

    def refresh_filters(self):

        self.load_master_data()
        self.load_allocations()

    # ==========================================================
    # REFRESH GRID
    # ==========================================================

    def refresh_grid(self):

        self.load_allocations()

    # ==========================================================
    # RESET FORM
    # ==========================================================

    def reset_form(self):

        self.clear_fields()

        if self.faculty:
            self.faculty_var.set(
                f"{self.faculty[0].first_name} {self.faculty[0].last_name}"
            )

        if self.subjects:
            self.subject_var.set(
                self.subjects[0].subject_name
            )

        self.calculate_workload()

    # ==========================================================
    # ENABLE BUTTONS
    # ==========================================================

    def enable_edit_mode(self):

        self.save_button.configure(
            state="disabled"
        )

        self.update_button.configure(
            state="normal"
        )

        self.delete_button.configure(
            state="normal"
        )

    # ==========================================================
    # ENABLE NEW MODE
    # ==========================================================

    def enable_new_mode(self):

        self.save_button.configure(
            state="normal"
        )

        self.update_button.configure(
            state="disabled"
        )

        self.delete_button.configure(
            state="disabled"
        )

    # ==========================================================
    # NEW RECORD
    # ==========================================================

    def new_record(self):
        self.reset_form()
        self.enable_new_mode()

    # ==========================================================
    # WINDOW INITIALIZATION
    # ==========================================================

    def initialize(self):

        self.refresh_filters()

        self.enable_new_mode()

        self.calculate_workload()
    
    
    # ==========================================================
    # EVENT BINDINGS
    # ==========================================================

    def bind_events(self):

        self.academic_year_combo.configure(
            command=lambda _:
            self.on_academic_year_change()
        )

        self.department_combo.configure(
            command=lambda _:
            self.on_department_change()
        )

        self.course_combo.configure(
            command=lambda _:
            self.on_course_change()
        )

        self.semester_combo.configure(
            command=lambda _:
            self.on_semester_change()
        )

        self.subject_combo.configure(
            command=lambda _:
            self.on_subject_change()
        )

        self.theory_hours_var.trace_add(
            "write",
            lambda *_:
            self.calculate_workload()
        )

        self.practical_hours_var.trace_add(
            "write",
            lambda *_:
            self.calculate_workload()
        )

        self.tutorial_hours_var.trace_add(
            "write",
            lambda *_:
            self.calculate_workload()
        )
    
    # ==========================================================
    # FILTER EVENTS
    # ==========================================================

    def on_academic_year_change(self):

        self.load_divisions()
        self.load_subjects()

    def on_department_change(self):
        self.load_faculty()
        self.load_courses()

    def on_course_change(self):

        self.load_semesters()

    def on_semester_change(self):
        print("Semester Selected :",self.semester_var.get())
        print("Semester ID :",self.get_semester_id())
        self.load_divisions()
        self.load_subjects()

    # ==========================================================
    # CLOSE
    # ==========================================================

    def close(self):

        if self.parent.winfo_exists():
            for widget in self.parent.winfo_children():
                widget.destroy()
