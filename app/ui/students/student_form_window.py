"""
FacultyERP
Student Form Window
-------------------
"""

import customtkinter as ctk

from tkinter import filedialog
from tkinter import messagebox

from app.services.student_service import StudentService
from app.services.department_service import DepartmentService
from app.services.course_service import CourseService
from app.services.semester_service import SemesterService
from app.services.division_service import DivisionService
from app.services.academic_year_service import AcademicYearService


class StudentFormWindow:
    """Student Add/Edit Form."""

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def __init__(self, parent, student_id=None):
        self.parent = parent
        self.student_id = student_id
        self.parent = parent
        self.photo_path = None

        self.departments = []
        self.courses = []
        self.semesters = []
        self.divisions = []
        self.academic_years = []

        self.department_map = {}
        self.course_map = {}
        self.semester_map = {}
        self.division_map = {}
        self.academic_year_map = {}

        self.selected_department_id = 0
        self.selected_course_id = 0
        self.selected_semester_id = 0
        self.selected_division_id = 0
        self.selected_academic_year_id = 0

        self.department_map = {}
        self.course_map = {}
        self.semester_map = {}
        self.division_map = {}
        self.academic_year_map = {}

        self.photo_path = None

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Student Master")

        self.window.geometry("1050x760")

        self.window.resizable(True, True)

        self.window.transient(parent)

        self.window.grab_set()

        self.main_frame = ctk.CTkScrollableFrame(
            self.window
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.build_ui()

        self.load_combo_data()

        if self.student_id:

            self.load_student()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        self.build_title()

        self.build_basic_information()

        self.build_academic_information()

        self.build_parent_information()

        self.build_address_information()

        self.build_emergency_information()

        self.build_photo_section()

        self.build_buttons()

    # ==========================================================
    # TITLE
    # ==========================================================

    def build_title(self):

        title = "Add Student"

        if self.student_id:

            title = "Edit Student"

        ctk.CTkLabel(
            self.main_frame,
            text=title,
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            pady=(10,20)
        )
            # ==========================================================
    # BASIC INFORMATION
    # ==========================================================

    def build_basic_information(self):

        self.basic_frame = ctk.CTkFrame(self.main_frame)

        self.basic_frame.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        ctk.CTkLabel(
            self.basic_frame,
            text="Basic Information",
            font=("Segoe UI", 18, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=6,
            padx=15,
            pady=(15,20),
            sticky="w"
        )

        for column in (1,3,5):
            self.basic_frame.grid_columnconfigure(
                column,
                weight=1
            )

        # ------------------------------------------------------
        # First Name
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="First Name *"
        ).grid(
            row=1,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_first_name = ctk.CTkEntry(
            self.basic_frame
        )

        self.entry_first_name.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Middle Name
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="Middle Name"
        ).grid(
            row=1,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_middle_name = ctk.CTkEntry(
            self.basic_frame
        )

        self.entry_middle_name.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Last Name
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="Last Name *"
        ).grid(
            row=1,
            column=4,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_last_name = ctk.CTkEntry(
            self.basic_frame
        )

        self.entry_last_name.grid(
            row=1,
            column=5,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Gender
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="Gender"
        ).grid(
            row=2,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_gender = ctk.CTkComboBox(
            self.basic_frame,
            values=[
                "",
                "Male",
                "Female",
                "Other"
            ]
        )

        self.cmb_gender.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        self.cmb_gender.set("")

        # ------------------------------------------------------
        # Date of Birth
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="Date of Birth"
        ).grid(
            row=2,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_dob = ctk.CTkEntry(
            self.basic_frame,
            placeholder_text="DD-MM-YYYY"
        )

        self.entry_dob.grid(
            row=2,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # PRN
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="PRN"
        ).grid(
            row=2,
            column=4,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_prn = ctk.CTkEntry(
            self.basic_frame
        )

        self.entry_prn.grid(
            row=2,
            column=5,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Mobile
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="Mobile"
        ).grid(
            row=3,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_mobile = ctk.CTkEntry(
            self.basic_frame
        )

        self.entry_mobile.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Email
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.basic_frame,
            text="Email"
        ).grid(
            row=3,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_email = ctk.CTkEntry(
            self.basic_frame
        )

        self.entry_email.grid(
            row=3,
            column=3,
            columnspan=3,
            padx=10,
            pady=(8,15),
            sticky="ew"
        )
            # ==========================================================
    # ACADEMIC INFORMATION
    # ==========================================================

    def build_academic_information(self):

        self.academic_frame = ctk.CTkFrame(self.main_frame)

        self.academic_frame.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        ctk.CTkLabel(
            self.academic_frame,
            text="Academic Information",
            font=("Segoe UI",18,"bold")
        ).grid(
            row=0,
            column=0,
            columnspan=6,
            padx=15,
            pady=(15,20),
            sticky="w"
        )

        for column in (1,3,5):
            self.academic_frame.grid_columnconfigure(
                column,
                weight=1
            )

        # ------------------------------------------------------
        # Admission Year
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Admission Year *"
        ).grid(
            row=1,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_admission_year = ctk.CTkComboBox(
            self.academic_frame,
            values=[
                "2026",
                "2025",
                "2024",
                "2023",
                "2022",
                "2021",
                "2020"
            ]
        )

        self.cmb_admission_year.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Academic Year
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Academic Year *"
        ).grid(
            row=1,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_academic_year = ctk.CTkComboBox(
            self.academic_frame,
            values=[],
            command=self.on_academic_year_changed
        )

        self.cmb_academic_year.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Department
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Department *"
        ).grid(
            row=1,
            column=4,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_department = ctk.CTkComboBox(
            self.academic_frame,
            values=[],
            command=self.on_department_changed
        )

        self.cmb_department.grid(
            row=1,
            column=5,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Course
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Course *"
        ).grid(
            row=2,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_course = ctk.CTkComboBox(
            self.academic_frame,
            values=[],
            command=self.on_course_changed
        )

        self.cmb_course.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Semester
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Semester *"
        ).grid(
            row=2,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_semester = ctk.CTkComboBox(
            self.academic_frame,
            values=[],
            command=self.on_semester_changed
        )

        self.cmb_semester.grid(
            row=2,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Division
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Division *"
        ).grid(
            row=2,
            column=4,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.cmb_division = ctk.CTkComboBox(
            self.academic_frame,
            values=[],
            command=self.on_division_changed
        )

        self.cmb_division.grid(
            row=2,
            column=5,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # Roll Number
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="Roll Number"
        ).grid(
            row=3,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_roll_no = ctk.CTkEntry(
            self.academic_frame,
            state="readonly"
        )

        self.entry_roll_no.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ------------------------------------------------------
        # College ID
        # ------------------------------------------------------

        ctk.CTkLabel(
            self.academic_frame,
            text="College ID"
        ).grid(
            row=3,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_college_id = ctk.CTkEntry(
            self.academic_frame,
            state="readonly"
        )

        self.entry_college_id.grid(
            row=3,
            column=3,
            columnspan=3,
            padx=10,
            pady=(8,15),
            sticky="ew"
        )
            # ==========================================================
    # PARENT INFORMATION
    # ==========================================================

    def build_parent_information(self):

        self.parent_frame = ctk.CTkFrame(self.main_frame)

        self.parent_frame.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        ctk.CTkLabel(
            self.parent_frame,
            text="Parent / Guardian Information",
            font=("Segoe UI",18,"bold")
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=15,
            pady=(15,20),
            sticky="w"
        )

        self.parent_frame.grid_columnconfigure(1, weight=1)
        self.parent_frame.grid_columnconfigure(3, weight=1)

        ctk.CTkLabel(
            self.parent_frame,
            text="Parent / Guardian Name"
        ).grid(
            row=1,
            column=0,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_parent_name = ctk.CTkEntry(
            self.parent_frame
        )

        self.entry_parent_name.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.parent_frame,
            text="Parent Mobile"
        ).grid(
            row=1,
            column=2,
            padx=(15,10),
            pady=8,
            sticky="w"
        )

        self.entry_parent_mobile = ctk.CTkEntry(
            self.parent_frame
        )

        self.entry_parent_mobile.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        ctk.CTkLabel(
            self.parent_frame,
            text="Parent Email"
        ).grid(
            row=2,
            column=0,
            padx=(15,10),
            pady=(8,15),
            sticky="w"
        )

        self.entry_parent_email = ctk.CTkEntry(
            self.parent_frame
        )

        self.entry_parent_email.grid(
            row=2,
            column=1,
            columnspan=3,
            padx=10,
            pady=(8,15),
            sticky="ew"
        )

    # ==========================================================
    # ADDRESS INFORMATION
    # ==========================================================

    def build_address_information(self):

        self.address_frame = ctk.CTkFrame(self.main_frame)

        self.address_frame.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        ctk.CTkLabel(
            self.address_frame,
            text="Address Information",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15,20)
        )

        ctk.CTkLabel(
            self.address_frame,
            text="Permanent Address"
        ).pack(
            anchor="w",
            padx=15
        )

        self.txt_permanent_address = ctk.CTkTextbox(
            self.address_frame,
            height=70
        )

        self.txt_permanent_address.pack(
            fill="x",
            padx=15,
            pady=(5,15)
        )

        ctk.CTkLabel(
            self.address_frame,
            text="Local Address"
        ).pack(
            anchor="w",
            padx=15
        )

        self.txt_local_address = ctk.CTkTextbox(
            self.address_frame,
            height=70
        )

        self.txt_local_address.pack(
            fill="x",
            padx=15,
            pady=(5,15)
        )

    # ==========================================================
    # EMERGENCY CONTACT
    # ==========================================================

    def build_emergency_information(self):

        self.emergency_frame = ctk.CTkFrame(self.main_frame)

        self.emergency_frame.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        ctk.CTkLabel(
            self.emergency_frame,
            text="Emergency Contact",
            font=("Segoe UI",18,"bold")
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=15,
            pady=(15,20),
            sticky="w"
        )

        self.emergency_frame.grid_columnconfigure(1, weight=1)
        self.emergency_frame.grid_columnconfigure(3, weight=1)

        ctk.CTkLabel(
            self.emergency_frame,
            text="Contact Name"
        ).grid(
            row=1,
            column=0,
            padx=(15,10),
            pady=(0,15),
            sticky="w"
        )

        self.entry_emergency_name = ctk.CTkEntry(
            self.emergency_frame
        )

        self.entry_emergency_name.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0,15),
            sticky="ew"
        )

        ctk.CTkLabel(
            self.emergency_frame,
            text="Contact Number"
        ).grid(
            row=1,
            column=2,
            padx=(15,10),
            pady=(0,15),
            sticky="w"
        )

        self.entry_emergency_number = ctk.CTkEntry(
            self.emergency_frame
        )

        self.entry_emergency_number.grid(
            row=1,
            column=3,
            padx=10,
            pady=(0,15),
            sticky="ew"
        )
            # ==========================================================
    # PHOTO SECTION
    # ==========================================================

    def build_photo_section(self):

        self.photo_frame = ctk.CTkFrame(self.main_frame)

        self.photo_frame.pack(
            fill="x",
            padx=10,
            pady=(0,15)
        )

        ctk.CTkLabel(
            self.photo_frame,
            text="Student Photograph",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15,20)
        )

        self.photo_label = ctk.CTkLabel(
            self.photo_frame,
            text="No Photo Selected",
            width=180,
            height=180
        )

        self.photo_label.pack(
            pady=10
        )

        button_frame = ctk.CTkFrame(
            self.photo_frame,
            fg_color="transparent"
        )

        button_frame.pack(
            pady=(0,15)
        )

        ctk.CTkButton(
            button_frame,
            text="Browse",
            width=120,
            command=self.browse_photo
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="Remove",
            width=120,
            command=self.remove_photo
        ).pack(
            side="left",
            padx=5
        )

    # ==========================================================
    # BUTTONS
    # ==========================================================

    def build_buttons(self):

        self.button_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.button_frame.pack(
            fill="x",
            padx=10,
            pady=20
        )

        ctk.CTkButton(
            self.button_frame,
            text="Save",
            width=140,
            command=self.save_student
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            self.button_frame,
            text="Clear",
            width=140,
            command=self.clear_form
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            self.button_frame,
            text="Cancel",
            width=140,
            command=self.window.destroy
        ).pack(
            side="right",
            padx=5
        )

    # ==========================================================
    # BROWSE PHOTO
    # ==========================================================

    def browse_photo(self):

        file_path = filedialog.askopenfilename(
            title="Select Student Photo",
            filetypes=[
                ("Image Files","*.png *.jpg *.jpeg")
            ]
        )

        if not file_path:
            return

        self.photo_path = file_path

        self.photo_label.configure(
            text=file_path.split("/")[-1]
        )

    # ==========================================================
    # REMOVE PHOTO
    # ==========================================================

    def remove_photo(self):

        self.photo_path = None

        self.photo_label.configure(
            text="No Photo Selected"
        )

    # ==========================================================
    # LOAD COMBO DATA
    # ==========================================================

    def load_combo_data(self):

        # ------------------------------------------------------
        # LOAD MASTER DATA
        # ------------------------------------------------------

        self.departments = DepartmentService.get_departments()

        self.academic_years = AcademicYearService.get_academic_years()

        self.semesters = SemesterService.get_semesters()

        self.courses = CourseService.get_courses()

        self.divisions = DivisionService.get_all_divisions()

        # ------------------------------------------------------
        # BUILD DEPARTMENT MAP
        # ------------------------------------------------------

        self.department_map = {}

        department_names = []

        for department in self.departments:

            department_names.append(
                department.department_name
            )

            self.department_map[
                department.department_name
            ] = department.department_id

        # ------------------------------------------------------
        # BUILD ACADEMIC YEAR MAP
        # ------------------------------------------------------

        self.academic_year_map = {}

        academic_year_names = []

        for academic_year in self.academic_years:

            academic_year_names.append(
                academic_year.academic_year
            )

            self.academic_year_map[
                academic_year.academic_year
            ] = academic_year.academic_year_id

        # ------------------------------------------------------
        # BUILD SEMESTER MAP
        # ------------------------------------------------------

        self.semester_map = {}

        semester_names = []

        for semester in self.semesters:

            semester_names.append(
                semester.semester_name
            )

            self.semester_map[
                semester.semester_name
            ] = semester.semester_id

        # ------------------------------------------------------
        # INITIALIZE COURSE/DIVISION MAPS
        # ------------------------------------------------------

        self.course_map = {}

        self.division_map = {}

        # ------------------------------------------------------
        # LOAD COMBO VALUES
        # ------------------------------------------------------

        self.cmb_department.configure(
            values=department_names
        )

        self.cmb_academic_year.configure(
            values=academic_year_names
        )

        self.cmb_semester.configure(
            values=semester_names
        )

        self.cmb_course.configure(
            values=[]
        )

        self.cmb_division.configure(
            values=[]
        )

        # ------------------------------------------------------
        # SET DEFAULT VALUES
        # ------------------------------------------------------

        if academic_year_names:

            self.cmb_academic_year.set(
                academic_year_names[0]
            )

            self.selected_academic_year_id = (
                self.academic_year_map[
                    academic_year_names[0]
                ]
            )

        if semester_names:

            self.cmb_semester.set(
                semester_names[0]
            )

            self.selected_semester_id = (
                self.semester_map[
                    semester_names[0]
                ]
            )

        if department_names:

            self.cmb_department.set(
                department_names[0]
            )

            self.selected_department_id = (
                self.department_map[
                    department_names[0]
                ]
            )

            self.on_department_changed(
                department_names[0]
            )
    # ==========================================================
    # DEPARTMENT CHANGED
    # ==========================================================

    def on_department_changed(self, value):

        self.selected_department_id = self.department_map.get(
            value,
            0
        )
        print("Courses available in handler:", len(self.courses))
        print("\nSelected Department ID :", self.selected_department_id)

        for course in self.courses:

            print(
                "Course:",
                course.course_name,
                "Course Department ID:",
                course.department_id,
                type(course.department_id)
            )

        self.course_map = {}

        course_names = []

        for course in self.courses:

            if course.department_id == self.selected_department_id:

                course_names.append(
                    course.course_name
                )

                self.course_map[
                    course.course_name
                ] = course.course_id

        self.cmb_course.configure(
            values=course_names
        )

        if course_names:

            self.cmb_course.set(
                course_names[0]
            )

            self.on_course_changed(
                course_names[0]
            )

        else:

            self.cmb_course.set("")

            self.cmb_division.configure(
                values=[]
            )

            self.cmb_division.set("")

    # ==========================================================
    # COURSE CHANGED
    # ==========================================================

    def on_course_changed(self, value):

        self.selected_course_id = self.course_map.get(
            value,
            0
        )
        print("\nSelected Course ID :", self.selected_course_id)

        for division in self.divisions:

            print(
                "Division:",
                division.division_name,
                "Course ID:",
                division.course_id,
                "Semester:",
                division.semester_id,
                "Academic Year:",
                division.academic_year_id
            )

        self.division_map = {}

        division_names = []

        for division in self.divisions:

            if (
                division.course_id == self.selected_course_id
                and division.semester_id == self.selected_semester_id
                and division.academic_year_id == self.selected_academic_year_id
            ):

                division_names.append(
                    division.division_name
                )

                self.division_map[
                    division.division_name
                ] = division.division_id

        self.cmb_division.configure(
            values=division_names
        )

        if division_names:

            self.cmb_division.set(
                division_names[0]
            )

            self.on_division_changed(
                division_names[0]
            )

        else:

            self.cmb_division.set("")

    # ==========================================================
    # SEMESTER CHANGED
    # ==========================================================

    def on_semester_changed(self, value):

        self.selected_semester_id = self.semester_map.get(
            value,
            0
        )

        if self.cmb_course.get():

            self.on_course_changed(
                self.cmb_course.get()
            )

    # ==========================================================
    # DIVISION CHANGED
    # ==========================================================

    def on_division_changed(self, value):

        self.selected_division_id = self.division_map.get(
            value,
            0
        )

    # ==========================================================
    # ACADEMIC YEAR CHANGED
    # ==========================================================

    def on_academic_year_changed(self, value):

        self.selected_academic_year_id = self.academic_year_map.get(
            value,
            0
        )

        if self.cmb_course.get():

            self.on_course_changed(
                self.cmb_course.get()
            )
    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.entry_first_name.delete(0, "end")
        self.entry_middle_name.delete(0, "end")
        self.entry_last_name.delete(0, "end")

        self.cmb_gender.set("")

        self.entry_dob.delete(0, "end")

        self.entry_prn.delete(0, "end")

        self.entry_mobile.delete(0, "end")

        self.entry_email.delete(0, "end")

        self.entry_parent_name.delete(0, "end")

        self.entry_parent_mobile.delete(0, "end")

        self.entry_parent_email.delete(0, "end")

        self.txt_permanent_address.delete("1.0", "end")

        self.txt_local_address.delete("1.0", "end")

        self.entry_emergency_name.delete(0, "end")

        self.entry_emergency_number.delete(0, "end")

        self.cmb_admission_year.set("")

        self.cmb_academic_year.set("")

        self.cmb_department.set("")

        self.cmb_course.configure(values=[])

        self.cmb_course.set("")

        self.cmb_semester.set("")

        self.cmb_division.configure(values=[])

        self.cmb_division.set("")

        self.entry_roll_no.configure(state="normal")

        self.entry_roll_no.delete(0, "end")

        self.entry_roll_no.configure(state="readonly")

        self.entry_college_id.configure(state="normal")

        self.entry_college_id.delete(0, "end")

        self.entry_college_id.configure(state="readonly")

        self.photo_path = None

        self.photo_label.configure(
            text="No Photo Selected"
        )

        self.selected_department_id = 0

        self.selected_course_id = 0

        self.selected_semester_id = 0

        self.selected_division_id = 0

        self.selected_academic_year_id = 0

    # ==========================================================
    # SET READONLY ENTRY
    # ==========================================================

    def set_readonly_value(self, entry, value):

        entry.configure(state="normal")

        entry.delete(0, "end")

        entry.insert(0, value)

        entry.configure(state="readonly")

    # ==========================================================
    # LOAD STUDENT
    # ==========================================================

    def load_student(self):

        student = StudentService.get_student(
            self.student_id
        )

        if student is None:

            messagebox.showerror(
                "Error",
                "Student record not found."
            )

            self.window.destroy()

            return

        self.entry_first_name.insert(
            0,
            student.first_name
        )

        self.entry_middle_name.insert(
            0,
            student.middle_name
        )

        self.entry_last_name.insert(
            0,
            student.last_name
        )

        self.cmb_gender.set(
            student.gender
        )

        self.entry_dob.insert(
            0,
            student.date_of_birth
        )

        self.entry_prn.insert(
            0,
            student.prn
        )

        self.entry_mobile.insert(
            0,
            student.mobile
        )

        self.entry_email.insert(
            0,
            student.email
        )

        self.entry_parent_name.insert(
            0,
            student.parent_name
        )

        self.entry_parent_mobile.insert(
            0,
            student.parent_mobile
        )

        self.entry_parent_email.insert(
            0,
            student.parent_email
        )

        self.txt_permanent_address.insert(
            "1.0",
            student.permanent_address
        )

        self.txt_local_address.insert(
            "1.0",
            student.local_address
        )

        self.entry_emergency_name.insert(
            0,
            student.emergency_contact_name
        )

        self.entry_emergency_number.insert(
            0,
            student.emergency_contact_number
        )

        self.cmb_admission_year.set(
            str(student.admission_year)
        )

        for academic_year in self.academic_years:

            if academic_year.academic_year_id == student.academic_year_id:

                self.cmb_academic_year.set(
                    academic_year.academic_year
                )

                self.selected_academic_year_id = academic_year.academic_year_id

                break

        for department in self.departments:

            if department.department_id == student.department_id:

                self.cmb_department.set(
                    department.department_name
                )

                self.on_department_changed(
                    department.department_name
                )

                break

        for course in self.courses:

            if course.course_id == student.course_id:

                self.cmb_course.set(
                    course.course_name
                )

                self.on_course_changed(
                    course.course_name
                )

                break

        for semester in self.semesters:

            if semester.semester_id == student.semester_id:

                self.cmb_semester.set(
                    semester.semester_name
                )

                self.on_semester_changed(
                    semester.semester_name
                )

                break

        for division in self.divisions:

            if division.division_id == student.division_id:

                self.cmb_division.set(
                    division.division_name
                )

                self.on_division_changed(
                    division.division_name
                )

                break

        self.set_readonly_value(
            self.entry_roll_no,
            student.roll_no
        )

        self.set_readonly_value(
            self.entry_college_id,
            student.college_id
        )

        self.photo_path = student.photo

        if student.photo:

            self.photo_label.configure(
                text=student.photo.split("/")[-1]
            )
    # ==========================================================
    # SAVE STUDENT
    # ==========================================================

    def save_student(self):

        first_name = self.entry_first_name.get().strip()

        middle_name = self.entry_middle_name.get().strip()

        last_name = self.entry_last_name.get().strip()

        gender = self.cmb_gender.get().strip()

        date_of_birth = self.entry_dob.get().strip()

        prn = self.entry_prn.get().strip()

        mobile = self.entry_mobile.get().strip()

        email = self.entry_email.get().strip()

        parent_name = self.entry_parent_name.get().strip()

        parent_mobile = self.entry_parent_mobile.get().strip()

        parent_email = self.entry_parent_email.get().strip()

        permanent_address = self.txt_permanent_address.get(
            "1.0",
            "end"
        ).strip()

        local_address = self.txt_local_address.get(
            "1.0",
            "end"
        ).strip()

        emergency_contact_name = self.entry_emergency_name.get().strip()

        emergency_contact_number = self.entry_emergency_number.get().strip()

        try:

            admission_year = int(
                self.cmb_admission_year.get()
            )

        except ValueError:

            messagebox.showerror(
                "Validation",
                "Please select Admission Year."
            )

            return

        academic_year_id = self.selected_academic_year_id

        department_id = self.selected_department_id

        course_id = self.selected_course_id

        semester_id = self.selected_semester_id

        division_id = self.selected_division_id

        photo = self.photo_path

        if self.student_id is None:

            success, message = StudentService.add_student(

                first_name=first_name,

                last_name=last_name,

                admission_year=admission_year,

                academic_year_id=academic_year_id,

                department_id=department_id,

                course_id=course_id,

                semester_id=semester_id,

                division_id=division_id,

                prn=prn,

                mobile=mobile,

                email=email,

                middle_name=middle_name,

                gender=gender,

                date_of_birth=date_of_birth,

                parent_name=parent_name,

                parent_mobile=parent_mobile,

                parent_email=parent_email,

                permanent_address=permanent_address,

                local_address=local_address,

                emergency_contact_name=emergency_contact_name,

                emergency_contact_number=emergency_contact_number,

                photo=photo,

                is_active=True

            )
            if success:

                messagebox.showinfo(
                    "Success",
                    message
                )

                self.window.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    message
                )

            return

        success, message = StudentService.update_student(

            student_id=self.student_id,

            first_name=first_name,

            middle_name=middle_name,

            last_name=last_name,

            gender=gender,

            date_of_birth=date_of_birth,

            mobile=mobile,

            email=email,

            parent_name=parent_name,

            parent_mobile=parent_mobile,

            parent_email=parent_email,

            permanent_address=permanent_address,

            local_address=local_address,

            emergency_contact_name=emergency_contact_name,

            emergency_contact_number=emergency_contact_number,

            prn=prn,

            admission_year=admission_year,

            academic_year_id=academic_year_id,

            department_id=department_id,

            course_id=course_id,

            semester_id=semester_id,

            division_id=division_id,

            photo=photo,

            is_active=True

        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

            self.window.destroy()

        else:

            messagebox.showerror(
                "Error",
                message
            )


