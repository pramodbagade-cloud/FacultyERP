"""
FacultyERP
Login Window
------------
"""

import customtkinter as ctk
from tkinter import messagebox

from app.core.config import AppConfig
from app.core.session import Session
from app.services.authentication_service import AuthenticationService


class LoginWindow:
    """Application Login Window."""

    def __init__(self, root):

        self.root = root

        self.build_ui()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        frame = ctk.CTkFrame(
            self.root,
            width=450,
            corner_radius=15
        )

        frame.grid(row=0, column=0)

        # ------------------------------------------------------
        # TITLE
        # ------------------------------------------------------

        title = ctk.CTkLabel(
            frame,
            text=AppConfig.APP_NAME,
            font=("Segoe UI", 30, "bold")
        )
        title.pack(pady=(30, 10))

        subtitle = ctk.CTkLabel(
            frame,
            text="Login"
        )
        subtitle.pack(pady=(0, 25))

        # ------------------------------------------------------
        # USERNAME
        # ------------------------------------------------------

        self.username_entry = ctk.CTkEntry(
            frame,
            width=300,
            placeholder_text="Username"
        )
        self.username_entry.pack(pady=10)

        # ------------------------------------------------------
        # PASSWORD
        # ------------------------------------------------------

        self.password_entry = ctk.CTkEntry(
            frame,
            width=300,
            show="*",
            placeholder_text="Password"
        )
        self.password_entry.pack(pady=10)

        # ------------------------------------------------------
        # LOGIN BUTTON
        # ------------------------------------------------------

        self.login_button = ctk.CTkButton(
            frame,
            width=300,
            text="Login",
            command=self.login
        )
        self.login_button.pack(pady=20)

        # ------------------------------------------------------
        # VERSION
        # ------------------------------------------------------

        version = ctk.CTkLabel(
            frame,
            text=f"Version {AppConfig.VERSION}"
        )
        version.pack(pady=(10, 20))

        # ======================================================
        # KEYBOARD SHORTCUTS
        # ======================================================

        # Initial cursor position
        self.username_entry.focus_set()

        # Enter in Username -> Password
        self.username_entry.bind(
            "<Return>",
            lambda event: self.password_entry.focus_set()
        )

        # Enter in Password -> Login

        self.password_entry.bind(
            "<Return>",
            lambda event: "break" if self.login() is None else "break"
        )

        # Enter anywhere -> Login
        self.root.bind(
            "<Return>",
            lambda event: self.login()
        )

        # Escape -> Exit Application
        self.root.bind(
            "<Escape>",
            lambda event: self.root.destroy()
        )

    # ==========================================================
    # LOGIN
    # ==========================================================

    def login(self):

        username = self.username_entry.get().strip()

        password = self.password_entry.get()

        if username == "":

            messagebox.showwarning(
                "Validation",
                "Please enter username."
            )

            self.username_entry.focus_set()

            return

        if password == "":

            messagebox.showwarning(
                "Validation",
                "Please enter password."
            )

            self.password_entry.focus_set()

            return

        user = AuthenticationService.login(
            username,
            password
        )

        if user is None:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

            self.password_entry.delete(0, "end")
            self.password_entry.focus_set()

            return

        Session.login(user)

        from app.ui.dashboard.dashboard_window import DashboardWindow

        DashboardWindow(self.root)