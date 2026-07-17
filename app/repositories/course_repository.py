"""
FacultyERP
Course Repository
-----------------
"""

from app.core.database import DatabaseManager
from app.models.course import Course


class CourseRepository:
    """Database operations for Course."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(course: Course):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO courses
            (
                course_code,
                course_name,
                course_short_name,
                degree,
                pattern,
                duration_years,
                intake,
                department_id,
                description
            )

            VALUES
            (
                ?,?,?,?,?,?,?,?,?
            )
            """,
            (
                course.course_code,
                course.course_name,
                course.course_short_name,
                course.degree,
                course.pattern,
                course.duration_years,
                course.intake,
                course.department_id,
                course.description
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
            SELECT *
            FROM courses
            ORDER BY course_name
            """
        )

        rows = cursor.fetchall()

        courses = []

        for row in rows:

            courses.append(

                Course(

                    course_id=row["course_id"],

                    course_code=row["course_code"],

                    course_name=row["course_name"],

                    course_short_name=row["course_short_name"],

                    degree=row["degree"],

                    pattern=row["pattern"],

                    duration_years=row["duration_years"],

                    intake=row["intake"],

                    department_id=row["department_id"],

                    description=row["description"],

                    is_active=row["is_active"],

                    created_at=row["created_at"]

                )

            )

        return courses

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(course_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM courses
            WHERE course_id=?
            """,
            (course_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return Course(

            course_id=row["course_id"],

            course_code=row["course_code"],

            course_name=row["course_name"],

            course_short_name=row["course_short_name"],

            degree=row["degree"],

            pattern=row["pattern"],

            duration_years=row["duration_years"],

            intake=row["intake"],

            department_id=row["department_id"],

            description=row["description"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )

    # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(course: Course):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE courses

            SET

                course_code=?,

                course_name=?,

                course_short_name=?,

                degree=?,

                pattern=?,

                duration_years=?,

                intake=?,

                department_id=?,

                description=?,

                is_active=?

            WHERE course_id=?
            """,
            (
                course.course_code,

                course.course_name,

                course.course_short_name,

                course.degree,

                course.pattern,

                course.duration_years,

                course.intake,

                course.department_id,

                course.description,

                course.is_active,

                course.course_id

            )
        )

        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(course_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM courses
            WHERE course_id=?
            """,
            (course_id,)
        )

        conn.commit()

    # ==========================================================
    # EXISTS
    # ==========================================================

    @staticmethod
    def exists(

            course_code,

            course_name,

            department_id

    ):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM courses

            WHERE

            course_code=?

            OR

            (

                course_name=?

                AND

                department_id=?

            )
            """,
            (
                course_code,

                course_name,

                department_id

            )
        )

        return cursor.fetchone()[0] > 0

    # ==========================================================
    # GENERATE COURSE CODE
    # ==========================================================

    @staticmethod
    def generate_course_code():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT MAX(course_id)
            FROM courses
            """
        )

        last_id = cursor.fetchone()[0]

        if last_id is None:

            next_id = 1

        else:

            next_id = last_id + 1

        return f"CRS{next_id:04d}"
        # ==========================================================
    # GET BY NAME
    # ==========================================================

    @staticmethod
    def get_by_name(

            course_name,

            department_id

    ):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *

            FROM courses

            WHERE

                course_name=?

                AND

                department_id=?
            """,
            (

                course_name,

                department_id

            )
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return Course(

            course_id=row["course_id"],

            course_code=row["course_code"],

            course_name=row["course_name"],

            course_short_name=row["course_short_name"],

            degree=row["degree"],

            pattern=row["pattern"],

            duration_years=row["duration_years"],

            intake=row["intake"],

            department_id=row["department_id"],

            description=row["description"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )