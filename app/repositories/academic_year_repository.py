"""
FacultyERP
Academic Year Repository
------------------------
"""

from app.core.database import DatabaseManager
from app.models.academic_year import AcademicYear


class AcademicYearRepository:
    """Database operations for Academic Years."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(academic_year: AcademicYear):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        if academic_year.is_current:

            cursor.execute(
                """
                UPDATE academic_years
                SET is_current=0
                """
            )

        cursor.execute(
            """
            INSERT INTO academic_years
            (
                academic_year,
                start_date,
                end_date,
                is_current
            )
            VALUES
            (
                ?, ?, ?, ?
            )
            """,
            (
                academic_year.academic_year,
                academic_year.start_date,
                academic_year.end_date,
                academic_year.is_current
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
            FROM academic_years
            ORDER BY start_date DESC,
                     academic_year DESC
            """
        )

        rows = cursor.fetchall()

        academic_years = []

        for row in rows:

            academic_years.append(

                AcademicYear(

                    academic_year_id=row["academic_year_id"],

                    academic_year=row["academic_year"],

                    start_date=row["start_date"],

                    end_date=row["end_date"],

                    is_current=row["is_current"],

                    created_at=row["created_at"]

                )

            )

        return academic_years

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(academic_year_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM academic_years
            WHERE academic_year_id=?
            """,
            (
                academic_year_id,
            )
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return AcademicYear(

            academic_year_id=row["academic_year_id"],

            academic_year=row["academic_year"],

            start_date=row["start_date"],

            end_date=row["end_date"],

            is_current=row["is_current"],

            created_at=row["created_at"]

        )

    # ==========================================================
    # GET BY NAME
    # ==========================================================

    @staticmethod
    def get_by_name(academic_year_name):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM academic_years
            WHERE academic_year=?
            """,
            (
                academic_year_name,
            )
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return AcademicYear(

            academic_year_id=row["academic_year_id"],

            academic_year=row["academic_year"],

            start_date=row["start_date"],

            end_date=row["end_date"],

            is_current=row["is_current"],

            created_at=row["created_at"]

        )

    # ==========================================================
    # GET CURRENT
    # ==========================================================

    @staticmethod
    def get_current():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM academic_years
            WHERE is_current=1
            LIMIT 1
            """
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return AcademicYear(

            academic_year_id=row["academic_year_id"],

            academic_year=row["academic_year"],

            start_date=row["start_date"],

            end_date=row["end_date"],

            is_current=row["is_current"],

            created_at=row["created_at"]

        )

    # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(academic_year: AcademicYear):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        if academic_year.is_current:

            cursor.execute(
                """
                UPDATE academic_years
                SET is_current=0
                """
            )

        cursor.execute(
            """
            UPDATE academic_years
            SET
                academic_year=?,
                start_date=?,
                end_date=?,
                is_current=?
            WHERE
                academic_year_id=?
            """,
            (
                academic_year.academic_year,
                academic_year.start_date,
                academic_year.end_date,
                academic_year.is_current,
                academic_year.academic_year_id
            )
        )

        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(academic_year_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT is_current
            FROM academic_years
            WHERE academic_year_id=?
            """,
            (
                academic_year_id,
            )
        )

        row = cursor.fetchone()

        if row and row["is_current"] == 1:

            raise ValueError(
                "Cannot delete the current Academic Year."
            )

        cursor.execute(
            """
            DELETE FROM academic_years
            WHERE academic_year_id=?
            """,
            (
                academic_year_id,
            )
        )

        conn.commit()