"""
FacultyERP
Faculty Management
------------------

Faculty CRUD Module
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from app.services.faculty_service import FacultyService
from app.services.department_service import DepartmentService
from tkinter import filedialog
from app.utils.faculty_template import FacultyTemplate
from app.utils.excel_importer import ExcelImporter

class FacultyWindow:
    """Faculty Management Window."""
    # ==========================================================
    # Constructor
    # ==========================================================
    def __init__(self, parent):
        self.parent = parent
        self.selected_faculty_id = None
        self.department_map = {}
        self.build_ui()
        self.initialize()
    # ==========================================================
    # Initialize
    # ==========================================================

    def initialize(self):
        self.update_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.load_departments()
        self.load_designations()
        self.load_faculty()
    # ==========================================================
    # Build UI
    # ==========================================================

    def build_ui(self):
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.parent.grid_rowconfigure(3, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        # =====================================================
        # TITLE
        # =====================================================

        title = ctk.CTkLabel(self.parent, text="Faculty Management",font=("Segoe UI", 24, "bold"))
        title.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 10))
        # =====================================================
        # FORM
        # =====================================================

        form = ctk.CTkFrame(self.parent)
        form.grid(row=1, column=0, sticky="ew", padx=20)
        form.grid_columnconfigure(1, weight=1)
        form.grid_columnconfigure(3, weight=1)

        # =====================================================
        # FACULTY CODE
        # =====================================================

        ctk.CTkLabel(form, text="Faculty Code").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.code_entry = ctk.CTkEntry(form, state="readonly")
        self.code_entry.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

        # =====================================================
        # EMPLOYEE CODE
        # =====================================================
        ctk.CTkLabel(form, text="Employee Code").grid(row=0, column=2, padx=10, pady=8, sticky="w")
        self.employee_code_entry = ctk.CTkEntry(form)
        self.employee_code_entry.grid(row=0, column=3, padx=10, pady=8, sticky="ew")

        # =====================================================
        # DEPARTMENT
        # =====================================================

        ctk.CTkLabel(form, text="Department").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.department_combo = ctk.CTkComboBox(form, values=[], state="readonly")
        self.department_combo.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

        # =====================================================
        # DESIGNATION
        # =====================================================

        ctk.CTkLabel(form, text="Designation").grid(row=1, column=2, padx=10, pady=8, sticky="w")
        self.designation_combo = ctk.CTkComboBox(form, values=[], state="readonly")
        self.designation_combo.grid(row=1, column=3, padx=10, pady=8, sticky="ew")

        # =====================================================
        # FIRST NAME
        # =====================================================

        ctk.CTkLabel(form, text="First Name").grid(row=2, column=0, padx=10, pady=8, sticky="w" )
        self.first_name_entry = ctk.CTkEntry(form)
        self.first_name_entry.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        # =====================================================
        # MIDDLE NAME
        # =====================================================
        ctk.CTkLabel(form, text="Middle Name").grid(row=2, column=2, padx=10, pady=8, sticky="w")
        self.middle_name_entry = ctk.CTkEntry(form)
        self.middle_name_entry.grid(row=2, column=3, padx=10, pady=8, sticky="ew" )

        # =====================================================
        # LAST NAME
        # =====================================================
        ctk.CTkLabel(form, text="Last Name").grid(row=3, column=0, padx=10, pady=8, sticky="w")
        self.last_name_entry = ctk.CTkEntry(form)
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=8, sticky="ew" )

        # =====================================================
        # GENDER
        # =====================================================
        ctk.CTkLabel(form, text="Gender").grid(row=3, column=2, padx=10, pady=8, sticky="w" )
        self.gender_combo = ctk.CTkComboBox(form, values=["Male", "Female", "Other"], state="readonly")
        self.gender_combo.grid(row=3, column=3, padx=10, pady=8, sticky="ew" )
        self.gender_combo.set("Male")

        # =====================================================
        # DATE OF BIRTH
        # =====================================================

        ctk.CTkLabel(form, text="Date of Birth").grid(row=4, column=0, padx=10, pady=8, sticky="w" )
        self.dob_entry = DateEntry(form, date_pattern="dd-mm-yyyy", width=18)
        self.dob_entry.grid(row=4, column=1, padx=10, pady=8, sticky="ew")

        # =====================================================
        # JOINING DATE
        # =====================================================
        ctk.CTkLabel(form, text="Joining Date" ).grid(row=4, column=2, padx=10, pady=8, sticky="w" )
        self.joining_entry = DateEntry(form, date_pattern="dd-mm-yyyy", width=18 )
        self.joining_entry.grid(row=4, column=3, padx=10, pady=8, sticky="ew")

        # =====================================================
        # MOBILE
        # =====================================================
        ctk.CTkLabel(form, text="Mobile" ).grid(row=5, column=0, padx=10, pady=8, sticky="w")
        self.mobile_entry = ctk.CTkEntry(form)
        self.mobile_entry.grid(row=5, column=1, padx=10, pady=8, sticky="ew")

        # =====================================================
        # EMAIL
        # =====================================================
        ctk.CTkLabel(form, text="Email").grid(row=5, column=2, padx=10, pady=8, sticky="w")
        self.email_entry = ctk.CTkEntry(form)
        self.email_entry.grid(row=5, column=3, padx=10, pady=8, sticky="ew" )

        # =====================================================
        # QUALIFICATION
        # =====================================================
        ctk.CTkLabel(form, text="Qualification" ).grid(row=6, column=0, padx=10, pady=8, sticky="w")
        self.qualification_combo = ctk.CTkComboBox(form,
            values=["BE", "BTech", "ME", "MTech", "MBA", "MCA", "MSc", "PhD", "Post Doctorate", "Other"],
            state="readonly"
        )
        self.qualification_combo.grid(row=6, column=1, padx=10, pady=8, sticky="ew")
        self.qualification_combo.set("BE")

        # =====================================================
        # EXPERIENCE
        # =====================================================
        ctk.CTkLabel(form, text="Experience (Years)").grid(row=6, column=2, padx=10, pady=8, sticky="w")
        self.experience_entry = ctk.CTkEntry(form)
        self.experience_entry.grid(row=6, column=3, padx=10, pady=8, sticky="ew" )

        # =====================================================
        # EMPLOYMENT TYPE
        # =====================================================
        ctk.CTkLabel(form, text="Employment Type").grid(row=7, column=0, padx=10, pady=8, sticky="w")
        self.employment_combo = ctk.CTkComboBox(form, values=["Permanent", "Contract", "Visiting", "Adjunct"],
            state="readonly"
        )
        self.employment_combo.grid(row=7, column=1, padx=10, pady=8, sticky="ew")
        self.employment_combo.set("Permanent")

        # =====================================================
        # SPECIALIZATION
        # =====================================================
        ctk.CTkLabel(form, text="Specialization").grid(row=7, column=2, padx=10, pady=8, sticky="w")
        self.specialization_entry = ctk.CTkEntry(form)
        self.specialization_entry.grid(row=7, column=3, padx=10, pady=8, sticky="ew" )

        # =====================================================
        # BUTTON FRAME
        # =====================================================
        button_frame = ctk.CTkFrame(self.parent)
        button_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10 )
        self.download_template_button = ctk.CTkButton(button_frame, text="Download Template", width=130,
            command=self.download_template
        )
        self.download_template_button.pack(side="left", padx=5)
        self.import_button = ctk.CTkButton(button_frame, text="Import Excel", width=120, command=self.import_excel)
        self.import_button.pack(side="left", padx=5)
        self.export_button = ctk.CTkButton(button_frame, text="Export Excel", width=120, command=self.export_excel)
        self.export_button.pack(side="left", padx=5)
        self.save_button = ctk.CTkButton(button_frame, text="Save", width=110, command=self.save_faculty)
        self.save_button.pack(side="left", padx=5)
        self.update_button = ctk.CTkButton(button_frame, text="Update", width=110, command=self.update_faculty)
        self.update_button.pack(side="left", padx=5)
        self.delete_button = ctk.CTkButton(button_frame, text="Delete", width=110, command=self.delete_faculty)
        self.delete_button.pack(side="left", padx=5)
        self.clear_button = ctk.CTkButton(button_frame, text="Clear", width=110, command=self.clear_form)
        self.clear_button.pack(side="left", padx=5)
        

        # =====================================================
        # FACULTY TABLE
        # =====================================================
        table_frame = ctk.CTkFrame(self.parent)
        table_frame.grid(row=3, column=0, sticky="nsew", padx=20, pady=(0, 20))
        columns = ("ID", "Faculty Code", "Employee Code", "Faculty Name", "Department", "Designation", "Mobile")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12 )
        for column in columns: self.tree.heading(column, text=column )
        self.tree.column("ID", width=60, anchor="center" )
        self.tree.column("Faculty Code", width=120, anchor="center" )
        self.tree.column("Employee Code", width=120, anchor="center" )
        self.tree.column("Faculty Name", width=220 )
        self.tree.column("Department", width=180 )
        self.tree.column("Designation", width=180)
        self.tree.column("Mobile", width=130, anchor="center")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview )
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True )
        scrollbar.pack(side="right", fill="y" )
        self.tree.bind("<<TreeviewSelect>>", self.on_row_selected)

        # ==========================================================
        # LOAD DEPARTMENTS
        # ==========================================================
    def load_departments(self):
        self.department_map.clear()
        departments = DepartmentService.get_departments()
        values = []
        for department in departments:
            values.append(department.department_name)
            self.department_map[
                department.department_name
            ] = department.department_id
        self.department_combo.configure(values=values)
        if values:
            self.department_combo.set(values[0])

        # ==========================================================
        # LOAD DESIGNATIONS
        # ==========================================================
    def load_designations(self):
        values = [
            "Professor",
            "Associate Professor",
            "Assistant Professor",
            "Lecturer",
            "Teaching Assistant",
            "Lab Assistant",
            "Workshop Superintendent",
            "Office Superintendent",
            "Librarian",
            "Physical Director"
        ]
        self.designation_combo.configure(values=values)
        self.designation_combo.set("Assistant Professor")

        # ==========================================================
        # LOAD FACULTY
        # ==========================================================
    def load_faculty(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        faculty_list = FacultyService.get_faculty()
        for faculty in faculty_list:
            department_name = ""
            if faculty.department_id:
                department = DepartmentService.get_department(faculty.department_id)
                if department:
                    department_name = department.department_name
            designation_name = faculty.designation
            full_name = " ".join(filter(None, [faculty.first_name, faculty.middle_name, faculty.last_name]))
            self.tree.insert(
                "",
                tk.END,
                values=(
                    faculty.faculty_id,
                    faculty.faculty_code,
                    faculty.employee_code,
                    full_name,
                    department_name,
                    designation_name,
                    faculty.mobile
                )
            )
        self.code_entry.configure(state="normal")
        self.code_entry.delete(0, tk.END)
        self.code_entry.insert(0, FacultyService.generate_faculty_code())
        self.code_entry.configure(state="readonly")

        # ==========================================================
        # VALIDATE FORM
        # ==========================================================
    def validate_form(self):
        if not self.first_name_entry.get().strip():
            messagebox.showwarning("Faculty", "First Name is required.")
            self.first_name_entry.focus()
            return False
        if not self.department_combo.get():
            messagebox.showwarning("Faculty", "Please select Department.")
            return False
        if not self.designation_combo.get():
            messagebox.showwarning("Faculty", "Please select Designation.")
            return False
        mobile = self.mobile_entry.get().strip()
        if mobile:
            if not mobile.isdigit():
                messagebox.showwarning("Faculty", "Mobile number should contain digits only.")
                return False
            if len(mobile) != 10:
                messagebox.showwarning("Faculty", "Mobile number must be exactly 10 digits.")
                return False
        email = self.email_entry.get().strip()
        if email:
            if "@" not in email or "." not in email:
                messagebox.showwarning("Faculty", "Invalid email address.")
                return False
        return True

        # ==========================================================
        # CLEAR FORM
        # ==========================================================
    def clear_form(self):
        self.selected_faculty_id = None
        self.employee_code_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.specialization_entry.delete(0, tk.END)
        self.experience_entry.delete(0, tk.END)
        self.gender_combo.set("Male")
        self.employment_combo.set("Permanent")
        self.qualification_combo.set("BE")
        if self.department_combo.cget("values"):
            self.department_combo.set(self.department_combo.cget("values")[0])
        if self.designation_combo.cget("values"): self.designation_combo.set("Assistant Professor")
        self.save_button.configure(state="normal")
        self.update_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.load_faculty()
        self.first_name_entry.focus()

            # ==========================================================
            # SAVE FACULTY
            # ==========================================================
    def save_faculty(self):
        if not self.validate_form():
            return
        department = DepartmentService.get_department_by_name(self.department_combo.get())
        if department is None:
            messagebox.showwarning("Faculty", "Please select a Department.")
            return

        success, message = FacultyService.add_faculty(
            self.first_name_entry.get().strip(),
            self.middle_name_entry.get().strip(),
            self.last_name_entry.get().strip(),
            self.gender_combo.get(),
            self.dob_entry.get(),
            self.mobile_entry.get().strip(),
            self.email_entry.get().strip(),
            "",                             # address
            "",                             # pan_card_no
            "",                             # aadhaar_number
            "",                             # blood_group
            "",                             # marital_status
            "",                             # bank_account_number
            "",                             # ifsc_code
            "",                             # uan_number
            "",                             # passport_number
            "",                             # joining_department_date
            "",                             # university_approval_number
            "",                             # university_approval_date
            department.department_id,
            self.designation_combo.get(),
            self.joining_entry.get(),
            self.employment_combo.get(),
            self.qualification_combo.get(),
            self.specialization_entry.get().strip(),
            self.experience_entry.get().strip(),
            "",                             # research_area
            "",                             # orcid_id
            "",                             # google_scholar_id
            "",                             # scopus_author_id
            "",                             # vidwan_id
            "",                             # aicte_id
            1,                              # university_approved
            self.employee_code_entry.get().strip(),
            "",                             # photo
            ""                              # remarks
        )
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
        else:
            messagebox.showwarning("Faculty", message)

        # ==========================================================
        # ROW SELECTED
        # ==========================================================
    def on_row_selected(self, event):
        selection = self.tree.selection()
        if not selection:
            return
        values = self.tree.item(selection[0], "values")
        faculty = FacultyService.get_faculty_by_id(int(values[0]))
        if faculty is None:
            return
        self.selected_faculty_id = faculty.faculty_id
        self.code_entry.configure(state="normal")
        self.code_entry.delete(0, tk.END)
        self.code_entry.insert(0, faculty.faculty_code)
        self.code_entry.configure(state="readonly")
        self.employee_code_entry.delete(0, tk.END )
        self.employee_code_entry.insert(0, faculty.employee_code or "")
        self.first_name_entry.delete(0, tk.END)
        self.first_name_entry.insert(0, faculty.first_name)
        self.middle_name_entry.delete(0, tk.END)
        self.middle_name_entry.insert(0, faculty.middle_name )
        self.last_name_entry.delete(0, tk.END)
        self.last_name_entry.insert(0, faculty.last_name )
        self.gender_combo.set(faculty.gender )
        try:
            self.dob_entry.set_date(faculty.date_of_birth)
        except Exception:
            pass
        try:
            self.joining_entry.set_date(faculty.joining_date)
        except Exception:
            pass
        self.mobile_entry.delete(0, tk.END)
        self.mobile_entry.insert(0, faculty.mobile)
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, faculty.email)
        department = DepartmentService.get_department(faculty.department_id )
        if department:
            self.department_combo.set(department.department_name)
        if faculty.designation:
            self.designation_combo.set(faculty.designation)
        self.employment_combo.set(faculty.employment_type)
        self.qualification_combo.set(faculty.qualification)
        self.specialization_entry.delete(0, tk.END)
        self.specialization_entry.insert(0, faculty.specialization)
        self.experience_entry.delete(0, tk.END)
        self.experience_entry.insert(0, faculty.experience)
        self.save_button.configure(state="disabled" )
        self.update_button.configure(state="normal" )
        self.delete_button.configure(state="normal" )

        # ==========================================================
        # UPDATE FACULTY
        # ==========================================================
    def update_faculty(self):
        if self.selected_faculty_id is None:
            return
        if not self.validate_form():
            return
        department = DepartmentService.get_department_by_name(
            self.department_combo.get()
        )
        
        if department is None:
            messagebox.showwarning("Faculty", "Please select a Department." )
            return

        success, message = FacultyService.update_faculty(
            self.selected_faculty_id,
            self.first_name_entry.get().strip(),
            self.middle_name_entry.get().strip(),
            self.last_name_entry.get().strip(),
            self.gender_combo.get(),
            self.dob_entry.get(),
            self.mobile_entry.get().strip(),
            self.email_entry.get().strip(),
            "",                             # address
            "",                             # pan_card_no
            "",                             # aadhaar_number
            "",                             # blood_group
            "",                             # marital_status
            "",                             # bank_account_number
            "",                             # ifsc_code
            "",                             # uan_number
            "",                             # passport_number
            "",                             # joining_department_date
            "",                             # university_approval_number
            "",                             # university_approval_date
            department.department_id,
            self.designation_combo.get(),
            self.joining_entry.get(),
            self.employment_combo.get(),
            self.qualification_combo.get(),
            self.specialization_entry.get().strip(),
            self.experience_entry.get().strip(),
            "",                             # research_area
            "",                             # orcid_id
            "",                             # google_scholar_id
            "",                             # scopus_author_id
            "",                             # vidwan_id
            "",                             # aicte_id
            1,                              # university_approved
            self.employee_code_entry.get().strip(),
            "",                             # photo
            ""                              # remarks
        )
            
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
        else:
            messagebox.showwarning("Faculty", message)
        # ==========================================================
        # DELETE FACULTY
        # ==========================================================

    def delete_faculty(self):
        if self.selected_faculty_id is None:
            return
        answer = messagebox.askyesno("Delete Faculty", "Are you sure you want to delete this faculty record?")
        if not answer:
            return
        success, message = FacultyService.delete_faculty(self.selected_faculty_id)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
        else:
            messagebox.showwarning("Faculty", message)
   # ==========================================================
   # SUBJECT ALLOCATION
   # ==========================================================
   # ==========================================================
   # DOWNLOAD TEMPLATE
   # ==========================================================
    def download_template(self):
        filename = filedialog.asksaveasfilename(
            title="Save Faculty Template",
            defaultextension=".xlsx",
            filetypes=[("Excel Workbook", "*.xlsx")], initialfile="Faculty_Template.xlsx")
        if not filename:
            return
        try:
            FacultyTemplate.create(filename)
            messagebox.showinfo("FacultyERP", "Faculty template downloaded successfully.")
        except Exception as error:
            messagebox.showerror("FacultyERP", str(error))
    def import_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if not filepath:
            return
        headers = [
            "Employee Code",
            "First Name",
            "Middle Name",
            "Last Name",
            "Department",
            "Designation",
            "Mobile",
            "Email",
            "PAN Card No",
            "Gender",
            "Qualification",
            "Experience",
            "Joining Date",
            "Employment Type",
            "Specialization"
        ]
        mandatory_columns = [
            "Employee Code",
            "First Name",
            "Last Name",
            "Department",
            "Designation",
            "PAN Card No"
        ]
        result = ExcelImporter.import_excel(
            filepath=filepath,
            headers=headers,
            mandatory_columns=mandatory_columns
        )
        if not result.success:
            error_text = ""
            for error in result.errors[:10]:
                error_text += f"Row {error['row']}: {error['message']}\n"
            if len(result.errors) > 10:
                error_text += f"\n...and {len(result.errors) - 10} more errors."
            messagebox.showerror("Import Validation Failed", error_text)
            return

        imported = 0
        skipped = 0
        error_list = []

        for index, record in enumerate(result.records, start=2):
            errors = FacultyService.validate_import_row(record)
            if errors:
                skipped += 1
                error_list.append(f"Row {index}: {'; '.join(errors)}")
                continue
            try:
                FacultyService.import_faculty(record)
                imported += 1
            except Exception as ex:
                skipped += 1
                error_list.append(f"Row {index}: {str(ex)}")

        self.load_faculty()

        message = (
            f"Faculty import completed successfully.\n\n"
            f"Total Rows : {result.total_rows}\n"
            f"Imported   : {imported}\n"
            f"Skipped    : {skipped}"
        )

        if error_list:
            message += "\n\nSkipped Rows\n-------------------------\n"
            max_errors = min(len(error_list), 10)
            for i in range(max_errors):
                message += error_list[i] + "\n"
            if len(error_list) > 10:
                message += f"\n...and {len(error_list) - 10} more skipped rows."

        if skipped == 0:
            messagebox.showinfo("Import Successful", message)
        else:
            messagebox.showwarning("Import Completed with Warnings", message)

    def export_excel(self):
        messagebox.showinfo("FacultyERP", "Faculty Excel Export will be implemented in the next step.")
