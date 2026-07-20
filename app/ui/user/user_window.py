"""
FacultyERP
User Management
---------------

User CRUD Module
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import customtkinter as ctk

from app.services.user_service import UserService
from app.services.faculty_service import FacultyService


class UserWindow:
    """User Management Window."""

    # ==========================================================
    # Constructor
    # ==========================================================

    def __init__(self, parent):

        self.parent = parent

        self.selected_user_id = None

        self.selected_faculty_id = None

        self.faculty_map = {}

        self.build_ui()

        self.initialize()

    # ==========================================================
    # Initialize
    # ==========================================================

    def initialize(self):

        self.update_button.configure(
            state="disabled"
        )

        self.delete_button.configure(
            state="disabled"
        )

        self.reset_button.configure(
            state="disabled"
        )

        self.load_faculty()

        self.load_users()

    # ==========================================================
    # Build UI
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

            text="User Management",

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

        self.form = ctk.CTkFrame(

            self.parent

        )

        self.form.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=20

        )

        self.form.grid_columnconfigure(
            1,
            weight=1
        )

        self.form.grid_columnconfigure(
            3,
            weight=1
        )
                # =====================================================
        # FACULTY
        # =====================================================

        ctk.CTkLabel(

            self.form,

            text="Faculty"

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.faculty_combo = ctk.CTkComboBox(

            self.form,

            values=[],

            state="readonly"

        )

        self.faculty_combo.grid(

            row=0,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # USERNAME
        # =====================================================

        ctk.CTkLabel(

            self.form,

            text="Username"

        ).grid(

            row=0,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.username_entry = ctk.CTkEntry(

            self.form

        )

        self.username_entry.grid(

            row=0,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # PASSWORD
        # =====================================================

        ctk.CTkLabel(

            self.form,

            text="Password"

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.password_entry = ctk.CTkEntry(

            self.form,

            show="*"

        )

        self.password_entry.grid(

            row=1,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # CONFIRM PASSWORD
        # =====================================================

        ctk.CTkLabel(

            self.form,

            text="Confirm Password"

        ).grid(

            row=1,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.confirm_password_entry = ctk.CTkEntry(

            self.form,

            show="*"

        )

        self.confirm_password_entry.grid(

            row=1,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        # =====================================================
        # ROLE
        # =====================================================

        ctk.CTkLabel(

            self.form,

            text="Role"

        ).grid(

            row=2,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.role_combo = ctk.CTkComboBox(

            self.form,

            values=[

                "Administrator",

                "Principal",

                "HOD",

                "Faculty"

            ],

            state="readonly"

        )

        self.role_combo.grid(

            row=2,

            column=1,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.role_combo.set(

            "Faculty"

        )

        # =====================================================
        # STATUS
        # =====================================================

        ctk.CTkLabel(

            self.form,

            text="Status"

        ).grid(

            row=2,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        self.status_combo = ctk.CTkComboBox(

            self.form,

            values=[

                "Active",

                "Inactive"

            ],

            state="readonly"

        )

        self.status_combo.grid(

            row=2,

            column=3,

            padx=10,

            pady=8,

            sticky="ew"

        )

        self.status_combo.set(

            "Active"

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

            command=self.save_user

        )

        self.save_button.pack(

            side="left",

            padx=5

        )

        self.update_button = ctk.CTkButton(

            button_frame,

            text="Update",

            width=120,

            command=self.update_user

        )

        self.update_button.pack(

            side="left",

            padx=5

        )

        self.delete_button = ctk.CTkButton(

            button_frame,

            text="Delete",

            width=120,

            command=self.delete_user

        )

        self.delete_button.pack(

            side="left",

            padx=5

        )

        self.reset_button = ctk.CTkButton(

            button_frame,

            text="Reset Password",

            width=140,

            command=self.reset_password

        )

        self.reset_button.pack(

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
        # USER TABLE
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

            "Faculty",

            "Username",

            "Role",

            "Status"

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

            "Faculty",

            width=260

        )

        self.tree.column(

            "Username",

            width=180

        )

        self.tree.column(

            "Role",

            width=140,

            anchor="center"

        )

        self.tree.column(

            "Status",

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
    # LOAD FACULTY
    # ==========================================================

    def load_faculty(self):

        self.faculty_map.clear()

        values = []

        faculty_list = FacultyService.get_faculty()

        for faculty in faculty_list:

            full_name = " ".join(

                filter(

                    None,

                    [

                        faculty.first_name,

                        faculty.middle_name,

                        faculty.last_name

                    ]

                )

            )

            values.append(

                full_name

            )

            self.faculty_map[

                full_name

            ] = faculty.faculty_id

        self.faculty_combo.configure(

            values=values

        )

        if values:

            self.faculty_combo.set(

                values[0]

            )

    # ==========================================================
    # LOAD USERS
    # ==========================================================

    def load_users(self):

        for item in self.tree.get_children():

            self.tree.delete(

                item

            )

        users = UserService.get_all_users()

        for user in users:

            faculty_name = ""

            if user.faculty_id:

                faculty = FacultyService.get_faculty_by_id(

                    user.faculty_id

                )

                if faculty:

                    faculty_name = " ".join(

                        filter(

                            None,

                            [

                                faculty.first_name,

                                faculty.middle_name,

                                faculty.last_name

                            ]

                        )

                    )

            status = "Active"

            if not user.is_active:

                status = "Inactive"

            self.tree.insert(

                "",

                tk.END,

                values=(

                    user.user_id,

                    faculty_name,

                    user.username,

                    user.role,

                    status

                )

            )
                # ==========================================================
    # VALIDATE FORM
    # ==========================================================

    def validate_form(self):

        if not self.faculty_combo.get():

            messagebox.showwarning(

                "User",

                "Please select a Faculty."

            )

            return False

        if not self.username_entry.get().strip():

            messagebox.showwarning(

                "User",

                "Username is required."

            )

            self.username_entry.focus()

            return False

        if not self.role_combo.get():

            messagebox.showwarning(

                "User",

                "Please select a Role."

            )

            return False

        password = self.password_entry.get()

        confirm = self.confirm_password_entry.get()

        if self.selected_user_id is None:

            if not password:

                messagebox.showwarning(

                    "User",

                    "Password is required."

                )

                self.password_entry.focus()

                return False

            if password != confirm:

                messagebox.showwarning(

                    "User",

                    "Password and Confirm Password do not match."

                )

                self.confirm_password_entry.focus()

                return False

        elif password or confirm:

            if password != confirm:

                messagebox.showwarning(

                    "User",

                    "Password and Confirm Password do not match."

                )

                self.confirm_password_entry.focus()

                return False

        return True

    # ==========================================================
    # CLEAR FORM
    # ==========================================================

    def clear_form(self):

        self.selected_user_id = None

        self.selected_faculty_id = None

        if self.faculty_combo.cget("values"):

            self.faculty_combo.set(

                self.faculty_combo.cget(

                    "values"

                )[0]

            )

        self.username_entry.delete(

            0,

            tk.END

        )

        self.password_entry.delete(

            0,

            tk.END

        )

        self.confirm_password_entry.delete(

            0,

            tk.END

        )

        self.role_combo.set(

            "Faculty"

        )

        self.status_combo.set(

            "Active"

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

        self.reset_button.configure(

            state="disabled"

        )

        self.load_users()

        self.username_entry.focus()
            # ==========================================================
    # SAVE USER
    # ==========================================================

    def save_user(self):

        if not self.validate_form():

            return

        faculty_id = self.faculty_map.get(

            self.faculty_combo.get()

        )

        if faculty_id is None:

            messagebox.showwarning(

                "User",

                "Please select a valid Faculty."

            )

            return

        success, message = UserService.add_user(

            faculty_id,

            self.username_entry.get().strip(),

            self.password_entry.get(),

            self.role_combo.get(),

            self.status_combo.get() == "Active"

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "User",

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

        user = UserService.get_user(

            int(values[0])

        )

        if user is None:

            return

        self.selected_user_id = user.user_id

        self.selected_faculty_id = user.faculty_id

        for name, faculty_id in self.faculty_map.items():

            if faculty_id == user.faculty_id:

                self.faculty_combo.set(

                    name

                )

                break

        self.username_entry.delete(

            0,

            tk.END

        )

        self.username_entry.insert(

            0,

            user.username

        )

        self.password_entry.delete(

            0,

            tk.END

        )

        self.confirm_password_entry.delete(

            0,

            tk.END

        )

        self.role_combo.set(

            user.role

        )

        if user.is_active:

            self.status_combo.set(

                "Active"

            )

        else:

            self.status_combo.set(

                "Inactive"

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

        self.reset_button.configure(

            state="normal"

        )
            # ==========================================================
    # UPDATE USER
    # ==========================================================

    def update_user(self):

        if self.selected_user_id is None:

            return

        if not self.validate_form():

            return

        faculty_id = self.faculty_map.get(

            self.faculty_combo.get()

        )

        if faculty_id is None:

            messagebox.showwarning(

                "User",

                "Please select a valid Faculty."

            )

            return

        success, message = UserService.update_user(

            self.selected_user_id,

            faculty_id,

            self.username_entry.get().strip(),

            self.role_combo.get(),

            self.status_combo.get() == "Active"

        )

        if success:

            password = self.password_entry.get().strip()

            if password:

                UserService.reset_password(

                    self.selected_user_id,

                    password

                )

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "User",

                message

            )

    # ==========================================================
    # DELETE USER
    # ==========================================================

    def delete_user(self):

        if self.selected_user_id is None:

            return

        answer = messagebox.askyesno(

            "Delete User",

            "Are you sure you want to delete this user?"

        )

        if not answer:

            return

        success, message = UserService.delete_user(

            self.selected_user_id

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.clear_form()

        else:

            messagebox.showwarning(

                "User",

                message

            )

    # ==========================================================
    # RESET PASSWORD
    # ==========================================================

    def reset_password(self):

        if self.selected_user_id is None:

            return

        password = self.password_entry.get().strip()

        confirm = self.confirm_password_entry.get().strip()

        if not password:

            messagebox.showwarning(

                "User",

                "Enter a new password."

            )

            return

        if password != confirm:

            messagebox.showwarning(

                "User",

                "Password and Confirm Password do not match."

            )

            return

        success, message = UserService.reset_password(

            self.selected_user_id,

            password

        )

        if success:

            messagebox.showinfo(

                "Success",

                message

            )

            self.password_entry.delete(

                0,

                tk.END

            )

            self.confirm_password_entry.delete(

                0,

                tk.END

            )

        else:

            messagebox.showwarning(

                "User",

                message
            )
            