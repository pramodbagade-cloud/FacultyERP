"""
FacultyERP
Student Model
-------------
"""

from dataclasses import dataclass


@dataclass
class Student:
    """Student Model."""

    student_id: int | None = None

    college_id: str = ""

    prn: str = ""

    roll_no: str = ""

    student_name: str = ""

    department_id: int = 0

    course_id: int = 0

    semester: int = 1

    division: str = "A"

    academic_year: str = ""

    mobile: str = ""

    email: str = ""

    is_active: int = 1

    created_at: str = ""
    