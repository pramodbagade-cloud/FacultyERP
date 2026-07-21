"""
FacultyERP
Semester Management
-------------------

Semester CRUD Module
"""

import tkinter as tk

from tkinter import ttk

from tkinter import messagebox

import customtkinter as ctk

from app.services.semester_service import SemesterService


class SemesterWindow:
    """Semester Management Window."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.selected_semester_id = None

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

        self.load_semesters()

        self.load_next_semester_number()

    # ==========================================================
    # LOAD NEXT SEMESTER NUMBER
    # ==========================================================

    def load_next_semester_number(self):

        semester_no = SemesterService.get_next_semester_number()

        self.number_combo.configure(

        state="normal"

        )

        if semester_no is None:

            self.number_combo.set("All Created")

            self.save_button.configure(

                state="disabled"

            )

        else:

            self.number_combo.set(

                str(semester_no)

            )

            self.save_button.configure(

                state="normal"

            )

        self.number_combo.configure(

            state="readonly"

        )
    # ==========================================================
    # BUILD USER INTERFACE
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

        # ======================================================
        # TITLE
        # ======================================================

        title = ctk.CTkLabel(

            self.parent,

            text="Semester Management",

            font=("Segoe UI", 24, "bold")

        )

        title.grid(

            row=0,

            column=0,

            sticky="w",

            padx=20,

            pady=(15, 10)

        )

        # ======================================================
        # FORM
        # ======================================================

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

        # ======================================================
        # SEMESTER NUMBER
        # ======================================================

        ctk.CTkLabel(

            form,

            text="Semester Number"

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=10,

            sticky="w"

        )

        self.number_combo = ctk.CTkComboBox(

            form,

            values=[

                "1",

                "2",

                "3",

                "4",

                "5",

                "6",

                "7",

                "8"

            ],

            state="readonly",

            width=180

        )

        self.number_combo.grid(

            row=0,

            column=1,

            padx=10,

            pady=10,

            sticky="w"

        )

        # ======================================================
        # SEMESTER NAME
        # ======================================================

        ctk.CTkLabel(

            form,

            text="Semester Name"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=10,

            sticky="w"

        )

        self.name_entry = ctk.CTkEntry(

            form

        )

        self.name_entry.grid(

            row=1,

            column=1,

            padx=10,

            pady=10,

            sticky="ew"

        )
                # ======================================================
        # BUTTON FRAME
        # ======================================================

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

            command=self.save_semester

        )

        self.save_button.pack(

            side="left",

            padx=5

        )

        self.update_button = ctk.CTkButton(

            button_frame,

            text="Update",

            width=120,

            command=self.update_semester

        )

        self.update_button.pack(

            side="left",

            padx=5

        )

        self.delete_button = ctk.CTkButton(

            button_frame,

            text="Delete",

            width=120,

            command=self.delete_semester

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

        # ======================================================
        # TABLE FRAME
        # ======================================================

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

            "Semester No",

            "Semester Name"

        )

        self.tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            height=12

        )

        self.tree.heading(

            "ID",

            text="ID"

        )

        self.tree.heading(

            "Semester No",

            text="Semester No"

        )

        self.tree.heading(

            "Semester Name",

            text="Semester Name"

        )

        self.tree.column(

            "ID",

            width=60,

            anchor="center"

        )

        self.tree.column(

            "Semester No",

            width=140,

            anchor="center"

        )

        self.tree.column(

            "Semester Name",

            width=300

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
    # LOAD SEMESTERS
    # ==========================================================

    def load_semesters(self):

        for item in self.tree.get_children():

            self.tree.delete(

                item

            )

        semesters = SemesterService.get_semesters()

        for semester in semesters:

            self.tree.insert(

                "",

                tk.END,

                values=(

                    semester.semester_id,

                    semester.semester_no,

                    semester.semester_name

                )

            )

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_semester_id = None

        self.name_entry.delete(

            0,

            tk.END

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

        self.load_semesters()

        self.load_next_semester_number()

        self.name_entry.focus()
            # ==========================================================
    # SAVE
    # ==========================================================

    def save_semester(self):

        success, message = SemesterService.add_semester(

            self.number_combo.get(),

            self.name_entry.get().strip()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "Semester",

                message

            )

    # ==========================================================
    # ROW SELECTED
    # ==========================================================

    def on_row_selected(self, event):

        selection = self.tree.selection()

        if not selection:

            return

        values = self.tree.item(

            selection[0],

            "values"

        )

        semester = SemesterService.get_semester(

            int(values[0])

        )

        if semester is None:

            return

        self.selected_semester_id = (

            semester.semester_id

        )

        self.number_combo.configure(

            state="normal"

        )

        self.number_combo.set(

            str(semester.semester_no)

        )

        self.number_combo.configure(

            state="readonly"

        )

        self.name_entry.delete(

            0,

            tk.END

        )

        self.name_entry.insert(

            0,

            semester.semester_name

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
    # UPDATE
    # ==========================================================

    def update_semester(self):

        if self.selected_semester_id is None:

            return

        success, message = SemesterService.update_semester(

            self.selected_semester_id,

            self.number_combo.get(),

            self.name_entry.get().strip()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "Semester",

                message

            )
                # ==========================================================
    # DELETE
    # ==========================================================

    def delete_semester(self):

        if self.selected_semester_id is None:

            return

        answer = messagebox.askyesno(

            "Delete Semester",

            "Are you sure you want to delete this Semester?"

        )

        if not answer:

            return

        success, message = SemesterService.delete_semester(

            self.selected_semester_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "Semester",

                message

            )
