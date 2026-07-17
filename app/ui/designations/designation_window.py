"""
FacultyERP
Designation Management
----------------------

Designation CRUD Module
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import customtkinter as ctk

from app.services.designation_service import DesignationService


class DesignationWindow:
    """Designation Management Window."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.selected_designation_id = None

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

        self.load_designations()

        self.load_next_designation_code()

    # ==========================================================
    # LOAD NEXT DESIGNATION CODE
    # ==========================================================

    def load_next_designation_code(self):

        code = DesignationService.get_next_designation_code()

        self.code_entry.configure(

            state="normal"

        )

        self.code_entry.delete(

            0,

            tk.END

        )

        self.code_entry.insert(

            0,

            code

        )

        self.code_entry.configure(

            state="disabled"

        )

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

            text="Designation Management",

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

        # =====================================================
        # DESIGNATION CODE
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Designation Code"

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.code_entry = ctk.CTkEntry(

            form,

            state="normal"

        )

        self.code_entry.grid(

            row=0,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )
                # =====================================================
        # DESIGNATION NAME
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Designation"

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
        # DESCRIPTION
        # =====================================================

        ctk.CTkLabel(

            form,

            text="Description"

        ).grid(

            row=2,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.description_entry = ctk.CTkEntry(

            form

        )

        self.description_entry.grid(

            row=2,

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

            command=self.save_designation

        )

        self.save_button.pack(

            side="left",

            padx=5

        )

        self.update_button = ctk.CTkButton(

            button_frame,

            text="Update",

            width=120,

            command=self.update_designation

        )

        self.update_button.pack(

            side="left",

            padx=5

        )

        self.delete_button = ctk.CTkButton(

            button_frame,

            text="Delete",

            width=120,

            command=self.delete_designation

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
        # DESIGNATION TABLE
        # =====================================================

        table_frame = ctk.CTkFrame(

            self.parent

        )

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

            "Designation"

        )

        self.tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            height=15

        )

        self.tree.heading(

            "ID",

            text="ID"

        )

        self.tree.heading(

            "Code",

            text="Code"

        )

        self.tree.heading(

            "Designation",

            text="Designation"

        )

        self.tree.column(

            "ID",

            width=60,

            anchor="center"

        )

        self.tree.column(

            "Code",

            width=120,

            anchor="center"

        )

        self.tree.column(

            "Designation",

            width=400

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
    # LOAD DESIGNATIONS
    # ==========================================================

    def load_designations(self):

        for item in self.tree.get_children():

            self.tree.delete(

                item

            )

        designations = DesignationService.get_designations()

        for designation in designations:

            self.tree.insert(

                "",

                tk.END,

                values=(

                    designation.designation_id,

                    designation.designation_code,

                    designation.designation_name

                )

            )
                # ==========================================================
    # SAVE DESIGNATION
    # ==========================================================

    def save_designation(self):

        success, message = DesignationService.add_designation(

            self.code_entry.get(),

            self.name_entry.get(),

            self.description_entry.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.load_designations()

            self.clear_form()

        else:

            messagebox.showwarning(

                "Designation",

                message

            )

    # ==========================================================
    # ROW SELECTED
    # ==========================================================

    def on_row_selected(self, event):

        selection = self.tree.selection()

        if not selection:

            return

        item = self.tree.item(

            selection[0]

        )

        designation_id = item["values"][0]

        designation = DesignationService.get_designation(

            designation_id

        )

        if designation is None:

            return

        self.selected_designation_id = designation.designation_id

        self.code_entry.configure(

            state="normal"

        )

        self.code_entry.delete(

            0,

            tk.END

        )

        self.code_entry.insert(

            0,

            designation.designation_code

        )

        self.code_entry.configure(

            state="disabled"

        )

        self.name_entry.delete(

            0,

            tk.END

        )

        self.name_entry.insert(

            0,

            designation.designation_name

        )

        self.description_entry.delete(

            0,

            tk.END

        )

        self.description_entry.insert(

            0,

            designation.description

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
    # UPDATE DESIGNATION
    # ==========================================================

    def update_designation(self):

        if self.selected_designation_id is None:

            messagebox.showwarning(

                "Designation",

                "Please select a designation."

            )

            return

        success, message = DesignationService.update_designation(

            self.selected_designation_id,

            self.code_entry.get(),

            self.name_entry.get(),

            self.description_entry.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.load_designations()

            self.clear_form()

        else:

            messagebox.showwarning(

                "Designation",

                message

            )

    # ==========================================================
    # DELETE DESIGNATION
    # ==========================================================

    def delete_designation(self):

        if self.selected_designation_id is None:

            messagebox.showwarning(

                "Designation",

                "Please select a designation."

            )

            return

        answer = messagebox.askyesno(

            "Delete Designation",

            "Are you sure you want to delete this designation?"

        )

        if not answer:

            return

        success, message = DesignationService.delete_designation(

            self.selected_designation_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.load_designations()

            self.clear_form()

        else:

            messagebox.showwarning(

                "Designation",

                message

            )
                # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_designation_id = None

        self.code_entry.configure(

            state="normal"

        )

        self.code_entry.delete(

            0,

            tk.END

        )

        self.name_entry.delete(

            0,

            tk.END

        )

        self.description_entry.delete(

            0,

            tk.END

        )

        self.code_entry.configure(

            state="disabled"

        )

        for item in self.tree.selection():

            self.tree.selection_remove(

                item

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

        self.load_next_designation_code()

        self.name_entry.focus()

    # ==========================================================
    # REFRESH
    # ==========================================================

    def refresh(self):

        self.load_designations()

        self.clear_form()
        