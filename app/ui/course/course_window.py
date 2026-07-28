"""
FacultyERP
Course Management
-----------------
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import customtkinter as ctk

from app.services.course_service import CourseService
from app.services.department_service import DepartmentService


class CourseWindow:
    """Course Management Window."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.selected_course_id = None

        self.department_map = {}

        self.build_ui()

        self.initialize()

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def initialize(self):

        self.update_button.configure(
            state="disabled"
        )

        self.delete_button.configure(
            state="disabled"
        )

        self.load_departments()

        self.load_courses()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        for widget in self.parent.winfo_children():

            widget.destroy()

        self.parent.grid_rowconfigure(
            3,
            weight=1
        )

        self.parent.grid_columnconfigure(
            0,
            weight=1
        )

        # =====================================================
        # TITLE
        # =====================================================

        title = ctk.CTkLabel(

            self.parent,

            text="Course Management",

            font=("Segoe UI", 24, "bold")

        )

        title.grid(

            row=0,

            column=0,

            sticky="w",

            padx=20,

            pady=(15, 10)

        )

        # =====================================================
        # FORM
        # =====================================================

        form = ctk.CTkFrame(

            self.parent

        )

        form.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=20

        )

        form.grid_columnconfigure(
            1,
            weight=1
        )

        form.grid_columnconfigure(
            3,
            weight=1
        )

        # =====================================================
        # COURSE CODE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Course ID"

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.code_entry = ctk.CTkEntry(

            form,

            state="readonly"

        )

        self.code_entry.grid(

            row=0,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # DEPARTMENT
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Department"

        ).grid(

            row=0,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.department_combo = ctk.CTkComboBox(

            form,

            values=[],

            state="readonly"

        )

        self.department_combo.grid(

            row=0,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # DEGREE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Degree"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.degree_combo = ctk.CTkComboBox(

            form,

            values=[

                "Diploma",
                "BE",

                "ME"

            ],

            state="readonly"

        )

        self.degree_combo.grid(

            row=1,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.degree_combo.set(

            "BE"

        )

        # =====================================================
        # PATTERN
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Pattern"

        ).grid(

            row=1,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.pattern_combo = ctk.CTkComboBox(

            form,

            values=[

                "2020 Pattern",

                "2024 Pattern"

            ],

            state="readonly"

        )

        self.pattern_combo.grid(

            row=1,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.pattern_combo.set(

            "2024 Pattern"

        )
                # =====================================================
        # COURSE NAME
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Course Name"

        ).grid(

            row=2,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.name_entry = ctk.CTkEntry(

            form

        )

        self.name_entry.grid(

            row=2,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # SHORT NAME
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Short Name"

        ).grid(

            row=2,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.short_name_entry = ctk.CTkEntry(

            form

        )

        self.short_name_entry.grid(

            row=2,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # DURATION
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Duration (Years)"

        ).grid(

            row=3,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.duration_combo = ctk.CTkComboBox(

            form,

            values=[

                "2",
                "3",

                "4"

            ],

            state="readonly"

        )

        self.duration_combo.grid(

            row=3,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.duration_combo.set(

            "4"

        )

        # =====================================================
        # INTAKE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Intake"

        ).grid(

            row=3,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.intake_entry = ctk.CTkEntry(

            form

        )

        self.intake_entry.grid(

            row=3,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # DESCRIPTION
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Description"

        ).grid(

            row=4,

            column=0,

            padx=10,

            pady=8,

            sticky="nw"

        )

        self.description_text = tk.Text(

            form,

            height=4,

            font=("Segoe UI", 10)

        )

        self.description_text.grid(

            row=4,

            column=1,

            columnspan=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # AUTO COURSE NAME
        # =====================================================

        self.department_combo.configure(

            command=self.generate_course_name

        )

        self.degree_combo.configure(

            command=self.on_degree_changed

        )
                # =====================================================
        # BUTTON FRAME
        # =====================================================

        button_frame = ctk.CTkFrame(

            self.parent

        )

        button_frame.grid(

            row=2,

            column=0,

            sticky="ew",

            padx=20,

            pady=10

        )

        self.save_button = ctk.CTkButton(

            button_frame,

            text="Save",

            width=120,

            command=self.save_course

        )

        self.save_button.pack(

            side="left",

            padx=5

        )

        self.update_button = ctk.CTkButton(

            button_frame,

            text="Update",

            width=120,

            command=self.update_course

        )

        self.update_button.pack(

            side="left",

            padx=5

        )

        self.delete_button = ctk.CTkButton(

            button_frame,

            text="Delete",

            width=120,

            command=self.delete_course

        )

        self.delete_button.pack(

            side="left",

            padx=5

        )

        self.clear_button = ctk.CTkButton(

            button_frame,

            text="Clear",

            width=120,

            command=self.clear_form

        )

        self.clear_button.pack(

            side="left",

            padx=5

        )

        # =====================================================
        # COURSE TABLE
        # =====================================================

        table_frame = ctk.CTkFrame(

            self.parent

        )

        table_frame.grid(

            row=3,

            column=0,

            sticky="nsew",

            padx=20,

            pady=(0,20)

        )

        columns = (

            "ID",

            "Course ID",

            "Course Name",

            "Degree",

            "Pattern",

            "Duration",

            "Intake",

            "Department"

        )

        self.tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            height=14

        )

        for col in columns:

            self.tree.heading(

                col,

                text=col

            )

        self.tree.column(

            "ID",

            width=60,

            anchor="center"

        )

        self.tree.column(

            "Course ID",

            width=120,

            anchor="center"

        )

        self.tree.column(

            "Course Name",

            width=240

        )

        self.tree.column(

            "Degree",

            width=80,

            anchor="center"

        )

        self.tree.column(

            "Pattern",

            width=130,

            anchor="center"

        )

        self.tree.column(

            "Duration",

            width=90,

            anchor="center"

        )

        self.tree.column(

            "Intake",

            width=90,

            anchor="center"

        )

        self.tree.column(

            "Department",

            width=220

        )

        scrollbar = ttk.Scrollbar(

            table_frame,

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

            self.on_row_selected

        )
    
    
    # ==========================================================
    # DEGREE CHANGED
    # ==========================================================

    def on_degree_changed(self, value=None):

        degree = self.degree_combo.get()

        if degree == "Diploma":

            self.duration_combo.set("3")

        elif degree == "BE":

            self.duration_combo.set("4")

        elif degree == "ME":

            self.duration_combo.set("2")

        self.generate_course_name()
    # ==========================================================
    # GENERATE COURSE NAME
    # ==========================================================

    def generate_course_name(self, value=None):
        department_name = self.department_combo.get().strip()
        degree = self.degree_combo.get().strip()
        if department_name == "" or degree == "":
            return
        course_name = f"{degree} {department_name}"
        self.name_entry.delete(
            0,
            tk.END
        )

        self.name_entry.insert(
            0,
            course_name
        )

        #
        # Generate Short Name
        #

        department = DepartmentService.get_department_by_name(
            department_name
        )

        if department:

            short_name = (
                degree +
                department.department_code
            )

        else:

            short_name = degree

        self.short_name_entry.delete(
            0,
            tk.END
        )

        self.short_name_entry.insert(
            0,
            short_name)

    # ==========================================================
    # LOAD DEPARTMENTS
    # ==========================================================

    def load_departments(self):

        self.department_map.clear()

        departments = DepartmentService.get_departments()

        department_names = []

        for department in departments:

            department_names.append(
                department.department_name
            )

            self.department_map[
                department.department_name
            ] = department.department_id

        department_names.insert(
            0,
            "Select Department"
        )

        self.department_combo.configure(
            values=department_names
        )

        self.department_combo.set(
            "Select Department"
        )

        self.name_entry.delete(
            0,
            tk.END
        )

        self.short_name_entry.delete(
            0,
            tk.END
        )

    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        courses = CourseService.get_courses()

        for course in courses:

            department = DepartmentService.get_department(
                course.department_id
            )

            self.tree.insert(

                "",

                tk.END,

                values=(

                    course.course_id,

                    course.course_code,

                    course.course_name,

                    course.degree,

                    course.pattern,

                    course.duration_years,

                    course.intake,

                    department.department_name
                    if department else ""

                )

            )

        #
        # Generate Next Course Code
        #

        self.code_entry.configure(
            state="normal"
        )

        self.code_entry.delete(
            0,
            tk.END
        )

        self.code_entry.insert(

            0,

            CourseService.generate_course_code()

        )

        self.code_entry.configure(
            state="readonly"
        )
            # ==========================================================
    # VALIDATE FORM
    # ==========================================================

    def validate_form(self):

        if not self.department_combo.get():

            messagebox.showwarning(

                "Course",

                "Please select Department."

            )

            return False

        if not self.degree_combo.get():

            messagebox.showwarning(

                "Course",

                "Please select Degree."

            )

            return False

        if not self.pattern_combo.get():

            messagebox.showwarning(

                "Course",

                "Please select Pattern."

            )

            return False

        if not self.name_entry.get().strip():

            messagebox.showwarning(

                "Course",

                "Course Name is required."

            )

            return False

        if not self.short_name_entry.get().strip():

            messagebox.showwarning(

                "Course",

                "Short Name is required."

            )

            return False

        intake = self.intake_entry.get().strip()

        if intake != "" and not intake.isdigit():

            messagebox.showwarning(

                "Course",

                "Intake must be numeric."

            )

            self.intake_entry.focus()

            return False

        return True

    # ==========================================================
    # SAVE COURSE
    # ==========================================================

    def save_course(self):

        self.generate_course_name()

        if not self.validate_form():

            return

        department = DepartmentService.get_department_by_name(

            self.department_combo.get()

        )

        if department is None:

            messagebox.showwarning(

                "Course",

                "Please select Department."

            )

            return

        success, message = CourseService.add_course(

            self.name_entry.get().strip(),

            self.short_name_entry.get().strip(),

            self.degree_combo.get(),

            self.pattern_combo.get(),

            self.duration_combo.get(),

            self.intake_entry.get().strip(),

            department.department_id,

            self.description_text.get(

                "1.0",

                tk.END

            ).strip()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

            self.load_courses()

        else:

            messagebox.showwarning(

                "Course",

                message

            )

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_course_id = None

        self.intake_entry.delete(

            0,

            tk.END

        )

        self.description_text.delete(

            "1.0",

            tk.END

        )

        if self.department_combo.cget("values"):

            self.department_combo.set(

                self.department_combo.cget("values")[0]

            )

        self.generate_course_name()

        self.degree_combo.set("BE")

        self.pattern_combo.set("2024 Pattern")

        self.on_degree_changed()

        self.save_button.configure(

            state="normal"

        )

        self.update_button.configure(

            state="disabled"

        )

        self.delete_button.configure(

            state="disabled"

        )

        self.load_courses()
            # ==========================================================
    # ROW SELECTED
    # ==========================================================

    def on_row_selected(self, event):

        selection = self.tree.selection()

        if not selection:

            return

        item = self.tree.item(selection[0])

        course_id = item["values"][0]

        course = CourseService.get_course(course_id)

        if course is None:

            return

        self.selected_course_id = course.course_id

        # ------------------------------------------------------
        # Course Code
        # ------------------------------------------------------

        self.code_entry.configure(state="normal")

        self.code_entry.delete(0, tk.END)

        self.code_entry.insert(0, course.course_code)

        self.code_entry.configure(state="readonly")

        # ------------------------------------------------------
        # Course Name
        # ------------------------------------------------------

        self.name_entry.delete(0, tk.END)

        self.name_entry.insert(0, course.course_name)

        # ------------------------------------------------------
        # Short Name
        # ------------------------------------------------------

        self.short_name_entry.delete(0, tk.END)

        self.short_name_entry.insert(0, course.course_short_name)

        # ------------------------------------------------------
        # Degree
        # ------------------------------------------------------

        self.degree_combo.set(course.degree)

        # ------------------------------------------------------
        # Pattern
        # ------------------------------------------------------

        self.pattern_combo.set(course.pattern)

        # ------------------------------------------------------
        # Duration
        # ------------------------------------------------------

        self.duration_combo.set(str(course.duration_years))

        # ------------------------------------------------------
        # Intake
        # ------------------------------------------------------

        self.intake_entry.delete(0, tk.END)

        self.intake_entry.insert(0, str(course.intake))

        # ------------------------------------------------------
        # Department
        # ------------------------------------------------------

        department = DepartmentService.get_department(
            course.department_id
        )

        if department:

            self.department_combo.set(
                department.department_name
            )

        # ------------------------------------------------------
        # Description
        # ------------------------------------------------------

        self.description_text.delete(
            "1.0",
            tk.END
        )

        self.description_text.insert(
            "1.0",
            course.description or ""
        )

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
    # UPDATE COURSE
    # ==========================================================

    def update_course(self):

        if self.selected_course_id is None:

            return

        self.on_degree_changed()

        if not self.validate_form():

            return

        department = DepartmentService.get_department_by_name(

            self.department_combo.get()

        )

        if department is None:

            return

        success, message = CourseService.update_course(

            self.selected_course_id,

            self.code_entry.get(),

            self.name_entry.get().strip(),

            self.short_name_entry.get().strip(),

            self.degree_combo.get(),

            self.pattern_combo.get(),

            self.duration_combo.get(),

            self.intake_entry.get().strip(),

            department.department_id,

            self.description_text.get(
                "1.0",
                tk.END
            ).strip()

        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

            self.clear_form()

            self.load_courses()

        else:

            messagebox.showwarning(
                "Course",
                message
            )

    # ==========================================================
    # DELETE COURSE
    # ==========================================================

    def delete_course(self):

        if self.selected_course_id is None:

            return

        answer = messagebox.askyesno(

            "Delete Course",

            "Are you sure you want to delete this course?"

        )

        if not answer:

            return

        success, message = CourseService.delete_course(

            self.selected_course_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

            self.load_courses()

        else:

            messagebox.showwarning(

                "Course",

                message

            )
            