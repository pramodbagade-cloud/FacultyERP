"""
FacultyERP
Division Model
--------------
"""

from dataclasses import dataclass

@dataclass
class Division:
    """Division Model."""
    division_id: int | None = None
    division_name: str = ""
    course_id: int | None = None
    academic_year_id: int | None = None
    semester_id: int | None = None
    intake: int = 0
    is_active: int = 1
    created_at: str = ""