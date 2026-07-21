"""
FacultyERP
Faculty Subject Assignment Model
--------------------------------
"""

from dataclasses import dataclass


@dataclass
class FacultySubjectAssignment:
    """Represents a faculty teaching assignment."""

    assignment_id: int | None = None

    faculty_id: int = 0

    department_id: int = 0

    course_id: int = 0

    semester: int = 1

    subject_id: int = 0

    academic_year_id: int = 0

    division_id: int = 0

    batch_name: str = "Full"

    workload_hours: float = 0.0

    remarks: str = ""

    is_active: int = 1

    created_at: str = ""
    