"""
FacultyERP
User Model
----------
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """Represents a system user."""

    user_id: Optional[int] = None

    faculty_id: Optional[int] = None

    username: str = ""

    password_hash: str = ""

    role: str = ""

    is_active: int = 1

    last_login: Optional[str] = None

    created_at: Optional[str] = None