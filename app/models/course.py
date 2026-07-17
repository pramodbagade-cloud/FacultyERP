"""
FacultyERP
Course Model
------------
"""

from dataclasses import dataclass


@dataclass
class Course:
    """Course Model."""

    course_id: int | None = None

    course_code: str = ""

    course_name: str = ""

    course_short_name: str = ""

    degree: str = "BE"

    pattern: str = "2024 Pattern"

    duration_years: int = 4

    intake: int = 0

    department_id: int = 0

    description: str = ""

    is_active: int = 1

    created_at: str = ""