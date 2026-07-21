"""
FacultyERP
Subject Management
------------------
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import customtkinter as ctk

from app.services.subject_service import SubjectService
from app.services.department_service import DepartmentService
from app.services.course_service import CourseService


class SubjectWindow:
    """Subject Management Window."""

    def __init__(self, parent):

        self.parent = parent

        self.selected_subject_id = None

        self.department_map = {}

        self.course_map = {}

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

        self.load_subjects()

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

            text="Subject Management",

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

        form.grid_columnconfigure(1, weight=1)
        form.grid_columnconfigure(3, weight=1)

        # =====================================================
        # SUBJECT CODE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Subject Code"

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

            values=[]

        )

        self.department_combo.grid(

            row=0,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # SUBJECT NAME
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Subject Name"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.name_entry = ctk.CTkEntry(

            form

        )

        self.name_entry.grid(

            row=1,

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

            row=1,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.short_name_entry = ctk.CTkEntry(

            form

        )

        self.short_name_entry.grid(

            row=1,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # COURSE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Course"

        ).grid(

            row=2,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.course_combo = ctk.CTkComboBox(

            form,

            values=[]

        )

        self.course_combo.grid(

            row=2,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # SEMESTER
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Semester"

        ).grid(

            row=2,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.semester_combo = ctk.CTkComboBox(

            form,

            values=[

                "1","2","3","4",

                "5","6","7","8"

            ]

        )

        self.semester_combo.grid(

            row=2,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.semester_combo.set("1")
                # =====================================================
        # CREDITS
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Credits"

        ).grid(

            row=3,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.credits_combo = ctk.CTkComboBox(

            form,

            values=[

                "1",

                "2",

                "3",

                "4",

                "5",

                "6"

            ]

        )

        self.credits_combo.grid(

            row=3,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.credits_combo.set("4")

        # =====================================================
        # SUBJECT TYPE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Subject Type"

        ).grid(

            row=4,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.subject_type_combo = ctk.CTkComboBox(

            form,

            values=[

                "Theory",

                "Practical",

                "Theory + Practical"

            ],

            state="readonly"

        )

        self.subject_type_combo.grid(

            row=4,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.subject_type_combo.set(

            "Theory"

        )
        # =====================================================
        # THEORY HOURS
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Theory Hours"

        ).grid(

            row=4,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.theory_hours_combo = ctk.CTkComboBox(

            form,

            values=[

                "0",

                "1",

                "2",

                "3",

                "4",

                "5"

            ],

            state="readonly"

        )

        self.theory_hours_combo.grid(

            row=4,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.theory_hours_combo.set(

            "3"

        )

        # =====================================================
        # PRACTICAL HOURS
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Practical Hours"

        ).grid(

            row=5,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.practical_hours_combo = ctk.CTkComboBox(

            form,

            values=[

                "0",

                "1",

                "2",

                "3",

                "4",

                "5"

            ],

            state="readonly"

        )

        self.practical_hours_combo.grid(

            row=5,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.practical_hours_combo.set(

            "0"

        )

        # =====================================================
        # TUTORIAL HOURS
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Tutorial Hours"

        ).grid(

            row=5,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.tutorial_hours_combo = ctk.CTkComboBox(

            form,

            values=[

                "0",

                "1",

                "2",

                "3"

            ],

            state="readonly"

        )

        self.tutorial_hours_combo.grid(

            row=5,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.tutorial_hours_combo.set(

            "0"

        )
        # =====================================================
        # DESCRIPTION
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Description"

        ).grid(

            row=6,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.description_entry = ctk.CTkEntry(

            form

        )

        self.description_entry.grid(

            row=6,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

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

            command=self.save_subject

        )

        self.save_button.pack(

            side="left",

            padx=5

        )

        self.update_button = ctk.CTkButton(

            button_frame,

            text="Update",

            width=120,

            command=self.update_subject

        )

        self.update_button.pack(

            side="left",

            padx=5

        )

        self.delete_button = ctk.CTkButton(

            button_frame,

            text="Delete",

            width=120,

            command=self.delete_subject

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
        # TABLE FRAME
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

            "Subject Code",

            "Subject Name",

            "Course",

            "Semester",

            "Credits"

        )

        self.tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            height=8

        )

        self.tree.heading(

            "ID",

            text="ID"

        )

        self.tree.heading(

            "Subject Code",

            text="Subject Code"

        )

        self.tree.heading(

            "Subject Name",

            text="Subject Name"

        )

        self.tree.heading(

            "Course",

            text="Course"

        )

        self.tree.heading(

            "Semester",

            text="Semester"

        )

        self.tree.heading(

            "Credits",

            text="Credits"

        )

        self.tree.column(

            "ID",

            width=60,

            anchor="center"

        )

        self.tree.column(

            "Subject Code",

            width=120,

            anchor="center"

        )

        self.tree.column(

            "Subject Name",

            width=280

        )

        self.tree.column(

            "Course",

            width=220

        )

        self.tree.column(

            "Semester",

            width=100,

            anchor="center"

        )

        self.tree.column(

            "Credits",

            width=100,

            anchor="center"

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
    # LOAD DEPARTMENTS
    # ==========================================================

    def load_departments(self):

        self.department_map.clear()

        departments = DepartmentService.get_departments()

        values = []

        for department in departments:

            values.append(
                department.department_name
            )

            self.department_map[
                department.department_name
            ] = department.department_id

        self.department_combo.configure(
            values=values
        )

        if values:

            self.department_combo.set(
                values[0]
            )

    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):

        self.course_map.clear()

        courses = CourseService.get_courses()

        values = []

        for course in courses:

            values.append(
                course.course_name
            )

            self.course_map[
                course.course_name
            ] = course.course_id

        self.course_combo.configure(
            values=values
        )

        if values:

            self.course_combo.set(
                values[0]
            )

    # ==========================================================
    # LOAD SUBJECTS
    # ==========================================================

    def load_subjects(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        subjects = SubjectService.get_subjects()

        for subject in subjects:

            course = CourseService.get_course(
                subject.course_id
            )

            self.tree.insert(

                "",

                tk.END,

                values=(

                    subject.subject_id,

                    subject.subject_code,

                    subject.subject_name,

                    course.course_name
                    if course else "",

                    subject.semester_id,

                    subject.credits

                )

            )

        #
        # Generate Next Subject Code
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

            SubjectService.generate_subject_code()

        )

        self.code_entry.configure(
            state="readonly"
        )

    # ==========================================================
    # SAVE SUBJECT
    # ==========================================================

    def save_subject(self):

        department_name = self.department_combo.get()

        course_name = self.course_combo.get()

        if department_name not in self.department_map:

            messagebox.showwarning(

                "Subject",

                "Please select Department."

            )

            return

        if course_name not in self.course_map:

            messagebox.showwarning(

                "Subject",

                "Please select Course."

            )

            return

        department_id = self.department_map[
            department_name
        ]

        course_id = self.course_map[
            course_name
        ]

        success, message = SubjectService.add_subject(

            self.name_entry.get(),

            self.short_name_entry.get(),

            department_id,

            course_id,

            self.semester_combo.get(),

            self.subject_type_combo.get(),

            self.credits_combo.get(),

            self.theory_hours_combo.get(),

            self.practical_hours_combo.get(),

            self.tutorial_hours_combo.get(),

            self.description_entry.get()

        )

        

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

            self.load_subjects()

        else:

            messagebox.showwarning(

                "Subject",

                message

            )

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_subject_id = None

        self.name_entry.delete(

            0,

            tk.END

        )

        self.short_name_entry.delete(

            0,

            tk.END

        )

        self.description_entry.delete(

            0,

            tk.END

        )

        if self.department_combo.cget("values"):

            self.department_combo.set(

                self.department_combo.cget("values")[0]

            )

        if self.course_combo.cget("values"):

            self.course_combo.set(

                self.course_combo.cget("values")[0]

            )

        self.semester_combo.set("1")

        self.credits_combo.set("4")
        
        self.subject_type_combo.set("Theory")

        self.theory_hours_combo.set("3")

        self.practical_hours_combo.set("0")

        self.tutorial_hours_combo.set("0")

        self.save_button.configure(
            state="normal"
        )

        self.save_button.configure(

            state="normal"

        )

        self.update_button.configure(

            state="disabled"

        )

        self.delete_button.configure(

            state="disabled"

        )

        self.load_subjects()

        self.name_entry.focus()
            # ==========================================================
    # ROW SELECTED
    # ==========================================================

    def on_row_selected(self, event):

        selection = self.tree.selection()

        if not selection:

            return

        item = self.tree.item(selection[0])

        subject_id = item["values"][0]

        subject = SubjectService.get_subject(subject_id)

        if subject is None:

            return

        self.selected_subject_id = subject.subject_id

        #
        # Subject Code
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

            subject.subject_code

        )

        self.code_entry.configure(

            state="readonly"

        )

        #
        # Subject Name
        #

        self.name_entry.delete(

            0,

            tk.END

        )

        self.name_entry.insert(

            0,

            subject.subject_name

        )

        #
        # Short Name
        #

        self.short_name_entry.delete(

            0,

            tk.END

        )

        self.short_name_entry.insert(

            0,

            subject.subject_short_name

        )

        #
        # Description
        #

        self.description_entry.delete(

            0,

            tk.END

        )

        self.description_entry.insert(

            0,

            subject.description

        )

        #
        # Semester
        #

        self.semester_combo.set(

            str(subject.semester)

        )

        #
        # Credits
        #

        self.credits_combo.set(

            str(subject.credits)

        )

        self.subject_type_combo.set(
            subject.subject_type
        )

        self.theory_hours_combo.set(
            str(subject.theory_hours)
        )

        self.practical_hours_combo.set(
            str(subject.practical_hours)
        )

        self.tutorial_hours_combo.set(
            str(subject.tutorial_hours)
        )


        #
        # Department
        #

        department = DepartmentService.get_department(

            subject.department_id

        )

        if department:

            self.department_combo.set(

                department.department_name

            )

        #
        # Course
        #

        course = CourseService.get_course(

            subject.course_id

        )

        if course:

            self.course_combo.set(

                course.course_name

            )

        #
        # Buttons
        #

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
    # UPDATE SUBJECT
    # ==========================================================

    def update_subject(self):

        if self.selected_subject_id is None:

            return

        department_name = self.department_combo.get()

        course_name = self.course_combo.get()

        department_id = self.department_map[
            department_name
        ]

        course_id = self.course_map[
            course_name
        ]

        success, message = SubjectService.update_subject(

            self.selected_subject_id,

            self.code_entry.get(),

            self.name_entry.get(),

            self.short_name_entry.get(),

            department_id,

            course_id,

            self.semester_combo.get(),

            self.subject_type_combo.get(),

            self.credits_combo.get(),

            self.theory_hours_combo.get(),

            self.practical_hours_combo.get(),

            self.tutorial_hours_combo.get(),

            self.description_entry.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

            self.load_subjects()

        else:

            messagebox.showwarning(

                "Subject",

                message

            )

    # ==========================================================
    # DELETE SUBJECT
    # ==========================================================

    def delete_subject(self):

        if self.selected_subject_id is None:

            return

        answer = messagebox.askyesno(

            "Delete Subject",

            "Are you sure you want to delete this subject?"

        )

        if not answer:

            return

        success, message = SubjectService.delete_subject(

            self.selected_subject_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

            self.load_subjects()

        else:

            messagebox.showwarning(

                "Subject",

                message

            )