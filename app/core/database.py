"""
FacultyERP
Database Manager
----------------

Handles SQLite database connection and initialization.
"""

import sqlite3

from app.core.config import AppConfig
from app.core.schema import DatabaseSchema


class DatabaseManager:
    """Database connection manager."""

    _connection = None

    @classmethod
    def initialize(cls):
        """Initialize the SQLite database."""

        AppConfig.DATABASE_DIR.mkdir(exist_ok=True)

        cls._connection = sqlite3.connect(AppConfig.DATABASE_FILE)

        print("DATABASE =", AppConfig.DATABASE_FILE.resolve())

        cls._connection.row_factory = sqlite3.Row

        DatabaseSchema.create(cls._connection)

        cls.run_migrations()

    @classmethod
    def get_connection(cls):
        """Return the active database connection."""

        return cls._connection

    @classmethod
    def run_migrations(cls):
        """Run all database schema migrations."""

        conn = cls._connection
        cursor = conn.cursor()

        # ==========================================================
        # Migration 001
        # Add University Subject Code
        # ==========================================================

        cursor.execute(
            "PRAGMA table_info(subjects)"
        )

        columns = [
            row["name"]
            for row in cursor.fetchall()
        ]

        if "university_subject_code" not in columns:

            cursor.execute(
                """
                ALTER TABLE subjects
                ADD COLUMN university_subject_code TEXT
                """
            )

            print(
                "Migration 001 Applied : university_subject_code added."
            )

        conn.commit()