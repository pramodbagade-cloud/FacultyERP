"""
FacultyERP
Department Model
----------------
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Department:
    """Department entity."""

    department_id: Optional[int] = None

    department_code: str = ""

    department_name: str = ""

    hod_name: str = ""

    description: str = ""

    is_active: int = 1

    created_at: Optional[str] = None