"""
FacultyERP
Division Repository
-------------------
"""

from app.core.database import DatabaseManager
from app.models.division import Division


class DivisionRepository:
    """Database operations for Division."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(division: Division):
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            INSERT INTO divisions
            (
                division_code,
                division_name,
                department_id,
                course_id,
                academic_year_id,
                semester_id,
                intake,
                is_active
            )
            VALUES
            (
            
                ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                division.division_code,
                division.division_name,
                division.department_id,
                division.course_id,
                division.academic_year_id,
                division.semester_id,
                division.intake,
                division.is_active
            )
        )
        conn.commit()

    # ==========================================================
    # GET ALL
    # ==========================================================
    @staticmethod
    def get_all():
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            SELECT
                d.division_id,
                d.division_code,
                d.department_id,
                d.division_name,
                d.course_id,
                c.course_name,
                d.academic_year_id,
                ay.academic_year,
                d.semester_id,
                s.semester_name,
                d.intake,
                d.is_active,
                d.created_at
            FROM divisions d
            LEFT JOIN courses c
                ON d.course_id=c.course_id
            LEFT JOIN academic_years ay
                ON d.academic_year_id=ay.academic_year_id
            LEFT JOIN semesters s
                ON d.semester_id=s.semester_id
            ORDER BY
                c.course_name,
                s.semester_no,
                d.division_name
            """
        )
        rows=cursor.fetchall()
        divisions=[]
        for row in rows:
            division=Division(
                division_id=row["division_id"],
                division_code=row["division_code"],
                division_name=row["division_name"],
                department_id=row["department_id"],
                course_id=row["course_id"],
                academic_year_id=row["academic_year_id"],
                semester_id=row["semester_id"],
                intake=row["intake"],
                is_active=row["is_active"],
                created_at=row["created_at"]
            )
            division.course_name=row["course_name"]
            division.academic_year_name=row["academic_year"]
            division.semester_name=row["semester_name"]
            divisions.append(division)
        return divisions
    # ==========================================================
    # GET BY COURSE / YEAR / SEMESTER
    # ==========================================================

    @staticmethod
    def get_by_course_year_semester(
            course_id,
            academic_year_id,
            semester_id
    ):

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM divisions
            WHERE
                course_id=?
                AND academic_year_id=?
                AND semester_id=?
                AND is_active=1
            ORDER BY division_name
            """,
            (
                course_id,
                academic_year_id,
                semester_id
            )
        )

        rows = cursor.fetchall()
        print("Divisions Found :", len(rows))

        divisions = []

        for row in rows:

            divisions.append(
          
                Division(
                    division_id=row["division_id"],
                    division_code=row["division_code"],
                    division_name=row["division_name"],
                    department_id=row["department_id"],
                    course_id=row["course_id"],
                    academic_year_id=row["academic_year_id"],
                    semester_id=row["semester_id"],
                    intake=row["intake"],
                    is_active=row["is_active"],
                    created_at=row["created_at"]
                )
            )

        return divisions

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(division_id):
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM divisions
            WHERE division_id=?
            """,
            (division_id,)
        )
        row=cursor.fetchone()
        if row is None:
            return None
        return Division(
            division_id=row["division_id"],
            division_code=row["division_code"],
            division_name=row["division_name"],
            department_id=row["department_id"],
            course_id=row["course_id"],
            academic_year_id=row["academic_year_id"],
            semester_id=row["semester_id"],
            intake=row["intake"],
            is_active=row["is_active"],
            created_at=row["created_at"]
        )

    # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(division: Division):
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            UPDATE divisions
            SET
                division_code=?,
                division_name=?,
                department_id=?,
                course_id=?,
                academic_year_id=?,
                semester_id=?,
                intake=?,
                is_active=?
            WHERE division_id=?
            """,
            (
                division.division_code,
                division.division_name,
                division.department_id,
                division.course_id,
                division.academic_year_id,
                division.semester_id,
                division.intake,
                division.is_active,
                division.division_id
            )
        )
        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(division_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM divisions
            WHERE division_id=?
            """,
            (division_id,)
        )

        conn.commit()
    
    # ==========================================================
    # GENERATE DIVISION CODE
    # ==========================================================

    @staticmethod
    def generate_division_code():
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            SELECT division_code
            FROM divisions
            ORDER BY division_id DESC
            LIMIT 1
            """
        )
        row=cursor.fetchone()
        if row is None or row["division_code"] is None:
            return "DIV0001"
        last_code=row["division_code"]
        number=int(last_code.replace("DIV",""))+1
        return f"DIV{number:04d}"

    # ==========================================================
    # EXISTS
    # ==========================================================
    @staticmethod
    def exists(
            course_id,
            academic_year_id,
            semester_id,
            division_name
    ):
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            SELECT division_id
            FROM divisions
            WHERE
                course_id=?
                AND academic_year_id=?
                AND semester_id=?
                AND division_name=?
            """,
            (
                course_id,
                academic_year_id,
                semester_id,
                division_name
            )
        )
        return cursor.fetchone() is not None
    # ==========================================================
    # EXISTS FOR UPDATE
    # ==========================================================

    @staticmethod
    def exists_for_update(
            division_id,
            course_id,
            academic_year_id,
            semester_id,
            division_name
    ):
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        cursor.execute(
            """
            SELECT division_id
            FROM divisions
            WHERE
                course_id=?
                AND academic_year_id=?
                AND semester_id=?
                AND division_name=?
                AND division_id<>?
            """,
            (
                course_id,
                academic_year_id,
                semester_id,
                division_name,
                division_id
            )
        )
        return cursor.fetchone() is not None
    