from typing import List, Optional

from app.models.student_batch_allocation import StudentBatchAllocation
from app.repositories.student_batch_allocation_repository import StudentBatchAllocationRepository


class StudentBatchAllocationService:

    @staticmethod
    def add(allocation: StudentBatchAllocation) -> int:
        return StudentBatchAllocationRepository.add(allocation)

    @staticmethod
    def update(allocation: StudentBatchAllocation) -> None:
        StudentBatchAllocationRepository.update(allocation)

    @staticmethod
    def delete(allocation_id: int) -> None:
        StudentBatchAllocationRepository.delete(allocation_id)

    @staticmethod
    def get_by_student(student_id: int) -> Optional[StudentBatchAllocation]:
        return StudentBatchAllocationRepository.get_by_student(student_id)

    @staticmethod
    def get_all() -> List[StudentBatchAllocation]:
        return StudentBatchAllocationRepository.get_all()
    