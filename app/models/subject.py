"""
FacultyERP
Subject Model
-------------
"""

from dataclasses import dataclass


@dataclass
class Subject:
    """Subject Model."""

    subject_id: int | None = None

    subject_code: str = ""

    subject_name: str = ""

    subject_short_name: str = ""

    department_id: int = 0

    course_id: int = 0

    semester: int = 1

    subject_type: str = "Theory"

    credits: int = 4

    theory_hours: int = 3

    practical_hours: int = 0

    tutorial_hours: int = 0

    description: str = ""

    is_active: int = 1

    created_at: str = ""