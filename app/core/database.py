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

        #print("DATABASE FILE =", AppConfig.DATABASE_FILE)

        cls._connection = sqlite3.connect(AppConfig.DATABASE_FILE)
        print("DATABASE =", AppConfig.DATABASE_FILE.resolve())
        cls._connection.row_factory = sqlite3.Row

        DatabaseSchema.create(cls._connection)

    @classmethod
    def get_connection(cls):
        """Return the active database connection."""

        return cls._connection