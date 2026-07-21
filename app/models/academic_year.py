"""
FacultyERP
Academic Year Model
-------------------
"""

from dataclasses import dataclass


@dataclass
class AcademicYear:
    """Academic Year Model."""

    academic_year_id: int | None = None

    academic_year: str = ""

    start_date: str = ""

    end_date: str = ""

    is_current: int = 0

    created_at: str = ""