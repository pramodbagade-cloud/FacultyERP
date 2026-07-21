"""
FacultyERP
Teaching, Assessment & Accreditation Management System
------------------------------------------------------

Dashboard Window
"""

import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from app.core.config import AppConfig
from app.core.session import Session

# ==========================================================
# EXISTING MODULES
# ==========================================================

from app.ui.departments.department_window import DepartmentWindow
from app.ui.course.course_window import CourseWindow
from app.ui.subject.subject_window import SubjectWindow
from app.ui.subject_workspace.subject_workspace_window import SubjectWorkspaceWindow
from app.ui.settings.settings_page import SettingsWindow
from app.ui.faculty.faculty_window import FacultyWindow
from app.ui.user.user_window import UserWindow
from app.ui.semester.semester_window import SemesterWindow



class DashboardWindow:
    """Main Dashboard"""

    # ==========================================================
    # INITIALIZE
    # ==========================================================

    def __init__(self, root):

        self.root = root

        # Sidebar Width

        self.sidebar_width = 270

        # Expand / Collapse

        self.master_expanded = False

        self.academics_expanded = False

        self.mentoring_expanded = False

        self.coursefile_expanded = False

        self.accreditation_expanded = False

        self.portfolio_expanded = False

        self.administration_expanded = False

        # Fonts

        self.title_font = ("Segoe UI", 22, "bold")

        self.section_font = ("Segoe UI", 12, "bold")

        self.button_font = ("Segoe UI", 12)

        self.status_font = ("Segoe UI", 11)

        # Widgets

        self.sidebar = None

        self.workspace = None

        self.statusbar = None

        self.clock_label = None

        self.date_label = None

        self.build_ui()

    # ==========================================================
    # BUILD USER INTERFACE
    # ==========================================================

    def build_ui(self):

        # ------------------------------------------
        # Remove Login Widgets
        # ------------------------------------------

        for widget in self.root.winfo_children():

            widget.destroy()

        # ------------------------------------------

        self.root.grid_rowconfigure(

            0,

            weight=1

        )

        self.root.grid_rowconfigure(

            1,

            weight=0

        )

        self.root.grid_columnconfigure(

            0,

            weight=0

        )

        self.root.grid_columnconfigure(

            1,

            weight=1

        )

        # ======================================================
        # SIDEBAR
        # ======================================================

        self.sidebar = ctk.CTkScrollableFrame(

            self.root,

            width=self.sidebar_width,

            corner_radius=0

        )

        self.sidebar.grid(

            row=0,

            column=0,

            sticky="ns"

        )

        

        # ======================================================
        # WORKSPACE
        # ======================================================

        self.workspace = ctk.CTkFrame(

            self.root

        )

        self.workspace.grid(

            row=0,

            column=1,

            sticky="nsew",

            padx=10,

            pady=10

        )

        # ======================================================
        # STATUS BAR
        # ======================================================

        self.statusbar = ctk.CTkFrame(

            self.root,

            height=30,

            corner_radius=0

        )

        self.statusbar.grid(

            row=1,

            column=0,

            columnspan=2,

            sticky="ew"

        )

        # ======================================================
        # BUILD COMPONENTS
        # ======================================================

        self.build_sidebar()

        self.show_home()

        self.build_statusbar()

    # ==========================================================
    # SIDEBAR
    # ==========================================================

    def build_sidebar(self):
        ctk.CTkLabel(self.sidebar,
            text="FacultyERP",
            font=self.title_font).pack(pady=(15,0))

        ctk.CTkLabel(self.sidebar,
                     text="Teaching, Assessment\n& Accreditation\nManagement System",
                     justify="center").pack(pady=(0,20))

        self.btn_dashboard=ctk.CTkButton(
            self.sidebar,
            text="🏠 Home",
            anchor="w",
            font=self.button_font,
            command=self.show_home
        )
        self.btn_dashboard.pack(fill="x",padx=10,pady=(0,10))

        # =====================================================
        # ACADEMIC MASTERS
        # =====================================================

        self.master_header=ctk.CTkButton(
            self.sidebar,
            text="▶ Settings",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.open_settings
        )
        self.master_header.pack(fill="x",padx=10,pady=(5,0))

        self.master_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        if self.master_expanded:

            self.master_frame.pack(
                fill="x",
                padx=20,
                pady=5
            )

        self.btn_departments=ctk.CTkButton(
            self.master_frame,
            text="Departments",
            anchor="w",
            command=self.open_departments
        )
        self.btn_departments.pack(fill="x",pady=2)

        self.btn_faculty=ctk.CTkButton(
            self.master_frame,
            text="Faculty",
            anchor="w",
            command=self.open_faculty
        )
        self.btn_faculty.pack(fill="x",pady=2)


        self.btn_semesters = ctk.CTkButton(
            self.master_frame,
            text="Semesters",
            anchor="w",
            command=self.open_semesters
        )
        self.btn_semesters.pack(fill="x",pady=2)

        self.btn_students=ctk.CTkButton(
            self.master_frame,
            text="Students",
            anchor="w",
            command=self.placeholder
        )
        self.btn_students.pack(fill="x",pady=2)

        self.btn_subjects=ctk.CTkButton(
            self.master_frame,
            text="Subjects",
            anchor="w",
            command=self.open_subjects
        )
        self.btn_subjects.pack(fill="x",pady=2)

        # =====================================================
        # ACADEMICS
        # =====================================================

        self.academics_header=ctk.CTkButton(
            self.sidebar,
            text="📚 My Teaching",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.open_teaching
        )

        self.academics_header.pack(fill="x",padx=10,pady=(6,0))

        self.academics_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.btn_course=ctk.CTkButton(
            self.academics_frame,
            text="Courses (Temporary)",
            anchor="w",
            command=self.open_courses
        )
        self.btn_course.pack(fill="x",pady=2)

        self.btn_timetable=ctk.CTkButton(
            self.academics_frame,
            text="Timetable",
            anchor="w",
            command=self.placeholder
        )
        self.btn_timetable.pack(fill="x",pady=2)

        self.btn_attendance=ctk.CTkButton(
            self.academics_frame,
            text="Attendance",
            anchor="w",
            command=self.placeholder
        )
        self.btn_attendance.pack(fill="x",pady=2)

        self.btn_assessment=ctk.CTkButton(
            self.academics_frame,
            text="Assessment",
            anchor="w",
            command=self.placeholder
        )
        self.btn_assessment.pack(fill="x",pady=2)

        self.btn_results=ctk.CTkButton(
            self.academics_frame,
            text="Results",
            anchor="w",
            command=self.placeholder
        )
        self.btn_results.pack(fill="x",pady=2)
        # =====================================================
        # STUDENT MENTORING
        # =====================================================

        self.mentoring_header=ctk.CTkButton(
            self.sidebar,
            text="▶ Student Mentoring",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.toggle_mentoring
        )
        self.mentoring_header.pack(fill="x",padx=10,pady=(6,0))

        self.mentoring_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.btn_gfm=ctk.CTkButton(
            self.mentoring_frame,
            text="Guardian Faculty Member (GFM)",
            anchor="w",
            command=self.placeholder
        )
        self.btn_gfm.pack(fill="x",pady=2)

        self.btn_counselling=ctk.CTkButton(
            self.mentoring_frame,
            text="Counselling",
            anchor="w",
            command=self.placeholder
        )
        self.btn_counselling.pack(fill="x",pady=2)

        self.btn_parent=ctk.CTkButton(
            self.mentoring_frame,
            text="Parent Interaction",
            anchor="w",
            command=self.placeholder
        )
        self.btn_parent.pack(fill="x",pady=2)

        self.btn_progress=ctk.CTkButton(
            self.mentoring_frame,
            text="Student Progress",
            anchor="w",
            command=self.placeholder
        )
        self.btn_progress.pack(fill="x",pady=2)

        # =====================================================
        # COURSE FILE
        # =====================================================

        self.coursefile_header=ctk.CTkButton(
            self.sidebar,
            text="▶ Course File",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.toggle_coursefile
        )
        self.coursefile_header.pack(fill="x",padx=10,pady=(6,0))

        self.coursefile_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.btn_course_file=ctk.CTkButton(
            self.coursefile_frame,
            text="Course File",
            anchor="w",
            command=self.placeholder
        )
        self.btn_course_file.pack(fill="x",pady=2)

        # =====================================================
        # ACCREDITATION
        # =====================================================

        self.accreditation_header=ctk.CTkButton(
            self.sidebar,
            text="▶ Accreditation",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.toggle_accreditation
        )
        self.accreditation_header.pack(fill="x",padx=10,pady=(6,0))

        self.accreditation_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.btn_nba=ctk.CTkButton(
            self.accreditation_frame,
            text="NBA",
            anchor="w",
            command=self.placeholder
        )
        self.btn_nba.pack(fill="x",pady=2)

        self.btn_naac=ctk.CTkButton(
            self.accreditation_frame,
            text="NAAC",
            anchor="w",
            command=self.placeholder
        )
        self.btn_naac.pack(fill="x",pady=2)

        self.btn_reports=ctk.CTkButton(
            self.accreditation_frame,
            text="Reports",
            anchor="w",
            command=self.placeholder
        )
        self.btn_reports.pack(fill="x",pady=2)

        # =====================================================
        # ACADEMIC PORTFOLIOS
        # =====================================================

        self.portfolio_header=ctk.CTkButton(
            self.sidebar,
            text="▶ Academic Portfolios",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.toggle_portfolios
        )
        self.portfolio_header.pack(fill="x",padx=10,pady=(6,0))

        self.portfolio_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.btn_department_portfolio=ctk.CTkButton(
            self.portfolio_frame,
            text="Department Portfolios",
            anchor="w",
            command=self.placeholder
        )
        self.btn_department_portfolio.pack(fill="x",pady=2)

        self.btn_institute_portfolio=ctk.CTkButton(
            self.portfolio_frame,
            text="Institute Portfolios",
            anchor="w",
            command=self.placeholder
        )
        self.btn_institute_portfolio.pack(fill="x",pady=2)

        # =====================================================
        # ADMINISTRATION
        # =====================================================

        self.administration_header=ctk.CTkButton(
            self.sidebar,
            text="▶ Administration",
            anchor="w",
            font=self.section_font,
            fg_color="gray30",
            command=self.toggle_administration
        )
        self.administration_header.pack(fill="x",padx=10,pady=(6,0))

        self.administration_frame=ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        self.btn_users=ctk.CTkButton(
            self.administration_frame,
            text="Users",
            anchor="w",
            command=self.open_users
        )
        self.btn_users.pack(fill="x",pady=2)

        self.btn_backup=ctk.CTkButton(
            self.administration_frame,
            text="Backup",
            anchor="w",
            command=self.placeholder
        )
        self.btn_backup.pack(fill="x",pady=2)

        self.btn_restore=ctk.CTkButton(
            self.administration_frame,
            text="Restore",
            anchor="w",
            command=self.placeholder
        )
        self.btn_restore.pack(fill="x",pady=2)

        self.btn_settings=ctk.CTkButton(
            self.administration_frame,
            text="Settings",
            anchor="w",
            command=self.placeholder
        )
        self.btn_settings.pack(fill="x",pady=2)

        # =====================================================
        # SYSTEM
        # =====================================================

        ctk.CTkLabel(
            self.sidebar,
            text="SYSTEM",
            font=self.section_font
        ).pack(anchor="w",padx=15,pady=(15,5))

        self.btn_logout=ctk.CTkButton(
            self.sidebar,
            text="Logout",
            anchor="w",
            command=self.logout
        )
        self.btn_logout.pack(fill="x",padx=10,pady=2)

        self.btn_exit=ctk.CTkButton(
            self.sidebar,
            text="Exit",
            anchor="w",
            command=self.root.destroy
        )
        self.btn_exit.pack(fill="x",padx=10,pady=(2,15))

    # =====================================================
    # HOME DASHBOARD
    # =====================================================
        # =====================================================
    # HOME DASHBOARD
    # =====================================================

    def show_home(self):

        for widget in self.workspace.winfo_children():

            widget.destroy()

        #
        # Main Container
        #

        container = ctk.CTkFrame(
            self.workspace
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        container.grid_rowconfigure(
            1,
            weight=1
        )

        container.grid_columnconfigure(
            0,
            weight=1,
            uniform="dashboard"
        )

        container.grid_columnconfigure(
            1,
            weight=1,
            uniform="dashboard"
        )

        container.grid_columnconfigure(
            2,
            weight=1,
            uniform="dashboard"
        )

        # =====================================================
        # HEADER
        # =====================================================

        header = ctk.CTkFrame(
            container
        )

        header.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            pady=(0,20)
        )

        ctk.CTkLabel(
            header,
            text="FacultyERP",
            font=("Segoe UI",28,"bold")
        ).pack(
            pady=(15,5)
        )

        ctk.CTkLabel(
            header,
            text=f"Welcome, {Session.get_user().username}",
            font=("Segoe UI",18)
        ).pack()

        ctk.CTkLabel(
            header,
            text="Personal Teaching Workspace",
            font=("Segoe UI",13)
        ).pack(
            pady=(0,15)
        )

        # =====================================================
        # COLUMN 1
        # MY SUBJECTS
        # =====================================================

        self.subject_frame = ctk.CTkFrame(
            container
        )

        self.subject_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0,10)
        )

        ctk.CTkLabel(
            self.subject_frame,
            text="📘 My Subjects",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15,15)
        )
                #
        # Heat Transfer Card
        #

        heat_card = ctk.CTkFrame(
            self.subject_frame
        )

        heat_card.pack(
            fill="x",
            padx=15,
            pady=(0,15)
        )

        ctk.CTkLabel(
            heat_card,
            text="Heat Transfer",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15,5)
        )

        ctk.CTkLabel(
            heat_card,
            text="BE Mechanical Engineering",
            font=("Segoe UI",13)
        ).pack(
            anchor="w",
            padx=15
        )

        ctk.CTkLabel(
            heat_card,
            text="Semester V",
            font=("Segoe UI",13)
        ).pack(
            anchor="w",
            padx=15,
            pady=(0,10)
        )

        ctk.CTkButton(

            heat_card,

            text="Open Workspace",

            height=40,

            command=self.placeholder

        ).pack(

            fill="x",

            padx=15,

            pady=(0,15)

        )

        #
        # Turbomachinery Card
        #

        turbo_card = ctk.CTkFrame(
            self.subject_frame
        )

        turbo_card.pack(
            fill="x",
            padx=15,
            pady=(0,15)
        )

        ctk.CTkLabel(
            turbo_card,
            text="Turbomachinery",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15,5)
        )

        ctk.CTkLabel(
            turbo_card,
            text="BE Mechanical Engineering",
            font=("Segoe UI",13)
        ).pack(
            anchor="w",
            padx=15
        )

        ctk.CTkLabel(
            turbo_card,
            text="Semester VIII",
            font=("Segoe UI",13)
        ).pack(
            anchor="w",
            padx=15,
            pady=(0,10)
        )

        ctk.CTkButton(

            turbo_card,

            text="Open Workspace",

            height=40,

            command=self.placeholder

        ).pack(

            fill="x",

            padx=15,

            pady=(0,15)

        )

        # =====================================================
        # COLUMN 2
        # TODAY'S WORK
        # =====================================================

        self.work_frame = ctk.CTkFrame(
            container
        )

        self.work_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10
        )

        ctk.CTkLabel(
            self.work_frame,
            text="Today's Work",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15,15)
        )
                #
        # Today's Tasks
        #

        tasks = [

            "📋 Take Attendance",

            "📖 Complete Lesson Plan",

            "📝 Update Lecture Diary",

            "📚 Prepare Notes",

            "📄 Prepare Assignment",

            "📊 Assessment Work",

            "📁 Update Course File"

        ]

        for task in tasks:

            task_button = ctk.CTkButton(

                self.work_frame,

                text=task,

                anchor="w",

                height=40,

                command=self.placeholder

            )

            task_button.pack(

                fill="x",

                padx=15,

                pady=5

            )

        # =====================================================
        # COLUMN 3
        # AI FACULTY ASSISTANT
        # =====================================================

        self.ai_frame = ctk.CTkFrame(

            container

        )

        self.ai_frame.grid(

            row=1,

            column=2,

            sticky="nsew",

            padx=(10,0)

        )

        ctk.CTkLabel(

            self.ai_frame,

            text="🤖 AI Faculty Assistant",

            font=("Segoe UI",18,"bold")

        ).pack(

            anchor="w",

            padx=15,

            pady=(15,15)

        )

        ai_tools = [

            "Generate Notes",

            "Generate PPT",

            "Generate MCQs",

            "Generate Quiz",

            "Generate Question Paper",

            "Bloom's Taxonomy",

            "CO-PO Mapping",

            "Ask AI"

        ]

        for tool in ai_tools:

            ctk.CTkButton(

                self.ai_frame,

                text=tool,

                anchor="w",

                height=40,

                command=self.placeholder

            ).pack(

                fill="x",

                padx=15,

                pady=5

            )

    # =====================================================
    # STATUS BAR
    # =====================================================

    def build_statusbar(self):
        left=ctk.CTkFrame(self.statusbar,fg_color="transparent")
        left.pack(side="left",padx=10)

        ctk.CTkLabel(
            left,
            text=f"{AppConfig.APP_NAME}  v{AppConfig.VERSION}",
            font=self.status_font
        ).pack(side="left",padx=(0,15))

        ctk.CTkLabel(
            left,
            text=f"User : {Session.get_user().username}",
            font=self.status_font
        ).pack(side="left",padx=(0,15))

        ctk.CTkLabel(
            left,
            text="Database : Connected",
            font=self.status_font
        ).pack(side="left")

        right=ctk.CTkFrame(self.statusbar,fg_color="transparent")
        right.pack(side="right",padx=10)

        self.date_label=ctk.CTkLabel(
            right,
            text="",
            font=self.status_font
        )
        self.date_label.pack(side="left",padx=10)

        self.clock_label=ctk.CTkLabel(
            right,
            text="",
            font=self.status_font
        )
        self.clock_label.pack(side="left")

        self.update_clock()

    # =====================================================
    # LIVE CLOCK
    # =====================================================

    def update_clock(self):

        now=datetime.now()

        self.date_label.configure(
            text=now.strftime("%d-%b-%Y")
        )

        self.clock_label.configure(
            text=now.strftime("%I:%M:%S %p")
        )

        self.root.after(
            1000,
            self.update_clock
        )

    # =====================================================
    # PLACEHOLDER
    # =====================================================

    def placeholder(self):

        messagebox.showinfo(
            "FacultyERP",
            "This module will be available in the next development phase."
        )


    # =====================================================
    # TOGGLE SECTIONS
    # =====================================================

    def toggle_master(self):

        if self.master_expanded:
            self.master_frame.pack_forget()
            self.master_header.configure(text="▶ Settings")
        else:
            self.master_frame.pack(fill="x",padx=20,pady=5)
            self.master_header.configure(text="▼ Settings")

        self.master_expanded=not self.master_expanded

    def toggle_academics(self):

        if self.academics_expanded:
            self.academics_frame.pack_forget()
            self.academics_header.configure(text="▶ Academics")
        else:
            self.academics_frame.pack(fill="x",padx=20,pady=5)
            self.academics_header.configure(text="▼ Academics")

        self.academics_expanded=not self.academics_expanded

    def toggle_mentoring(self):

        if self.mentoring_expanded:
            self.mentoring_frame.pack_forget()
            self.mentoring_header.configure(text="▶ Student Mentoring")
        else:
            self.mentoring_frame.pack(fill="x",padx=20,pady=5)
            self.mentoring_header.configure(text="▼ Student Mentoring")

        self.mentoring_expanded=not self.mentoring_expanded

    def toggle_coursefile(self):

        if self.coursefile_expanded:
            self.coursefile_frame.pack_forget()
            self.coursefile_header.configure(text="▶ Course File")
        else:
            self.coursefile_frame.pack(fill="x",padx=20,pady=5)
            self.coursefile_header.configure(text="▼ Course File")

        self.coursefile_expanded=not self.coursefile_expanded

    def toggle_accreditation(self):

        if self.accreditation_expanded:
            self.accreditation_frame.pack_forget()
            self.accreditation_header.configure(text="▶ Accreditation")
        else:
            self.accreditation_frame.pack(fill="x",padx=20,pady=5)
            self.accreditation_header.configure(text="▼ Accreditation")

        self.accreditation_expanded=not self.accreditation_expanded

    def toggle_portfolios(self):

        if self.portfolio_expanded:
            self.portfolio_frame.pack_forget()
            self.portfolio_header.configure(text="▶ Academic Portfolios")
        else:
            self.portfolio_frame.pack(fill="x",padx=20,pady=5)
            self.portfolio_header.configure(text="▼ Academic Portfolios")

        self.portfolio_expanded=not self.portfolio_expanded

    def toggle_administration(self):

        if self.administration_expanded:
            self.administration_frame.pack_forget()
            self.administration_header.configure(text="▶ Administration")
        else:
            self.administration_frame.pack(fill="x",padx=20,pady=5)
            self.administration_header.configure(text="▼ Administration")

        self.administration_expanded=not self.administration_expanded

    # =====================================================
    # CLEAR WORKSPACE
    # =====================================================

    def clear_workspace(self):
        for widget in self.workspace.winfo_children():
            widget.destroy()

    # =====================================================
    # OPEN DEPARTMENTS
    # =====================================================

    def open_departments(self):
        self.clear_workspace()
        DepartmentWindow(self.workspace)

    # =====================================================
    # OPEN FACULTY
    # =====================================================

    def open_faculty(self):

        self.clear_workspace()

        FacultyWindow(self.workspace)

    # =====================================================
    # OPEN USERS
    # =====================================================

    def open_users(self):

        self.clear_workspace()

        UserWindow(self.workspace)

    # =====================================================
    # OPEN COURSES
    # =====================================================

    def open_courses(self):
        self.clear_workspace()
        CourseWindow(self.workspace)

    # =====================================================
    # OPEN SUBJECTS
    # =====================================================

    def open_subjects(self):

        self.clear_workspace()

        SubjectWindow(self.workspace)
    
    # =====================================================
    # OPEN SEMESTERS
    # =====================================================

    def open_semesters(self):

        self.clear_workspace()

        SemesterWindow(self.workspace)


    # =====================================================
    # OPEN SETTINGS
    # =====================================================

    def open_settings(self):

        self.clear_workspace()

        SettingsWindow(
            self.workspace
    )
        

    # =====================================================
