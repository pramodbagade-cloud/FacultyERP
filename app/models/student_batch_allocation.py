from dataclasses import dataclass
from typing import Optional

@dataclass
class StudentBatchAllocation:
    allocation_id: Optional[int] = None
    student_id: Optional[int] = None
    batch_no: int = 1
    is_active: bool = True
    created_at: Optional[str] = None