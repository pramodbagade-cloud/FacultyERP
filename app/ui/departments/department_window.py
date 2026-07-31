"""
FacultyERP
Department Management
---------------------

Department CRUD Module
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from app.services.department_service import DepartmentService

class DepartmentWindow:
    """Department Management Screen."""
    def __init__(self, parent):
        self.parent = parent
        self.selected_department_id = None
        self.build_ui()
        self.initialize()

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def initialize(self):

        self.update_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.load_departments()
        #self.load_next_department_code()    


    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        # ---------------------------------------------
        # Clear Workspace
        # ---------------------------------------------

        for widget in self.parent.winfo_children():
            widget.destroy()
        self.parent.grid_rowconfigure(3, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        # ---------------------------------------------
        # Title
        # ---------------------------------------------

        title = ctk.CTkLabel(self.parent, text="Department Management", font=("Segoe UI", 24, "bold"))
        title.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 10))

        # ---------------------------------------------
        # Form
        # ---------------------------------------------

        form = ctk.CTkFrame(self.parent)
        form.grid(row=1, column=0, sticky="ew", padx=20)
        form.grid_columnconfigure(1, weight=1)

        # ---------------------------------------------
        # Department Code
        # ---------------------------------------------

        ctk.CTkLabel(form, text="Department Code").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.code_entry = ctk.CTkEntry(form, state="normal")
        self.code_entry.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

        # ---------------------------------------------
        # Department Name
        # ---------------------------------------------

        ctk.CTkLabel(form, text="Department Name" ).grid(row=1, column=0, padx=10, pady=8, sticky="w" )
        self.name_entry = ctk.CTkEntry(form)
        self.name_entry.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

        # ---------------------------------------------
        # HOD
        # ---------------------------------------------

        ctk.CTkLabel(form, text="HOD Name" ).grid(row=2, column=0, padx=10, pady=8, sticky="w")
        self.hod_entry = ctk.CTkEntry(form)
        self.hod_entry.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        # ---------------------------------------------
        # Description
        # ---------------------------------------------

        ctk.CTkLabel(form, text="Description" ).grid(row=3, column=0, padx=10, pady=8, sticky="w")
        self.description_entry = ctk.CTkEntry(form)
        self.description_entry.grid(row=3, column=1, padx=10, pady=8, sticky="ew")

        # ---------------------------------------------
        # Buttons
        # ---------------------------------------------

        button_frame = ctk.CTkFrame(self.parent)
        button_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
        self.save_button = ctk.CTkButton(button_frame, text="Save", command=self.save_department)
        self.save_button.pack(side="left", padx=5)
        self.update_button = ctk.CTkButton(button_frame, text="Update", command=self.update_department)
        self.update_button.pack(side="left", padx=5)
        self.delete_button = ctk.CTkButton(button_frame, text="Delete", command=self.delete_department)
        self.delete_button.pack(side="left", padx=5 )
        self.clear_button = ctk.CTkButton(button_frame, text="Clear", command=self.clear_form )
        self.clear_button.pack(side="left", padx=5)

        # ---------------------------------------------
        # Department Table
        # ---------------------------------------------

        table_frame = ctk.CTkFrame(self.parent)
        table_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )
        columns = (
            "ID",
            "Code",
            "Department",
            "HOD"
        )
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=14
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Code", text="Code")
        self.tree.heading("Department", text="Department Name")
        self.tree.heading("HOD", text="HOD Name")
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Code", width=120, anchor="center")
        self.tree.column("Department", width=350)
        self.tree.column("HOD", width=250)

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
        self.tree.delete(*self.tree.get_children())
        departments = DepartmentService.get_departments()
        for department in departments:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    department.department_id,
                    department.department_code,
                    department.department_name,
                    department.hod_name
                )
            )
    # ==========================================================
    # SAVE DEPARTMENT
    # ==========================================================
    def save_department(self):
        success, message = DepartmentService.add_department(
            self.code_entry.get(),
            self.name_entry.get(),
            self.hod_entry.get(),
            self.description_entry.get()
        )
        if success:
            messagebox.showinfo("Success", message)
            self.load_departments()
            self.clear_form()
    
        else:
            messagebox.showwarning("Department", message)
    # ==========================================================
    # ROW SELECTED
    # ==========================================================

    def on_row_selected(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0])["values"]
        self.selected_department_id = values[0]
        department = DepartmentService.get_department(
            self.selected_department_id
        )

        if department is None:
            return
        self.code_entry.configure(state="normal")
        self.code_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.hod_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.code_entry.insert(0, department.department_code)
        self.name_entry.insert(0, department.department_name)
        self.hod_entry.insert(0, department.hod_name)
        self.description_entry.insert(0, department.description)
        self.save_button.configure(state="disabled")
        self.update_button.configure(state="normal")
        self.delete_button.configure(state="normal")
    
    
    # ==========================================================
    # UPDATE DEPARTMENT
    # ==========================================================

    def update_department(self):

        if self.selected_department_id is None:
            messagebox.showwarning(
                "Department",
                "Please select a department."
            )
            return

        success, message = DepartmentService.update_department(
            self.selected_department_id,
            self.code_entry.get(),
            self.name_entry.get(),
            self.hod_entry.get(),
            self.description_entry.get()
        )

        if success:
            messagebox.showinfo("Success", message)
            self.load_departments()
            self.clear_form()

        else:

            messagebox.showwarning("Department", message)

    # ==========================================================
    # DELETE DEPARTMENT
    # ==========================================================

    def delete_department(self):

        if self.selected_department_id is None:
            messagebox.showwarning("Department", "Please select a department.")
            return

        answer = messagebox.askyesno("Confirm Delete", "Do you really want to delete this department?")
        if not answer:
            return
        success, message = DepartmentService.delete_department(self.selected_department_id)

        if success:
            messagebox.showinfo("Success", message)
            self.load_departments()
            self.clear_form()
        else:
            messagebox.showwarning("Department", message)

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_department_id = None
        self.code_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.hod_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        for item in self.tree.selection():
            self.tree.selection_remove(item)
        self.save_button.configure(state="normal")
        self.update_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.code_entry.focus()
        #self.load_next_department_code()
    
    
    # ==========================================================
    # REFRESH GRID
    # ==========================================================

    def refresh(self):
        """Refresh department records."""
        self.load_departments()
    # ==========================================================
    # RESET MODULE
    # ==========================================================

    def reset(self):
        """Reset the complete module."""
        self.clear_form()
        self.load_departments()
    # ==========================================================
    # END OF CLASS
    # ==========================================================