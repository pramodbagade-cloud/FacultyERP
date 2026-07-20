"""
FacultyERP
User Repository
---------------
"""

from app.core.database import DatabaseManager
from app.models.user import User


class UserRepository:
    """Handles database operations for users."""

    # ==========================================================
    # ADD USER
    # ==========================================================

    @staticmethod
    def add(user: User):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

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
                user.faculty_id,
                user.username,
                user.password_hash,
                user.role,
                user.is_active
            )
        )

        conn.commit()

        return cursor.lastrowid

    # ==========================================================
    # UPDATE USER
    # ==========================================================

    @staticmethod
    def update(user: User):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET
                faculty_id=?,
                username=?,
                role=?,
                is_active=?
            WHERE
                user_id=?
            """,
            (
                user.faculty_id,
                user.username,
                user.role,
                user.is_active,
                user.user_id
            )
        )

        conn.commit()

    # ==========================================================
    # RESET PASSWORD
    # ==========================================================

    @staticmethod
    def update_password(user_id: int, password_hash: str):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET
                password_hash=?
            WHERE
                user_id=?
            """,
            (
                password_hash,
                user_id
            )
        )

        conn.commit()

    # ==========================================================
    # DELETE USER
    # ==========================================================

    @staticmethod
    def delete(user_id: int):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM users
            WHERE user_id=?
            """,
            (user_id,)
        )

        conn.commit()

    # ==========================================================
    # GET USER BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(user_id: int):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE user_id=?
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return UserRepository._row_to_user(row)

    # ==========================================================
    # GET USER BY USERNAME
    # ==========================================================

    @staticmethod
    def get_by_username(username: str):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=?
            """,
            (username,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return UserRepository._row_to_user(row)

    # ==========================================================
    # GET USER BY FACULTY
    # ==========================================================

    @staticmethod
    def get_by_faculty_id(faculty_id: int):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE faculty_id=?
            """,
            (faculty_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return UserRepository._row_to_user(row)

    # ==========================================================
    # USERNAME EXISTS
    # ==========================================================

    @staticmethod
    def username_exists(username: str):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM users
            WHERE username=?
            """,
            (username,)
        )

        return cursor.fetchone() is not None

    # ==========================================================
    # GET ALL USERS
    # ==========================================================

    @staticmethod
    def get_all():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            ORDER BY username
            """
        )

        rows = cursor.fetchall()

        return [

            UserRepository._row_to_user(row)

            for row in rows

        ]

    # ==========================================================
    # ROW TO USER
    # ==========================================================

    @staticmethod
    def _row_to_user(row):

        return User(

            user_id=row["user_id"],

            faculty_id=row["faculty_id"],

            username=row["username"],

            password_hash=row["password_hash"],

            role=row["role"],

            is_active=row["is_active"],

            last_login=row["last_login"],

            created_at=row["created_at"]

        )