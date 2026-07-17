"""
FacultyERP
Subject Workspace
-----------------
Heat Transfer / Turbomachinery Workspace
"""

import customtkinter as ctk
from tkinter import messagebox
from app.ui.attendance.attendance_window import AttendanceWindow


class SubjectWorkspaceWindow:
    """Faculty Subject Workspace."""

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(
            self,
            parent,
            subject_name,
            department,
            programme,
            semester,
            faculty_name
    ):

        self.parent = parent

        self.subject_name = subject_name

        self.department = department

        self.programme = programme

        self.semester = semester

        self.faculty_name = faculty_name

        #
        # Temporary values
        #

        self.lecture_no = 1

        self.topic = "Introduction"

        self.progress = 0

        self.build_ui()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        #
        # Clear Workspace
        #

        for widget in self.parent.winfo_children():

            widget.destroy()

        self.parent.grid_rowconfigure(
            2,
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

            text=self.subject_name,

            font=("Segoe UI", 26, "bold")

        )

        title.grid(

            row=0,

            column=0,

            sticky="w",

            padx=20,

            pady=(20, 5)

        )

        # =====================================================
        # INFORMATION CARD
        # =====================================================

        self.info_frame = ctk.CTkFrame(

            self.parent

        )

        self.info_frame.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=20,

            pady=10

        )

        self.info_frame.grid_columnconfigure(
            1,
            weight=1
        )

        self.info_frame.grid_columnconfigure(
            3,
            weight=1
        )

        #
        # Department
        #

        ctk.CTkLabel(

            self.info_frame,

            text="Department",

            font=("Segoe UI", 12, "bold")

        ).grid(

            row=0,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        ctk.CTkLabel(

            self.info_frame,

            text=self.department

        ).grid(

            row=0,

            column=1,

            padx=10,

            pady=8,

            sticky="w"

        )

        #
        # Programme
        #

        ctk.CTkLabel(

            self.info_frame,

            text="Programme",

            font=("Segoe UI", 12, "bold")

        ).grid(

            row=0,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        ctk.CTkLabel(

            self.info_frame,

            text=self.programme

        ).grid(

            row=0,

            column=3,

            padx=10,

            pady=8,

            sticky="w"

        )

        #
        # Semester
        #

        ctk.CTkLabel(

            self.info_frame,

            text="Semester",

            font=("Segoe UI", 12, "bold")

        ).grid(

            row=1,

            column=0,

            padx=10,

            pady=8,

            sticky="w"

        )

        ctk.CTkLabel(

            self.info_frame,

            text=self.semester

        ).grid(

            row=1,

            column=1,

            padx=10,

            pady=8,

            sticky="w"

        )

        #
        # Faculty
        #

        ctk.CTkLabel(

            self.info_frame,

            text="Faculty",

            font=("Segoe UI", 12, "bold")

        ).grid(

            row=1,

            column=2,

            padx=10,

            pady=8,

            sticky="w"

        )

        ctk.CTkLabel(

            self.info_frame,

            text=self.faculty_name

        ).grid(

            row=1,

            column=3,

            padx=10,

            pady=8,

            sticky="w"

        )
                # =====================================================
        # TODAY'S LECTURE
        # =====================================================

        lecture_frame = ctk.CTkFrame(

            self.parent

        )

        lecture_frame.grid(

            row=2,

            column=0,

            sticky="ew",

            padx=20,

            pady=(5,10)

        )

        lecture_frame.grid_columnconfigure(
            1,
            weight=1
        )

        ctk.CTkLabel(

            lecture_frame,

            text="Today's Lecture",

            font=("Segoe UI",16,"bold")

        ).grid(

            row=0,

            column=0,

            columnspan=2,

            padx=15,

            pady=(12,10),

            sticky="w"

        )

        # -------------------------------------------------

        ctk.CTkLabel(

            lecture_frame,

            text="Lecture No."

        ).grid(

            row=1,

            column=0,

            padx=15,

            pady=6,

            sticky="w"

        )

        self.lecture_no_label = ctk.CTkLabel(

            lecture_frame,

            text=str(self.lecture_no),

            font=("Segoe UI",14,"bold")

        )

        self.lecture_no_label.grid(

            row=1,

            column=1,

            padx=10,

            pady=6,

            sticky="w"

        )

        # -------------------------------------------------

        ctk.CTkLabel(

            lecture_frame,

            text="Topic"

        ).grid(

            row=2,

            column=0,

            padx=15,

            pady=6,

            sticky="w"

        )

        self.topic_entry = ctk.CTkEntry(

            lecture_frame

        )

        self.topic_entry.grid(

            row=2,

            column=1,

            padx=10,

            pady=6,

            sticky="ew"

        )

        self.topic_entry.insert(

            0,

            self.topic

        )

        # -------------------------------------------------

        ctk.CTkLabel(

            lecture_frame,

            text="Course Progress"

        ).grid(

            row=3,

            column=0,

            padx=15,

            pady=(15,6),

            sticky="w"

        )

        self.progressbar = ctk.CTkProgressBar(

            lecture_frame,

            height=18

        )

        self.progressbar.grid(

            row=3,

            column=1,

            padx=10,

            pady=(15,6),

            sticky="ew"

        )

        self.progressbar.set(

            self.progress / 100

        )

        self.progress_label = ctk.CTkLabel(

            lecture_frame,

            text=f"{self.progress}% Completed",

            font=("Segoe UI",12,"bold")

        )

        self.progress_label.grid(

            row=4,

            column=1,

            padx=10,

            pady=(0,10),

            sticky="w"

        )
                # =====================================================
        # TODAY'S TOOLS
        # =====================================================

        tools_frame = ctk.CTkFrame(

            self.parent

        )

        tools_frame.grid(

            row=3,

            column=0,

            sticky="nsew",

            padx=20,

            pady=(5,20)

        )

        for i in range(4):

            tools_frame.grid_columnconfigure(
                i,
                weight=1
            )

        # =====================================================
        # ROW 1
        # =====================================================

        self.attendance_button = ctk.CTkButton(

            tools_frame,

            text="📋\nAttendance",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_attendance

        )

        self.attendance_button.grid(

            row=0,

            column=0,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        self.lesson_plan_button = ctk.CTkButton(

            tools_frame,

            text="📖\nLesson Plan",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_lesson_plan

        )

        self.lesson_plan_button.grid(

            row=0,

            column=1,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        self.lecture_diary_button = ctk.CTkButton(

            tools_frame,

            text="📝\nLecture Diary",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_lecture_diary

        )

        self.lecture_diary_button.grid(

            row=0,

            column=2,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        self.notes_button = ctk.CTkButton(

            tools_frame,

            text="📚\nNotes",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_notes

        )

        self.notes_button.grid(

            row=0,

            column=3,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        # =====================================================
        # ROW 2
        # =====================================================

        self.ppt_button = ctk.CTkButton(

            tools_frame,

            text="📊\nPPT",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_ppt

        )

        self.ppt_button.grid(

            row=1,

            column=0,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        self.mcq_button = ctk.CTkButton(

            tools_frame,

            text="❓\nMCQ",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_mcq

        )

        self.mcq_button.grid(

            row=1,

            column=1,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        self.question_paper_button = ctk.CTkButton(

            tools_frame,

            text="📄\nQuestion Paper",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_question_paper

        )

        self.question_paper_button.grid(

            row=1,

            column=2,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        self.ai_button = ctk.CTkButton(

            tools_frame,

            text="🤖\nAI Assistant",

            height=90,

            font=("Segoe UI",16,"bold"),

            command=self.open_ai

        )

        self.ai_button.grid(

            row=1,

            column=3,

            padx=10,

            pady=10,

            sticky="nsew"

        )


# ==========================================================
# ATTENDANCE
# ==========================================================

    def open_attendance(self):

        AttendanceWindow(

            parent=self.parent,

            subject_name=self.subject_name,

            semester=self.semester,

            lecture_no=self.lecture_no,

            topic=self.topic_entry.get()

        )

    # ==========================================================
    # LESSON PLAN
    # ==========================================================

    def open_lesson_plan(self):

        messagebox.showinfo(

            "Lesson Plan",

            f"Opening Lesson Plan\n\n"
            f"Subject : {self.subject_name}"

        )

    # ==========================================================
    # LECTURE DIARY
    # ==========================================================

    def open_lecture_diary(self):

        messagebox.showinfo(

            "Lecture Diary",

            f"Opening Lecture Diary\n\n"
            f"Subject : {self.subject_name}"

        )

    # ==========================================================
    # NOTES
    # ==========================================================

    def open_notes(self):

        messagebox.showinfo(

            "Notes",

            f"Opening Notes Module\n\n"
            f"{self.subject_name}"

        )

    # ==========================================================
    # PPT
    # ==========================================================

    def open_ppt(self):

        messagebox.showinfo(

            "PPT",

            f"Opening PPT Module\n\n"
            f"{self.subject_name}"

        )

    # ==========================================================
    # MCQ
    # ==========================================================

    def open_mcq(self):

        messagebox.showinfo(

            "MCQ",

            f"Opening MCQ Generator\n\n"
            f"{self.subject_name}"

        )

    # ==========================================================
    # QUESTION PAPER
    # ==========================================================

    def open_question_paper(self):

        messagebox.showinfo(

            "Question Paper",

            f"Opening Question Paper Generator\n\n"
            f"{self.subject_name}"

        )

    # ==========================================================
    # AI ASSISTANT
    # ==========================================================

    def open_ai(self):

        messagebox.showinfo(

            "AI Assistant",

            f"AI Assistant for\n\n"
            f"{self.subject_name}"

        )
        