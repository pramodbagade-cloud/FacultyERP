"""
FacultyERP
Application Settings Repository
-------------------------------
"""

from app.core.database import DatabaseManager


class AppSettingsRepository:
    """Database operations for application settings."""

    @staticmethod
    def get_setting(setting_key):
        """Return the value of a setting."""
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT setting_value
            FROM app_settings
            WHERE setting_key = ?
            """,
            (
                setting_key,
            )
        )
        row = cursor.fetchone()
        if row:
            return row[0]
        return None

    @staticmethod
    def set_setting(setting_key, setting_value):
        """Insert or update a setting."""
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO app_settings
            (
                setting_key,
                setting_value
            )
            VALUES
            (
                ?,
                ?
            )
            ON CONFLICT(setting_key)
            DO UPDATE SET
                setting_value = excluded.setting_value
            """,
            (
                setting_key,
                setting_value
            )
        )
        connection.commit()
        