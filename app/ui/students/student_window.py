"""
FacultyERP
Student Master Window
---------------------

Manage Students
Import Excel
Attendance Database
GFM Database
Academic Modules
"""

import customtkinter as ctk

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import openpyxl

from openpyxl.styles import Font

from app.services.student_service import StudentService


class StudentWindow:
    """Student Master Window."""

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def __init__(

            self,

            parent

    ):

        self.parent = parent

        #
        # Fonts
        #

        self.title_font = (

            "Segoe UI",

            24,

            "bold"

        )

        self.heading_font = (

            "Segoe UI",

            16,

            "bold"

        )

        self.normal_font = (

            "Segoe UI",

            12

        )

        #
        # Data
        #

        self.import_students = []

        #
        # Widgets
        #

        self.container = None

        self.header = None

        self.info_frame = None

        self.toolbar = None

        self.grid_frame = None

        self.student_grid = None

        #
        # Combo Boxes
        #

        self.cmb_department = None

        self.cmb_course = None

        self.cmb_semester = None

        self.cmb_division = None

        self.cmb_academic_year = None

        self.cmb_admission_year = None

        #
        # Search
        #

        self.search_entry = None

        #
        # Build UI
        #

        self.build_ui()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        #
        # Clear Parent
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

        self.header = ctk.CTkFrame(

            self.container

        )

        self.header.pack(

            fill="x",

            padx=10,

            pady=(10,15)

        )

        ctk.CTkLabel(

            self.header,

            text="🎓 Student Master",

            font=self.title_font

        ).pack(

            anchor="w",

            padx=20,

            pady=(15,5)

        )

        ctk.CTkLabel(

            self.header,

            text="Import and manage students for Attendance, GFM and Academic Modules",

            font=self.normal_font

        ).pack(

            anchor="w",

            padx=20,

            pady=(0,15)

        )
                #
        # ==========================================================
        # ACADEMIC INFORMATION
        # ==========================================================
        #

        self.info_frame = ctk.CTkFrame(

            self.container

        )

        self.info_frame.pack(

            fill="x",

            padx=10,

            pady=(0,15)

        )

        self.info_frame.grid_columnconfigure(

            1,

            weight=1

        )

        self.info_frame.grid_columnconfigure(

            3,

            weight=1

        )

        self.info_frame.grid_columnconfigure(

            5,

            weight=1

        )

        #
        # -------------------------
        # ROW 1
        # -------------------------
        #

        ctk.CTkLabel(

            self.info_frame,

            text="Department"

        ).grid(

            row=0,

            column=0,

            padx=(20,10),

            pady=15,

            sticky="w"

        )

        self.cmb_department = ctk.CTkComboBox(

            self.info_frame,

            values=[

                "Civil Engineering",

                "Computer Engineering",

                "Electrical Engineering",

                "ENTC",

                "Mechanical Engineering",

                "Basic Sciences"

            ],

            width=240

        )

        self.cmb_department.grid(

            row=0,

            column=1,

            padx=10,

            pady=15,

            sticky="ew"

        )

        ctk.CTkLabel(

            self.info_frame,

            text="Course"

        ).grid(

            row=0,

            column=2,

            padx=(20,10),

            pady=15,

            sticky="w"

        )

        self.cmb_course = ctk.CTkComboBox(

            self.info_frame,

            values=[

                "BE",

                "ME",

                "Diploma"

            ],

            width=180

        )

        self.cmb_course.grid(

            row=0,

            column=3,

            padx=10,

            pady=15,

            sticky="ew"

        )

        ctk.CTkLabel(

            self.info_frame,

            text="Semester"

        ).grid(

            row=0,

            column=4,

            padx=(20,10),

            pady=15,

            sticky="w"

        )

        self.cmb_semester = ctk.CTkComboBox(

            self.info_frame,

            values=[

                "I",

                "II",

                "III",

                "IV",

                "V",

                "VI",

                "VII",

                "VIII"

            ],

            width=150

        )

        self.cmb_semester.grid(

            row=0,

            column=5,

            padx=10,

            pady=15,

            sticky="ew"

        )

        #
        # -------------------------
        # ROW 2
        # -------------------------
        #

        ctk.CTkLabel(

            self.info_frame,

            text="Division"

        ).grid(

            row=1,

            column=0,

            padx=(20,10),

            pady=(0,20),

            sticky="w"

        )

        self.cmb_division = ctk.CTkComboBox(

            self.info_frame,

            values=[

                "A",

                "B",

                "C",

                "D",

                "E",

                "F",

                "G",

                "H"

            ],

            width=150

        )

        self.cmb_division.grid(

            row=1,

            column=1,

            padx=10,

            pady=(0,20),

            sticky="ew"

        )

        ctk.CTkLabel(

            self.info_frame,

            text="Academic Year"

        ).grid(

            row=1,

            column=2,

            padx=(20,10),

            pady=(0,20),

            sticky="w"

        )

        self.cmb_academic_year = ctk.CTkComboBox(

            self.info_frame,

            values=[

                "2026-27",

                "2025-26",

                "2024-25"

            ],

            width=180

        )

        self.cmb_academic_year.grid(

            row=1,

            column=3,

            padx=10,

            pady=(0,20),

            sticky="ew"

        )

        ctk.CTkLabel(

            self.info_frame,

            text="Admission Year"

        ).grid(

            row=1,

            column=4,

            padx=(20,10),

            pady=(0,20),

            sticky="w"

        )

        self.cmb_admission_year = ctk.CTkComboBox(

            self.info_frame,

            values=[

                "2026",

                "2025",

                "2024",

                "2023"

            ],

            width=150

        )

        self.cmb_admission_year.grid(

            row=1,

            column=5,

            padx=10,

            pady=(0,20),

            sticky="ew"

        )
                #
        # ==========================================================
        # TOOLBAR
        # ==========================================================
        #

        self.toolbar = ctk.CTkFrame(

            self.container

        )

        self.toolbar.pack(

            fill="x",

            padx=10,

            pady=(0,15)

        )

        #
        # Left Toolbar
        #

        left_toolbar = ctk.CTkFrame(

            self.toolbar,

            fg_color="transparent"

        )

        left_toolbar.pack(

            side="left",

            padx=10,

            pady=10

        )

        self.btn_download = ctk.CTkButton(

            left_toolbar,

            text="Download Template",

            width=170,

            command=self.download_template

        )

        self.btn_download.pack(

            side="left",

            padx=5

        )

        self.btn_import = ctk.CTkButton(

            left_toolbar,

            text="Import Excel",

            width=150,

            command=self.import_excel

        )

        self.btn_import.pack(

            side="left",

            padx=5

        )

        self.btn_add = ctk.CTkButton(

            left_toolbar,

            text="Add Student",

            width=140,

            command=self.add_student

        )

        self.btn_add.pack(

            side="left",

            padx=5

        )

        self.btn_edit = ctk.CTkButton(

            left_toolbar,

            text="Edit Student",

            width=140,

            command=self.edit_student

        )

        self.btn_edit.pack(

            side="left",

            padx=5

        )

        self.btn_delete = ctk.CTkButton(

            left_toolbar,

            text="Delete Student",

            width=140,

            command=self.delete_student

        )

        self.btn_delete.pack(

            side="left",

            padx=5

        )

        #
        # Search
        #

        right_toolbar = ctk.CTkFrame(

            self.toolbar,

            fg_color="transparent"

        )

        right_toolbar.pack(

            side="right",

            padx=10,

            pady=10

        )

        ctk.CTkLabel(

            right_toolbar,

            text="Search"

        ).pack(

            side="left",

            padx=(0,10)

        )

        self.search_entry = ctk.CTkEntry(

            right_toolbar,

            width=300,

            placeholder_text="Roll No / Student Name / PRN"

        )

        self.search_entry.pack(

            side="left"

        )

        self.search_entry.bind(

            "<KeyRelease>",

            self.search_students

        )
                #
        # ==========================================================
        # STUDENT GRID
        # ==========================================================
        #

        self.grid_frame = ctk.CTkFrame(

            self.container

        )

        self.grid_frame.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=(0,10)

        )

        columns = (

            "Roll No",

            "College ID",

            "Student Name",

            "PRN",

            "Mobile",

            "Status"

        )

        self.student_grid = ttk.Treeview(

            self.grid_frame,

            columns=columns,

            show="headings",

            height=18

        )

        self.student_grid.heading(

            "Roll No",

            text="Roll No"

        )

        self.student_grid.heading(

            "College ID",

            text="College ID"

        )

        self.student_grid.heading(

            "Student Name",

            text="Student Name"

        )

        self.student_grid.heading(

            "PRN",

            text="PRN"

        )

        self.student_grid.heading(

            "Mobile",

            text="Mobile"

        )

        self.student_grid.heading(

            "Status",

            text="Status"

        )

        self.student_grid.column(

            "Roll No",

            width=70,

            anchor="center"

        )

        self.student_grid.column(

            "College ID",

            width=140,

            anchor="center"

        )

        self.student_grid.column(

            "Student Name",

            width=320,

            anchor="w"

        )

        self.student_grid.column(

            "PRN",

            width=180,

            anchor="center"

        )

        self.student_grid.column(

            "Mobile",

            width=140,

            anchor="center"

        )

        self.student_grid.column(

            "Status",

            width=90,

            anchor="center"

        )

        scrollbar = ttk.Scrollbar(

            self.grid_frame,

            orient="vertical",

            command=self.student_grid.yview

        )

        self.student_grid.configure(

            yscrollcommand=scrollbar.set

        )

        self.student_grid.pack(

            side="left",

            fill="both",

            expand=True

        )

        scrollbar.pack(

            side="right",

            fill="y"

        )

        self.student_grid.bind(

            "<Double-1>",

            self.edit_student

        )

        #
        # Load Existing Students
        #

        self.load_students()
            # ==========================================================
    # DOWNLOAD TEMPLATE
    # ==========================================================

    def download_template(self):

        workbook = openpyxl.Workbook()

        sheet = workbook.active

        sheet.title = "Students"

        headers = [

            "Roll No.",

            "Name of the Student",

            "PRN",

            "Mobile",

            "Email"

        ]

        header_font = Font(

            bold=True

        )

        for column, header in enumerate(

                headers,

                start=1

        ):

            cell = sheet.cell(

                row=1,

                column=column

            )

            cell.value = header

            cell.font = header_font

        #
        # Sample Roll Numbers
        #

        for row in range(

                2,

                102

        ):

            sheet.cell(

                row=row,

                column=1

            ).value = row - 1

        #
        # Column Widths
        #

        sheet.column_dimensions["A"].width = 12

        sheet.column_dimensions["B"].width = 35

        sheet.column_dimensions["C"].width = 20

        sheet.column_dimensions["D"].width = 18

        sheet.column_dimensions["E"].width = 32

        filename = filedialog.asksaveasfilename(

            title="Save Student Import Template",

            initialfile="Student_Import_Template.xlsx",

            defaultextension=".xlsx",

            filetypes=[

                (

                    "Excel Workbook",

                    "*.xlsx"

                )

            ]

        )

        if not filename:

            return

        workbook.save(

            filename

        )

        messagebox.showinfo(

            "FacultyERP",

            "Student Import Template saved successfully."

        )

    # ==========================================================
    # IMPORT EXCEL
    # ==========================================================

    def import_excel(self):

        filename = filedialog.askopenfilename(

            title="Select Student Excel File",

            filetypes=[

                (

                    "Excel Workbook",

                    "*.xlsx"

                ),

                (

                    "Excel Workbook",

                    "*.xls"

                )

            ]

        )

        if not filename:

            return

        try:

            workbook = openpyxl.load_workbook(

                filename,

                data_only=True

            )

            sheet = workbook.active

            self.import_students.clear()

            #
            # Header Detection
            #

            first_cell = sheet["A1"].value

            if first_cell is None:

                messagebox.showerror(

                    "FacultyERP",

                    "Selected Excel file is empty."

                )

                return

            if str(first_cell).strip().lower().startswith(

                    "roll"

            ):

                start_row = 2

            else:

                start_row = 1

            #
            # Read Students
            #

            for row in sheet.iter_rows(

                    min_row=start_row,

                    values_only=True

            ):

                if row[0] is None:

                    continue

                if row[1] is None:

                    continue

                self.import_students.append(

                    {

                        "roll_no": str(row[0]).strip(),

                        "student_name": str(row[1]).strip(),

                        "prn": "" if len(row) < 3 or row[2] is None else str(row[2]).strip(),

                        "mobile": "" if len(row) < 4 or row[3] is None else str(row[3]).strip(),

                        "email": "" if len(row) < 5 or row[4] is None else str(row[4]).strip()

                    }

                )

            if len(

                    self.import_students

            ) == 0:

                messagebox.showwarning(

                    "FacultyERP",

                    "No student records found."

                )

                return

            self.save_imported_students()

        except Exception as ex:

            messagebox.showerror(

                "FacultyERP",

                str(ex)

            )
                # ==========================================================
    # SAVE IMPORTED STUDENTS
    # ==========================================================

    def save_imported_students(self):

        department = self.cmb_department.get()

        course = self.cmb_course.get()

        semester = self.cmb_semester.get()

        division = self.cmb_division.get()

        academic_year = self.cmb_academic_year.get()

        admission_year = self.cmb_admission_year.get()

        #
        # Validation
        #

        if department == "":

            messagebox.showwarning(

                "FacultyERP",

                "Please select Department."

            )

            return

        if course == "":

            messagebox.showwarning(

                "FacultyERP",

                "Please select Course."

            )

            return

        if semester == "":

            messagebox.showwarning(

                "FacultyERP",

                "Please select Semester."

            )

            return

        if division == "":

            messagebox.showwarning(

                "FacultyERP",

                "Please select Division."

            )

            return

        success = 0

        failed = 0

        errors = []

        for student in self.import_students:

            try:

                status, message = StudentService.add_student(

                    admission_year=admission_year,

                    academic_year=academic_year,

                    department_name=department,

                    course_name=course,

                    semester=semester,

                    division=division,

                    roll_no=student["roll_no"],

                    student_name=student["student_name"],

                    prn=student["prn"],

                    mobile=student["mobile"],

                    email=student["email"]

                )

                if status:

                    success += 1

                else:

                    failed += 1

                    errors.append(

                        message

                    )

            except Exception as ex:

                failed += 1

                errors.append(

                    str(ex)

                )

        #
        # Refresh Grid
        #

        self.load_students()

        self.import_students.clear()

        #
        # Result
        #

        if failed == 0:

            messagebox.showinfo(

                "FacultyERP",

                f"{success} students imported successfully."

            )

        else:

            messagebox.showwarning(

                "FacultyERP",

                f"Imported : {success}\n"

                f"Failed : {failed}\n\n"

                f"First Error:\n"

                f"{errors[0]}"

            )
                # ==========================================================
    # LOAD STUDENTS
    # ==========================================================

    def load_students(self):

        self.refresh_grid()

    # ==========================================================
    # REFRESH GRID
    # ==========================================================

    def refresh_grid(self):

        #
        # Treeview Safety
        #

        if self.student_grid is None:

            return

        #
        # Clear Existing Rows
        #

        for item in self.student_grid.get_children():

            self.student_grid.delete(item)

        #
        # Read Database
        #

        students = StudentService.get_students()

        #
        # Populate Grid
        #

        for student in students:

            status = "Active"

            if hasattr(

                    student,

                    "is_active"

            ):

                if student.is_active == 0:

                    status = "Inactive"

            self.student_grid.insert(

                "",

                "end",

                iid=str(

                    student.student_id

                ),

                values=(

                    student.roll_no,

                    student.college_id,

                    student.student_name,

                    student.prn,

                    student.mobile,

                    status

                )

            )

    # ==========================================================
    # SEARCH STUDENTS
    # ==========================================================

    def search_students(

            self,

            event=None

    ):

        keyword = self.search_entry.get().strip().lower()

        #
        # Reload All
        #

        if keyword == "":

            self.refresh_grid()

            return

        #
        # Clear Grid
        #

        for item in self.student_grid.get_children():

            self.student_grid.delete(item)

        students = StudentService.get_students()

        for student in students:

            if (

                keyword in str(

                    student.roll_no

                ).lower()

                or

                keyword in student.student_name.lower()

                or

                keyword in str(

                    student.prn

                ).lower()

            ):

                status = "Active"

                if student.is_active == 0:

                    status = "Inactive"

                self.student_grid.insert(

                    "",

                    "end",

                    iid=str(

                        student.student_id

                    ),

                    values=(

                        student.roll_no,

                        student.college_id,

                        student.student_name,

                        student.prn,

                        student.mobile,

                        status

                    )

                )
                    # ==========================================================
    # ADD STUDENT
    # ==========================================================

    def add_student(self):

        messagebox.showinfo(

            "FacultyERP",

            "Manual Student Entry will be implemented after Excel Import is fully verified."

        )

    # ==========================================================
    # EDIT STUDENT
    # ==========================================================

    def edit_student(

            self,

            event=None

    ):

        selected = self.student_grid.selection()

        if not selected:

            messagebox.showwarning(

                "FacultyERP",

                "Please select a student."

            )

            return

        messagebox.showinfo(

            "FacultyERP",

            "Edit Student will be implemented next."

        )

    # ==========================================================
    # DELETE STUDENT
    # ==========================================================

    def delete_student(self):

        selected = self.student_grid.selection()

        if not selected:

            messagebox.showwarning(

                "FacultyERP",

                "Please select a student."

            )

            return

        messagebox.showinfo(

            "FacultyERP",

            "Delete Student will be implemented next."

        )

    # ==========================================================
    # END OF STUDENT WINDOW
    # ==========================================================