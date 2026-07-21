"""
FacultyERP
Academic Year Management
------------------------
"""

import tkinter as tk

from tkinter import ttk

from tkinter import messagebox

import customtkinter as ctk

from tkcalendar import DateEntry

from app.services.academic_year_service import AcademicYearService


class AcademicYearWindow:
    """Academic Year Management Window."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.selected_academic_year_id = None

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

        self.load_academic_years()

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

        # ======================================================
        # TITLE
        # ======================================================

        title = ctk.CTkLabel(

            self.parent,

            text="Academic Year Management",

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

        form.grid_columnconfigure(

            3,

            weight=1

        )
                # ======================================================
        # ACADEMIC YEAR
        # ======================================================

        ctk.CTkLabel(

            form,

            text="Academic Year"

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=10,

            sticky="w"

        )

        self.academic_year_entry = ctk.CTkEntry(

            form

        )

        self.academic_year_entry.grid(

            row=0,

            column=1,

            padx=10,

            pady=10,

            sticky="ew"

        )

        # ======================================================
        # START DATE
        # ======================================================

        ctk.CTkLabel(

            form,

            text="Start Date"

        ).grid(

            row=0,

            column=2,

            padx=10,

            pady=10,

            sticky="w"

        )

        self.start_date_entry = DateEntry(

            form,

            date_pattern="dd-mm-yyyy",

            width=18

        )

        self.start_date_entry.grid(

            row=0,

            column=3,

            padx=10,

            pady=10,

            sticky="ew"

        )

        # ======================================================
        # END DATE
        # ======================================================

        ctk.CTkLabel(

            form,

            text="End Date"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=10,

            sticky="w"

        )

        self.end_date_entry = DateEntry(

            form,

            date_pattern="dd-mm-yyyy",

            width=18

        )

        self.end_date_entry.grid(

            row=1,

            column=1,

            padx=10,

            pady=10,

            sticky="ew"

        )

        # ======================================================
        # CURRENT YEAR
        # ======================================================

        self.current_var = tk.IntVar(

            value=0

        )

        self.current_checkbox = ctk.CTkCheckBox(

            form,

            text="Current Academic Year",

            variable=self.current_var,

            onvalue=1,

            offvalue=0

        )

        self.current_checkbox.grid(

            row=1,

            column=2,

            columnspan=2,

            padx=10,

            pady=10,

            sticky="w"

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

            command=self.save_academic_year

        )

        self.save_button.pack(

            side="left",

            padx=5

        )

        self.update_button = ctk.CTkButton(

            button_frame,

            text="Update",

            width=120,

            command=self.update_academic_year

        )

        self.update_button.pack(

            side="left",

            padx=5

        )

        self.delete_button = ctk.CTkButton(

            button_frame,

            text="Delete",

            width=120,

            command=self.delete_academic_year

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

            "Academic Year",

            "Start Date",

            "End Date",

            "Current"

        )

        self.tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            height=12

        )

        for column in columns:

            self.tree.heading(

                column,

                text=column

            )

        self.tree.column(

            "ID",

            width=60,

            anchor="center"

        )

        self.tree.column(

            "Academic Year",

            width=180,

            anchor="center"

        )

        self.tree.column(

            "Start Date",

            width=140,

            anchor="center"

        )

        self.tree.column(

            "End Date",

            width=140,

            anchor="center"

        )

        self.tree.column(

            "Current",

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
    # LOAD ACADEMIC YEARS
    # ==========================================================

    def load_academic_years(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        academic_years = AcademicYearService.get_academic_years()

        for year in academic_years:

            self.tree.insert(

                "",

                tk.END,

                values=(

                    year.academic_year_id,

                    year.academic_year,

                    year.start_date,

                    year.end_date,

                    "Yes" if year.is_current else "No"

                )

            )

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_academic_year_id = None

        self.academic_year_entry.delete(

            0,

            tk.END

        )

        self.current_var.set(

            0

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

        self.load_academic_years()

        self.academic_year_entry.focus()

    # ==========================================================
    # SAVE
    # ==========================================================

    def save_academic_year(self):

        success, message = AcademicYearService.add_academic_year(

            self.academic_year_entry.get().strip(),

            self.start_date_entry.get(),

            self.end_date_entry.get(),

            self.current_var.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "Academic Year",

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

        academic_year = AcademicYearService.get_academic_year(

            int(values[0])

        )

        if academic_year is None:

            return

        self.selected_academic_year_id = (

            academic_year.academic_year_id

        )

        self.academic_year_entry.delete(

            0,

            tk.END

        )

        self.academic_year_entry.insert(

            0,

            academic_year.academic_year

        )

        try:

            self.start_date_entry.set_date(

                academic_year.start_date

            )

        except Exception:

            pass

        try:

            self.end_date_entry.set_date(

                academic_year.end_date

            )

        except Exception:

            pass

        self.current_var.set(

            academic_year.is_current

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

    def update_academic_year(self):

        if self.selected_academic_year_id is None:

            return

        success, message = AcademicYearService.update_academic_year(

            self.selected_academic_year_id,

            self.academic_year_entry.get().strip(),

            self.start_date_entry.get(),

            self.end_date_entry.get(),

            self.current_var.get()

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "Academic Year",

                message

            )

    # ==========================================================
    # DELETE
    # ==========================================================

    def delete_academic_year(self):

        if self.selected_academic_year_id is None:

            return

        answer = messagebox.askyesno(

            "Delete Academic Year",

            "Are you sure you want to delete this Academic Year?"

        )

        if not answer:

            return

        success, message = AcademicYearService.delete_academic_year(

            self.selected_academic_year_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "Academic Year",

                message

            )
            