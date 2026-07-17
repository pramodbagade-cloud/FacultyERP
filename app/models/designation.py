"""
FacultyERP
Designation Model
-----------------
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Designation:
    """Designation Entity."""

    designation_id: Optional[int] = None

    designation_code: str = ""

    designation_name: str = ""

    description: str = ""

    is_active: int = 1

    created_at: Optional[str] = None