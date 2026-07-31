from typing import List, Optional


from app.core.database import DatabaseManager
from app.models.student_batch_allocation import StudentBatchAllocation


class StudentBatchAllocationRepository:

    @staticmethod
    def add(allocation: StudentBatchAllocation) -> int:
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO student_batch_allocations
            (
                student_id,
                batch_no,
                is_active
            )
            VALUES
            (
                ?, ?, ?
            )
            """,
            (
                allocation.student_id,
                allocation.batch_no,
                int(allocation.is_active)
            )
        )
        connection.commit()
        allocation_id = cursor.lastrowid
        connection.close()
        return allocation_id

    @staticmethod
    def update(allocation: StudentBatchAllocation) -> None:
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE student_batch_allocations
            SET
                batch_no=?,
                is_active=?
            WHERE allocation_id=?
            """,
            (
                allocation.batch_no,
                int(allocation.is_active),
                allocation.allocation_id
            )
        )
        connection.commit()
        connection.close()

    @staticmethod
    def delete(allocation_id: int) -> None:
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM student_batch_allocations
            WHERE allocation_id=?
            """,
            (allocation_id,)
        )
        connection.commit()
        connection.close()

    @staticmethod
    def get_by_student(student_id: int) -> Optional[StudentBatchAllocation]:
        connection = DatabaseManager.get_connection()
        connection.row_factory = DatabaseManager.dict_factory
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM student_batch_allocations
            WHERE student_id=?
            """,
            (student_id,)
        )
        row = cursor.fetchone()
        connection.close()
        if not row:
            return None
        return StudentBatchAllocation(**row)

    @staticmethod
    def get_all() -> List[StudentBatchAllocation]:
        connection = DatabaseManager.get_connection()
        connection.row_factory = DatabaseManager.dict_factory
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM student_batch_allocations
            ORDER BY batch_no, student_id
            """
        )
        rows = cursor.fetchall()
        connection.close()
        return [StudentBatchAllocation(**row) for row in rows]
    