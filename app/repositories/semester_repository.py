"""
FacultyERP
Semester Repository
-------------------
"""

from app.core.database import DatabaseManager
from app.models.semester import Semester


class SemesterRepository:
    """Database operations for Semester."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(semester: Semester):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO semesters
            (
                semester_no,
                semester_name
            )
            VALUES
            (
                ?, ?
            )
            """,
            (
                semester.semester_no,
                semester.semester_name
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
            FROM semesters
            ORDER BY semester_no
            """
        )

        rows = cursor.fetchall()

        semesters = []

        for row in rows:

            semesters.append(

                Semester(

                    semester_id=row["semester_id"],

                    semester_no=row["semester_no"],

                    semester_name=row["semester_name"],

                    created_at=row["created_at"]

                )

            )

        return semesters

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(semester_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM semesters
            WHERE semester_id=?
            """,
            (semester_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return Semester(

            semester_id=row["semester_id"],

            semester_no=row["semester_no"],

            semester_name=row["semester_name"],

            created_at=row["created_at"]

        )

    # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(semester: Semester):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE semesters
            SET
                semester_no=?,
                semester_name=?
            WHERE semester_id=?
            """,
            (
                semester.semester_no,
                semester.semester_name,
                semester.semester_id
            )
        )

        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(semester_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM semesters
            WHERE semester_id=?
            """,
            (semester_id,)
        )

        conn.commit()

    # ==========================================================
    # EXISTS
    # ==========================================================

    @staticmethod
    def exists(semester_no):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT semester_id
            FROM semesters
            WHERE semester_no=?
            """,
            (semester_no,)
        )

        return cursor.fetchone() is not None

    # ==========================================================
    # GET NEXT SEMESTER NUMBER
    # ==========================================================
    @staticmethod
    def get_next_semester_number():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT semester_no
            FROM semesters
            ORDER BY semester_no
            """
        )

        existing = {

            row["semester_no"]

            for row in cursor.fetchall()

        }

        for semester_no in range(1, 9):

            if semester_no not in existing:

                return semester_no

        return None
    # ==========================================================
    # EXISTS FOR UPDATE
    # ==========================================================
    @staticmethod
    def exists_for_update(semester_no, semester_id):
        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT semester_id
            FROM semesters
            WHERE semester_no=?
            AND semester_id<>?
            """,
            (
                semester_no,
                semester_id
            )
        )
        return cursor.fetchone() is not None

        
    