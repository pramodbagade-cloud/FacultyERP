"""
FacultyERP
Faculty Subject Allocation Repository
-------------------------------------
"""

#from app.database.database import DatabaseManager
from app.core.database import DatabaseManager
from app.models.faculty_subject_allocation import FacultySubjectAllocation


class FacultySubjectAllocationRepository:
    """Repository for Faculty Subject Allocation."""

    @staticmethod
    def add(allocation: FacultySubjectAllocation):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO faculty_subject_allocations
            (
                faculty_id,
                subject_id,
                academic_year_id,
                division_id,
                batch_name,
                theory_hours,
                practical_hours,
                tutorial_hours,
                workload_hours,
                is_class_teacher,
                display_order,
                remarks,
                is_active
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                allocation.faculty_id,
                allocation.subject_id,
                allocation.academic_year_id,
                allocation.division_id,
                allocation.batch_name,
                allocation.theory_hours,
                allocation.practical_hours,
                allocation.tutorial_hours,
                allocation.workload_hours,
                allocation.is_class_teacher,
                allocation.display_order,
                allocation.remarks,
                allocation.is_active
            )
        )

        connection.commit()

        return cursor.lastrowid

    @staticmethod
    def get_all():

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM faculty_subject_allocations
            ORDER BY
                display_order,
                subject_id
            """
        )

        return cursor.fetchall()

    @staticmethod
    def get_by_id(allocation_id):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM faculty_subject_allocations
            WHERE allocation_id = ?
            """,
            (allocation_id,)
        )

        return cursor.fetchone()

    @staticmethod
    def update(allocation: FacultySubjectAllocation):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE faculty_subject_allocations
            SET
                faculty_id=?,
                subject_id=?,
                academic_year_id=?,
                division_id=?,
                batch_name=?,
                theory_hours=?,
                practical_hours=?,
                tutorial_hours=?,
                workload_hours=?,
                is_class_teacher=?,
                display_order=?,
                remarks=?,
                is_active=?
            WHERE allocation_id=?
            """,
            (
                allocation.faculty_id,
                allocation.subject_id,
                allocation.academic_year_id,
                allocation.division_id,
                allocation.batch_name,
                allocation.theory_hours,
                allocation.practical_hours,
                allocation.tutorial_hours,
                allocation.workload_hours,
                allocation.is_class_teacher,
                allocation.display_order,
                allocation.remarks,
                allocation.is_active,
                allocation.allocation_id
            )
        )

        connection.commit()

    @staticmethod
    def delete(allocation_id):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM faculty_subject_allocations
            WHERE allocation_id = ?
            """,
            (allocation_id,)
        )

        connection.commit()
