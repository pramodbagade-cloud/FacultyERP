"""
FacultyERP
Database Schema
---------------

Creates all database tables required by FacultyERP.

Phase-1 Master Tables

    Users
    Departments
    Faculty
    Courses
    Subjects
    Academic Years
    Semesters
    Divisions
    Students
    Institute
    App Settings

Phase-2 Transaction Tables

    Faculty Subject Assignment
    Timetable
    Attendance
    Internal Assessment
    Practical Attendance
    Course File
"""

import sqlite3

from app.services.password_service import PasswordService


class DatabaseSchema:
    """Creates FacultyERP database schema."""

    @staticmethod
    def create(connection: sqlite3.Connection):

        cursor = connection.cursor()
                # ==========================================================
        # USERS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (

                user_id INTEGER PRIMARY KEY AUTOINCREMENT,

                faculty_id INTEGER,

                username TEXT UNIQUE NOT NULL,

                password_hash TEXT NOT NULL,

                role TEXT NOT NULL,

                is_active INTEGER NOT NULL DEFAULT 1,

                last_login TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (faculty_id)
                    REFERENCES faculty(faculty_id)

            )
            """
        )
                # ==========================================================
        # DEPARTMENTS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS departments
            (

                department_id INTEGER PRIMARY KEY AUTOINCREMENT,

                department_code TEXT UNIQUE NOT NULL,

                department_name TEXT UNIQUE NOT NULL,

                hod_name TEXT,

                description TEXT,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )
                # ==========================================================
        # FACULTY
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS faculty
            (

                faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,

                faculty_code TEXT UNIQUE NOT NULL,

                employee_code TEXT UNIQUE NOT NULL,

                first_name TEXT NOT NULL,

                middle_name TEXT,

                last_name TEXT NOT NULL,

                gender TEXT,

                date_of_birth TEXT,

                mobile TEXT,

                email TEXT,

                address TEXT,

                department_id INTEGER NOT NULL,

                designation TEXT NOT NULL,

                joining_date TEXT,

                employment_type TEXT,

                qualification TEXT,

                specialization TEXT,

                experience REAL DEFAULT 0,

                research_area TEXT,

                orcid_id TEXT,

                google_scholar_id TEXT,

                scopus_author_id TEXT,

                vidwan_id TEXT,

                aicte_id TEXT,

                university_approved INTEGER NOT NULL DEFAULT 1,

                photo TEXT,

                remarks TEXT,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (department_id)
                    REFERENCES departments(department_id)

            )
            """
        )
                # ==========================================================
        # COURSES
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS courses
            (

                course_id INTEGER PRIMARY KEY AUTOINCREMENT,

                course_code TEXT UNIQUE NOT NULL,

                course_name TEXT NOT NULL,

                course_short_name TEXT NOT NULL,

                degree TEXT NOT NULL,

                pattern TEXT NOT NULL,

                duration_years INTEGER NOT NULL,

                intake INTEGER NOT NULL DEFAULT 0,

                department_id INTEGER NOT NULL,

                description TEXT,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (department_id)
                    REFERENCES departments(department_id),

                UNIQUE
                (
                    course_name,
                    department_id,
                    pattern
                )

            )
            """
        )
                # ==========================================================
        # SUBJECTS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS subjects
            (

                subject_id INTEGER PRIMARY KEY AUTOINCREMENT,

                subject_code TEXT UNIQUE NOT NULL,

                subject_name TEXT NOT NULL,

                subject_short_name TEXT NOT NULL,

                department_id INTEGER NOT NULL,

                course_id INTEGER NOT NULL,

                semester_id INTEGER NOT NULL,

                subject_type TEXT NOT NULL,

                credits INTEGER NOT NULL DEFAULT 4,

                theory_hours INTEGER NOT NULL DEFAULT 0,

                practical_hours INTEGER NOT NULL DEFAULT 0,

                tutorial_hours INTEGER NOT NULL DEFAULT 0,

                description TEXT,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (department_id)
                    REFERENCES departments(department_id),

                FOREIGN KEY (course_id)
                    REFERENCES courses(course_id),

                FOREIGN KEY (semester_id)
                    REFERENCES semesters(semester_id),

                UNIQUE
                (
                    subject_name,
                    course_id,
                    semester_id
                )

            )
            """
        )
                # ==========================================================
        # ACADEMIC YEARS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS academic_years
            (

                academic_year_id INTEGER PRIMARY KEY AUTOINCREMENT,

                academic_year TEXT UNIQUE NOT NULL,

                start_date TEXT,

                end_date TEXT,

                is_current INTEGER NOT NULL DEFAULT 0,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )
                # ==========================================================
        # SEMESTERS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS semesters
            (

                semester_id INTEGER PRIMARY KEY AUTOINCREMENT,

                semester_no INTEGER UNIQUE NOT NULL,

                semester_name TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )
                # ==========================================================
        # DIVISIONS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS divisions
            (

                division_id INTEGER PRIMARY KEY AUTOINCREMENT,

                division_code TEXT NOT NULL,

                division_name TEXT NOT NULL,

                course_id INTEGER NOT NULL,

                academic_year_id INTEGER NOT NULL,

                semester_id INTEGER NOT NULL,

                intake INTEGER NOT NULL DEFAULT 0,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (course_id)
                    REFERENCES courses(course_id),

                FOREIGN KEY (academic_year_id)
                    REFERENCES academic_years(academic_year_id),

                FOREIGN KEY (semester_id)
                    REFERENCES semesters(semester_id),

                UNIQUE
                (
                    course_id,
                    academic_year_id,
                    semester_id,
                    division_code
                )

            )
            """
        )
                # ==========================================================
        # STUDENTS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students
            (

                student_id INTEGER PRIMARY KEY AUTOINCREMENT,

                college_id TEXT UNIQUE NOT NULL,

                prn TEXT UNIQUE,

                roll_no TEXT NOT NULL,

                first_name TEXT NOT NULL,

                middle_name TEXT,

                last_name TEXT NOT NULL,

                gender TEXT,

                date_of_birth TEXT,

                mobile TEXT,

                email TEXT,

                parent_name TEXT,

                parent_mobile TEXT,

                parent_email TEXT,
                permanent_address TEXT,

                local_address TEXT,

                emergency_contact_name TEXT,

                emergency_contact_number TEXT,
                blood_group TEXT,

                aadhaar_number TEXT,

                photo TEXT,

                admission_year INTEGER,

                academic_year_id INTEGER NOT NULL,

                department_id INTEGER NOT NULL,

                course_id INTEGER NOT NULL,

                semester_id INTEGER NOT NULL,

                division_id INTEGER NOT NULL,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (academic_year_id)
                    REFERENCES academic_years(academic_year_id),

                FOREIGN KEY (department_id)
                    REFERENCES departments(department_id),

                FOREIGN KEY (course_id)
                    REFERENCES courses(course_id),

                FOREIGN KEY (semester_id)
                    REFERENCES semesters(semester_id),

                FOREIGN KEY (division_id)
                    REFERENCES divisions(division_id)

            )
            """
        )
                # ==========================================================
        # FACULTY SUBJECT ASSIGNMENTS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS faculty_subject_assignments
            (

                assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,

                faculty_id INTEGER NOT NULL,

                department_id INTEGER NOT NULL,

                course_id INTEGER NOT NULL,

                semester_id INTEGER NOT NULL,

                subject_id INTEGER NOT NULL,

                academic_year_id INTEGER NOT NULL,

                division_id INTEGER NOT NULL,

                batch_name TEXT DEFAULT 'Full',

                workload_hours REAL DEFAULT 0,

                remarks TEXT,

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (faculty_id)
                    REFERENCES faculty(faculty_id),

                FOREIGN KEY (department_id)
                    REFERENCES departments(department_id),

                FOREIGN KEY (course_id)
                    REFERENCES courses(course_id),

                FOREIGN KEY (semester_id)
                    REFERENCES semesters(semester_id),

                FOREIGN KEY (subject_id)
                    REFERENCES subjects(subject_id),

                FOREIGN KEY (academic_year_id)
                    REFERENCES academic_years(academic_year_id),

                FOREIGN KEY (division_id)
                    REFERENCES divisions(division_id),

                UNIQUE
                (
                    faculty_id,
                    subject_id,
                    academic_year_id,
                    division_id,
                    batch_name
                )

            )
            """
        )
                # ==========================================================
        # INSTITUTE
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS institute
            (

                institute_id INTEGER PRIMARY KEY AUTOINCREMENT,

                institute_name TEXT NOT NULL,

                short_name TEXT,

                university_name TEXT,

                address TEXT,

                city TEXT,

                state TEXT,

                pincode TEXT,

                website TEXT,

                email TEXT,

                phone TEXT,

                principal_name TEXT,

                logo TEXT,

                established_year INTEGER,

                affiliation TEXT,

                accreditation TEXT,

                description TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )
                # ==========================================================
        # APP SETTINGS
        # ==========================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS app_settings
            (

                setting_key TEXT PRIMARY KEY,

                setting_value TEXT

            )
            """
        )
                # ==========================================================
        # DEFAULT ADMIN USER
        # ==========================================================

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM users
            """
        )

        if cursor.fetchone()[0] == 0:

            cursor.execute(
                """
                INSERT INTO users
                (
                    faculty_id,
                    username,
                    password_hash,
                    role,
                    is_active
                )
                VALUES
                (
                    ?, ?, ?, ?, ?
                )
                """,
                (
                    None,
                    "admin",
                    PasswordService.hash_password("admin123"),
                    "Administrator",
                    1
                )
            )
                    # ==========================================================
        # DEFAULT SEMESTERS
        # ==========================================================

        default_semesters = [

            (1, "Semester I"),

            (2, "Semester II"),

            (3, "Semester III"),

            (4, "Semester IV"),

            (5, "Semester V"),

            (6, "Semester VI"),

            (7, "Semester VII"),

            (8, "Semester VIII")

        ]

        for semester_no, semester_name in default_semesters:

            cursor.execute(
                """
                INSERT INTO semesters
                (
                    semester_no,
                    semester_name
                )

                SELECT ?, ?

                WHERE NOT EXISTS
                (
                    SELECT 1
                    FROM semesters
                    WHERE semester_no=?
                )
                """,
                (
                    semester_no,
                    semester_name,
                    semester_no
                )
            )
                    # ==========================================================
        # DEFAULT ACADEMIC YEAR
        # ==========================================================

        cursor.execute(
            """
            INSERT INTO academic_years
            (
                academic_year,
                start_date,
                end_date,
                is_current
            )

            SELECT ?, ?, ?, ?

            WHERE NOT EXISTS
            (
                SELECT 1
                FROM academic_years
            )
            """,
            (
                "2026-2027",
                "2026-07-01",
                "2027-06-30",
                1
            )
        )
                # ==========================================================
        # DEFAULT INSTITUTE
        # ==========================================================

        cursor.execute(
            """
            INSERT INTO institute
            (
                institute_name,
                short_name,
                university_name,
                address,
                city,
                state,
                pincode,
                website,
                email,
                phone,
                principal_name,
                logo,
                established_year,
                affiliation,
                accreditation,
                description
            )

            SELECT
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?

            WHERE NOT EXISTS
            (
                SELECT 1
                FROM institute
            )
            """,
            (
                "TSSM's Bhivarabai Sawant College of Engineering & Research",
                "TSSM's BSCOER",
                "Savitribai Phule Pune University",
                "Narhe",
                "Pune",
                "Maharashtra",
                "411041",
                "",
                "",
                "",
                "",
                "",
                2009,
                "AICTE Approved | Affiliated to SPPU",
                "NAAC / NBA",
                "FacultyERP Default Institute Record"
            )
        )
                # ==========================================================
        # DEFAULT APPLICATION SETTINGS
        # ==========================================================

        default_settings = [

            ("appearance_mode", "Light"),

            ("theme_name", "Professional Blue"),

            ("accent_color", "#2563EB")

        ]

        for setting_key, setting_value in default_settings:

            cursor.execute(
                """
                INSERT INTO app_settings
                (
                    setting_key,
                    setting_value
                )

                SELECT ?, ?

                WHERE NOT EXISTS
                (
                    SELECT 1
                    FROM app_settings
                    WHERE setting_key=?
                )
                """,
                (
                    setting_key,
                    setting_value,
                    setting_key
                )
            )
                    # ==========================================================
        # COMMIT
        # ==========================================================

        connection.commit()
