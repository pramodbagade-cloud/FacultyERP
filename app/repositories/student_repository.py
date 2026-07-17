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
                student_name,
                department_id,
                course_id,
                semester,
                division,
                academic_year,
                mobile,
                email
            )

            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,?
            )
            """,
            (
                student.college_id,
                student.prn,
                student.roll_no,
                student.student_name,
                student.department_id,
                student.course_id,
                student.semester,
                student.division,
                student.academic_year,
                student.mobile,
                student.email
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

        cursor.execute("""

            SELECT *

            FROM students

            ORDER BY

                course_id,

                department_id,

                semester,

                division,

                roll_no

        """)

        rows = cursor.fetchall()

        students = []

        for row in rows:

            students.append(

                Student(

                    student_id=row["student_id"],

                    college_id=row["college_id"],

                    prn=row["prn"],

                    roll_no=row["roll_no"],

                    student_name=row["student_name"],

                    department_id=row["department_id"],

                    course_id=row["course_id"],

                    semester=row["semester"],

                    division=row["division"],

                    academic_year=row["academic_year"],

                    mobile=row["mobile"],

                    email=row["email"],

                    is_active=row["is_active"],

                    created_at=row["created_at"]

                )

            )

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

            SELECT *

            FROM students

            WHERE student_id=?

            """,

            (student_id,)

        )

        row = cursor.fetchone()

        if row is None:

            return None

        return Student(

            student_id=row["student_id"],

            college_id=row["college_id"],

            prn=row["prn"],

            roll_no=row["roll_no"],

            student_name=row["student_name"],

            department_id=row["department_id"],

            course_id=row["course_id"],

            semester=row["semester"],

            division=row["division"],

            academic_year=row["academic_year"],

            mobile=row["mobile"],

            email=row["email"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )
    