"""
FacultyERP
Division Management
-------------------
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from app.services.division_service import DivisionService
from app.services.course_service import CourseService
from app.services.academic_year_service import AcademicYearService
from app.services.semester_service import SemesterService
from app.services.department_service import DepartmentService


class DivisionWindow:

    def __init__(self,parent):

        self.parent=parent
        self.selected_division_id=None
        self.selected_division_code=""
        self.build_ui()
        self.initialize()

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def initialize(self):

        self.update_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.load_departments()
        self.load_courses()
        self.load_academic_years()
        self.load_semesters()
        self.load_divisions()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        self.parent.grid_rowconfigure(3,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)

        title=ctk.CTkLabel(
            self.parent,
            text="Division Management",
            font=("Segoe UI",24,"bold")
        )
        title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(15,10),
            sticky="w"
        )

        form=ctk.CTkFrame(self.parent)
        form.grid(
            row=1,
            column=0,
            padx=20,
            sticky="ew"
        )

        form.grid_columnconfigure(1,weight=1)
        form.grid_columnconfigure(3,weight=1)

        ctk.CTkLabel(form,text="Division Name").grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.name_entry=ctk.CTkEntry(form)

        self.name_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(form,text="Department").grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.department_combo=ctk.CTkComboBox(
            form,
            values=[],
            state="readonly"
        )

        self.department_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )
        self.department_combo.configure(
            command=self.on_department_changed
        )

        ctk.CTkLabel(form,text="Course").grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.course_combo=ctk.CTkComboBox(
            form,
            values=[],
            state="readonly"
        )

        self.course_combo.grid(
            row=1,
            column=3,
            padx=10,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(form,text="Academic Year").grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.academic_year_combo=ctk.CTkComboBox(
            form,
            values=[],
            state="readonly"
        )

        self.academic_year_combo.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )
        ctk.CTkLabel(form,text="Semester").grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )
        self.semester_combo=ctk.CTkComboBox(
            form,
            values=[],
            state="readonly"
        )
        self.semester_combo.grid(
            row=2,
            column=3,
            padx=10,
            pady=10,
            sticky="ew"
        )

        ctk.CTkLabel(form,text="Intake").grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )
        self.intake_entry=ctk.CTkEntry(form)
        self.intake_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.active_var=tk.IntVar(value=1)

        self.active_checkbox=ctk.CTkCheckBox(
            form,
            text="Active Division",
            variable=self.active_var,
            onvalue=1,
            offvalue=0
        )
        self.active_checkbox.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        button_frame=ctk.CTkFrame(self.parent)
        button_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        self.save_button=ctk.CTkButton(
            button_frame,
            text="Save",
            width=120,
            command=self.save_division
        )
        self.save_button.pack(side="left",padx=5)

        self.update_button=ctk.CTkButton(
            button_frame,
            text="Update",
            width=120,
            command=self.update_division
        )
        self.update_button.pack(side="left",padx=5)

        self.delete_button=ctk.CTkButton(
            button_frame,
            text="Delete",
            width=120,
            command=self.delete_division
        )
        self.delete_button.pack(side="left",padx=5)

        self.clear_button=ctk.CTkButton(
            button_frame,
            text="Clear",
            width=120,
            command=self.clear_form
        )
        self.clear_button.pack(side="left",padx=5)

        table_frame=ctk.CTkFrame(self.parent)
        table_frame.grid(
            row=3,
            column=0,
            padx=20,
            pady=(0,20),
            sticky="nsew"
        )

        columns=(
            "ID",
            "Division",
            "Course",
            "Academic Year",
            "Semester",
            "Intake",
            "Status"
        )

        self.tree=ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        for column in columns:
            self.tree.heading(column,text=column)

        self.tree.column("ID",width=60,anchor="center")
        self.tree.column("Division",width=180)
        self.tree.column("Course",width=180)
        self.tree.column("Academic Year",width=130,anchor="center")
        self.tree.column("Semester",width=120,anchor="center")
        self.tree.column("Intake",width=80,anchor="center")
        self.tree.column("Status",width=80,anchor="center")

        scrollbar=ttk.Scrollbar(
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
        departments=DepartmentService.get_departments()
        values=[]
        self.department_map={}
        for department in departments:
            values.append(department.department_name)
            self.department_map[department.department_name]=department.department_id
        self.department_combo.configure(values=values)
        if values:
            self.department_combo.set(values[0])

    # ==========================================================
    # DEPARTMENT CHANGED
    # ==========================================================

    def on_department_changed(self,value):
        self.load_courses()
            
    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):

        department_name=self.department_combo.get()
        department_id=self.department_map.get(department_name)
        if department_id is None:
            return
        courses=CourseService.get_courses_by_department(department_id)
        values=[]
        self.course_map={}
        for course in courses:
            values.append(course.course_name)
            self.course_map[course.course_name]=course.course_id
        self.course_combo.configure(values=values)
        if values:
            self.course_combo.set(values[0])

    # ==========================================================
    # LOAD ACADEMIC YEARS
    # ==========================================================

    def load_academic_years(self):

        academic_years=AcademicYearService.get_academic_years()
        values=[]
        self.academic_year_map={}
        for academic_year in academic_years:
            values.append(academic_year.academic_year)
            self.academic_year_map[academic_year.academic_year]=academic_year.academic_year_id
        self.academic_year_combo.configure(values=values)
        if values:
            self.academic_year_combo.set(values[0])

    # ==========================================================
    # LOAD SEMESTERS
    # ==========================================================

    def load_semesters(self):

        semesters=SemesterService.get_semesters()
        values=[]
        self.semester_map={}
        for semester in semesters:
            values.append(semester.semester_name)
            self.semester_map[semester.semester_name]=semester.semester_id
        self.semester_combo.configure(values=values)
        if values:
            self.semester_combo.set(values[0])

    # ==========================================================
    # LOAD DIVISIONS
    # ==========================================================

    def load_divisions(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        divisions=DivisionService.get_all_divisions()

        for division in divisions:

            status="Active"

            if division.is_active==0:
                status="Inactive"

            course_name=getattr(
                division,
                "course_name",
                ""
            )

            academic_year_name=getattr(
                division,
                "academic_year_name",
                ""
            )

            semester_name=getattr(
                division,
                "semester_name",
                ""
            )

            self.tree.insert(
                "",
                "end",
                values=(
                    division.division_id,
                    division.division_name,
                    course_name,
                    academic_year_name,
                    semester_name,
                    division.intake,
                    status
                )
            )
    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):
        self.selected_division_id=None
        self.selected_division_code=""
        self.name_entry.delete(0,"end")
        self.intake_entry.delete(0,"end")
        self.intake_entry.insert(0,"60")
        if self.course_combo.cget("values"):
            self.course_combo.set(self.course_combo.cget("values")[0])
        if self.academic_year_combo.cget("values"):
            self.academic_year_combo.set(self.academic_year_combo.cget("values")[0])
        if self.semester_combo.cget("values"):
            self.semester_combo.set(self.semester_combo.cget("values")[0])
        self.active_var.set(1)
        self.save_button.configure(state="normal")
        self.update_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.tree.selection_remove(self.tree.selection())

    # ==========================================================
    # SAVE DIVISION
    # ==========================================================

    def save_division(self):

        name=self.name_entry.get().strip()
        intake=self.intake_entry.get().strip()
        if name=="" or intake=="":
            messagebox.showwarning("Validation","Please fill all required fields.")
            return
        try:
            intake=int(intake)
            DivisionService.add_division(
                name,
                self.department_map[self.department_combo.get()],
                self.course_map[self.course_combo.get()],
                self.academic_year_map[self.academic_year_combo.get()],
                self.semester_map[self.semester_combo.get()],
                intake,
                self.active_var.get()
            )
            messagebox.showinfo(
                "Success",
                "Division added successfully."
            )
            self.clear_form()
            self.load_divisions()
        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )

    # ==========================================================
    # ROW SELECTED
    # ==========================================================

    def on_row_selected(self,event):

        selected=self.tree.selection()

        if not selected:
            return

        values=self.tree.item(selected[0],"values")

        self.selected_division_id=int(values[0])

        division=DivisionService.get_division_by_id(
            self.selected_division_id
        )

        if division is None:
            return
        self.selected_division_code=division.division_code
        for name,id in self.department_map.items():
            if id==division.department_id:
                self.department_combo.set(name)
                self.load_courses()
                break

        self.name_entry.delete(0,"end")
        self.name_entry.insert(0,division.division_name)
        self.intake_entry.delete(0,"end")
        self.intake_entry.insert(0,str(division.intake))

        for name,id in self.course_map.items():
            if id==division.course_id:
                self.course_combo.set(name)
                break

        for name,id in self.academic_year_map.items():
            if id==division.academic_year_id:
                self.academic_year_combo.set(name)
                break

        for name,id in self.semester_map.items():
            if id==division.semester_id:
                self.semester_combo.set(name)
                break

        self.active_var.set(division.is_active)

        self.save_button.configure(state="disabled")
        self.update_button.configure(state="normal")
        self.delete_button.configure(state="normal")



    # ==========================================================
    # UPDATE DIVISION
    # ==========================================================


    def update_division(self):

        if self.selected_division_id is None:
            return
        name=self.name_entry.get().strip()
        intake=self.intake_entry.get().strip()
        if name=="" or intake=="":
            messagebox.showwarning("Validation","Please fill all required fields.")
            return
        try:
            intake=int(intake)
            DivisionService.update_division(
                self.selected_division_id,
                self.selected_division_code,
                name,
                self.department_map[self.department_combo.get()],
                self.course_map[self.course_combo.get()],
                self.academic_year_map[self.academic_year_combo.get()],
                self.semester_map[self.semester_combo.get()],
                intake,
                self.active_var.get()
            )
            messagebox.showinfo(
                "Success",
                "Division updated successfully."
            )
            self.clear_form()
            self.load_divisions()
        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )

    # ==========================================================
    # DELETE DIVISION
    # ==========================================================

    def delete_division(self):

        if self.selected_division_id is None:
            return

        answer=messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this division?"
        )

        if not answer:
            return

        try:

            DivisionService.delete_division(
                self.selected_division_id
            )

            messagebox.showinfo(
                "Success",
                "Division deleted successfully."
            )

            self.clear_form()
            self.load_divisions()

        except Exception as ex:

            messagebox.showerror(
                "Error",
                str(ex)
            )
