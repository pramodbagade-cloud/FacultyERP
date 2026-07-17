"""
FacultyERP
User Repository
---------------
"""

from app.core.database import DatabaseManager
from app.models.user import User


class UserRepository:
    """Handles database operations for users."""

    @staticmethod
    def get_by_username(username: str):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        row = cursor.fetchone()

        if row is None:
            return None


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