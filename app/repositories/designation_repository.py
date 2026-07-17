"""
FacultyERP
Designation Repository
----------------------
"""

from app.core.database import DatabaseManager
from app.models.designation import Designation


class DesignationRepository:
    """Database operations for Designations."""

    @staticmethod
    def add(designation: Designation):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO designations
            (
                designation_code,
                designation_name,
                description
            )

            VALUES (?,?,?)
            """,
            (
                designation.designation_code,
                designation.designation_name,
                designation.description
            )
        )

        conn.commit()

    @staticmethod
    def get_all():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM designations
            ORDER BY designation_name
            """
        )

        rows = cursor.fetchall()

        designations = []

        for row in rows:

            designations.append(

                Designation(

                    designation_id=row["designation_id"],

                    designation_code=row["designation_code"],

                    designation_name=row["designation_name"],

                    description=row["description"],

                    is_active=row["is_active"],

                    created_at=row["created_at"]

                )

            )

        return designations

    @staticmethod
    def get_by_id(designation_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM designations
            WHERE designation_id=?
            """,
            (designation_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Designation(

            designation_id=row["designation_id"],

            designation_code=row["designation_code"],

            designation_name=row["designation_name"],

            description=row["description"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )

    @staticmethod
    def update(designation: Designation):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE designations

            SET

                designation_code=?,

                designation_name=?,

                description=?

            WHERE designation_id=?
            """,
            (

                designation.designation_code,

                designation.designation_name,

                designation.description,

                designation.designation_id

            )

        )

        conn.commit()

    @staticmethod
    def delete(designation_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM designations
            WHERE designation_id=?
            """,
            (designation_id,)
        )

        conn.commit()

    @staticmethod
    def exists(code, name):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM designations

            WHERE designation_code=?

               OR designation_name=?
            """,
            (
                code,
                name
            )
        )

        return cursor.fetchone()[0] > 0
        # ==========================================================
    # NEXT DESIGNATION CODE
    # ==========================================================

    @staticmethod
    def get_next_designation_code():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT MAX(
                CAST(designation_code AS INTEGER)
            )
            FROM designations
            """

        )

        value = cursor.fetchone()[0]

        if value is None:

            return "01"

        return f"{value + 1:02d}"