"""
FacultyERP
Student Repository
------------------
"""

from app.core.database import DatabaseManager
from app.models.student import Student


class StudentRepository:
    """Database operations for Student."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(student: Student):

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO students
            (
                college_id,
                prn,
                roll_no,
                first_name,
                middle_name,
                last_name,
                gender,
                date_of_birth,
                mobile,
                email,
                parent_name,
                parent_mobile,
                parent_email,
                permanent_address,
                local_address,
                emergency_contact_name,
                emergency_contact_number,
                photo,
                admission_year,
                academic_year_id,
                department_id,
                course_id,
                semester_id,
                division_id,
                is_active
            )
            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?
            )
            """,
            (
                student.college_id,
                student.prn,
                student.roll_no,
                student.first_name,
                student.middle_name,
                student.last_name,
                student.gender,
                student.date_of_birth,
                student.mobile,
                student.email,
                student.parent_name,
                student.parent_mobile,
                student.parent_email,
                student.permanent_address,
                student.local_address,
                student.emergency_contact_name,
                student.emergency_contact_number,
                student.photo,
                student.admission_year,
                student.academic_year_id,
                student.department_id,
                student.course_id,
                student.semester_id,
                student.division_id,
                student.is_active
            )
        )

        conn.commit()

    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_all():

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT

                s.*,

                ay.academic_year,

                d.department_name,

                c.course_name,

                sem.semester_name,

                div.division_name

            FROM students s

            INNER JOIN academic_years ay
                ON s.academic_year_id=ay.academic_year_id

            INNER JOIN departments d
                ON s.department_id=d.department_id

            INNER JOIN courses c
                ON s.course_id=c.course_id

            INNER JOIN semesters sem
                ON s.semester_id=sem.semester_id

            INNER JOIN divisions div
                ON s.division_id=div.division_id

            ORDER BY

                ay.academic_year,

                d.department_name,

                c.course_name,

                sem.semester_no,

                div.division_name,

                s.roll_no
            """
        )

        rows = cursor.fetchall()

        students = []
        for row in rows:

                student = Student(

                student_id=row["student_id"],

                college_id=row["college_id"],

                prn=row["prn"],

                roll_no=row["roll_no"],

                first_name=row["first_name"],

                middle_name=row["middle_name"],

                last_name=row["last_name"],

                gender=row["gender"],

                date_of_birth=row["date_of_birth"],

                mobile=row["mobile"],

                email=row["email"],

                photo=row["photo"],

                parent_name=row["parent_name"],

                parent_mobile=row["parent_mobile"],

                parent_email=row["parent_email"],

                permanent_address=row["permanent_address"],

                local_address=row["local_address"],

                emergency_contact_name=row["emergency_contact_name"],

                emergency_contact_number=row["emergency_contact_number"],

                admission_year=row["admission_year"],

                academic_year_id=row["academic_year_id"],

                department_id=row["department_id"],

                course_id=row["course_id"],

                semester_id=row["semester_id"],

                division_id=row["division_id"],

                is_active=row["is_active"],

                created_at=row["created_at"]

            )

                student.academic_year_name = row["academic_year"]

                student.department_name = row["department_name"]

                student.course_name = row["course_name"]

                student.semester_name = row["semester_name"]

                student.division_name = row["division_name"]

                students.append(student)

        return students

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(student_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                s.*,
                ay.academic_year,
                d.department_name,
                c.course_name,
                sem.semester_name,
                div.division_name
            FROM students s
            INNER JOIN academic_years ay
                ON s.academic_year_id=ay.academic_year_id
            INNER JOIN departments d
                ON s.department_id=d.department_id
            INNER JOIN courses c
                ON s.course_id=c.course_id
            INNER JOIN semesters sem
                ON s.semester_id=sem.semester_id
            INNER JOIN divisions div
                ON s.division_id=div.division_id
            WHERE s.student_id=?
            """,
            (student_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        student = Student(

            student_id=row["student_id"],

            college_id=row["college_id"],

            prn=row["prn"],

            roll_no=row["roll_no"],

            first_name=row["first_name"],

            middle_name=row["middle_name"],

            last_name=row["last_name"],

            gender=row["gender"],

            date_of_birth=row["date_of_birth"],

            mobile=row["mobile"],

            email=row["email"],

            photo=row["photo"],

            parent_name=row["parent_name"],

            parent_mobile=row["parent_mobile"],

            parent_email=row["parent_email"],

            permanent_address=row["permanent_address"],

            local_address=row["local_address"],

            emergency_contact_name=row["emergency_contact_name"],

            emergency_contact_number=row["emergency_contact_number"],

            admission_year=row["admission_year"],

            academic_year_id=row["academic_year_id"],

            department_id=row["department_id"],

            course_id=row["course_id"],

            semester_id=row["semester_id"],

            division_id=row["division_id"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )

        student.academic_year_name = row["academic_year"]

        student.department_name = row["department_name"]

        student.course_name = row["course_name"]

        student.semester_name = row["semester_name"]

        student.division_name = row["division_name"]

        return student
        # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(student: Student):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE students
            SET
                college_id=?,
                prn=?,
                roll_no=?,
                first_name=?,
                middle_name=?,
                last_name=?,
                gender=?,
                date_of_birth=?,
                mobile=?,
                email=?,
                parent_name=?,
                parent_mobile=?,
                parent_email=?,
                permanent_address=?,
                local_address=?,
                emergency_contact_name=?,
                emergency_contact_number=?,
                photo=?,
                admission_year=?,
                academic_year_id=?,
                department_id=?,
                course_id=?,
                semester_id=?,
                division_id=?,
                is_active=?
            WHERE student_id=?
            """,
            (
                student.college_id,
                student.prn,
                student.roll_no,
                student.first_name,
                student.middle_name,
                student.last_name,
                student.gender,
                student.date_of_birth,
                student.mobile,
                student.email,
                student.parent_name,
                student.parent_mobile,
                student.parent_email,
                student.permanent_address,
                student.local_address,
                student.emergency_contact_name,
                student.emergency_contact_number,
                student.photo,
                student.admission_year,
                student.academic_year_id,
                student.department_id,
                student.course_id,
                student.semester_id,
                student.division_id,
                student.is_active,
                student.student_id
            )
        )

        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(student_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM students
            WHERE student_id=?
            """,
            (student_id,)
        )

        conn.commit()
            # ==========================================================
    # EXISTS
    # ==========================================================

    @staticmethod
    def exists(college_id, prn, student_id=None):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        if student_id is None:

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM students
                WHERE college_id=?
                   OR (prn=? AND prn<>'')
                """,
                (
                    college_id,
                    prn
                )
            )

        else:

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM students
                WHERE
                (
                    college_id=?
                    OR (prn=? AND prn<>'')
                )
                AND student_id<>?
                """,
                (
                    college_id,
                    prn,
                    student_id
                )
            )

        return cursor.fetchone()[0] > 0

    # ==========================================================
    # GET NEXT ROLL NUMBER
    # ==========================================================

    @staticmethod
    def get_next_roll_no(

            academic_year_id,

            course_id,

            semester_id,

            division_id

    ):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT MAX(CAST(roll_no AS INTEGER))
            FROM students
            WHERE academic_year_id=?
            AND course_id=?
            AND semester_id=?
            AND division_id=?
            """,
            (
                academic_year_id,
                course_id,
                semester_id,
                division_id
            )
        )

        last_roll = cursor.fetchone()[0]

        if last_roll is None:

            return 1

        return last_roll + 1
        # ==========================================================
    # GET BY COLLEGE ID
    # ==========================================================

    @staticmethod
    def get_by_college_id(college_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM students
            WHERE college_id=?
            """,
            (college_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return Student(

            student_id=row["student_id"],

            college_id=row["college_id"],

            prn=row["prn"],

            roll_no=row["roll_no"],

            first_name=row["first_name"],

            middle_name=row["middle_name"],

            last_name=row["last_name"],

            gender=row["gender"],

            date_of_birth=row["date_of_birth"],

            mobile=row["mobile"],

            email=row["email"],

            photo=row["photo"],

            parent_name=row["parent_name"],

            parent_mobile=row["parent_mobile"],

            parent_email=row["parent_email"],

            permanent_address=row["permanent_address"],

            local_address=row["local_address"],

            emergency_contact_name=row["emergency_contact_name"],

            emergency_contact_number=row["emergency_contact_number"],

            admission_year=row["admission_year"],

            academic_year_id=row["academic_year_id"],

            department_id=row["department_id"],

            course_id=row["course_id"],

            semester_id=row["semester_id"],

            division_id=row["division_id"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )
    