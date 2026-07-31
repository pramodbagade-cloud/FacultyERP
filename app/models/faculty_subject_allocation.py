"""
FacultyERP
Faculty Subject Allocation Model
--------------------------------
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class FacultySubjectAllocation:
    allocation_id: Optional[int] = None
    faculty_id: int = 0
    subject_id: int = 0
    academic_year_id: int = 0
    division_id: int = 0
    batch_name: str = "Full"
    theory_hours: float = 0.0
    practical_hours: float = 0.0
    tutorial_hours: float = 0.0
    workload_hours: float = 0.0
    is_class_teacher: int = 0
    display_order: int = 1
    remarks: str = ""
    is_active: int = 1
    created_at: Optional[str] = None
    