# MY TEACHING
# =====================================================

    def open_teaching(self):

        self.clear_workspace()

        ctk.CTkLabel(
            self.workspace,
            text="My Teaching",
            font=("Segoe UI", 26, "bold")
        ).pack(
            pady=(20, 20)
        )

        ctk.CTkButton(
            self.workspace,
            text="📘 Heat Transfer\nSemester V",
            height=70,
            command=self.open_heat_transfer
        ).pack(
            fill="x",
            padx=30,
            pady=10
        )

        ctk.CTkButton(
            self.workspace,
            text="⚙ Turbomachinery\nSemester VIII",
            height=70,
            command=self.open_turbomachinery
        ).pack(
            fill="x",
            padx=30,
            pady=10
        )
    # =====================================================
    # HEAT TRANSFER
    # =====================================================

    def open_heat_transfer(self):

        self.clear_workspace()

        SubjectWorkspaceWindow(

            self.workspace,

            subject_name="Heat Transfer",

            department="Mechanical Engineering",

            programme="BE",

            semester="V",

            faculty_name="Dr. Pramod Bagade"

        )

    # =====================================================
    # TURBOMACHINERY
    # =====================================================

    def open_turbomachinery(self):

        self.clear_workspace()

        SubjectWorkspaceWindow(

            self.workspace,

            subject_name="Turbomachinery",

            department="Mechanical Engineering",

            programme="BE",

            semester="VIII",

            faculty_name="Dr. Pramod Bagade"

        )
    # =====================================================
    # LOGOUT
    # =====================================================

    def logout(self):
        answer=messagebox.askyesno(
            "Logout",
            "Do you really want to logout?"
        )
        if not answer:
            return
        Session.logout()
        for widget in self.root.winfo_children():
            widget.destroy()
        from app.ui.login.login_window import LoginWindow
        LoginWindow(self.root)
