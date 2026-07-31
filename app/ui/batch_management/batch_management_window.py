import customtkinter as ctk
from tkinter import ttk
from app.utils.window_utils import WindowUtils
from app.services.academic_year_service import AcademicYearService
from app.services.department_service import DepartmentService
from app.services.course_service import CourseService
from app.services.semester_service import SemesterService
from app.services.division_service import DivisionService
from app.services.student_service import StudentService
from app.services.student_batch_allocation_service import StudentBatchAllocationService


class BatchManagementWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Batch Management")

        WindowUtils.center_and_fit(
            self,
            preferred_width=1500,
            preferred_height=850,
            min_width=1200,
            min_height=800
        )
        self.transient(parent)
        self.grab_set()
        self.batch_mode_var = ctk.StringVar(value="equal")
        self.academic_year_service = AcademicYearService()
        self.department_service = DepartmentService()
        self.course_service = CourseService()
        self.semester_service = SemesterService()
        self.division_service = DivisionService()
        self.student_service = StudentService()
        self.batch_service = StudentBatchAllocationService()
        self.students = []
        self.generated_batches = []
        self.create_widgets()
        self.load_master_data()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="Batch Management",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=(15, 5))
        self.division_label = ctk.CTkLabel(
            self,
            text="Current Division : Not Selected",
            font=("Arial", 14, "bold")
        )
        self.division_label.pack(pady=(0, 10))
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.create_filter_frame()
        self.create_summary_frame()
        self.create_work_area()
        self.create_bottom_buttons()


    def create_filter_frame(self):
        self.filter_frame = ctk.CTkFrame(self.main_frame)
        self.filter_frame.pack(fill="x", padx=10, pady=(10, 5))

        self.filter_frame.grid_columnconfigure(1, weight=1)
        self.filter_frame.grid_columnconfigure(3, weight=2)
        self.filter_frame.grid_columnconfigure(5, weight=1)
        self.filter_frame.grid_columnconfigure(6, minsize=25)
        self.filter_frame.grid_columnconfigure(7, weight=0)

        ctk.CTkLabel(
            self.filter_frame,
            text="Academic Year"
        ).grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")

        self.academic_year_combo = ctk.CTkComboBox(
            self.filter_frame,
            values=[],
            width=170
        )
        self.academic_year_combo.grid(
            row=0,
            column=1,
            padx=(0, 20),
            pady=10,
            sticky="ew"
        )
        self.academic_year_combo.configure(
            command=self.on_academic_year_changed
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Department"
        ).grid(row=0, column=2, padx=(0, 5), pady=10, sticky="w")

        self.department_combo = ctk.CTkComboBox(
            self.filter_frame,
            values=[],
            width=260
        )
        self.department_combo.grid(
            row=0,
            column=3,
            padx=(0, 20),
            pady=10,
            sticky="ew"
        )
        self.department_combo.configure(
            command=self.on_department_changed
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Course"
        ).grid(row=0, column=4, padx=(0, 5), pady=10, sticky="w")

        self.course_combo = ctk.CTkComboBox(
            self.filter_frame,
            values=[],
            width=170
        )
        self.course_combo.grid(
            row=0,
            column=5,
            padx=(0, 15),
            pady=10,
            sticky="ew"
        )
        self.course_combo.configure(
            command=self.on_course_changed
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Semester"
        ).grid(row=1, column=0, padx=(10, 5), pady=(0, 10), sticky="w")

        self.semester_combo = ctk.CTkComboBox(
            self.filter_frame,
            values=[],
            width=170
        )
        self.semester_combo.grid(
            row=1,
            column=1,
            padx=(0, 20),
            pady=(0, 10),
            sticky="ew"
        )
        self.semester_combo.configure(
            command=self.on_semester_changed
        )

        ctk.CTkLabel(
            self.filter_frame,
            text="Division"
        ).grid(row=1, column=2, padx=(0, 5), pady=(0, 10), sticky="w")

        self.division_combo = ctk.CTkComboBox(
            self.filter_frame,
            values=[],
            width=170
        )
        self.division_combo.grid(
            row=1,
            column=3,
            padx=(0, 20),
            pady=(0, 10),
            sticky="w"
        )

        self.load_students_button = ctk.CTkButton(
            self.filter_frame,
            text="LOAD\nSTUDENTS",
            width=150,
            height=70,
            command=self.load_students
        )
        self.load_students_button.grid(
            row=0,
            column=7,
            rowspan=2,
            padx=(20, 15),
            pady=10,
            sticky="ns"
        )

    def create_summary_frame(self):
        self.summary_frame = ctk.CTkFrame(self.main_frame)
        self.summary_frame.pack(fill="x", padx=10, pady=(0, 5))

        self.current_division_label = ctk.CTkLabel(
            self.summary_frame,
            text="Division : -",
            font=("Arial", 13, "bold")
        )
        self.current_division_label.pack(side="left", padx=(15, 20), pady=8)

        self.total_students_label = ctk.CTkLabel(
            self.summary_frame,
            text="Students : 0",
            font=("Arial", 13, "bold")
        )
        self.total_students_label.pack(side="left", padx=20)

        self.total_batches_label = ctk.CTkLabel(
            self.summary_frame,
            text="Batches : 0",
            font=("Arial", 13, "bold")
        )
        self.total_batches_label.pack(side="left", padx=20)

        self.unallocated_label = ctk.CTkLabel(
            self.summary_frame,
            text="Unallocated : 0",
            font=("Arial", 13, "bold")
        )
        self.unallocated_label.pack(side="left", padx=20)


    def create_work_area(self):
        self.work_frame = ctk.CTkFrame(self.main_frame)
        self.work_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.top_work_frame = ctk.CTkFrame(self.work_frame, fg_color="transparent")
        self.top_work_frame.pack(fill="x", pady=(0, 5))

        self.top_work_frame.grid_columnconfigure(0, weight=1)
        self.top_work_frame.grid_columnconfigure(1, weight=2)

        self.batch_generation_frame = ctk.CTkFrame(self.top_work_frame)
        self.batch_generation_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        self.generated_batches_frame = ctk.CTkFrame(self.top_work_frame)
        self.generated_batches_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

        self.student_frame = ctk.CTkFrame(self.work_frame)
        self.student_frame.pack(fill="both", expand=True, pady=(5, 0))

    def create_batch_frame(self):
        self.batch_frame = ctk.CTkFrame(self.main_frame)
        self.batch_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(
            self.batch_frame,
            text="Batch Generation",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=6, sticky="w", padx=15, pady=(10, 15))

        self.equal_radio = ctk.CTkRadioButton(
            self.batch_frame,
            text="Equal Distribution",
            variable=self.batch_mode_var,
            value="equal"
        )
        self.equal_radio.grid(row=1, column=0, padx=(15, 5), pady=5, sticky="w")

        ctk.CTkLabel(
            self.batch_frame,
            text="Number of Batches"
        ).grid(row=1, column=1, padx=(10, 5), pady=5, sticky="e")

        self.batch_count_entry = ctk.CTkEntry(
            self.batch_frame,
            width=80
        )
        self.batch_count_entry.grid(row=1, column=2, padx=(0, 25), pady=5, sticky="w")

        self.size_radio = ctk.CTkRadioButton(
            self.batch_frame,
            text="Batch Size",
            variable=self.batch_mode_var,
            value="size"
        )
        self.size_radio.grid(row=2, column=0, padx=(15, 5), pady=(5, 10), sticky="w")

        ctk.CTkLabel(
            self.batch_frame,
            text="Students per Batch"
        ).grid(row=2, column=1, padx=(10, 5), pady=(5, 10), sticky="e")

        self.batch_size_entry = ctk.CTkEntry(
            self.batch_frame,
            width=80
        )
        self.batch_size_entry.grid(row=2, column=2, padx=(0, 25), pady=(5, 10), sticky="w")

        self.generate_button = ctk.CTkButton(
            self.batch_frame,
            text="Generate Batches",
            width=180
        )
        self.generate_button.grid(row=1, column=4, rowspan=2, padx=(40, 20), pady=10)

        self.total_students_label = ctk.CTkLabel(
            self.batch_frame,
            text="Total Students : 0",
            font=("Arial", 13, "bold")
        )
        self.total_students_label.grid(row=1, column=5, padx=20, sticky="w")

        self.total_batches_label = ctk.CTkLabel(
            self.batch_frame,
            text="Generated Batches : 0",
            font=("Arial", 13, "bold")
        )
        self.total_batches_label.grid(row=2, column=5, padx=20, sticky="w")
    # ==========================================================
    # LOAD MASTER DATA
    # ==========================================================

    def load_master_data(self):

        academic_years = self.academic_year_service.get_academic_years()
        departments = self.department_service.get_departments()
        courses = self.course_service.get_courses()
        semesters = self.semester_service.get_semesters()
        

        self.academic_year_map = {
            item.academic_year: item
            for item in academic_years
        }

        self.department_map = {
            item.department_name: item
            for item in departments
        }

        self.course_map = {
            item.course_name: item
            for item in courses
        }

        self.semester_map = {
            item.semester_name: item
            for item in semesters
        }

        self.academic_year_combo.configure(
            values=list(self.academic_year_map.keys())
        )

        self.department_combo.configure(
            values=list(self.department_map.keys())
        )

        self.course_combo.configure(
            values=list(self.course_map.keys())
        )

        self.semester_combo.configure(
            values=list(self.semester_map.keys())
        )


        if self.academic_year_map:
            self.academic_year_combo.set(next(iter(self.academic_year_map)))

        if self.department_map:
            self.department_combo.set(next(iter(self.department_map)))

        if self.course_map:
            self.course_combo.set(next(iter(self.course_map)))

        if self.semester_map:
            self.semester_combo.set(next(iter(self.semester_map)))

        self.on_department_changed(
            self.department_combo.get()
        )


    def load_divisions(self):
        selected_course = self.course_map.get(self.course_combo.get())
        selected_year = self.academic_year_map.get(self.academic_year_combo.get())
        selected_semester = self.semester_map.get(self.semester_combo.get())

        if not selected_course or not selected_year or not selected_semester:
            self.division_combo.configure(values=[])
            self.division_combo.set("")
            return

        divisions = self.division_service.get_divisions_by_course_year_semester(
            selected_course.course_id,
            selected_year.academic_year_id,
            selected_semester.semester_id
        )

        self.division_map = {
            division.division_name: division
            for division in divisions
        }

        self.division_combo.configure(
            values=list(self.division_map.keys())
        )

        if self.division_map:
            self.division_combo.set(next(iter(self.division_map)))
        else:
            self.division_combo.set("")

    # ==========================================================
    # LOAD STUDENTS
    # ==========================================================

    def load_students(self):

        selected_division = self.division_map.get(
            self.division_combo.get()
        )

        if selected_division is None:
            self.students = []
            self.total_students_label.configure(
                text="Total Students : 0"
            )
            return

        self.students = self.student_service.get_students_by_division(
            selected_division.division_id
        )

        self.total_students_label.configure(
            text=f"Students : {len(self.students)}"
        )

        self.current_division_label.configure(
            text=f"Division : {selected_division.division_name}"
        )

        self.unallocated_label.configure(
            text=f"Unallocated : {len(self.students)}"
        )

        self.total_batches_label.configure(
            text="Batches : 0"
        )

        self.refresh_student_grid()

    def on_academic_year_changed(self, value):
        self.load_divisions()

    def on_department_changed(self, value):
        department = self.department_map.get(value)
        if department is None:
            return
        courses = self.course_service.get_courses_by_department(
            department.department_id
        )
        self.course_map = {
            course.course_name: course
            for course in courses
        }
        self.course_combo.configure(
            values=list(self.course_map.keys())
        )
        if self.course_map:
            self.course_combo.set(next(iter(self.course_map)))
        else:
            self.course_combo.set("")
        self.load_divisions()

    def on_course_changed(self, value):
        self.load_divisions()

    def on_semester_changed(self, value):
        self.load_divisions()

    def create_batches_grid(self):

        self.batch_grid_frame = ctk.CTkFrame(self.main_frame)
        self.batch_grid_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(
            self.batch_grid_frame,
            text="Generated Batches",
            font=("Arial", 16, "bold")
        ).pack(anchor="w", padx=15, pady=(10, 5))

        columns = (
            "Batch",
            "Students"
        )

        self.batch_tree = ttk.Treeview(
            self.batch_grid_frame,
            columns=columns,
            show="headings",
            height=5
        )

        self.batch_tree.heading(
            "Batch",
            text="Batch"
        )

        self.batch_tree.heading(
            "Students",
            text="Students"
        )

        self.batch_tree.column(
            "Batch",
            width=150,
            anchor="center"
        )

        self.batch_tree.column(
            "Students",
            width=150,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            self.batch_grid_frame,
            orient="vertical",
            command=self.batch_tree.yview
        )

        self.batch_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.batch_tree.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 0),
            pady=(0, 15)
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 15),
            pady=(0, 15)
        )

    def create_student_frame(self):

        self.student_frame = ctk.CTkFrame(self.main_frame)
        self.student_frame.pack(fill="both", expand=True, padx=10, pady=5)

        ctk.CTkLabel(
            self.student_frame,
            text="Students",
            font=("Arial", 16, "bold")
        ).pack(anchor="w", padx=15, pady=(10, 5))

        columns = (
            "Roll No",
            "College ID",
            "Student Name",
            "Batch"
        )

        self.student_tree = ttk.Treeview(
            self.student_frame,
            columns=columns,
            show="headings",
            height=16
        )

        self.student_tree.heading("Roll No", text="Roll No")
        self.student_tree.heading("College ID", text="College ID")
        self.student_tree.heading("Student Name", text="Student Name")
        self.student_tree.heading("Batch", text="Batch")

        self.student_tree.column("Roll No", width=80, anchor="center")
        self.student_tree.column("College ID", width=180)
        self.student_tree.column("Student Name", width=320)
        self.student_tree.column("Batch", width=100, anchor="center")

        scrollbar = ttk.Scrollbar(
            self.student_frame,
            orient="vertical",
            command=self.student_tree.yview
        )

        self.student_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.student_tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(15, 0),
            pady=(0, 15)
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 15),
            pady=(0, 15)
        )

    def create_bottom_buttons(self):

        self.button_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        self.button_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="Save Batches",
            width=150,
            command=self.save_batches
        )
        self.save_button.pack(
            side="left",
            padx=5
        )

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Clear",
            width=120,
            command=self.clear_batches
        )
        self.clear_button.pack(
            side="left",
            padx=5
        )

        self.close_button = ctk.CTkButton(
            self.button_frame,
            text="Close",
            width=120,
            command=self.destroy
        )
        self.close_button.pack(
            side="right",
            padx=5
        )
    def refresh_student_grid(self):

        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        for student in self.students:

            roll_no = getattr(student, "roll_no", "")
            college_id = getattr(student, "college_id", "")
            student_name = getattr(student, "student_name", "")
            batch = getattr(student, "batch_no", "")

            self.student_tree.insert(
                "",
                "end",
                iid=str(student.student_id),
                values=(
                    roll_no,
                    college_id,
                    student_name,
                    batch
                )
            )

    def clear_batches(self):
        pass

    def save_batches(self):
        pass
