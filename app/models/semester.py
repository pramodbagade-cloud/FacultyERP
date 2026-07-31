"""
FacultyERP
Semester Model
--------------
"""
from dataclasses import dataclass
@dataclass
class Semester:
    """Semester Model."""
    semester_id: int | None = None
    semester_no: int = 1
    semester_name: str = ""
    created_at: str = ""