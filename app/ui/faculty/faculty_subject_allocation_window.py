"""
FacultyERP
Faculty Subject Allocation Window
---------------------------------
"""

import customtkinter as ctk
from tkinter import ttk

from app.services.faculty_subject_allocation_service import (
    FacultySubjectAllocationService
)
from app.services.academic_year_service import AcademicYearService
from app.services.department_service import DepartmentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService
from app.services.semester_service import SemesterService
from app.services.subject_service import SubjectService
from app.services.division_service import DivisionService


class FacultySubjectAllocationWindow(ctk.CTkToplevel):
    """Faculty Subject Allocation Window."""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Faculty Subject Allocation")
        self.geometry("1050x650")
        self.resizable(True, True)
        self.transient(parent)
        self.grab_set()
        self.selected_allocation_id = None
        self.academic_year_map = {}
        self.department_map = {}
        self.course_map = {}
        self.semester_map = {}
        self.subject_map = {}
        self.division_map = {}
        self.faculty_map = {}
        self.create_widgets()
        self.initialize()
        
    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def initialize(self):

        self.load_academic_years()
        self.load_semesters()
        self.load_departments()
        self.load_faculty()
        self.load_allocations()

        
    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        title_label = ctk.CTkLabel(self, text="Faculty Subject Allocation", font=("Segoe UI", 20, "bold"))
        title_label.grid(row=0, column=0, padx=20, pady=(15, 10), sticky="w")
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

        row = 0

        ctk.CTkLabel(self.main_frame, text="Academic Year").grid(row=row, column=0, padx=10, pady=(12, 2), sticky="w")
        self.academic_year_combo = ctk.CTkComboBox(self.main_frame, values=[])
        self.academic_year_combo.grid(row=row + 1, column=0, padx=10, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.main_frame, text="Department").grid(row=row, column=1, padx=10, pady=(12, 2), sticky="w")
        self.department_combo = ctk.CTkComboBox(self.main_frame, values=[], command=self.on_department_changed)
        self.department_combo.grid(row=row + 1, column=1, padx=10, pady=(0, 10), sticky="ew")

        row += 2

        ctk.CTkLabel(self.main_frame, text="Course").grid(row=row, column=0, padx=10, pady=(10, 2), sticky="w")
        self.course_combo = ctk.CTkComboBox(self.main_frame, values=[], command=self.on_course_changed)
        self.course_combo.grid(row=row + 1, column=0, padx=10, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.main_frame, text="Semester" ).grid(row=row, column=1, padx=10, pady=(10, 2), sticky="w")
        self.semester_combo = ctk.CTkComboBox(self.main_frame, values=[], command=self.on_semester_changed)

        self.semester_combo.grid(row=row + 1, column=1, padx=10, pady=(0, 10), sticky="ew")
        row += 2

        ctk.CTkLabel(self.main_frame, text="Division").grid(row=row, column=0, padx=10, pady=(10, 2), sticky="w")

        self.division_combo = ctk.CTkComboBox(self.main_frame, values=[])
        self.division_combo.grid(row=row + 1, column=0, padx=10, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.main_frame, text="Faculty").grid(row=row, column=1, padx=10, pady=(10, 2), sticky="w")
        self.faculty_combo = ctk.CTkComboBox(self.main_frame, values=[])
        self.faculty_combo.grid(row=row + 1, column=1, padx=10, pady=(0, 10), sticky="ew")
        row += 2
        ctk.CTkLabel(self.main_frame, text="Subject").grid(row=row, column=0,  padx=10, pady=(10, 2), sticky="w")
        self.subject_combo = ctk.CTkComboBox(self.main_frame, values=[])
        self.subject_combo.grid(row=row + 1, column=0, padx=10, pady=(0, 10), sticky="ew")
        ctk.CTkLabel(self.main_frame, text="Batch").grid(row=row, column=1, padx=10, pady=(10, 2), sticky="w")
        #BATCH_VALUES = ["Full", "Batch A", "Batch B", "Batch C"]
        self.batch_combo = ctk.CTkComboBox(self.main_frame, values=["Full", "Batch A", "Batch B", "Batch C"])
        self.batch_combo.set("Full")
        self.batch_combo.grid(row=row + 1, column=1, padx=10, pady=(0, 10), sticky="ew")

        row += 2

        ctk.CTkLabel(self.main_frame, text="Theory Hours" ).grid(row=row, column=0, padx=10, pady=(10, 2), sticky="w")
        self.theory_entry = ctk.CTkEntry(self.main_frame)
        self.theory_entry.insert(0, "0")
        self.theory_entry.grid(row=row + 1, column=0, padx=10, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(self.main_frame, text="Practical Hours").grid(row=row, column=1, padx=10, pady=(10, 2), sticky="w")
        self.practical_entry = ctk.CTkEntry(self.main_frame)
        self.practical_entry.insert(0, "0")

        self.practical_entry.grid(row=row + 1, column=1, padx=10, pady=(0, 10), sticky="ew")
        row += 2

        ctk.CTkLabel(self.main_frame, text="Tutorial Hours").grid(row=row, column=0, padx=10, pady=(10, 2), sticky="w")
        self.tutorial_entry = ctk.CTkEntry(self.main_frame)
        self.tutorial_entry.insert(0,"0")
        self.tutorial_entry.grid(row=row + 1, column=0, padx=10, pady=(0, 10),sticky="ew")

        ctk.CTkLabel(self.main_frame, text="Workload Hours").grid(row=row,column=1, padx=10, pady=(10, 2), sticky="w")
        self.workload_entry = ctk.CTkEntry(self.main_frame, state="normal")
        self.workload_entry.insert(0, "0")
        self.workload_entry.configure(state="disabled")
        self.workload_entry.grid(row=row + 1, column=1, padx=10, pady=(0, 10), sticky="ew")

        row += 2

        self.class_teacher_var = ctk.BooleanVar(value=False)
        self.class_teacher_check = ctk.CTkCheckBox(self.main_frame, text="Class Teacher", variable=self.class_teacher_var)
        self.class_teacher_check.grid(row=row, column=0, padx=10, pady=(10, 10), sticky="w" )

        row += 1

        ctk.CTkLabel(self.main_frame, text="Remarks").grid(row=row, column=0, padx=10, pady=(10, 2), sticky="w")
        self.remarks_text = ctk.CTkTextbox(self.main_frame, height=50)
        self.remarks_text.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="ew")

        row += 2
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.grid(row=row, column=0, columnspan=2, padx=10, pady=15, sticky="ew")
        self.save_button = ctk.CTkButton(self.button_frame, text="Save", width=120, command=self.save_allocation)
        self.save_button.pack(side="left", padx=5)
        self.update_button = ctk.CTkButton(self.button_frame, text="Update",width=120, command=self.update_allocation)
        self.update_button.pack(side="left", padx=5)
        self.delete_button = ctk.CTkButton(self.button_frame, text="Delete", width=120, command=self.delete_allocation)
        self.delete_button.pack(side="left", padx=5)
        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear", width=120, command=self.clear_form)
        self.clear_button.pack(side="left", padx=5)

        row += 1
        self.tree_frame = ctk.CTkFrame(self.main_frame)
        self.tree_frame.grid(row=row, column=0, columnspan=2, padx=10, pady=(15, 10), sticky="nsew")
        self.main_frame.rowconfigure(row, weight=1)
        columns = ("Faculty", "Subject", "Division", "Batch", "Theory", "Practical", "Tutorial", "Workload" )
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", height=6)
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=120, anchor="center")
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both",expand=True)
        scrollbar.pack(side="right", fill="y")

    # ==========================================================
    # LOAD ACADEMIC YEARS
    # ==========================================================

    def load_academic_years(self):
        self.academic_year_map.clear()
        academic_years = AcademicYearService.get_academic_years()
        names = []
        for year in academic_years:
            names.append(year.academic_year)
            self.academic_year_map[year.academic_year] = year.academic_year_id
        self.academic_year_combo.configure(values=names)
        if names:
            current = AcademicYearService.get_current_academic_year()
            if current:
                self.academic_year_combo.set(current.academic_year)
            else:
                self.academic_year_combo.set(names[0])

    # ==========================================================
    # LOAD DEPARTMENTS
    # ==========================================================
    def load_departments(self):
        self.department_map.clear()
        departments = DepartmentService.get_departments()
        names = []
        for department in departments:
            names.append(department.department_name)
            self.department_map[department.department_name] = department.department_id
        self.department_combo.configure(values=names)
        if names:
            self.department_combo.set(names[0])
            self.load_courses()

    # ==========================================================
    # DEPARTMENT CHANGED
    # ==========================================================
    def on_department_changed(self, value): self.load_courses()

    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):
        self.course_map.clear()
        department_name = self.department_combo.get()
        if department_name == "":
            self.course_combo.configure(values=[])
            self.course_combo.set("")
            return
        department_id = self.department_map.get(department_name)
        courses = CourseService.get_courses_by_department(department_id)
        names = []

        for course in courses:
            names.append(course.course_name)
            self.course_map[course.course_name] = course.course_id
        self.course_combo.configure(values=names)
        if names:
            self.course_combo.set(names[0])
            self.load_subjects()
            self.load_divisions()
        else:
            self.course_combo.set("")
            self.subject_combo.configure(values=[])
            self.subject_combo.set("")
            self.division_combo.configure(values=[])
            self.division_combo.set("")
    # ==========================================================
    # LOAD SEMESTERS
    # ==========================================================

    def load_semesters(self):
        self.semester_map.clear()
        semesters = SemesterService.get_semesters()
        names = []
        for semester in semesters:names.append(semester.semester_name)
        self.semester_map[semester.semester_name] = semester.semester_id
        self.semester_combo.configure(values=names)
        if names: self.semester_combo.set(names[0])

    # ==========================================================
    # COURSE CHANGED
    # ==========================================================
    def on_course_changed(self, value):
        self.load_subjects()
        self.load_divisions()

    # ==========================================================
    # SEMESTER CHANGED
    # ==========================================================

    def on_semester_changed(self, value):
        self.load_subjects()
        self.load_divisions()

    # ==========================================================
    # LOAD SUBJECTS
    # ==========================================================

    def load_subjects(self):
        self.subject_map.clear()
        course_name = self.course_combo.get()
        semester_name = self.semester_combo.get()

        if course_name == "" or semester_name == "":
            self.subject_combo.configure(values=[])
            self.subject_combo.set("")
            return

        course_id = self.course_map.get(course_name)
        semester_id = self.semester_map.get(semester_name)
        print(course_id, semester_id)
        subjects = SubjectService.get_subjects_by_course_semester(
            course_id,
            semester_id
        )

        names = []

        for subject in subjects:
            names.append(subject.subject_name)
            self.subject_map[
                subject.subject_name
            ] = subject.subject_id
        self.subject_combo.configure(values=names)
        if names:
            self.subject_combo.set(names[0])
        else:
            self.subject_combo.set("")

    # ==========================================================
    # LOAD DIVISIONS
    # ==========================================================

    def load_divisions(self):
        self.division_map.clear()
        academic_year_name = self.academic_year_combo.get()
        course_name = self.course_combo.get()
        semester_name = self.semester_combo.get()

        if (academic_year_name == "" or course_name == "" or semester_name == ""):
            self.division_combo.configure(values=[])
            self.division_combo.set("")
            return

        academic_year_id = self.academic_year_map.get(academic_year_name)

        course_id = self.course_map.get(course_name)

        semester_id = self.semester_map.get(semester_name)
        print(academic_year_id, course_id, semester_id)
        divisions = DivisionService.get_divisions_by_course_year_semester(course_id, academic_year_id, semester_id)

        names = []

        for division in divisions:

            names.append(division.division_name)
            self.division_map[division.division_name] = division.division_id

        self.division_combo.configure(values=names)

        if names: self.division_combo.set(names[0])
        else:
            self.division_combo.set("")
            


    # ==========================================================
    # LOAD FACULTY
    # ==========================================================

    def load_faculty(self):
        self.faculty_map.clear()
        faculty_members = FacultyService.get_faculty()
        names = []
        for faculty in faculty_members:
            full_name = (f"{faculty.first_name} " f"{faculty.last_name}")
            names.append(full_name)
            self.faculty_map[full_name] = faculty.faculty_id
        self.faculty_combo.configure(values=names)
        if names: self.faculty_combo.set(names[0])
    # ==========================================================
    # BUTTON EVENTS
    # ==========================================================

    def save_allocation(self): print("Save Allocation")
    def update_allocation(self): print("Update Allocation")
    def delete_allocation(self): print("Delete Allocation")
    def clear_form(self):
        self.selected_allocation_id = None
        self.academic_year_combo.set("")
        self.department_combo.set("")
        self.course_combo.set("")
        self.semester_combo.set("")
        self.division_combo.set("")
        self.faculty_combo.set("")
        self.subject_combo.set("")
        self.batch_entry.delete(0, "end")
        self.batch_entry.insert(0, "Full")
        self.theory_entry.delete(0, "end")
        self.theory_entry.insert(0, "0")
        self.practical_entry.delete(0, "end")
        self.practical_entry.insert(0, "0")
        self.tutorial_entry.delete(0, "end")
        self.tutorial_entry.insert(0, "0")
        self.workload_entry.configure(state="normal")
        self.workload_entry.delete(0, "end")
        self.workload_entry.insert(0, "0")
        self.workload_entry.configure(state="disabled")
        self.class_teacher_var.set(False)
        self.remarks_text.delete("1.0", "end")

    def load_allocations(self):
        """Will be implemented in next step."""
        pass