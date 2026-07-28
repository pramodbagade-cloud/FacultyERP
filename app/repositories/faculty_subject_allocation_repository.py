"""
FacultyERP
Faculty Subject Allocation Repository
-------------------------------------
"""

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
                ?,?,?,?,?,?,?,?,?,?,?,?,?
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
            WHERE allocation_id=?
            """,
            (allocation_id,)
        )
        connection.commit()

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
            WHERE allocation_id=?
            """,
            (allocation_id,)
        )
        return cursor.fetchone()

    @staticmethod
    def exists(
        faculty_id,
        subject_id,
        academic_year_id,
        division_id,
        batch_name
    ):
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT allocation_id
            FROM faculty_subject_allocations
            WHERE faculty_id=?
            AND subject_id=?
            AND academic_year_id=?
            AND division_id=?
            AND batch_name=?
            """,
            (
                faculty_id,
                subject_id,
                academic_year_id,
                division_id,
                batch_name
            )
        )

        return cursor.fetchone() is not None

    @staticmethod
    def exists_for_update(
        allocation_id,
        faculty_id,
        subject_id,
        academic_year_id,
        division_id,
        batch_name
    ):
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT allocation_id
            FROM faculty_subject_allocations
            WHERE faculty_id=?
            AND subject_id=?
            AND academic_year_id=?
            AND division_id=?
            AND batch_name=?
            AND allocation_id<>?
            """,
            (
                faculty_id,
                subject_id,
                academic_year_id,
                division_id,
                batch_name,
                allocation_id
            )
        )
        return cursor.fetchone() is not None
    
    @staticmethod
    def get_grid_data():
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT
                fsa.allocation_id,
                ay.academic_year,
                d.division_name,
                TRIM(
                    f.first_name || ' ' ||
                    COALESCE(f.middle_name || ' ', '') ||
                    f.last_name
                ) AS faculty_name,
                s.subject_code,
                s.subject_code,
                s.subject_name,
                fsa.batch_name,
                fsa.theory_hours,
                fsa.practical_hours,
                fsa.tutorial_hours,
                fsa.workload_hours,
                fsa.display_order,
                fsa.is_active
            FROM faculty_subject_allocations fsa
            INNER JOIN faculty f
                ON fsa.faculty_id=f.faculty_id
            INNER JOIN subjects s
                ON fsa.subject_id=s.subject_id
            INNER JOIN academic_years ay
                ON fsa.academic_year_id=ay.academic_year_id
            INNER JOIN divisions d
                ON fsa.division_id=d.division_id
            ORDER BY
                ay.academic_year,
                d.division_name,
                fsa.display_order,
                s.subject_code,
                faculty_name
            """
        )
        return cursor.fetchall()

    @staticmethod
    def get_by_division(academic_year_id, division_id):
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT
                fsa.*,
                f.faculty_name,
                s.subject_code,
                s.subject_name
            FROM faculty_subject_allocations fsa
            INNER JOIN faculty f
                ON fsa.faculty_id=f.faculty_id
            INNER JOIN subjects s
                ON fsa.subject_id=s.subject_id
            WHERE
                fsa.academic_year_id=?
                AND fsa.division_id=?
                AND fsa.is_active=1
            ORDER BY
                fsa.display_order,
                s.subject_code
            """,
            (
                academic_year_id,
                division_id
            )
        )
        return cursor.fetchall()

    @staticmethod
    def get_by_faculty(faculty_id):
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT
                fsa.*,
                s.subject_code,
                s.subject_name,
                d.division_name,
                ay.academic_year
            FROM faculty_subject_allocations fsa
            INNER JOIN subjects s
                ON fsa.subject_id=s.subject_id
            INNER JOIN divisions d
                ON fsa.division_id=d.division_id
            INNER JOIN academic_years ay
                ON fsa.academic_year_id=ay.academic_year_id
            WHERE
                fsa.faculty_id=?
                AND fsa.is_active=1
            ORDER BY
                ay.display_order,
                d.division_name,
                s.subject_code
            """,
            (faculty_id,)
        )
        return cursor.fetchall()

    @staticmethod
    def get_faculty_workload(faculty_id, academic_year_id):
        connection = DatabaseManager.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT
                COALESCE(SUM(workload_hours),0)
            FROM faculty_subject_allocations
            WHERE
                faculty_id=?
                AND academic_year_id=?
                AND is_active=1
            """,
            (
                faculty_id,
                academic_year_id
            )
        )
        row = cursor.fetchone()
        if row:
            return row[0]
        return 0
    