"""
FacultyERP
Faculty Subject Assignment Repository
-------------------------------------
"""

import sqlite3

from app.core.database import DatabaseManager
from app.models.faculty_subject_assignment import FacultySubjectAssignment


class FacultySubjectAssignmentRepository:
    """Database operations for Faculty Subject Assignments."""

    # ==========================================================
    # ADD ASSIGNMENT
    # ==========================================================

    @staticmethod
    def add(assignment: FacultySubjectAssignment):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO faculty_subject_assignments
            (
                faculty_id,
                department_id,
                course_id,
                semester,
                subject_id,
                academic_year_id,
                division_id,
                batch_name,
                workload_hours,
                remarks,
                is_active
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                assignment.faculty_id,
                assignment.department_id,
                assignment.course_id,
                assignment.semester,
                assignment.subject_id,
                assignment.academic_year_id,
                assignment.division_id,
                assignment.batch_name,
                assignment.workload_hours,
                assignment.remarks,
                assignment.is_active
            )
        )

        connection.commit()

        assignment_id = cursor.lastrowid

        connection.close()

        return assignment_id

    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_all():

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                fsa.assignment_id,

                f.faculty_code,

                f.first_name || ' ' || f.last_name AS faculty_name,

                d.department_name,

                c.course_name,

                fsa.semester,

                s.subject_code,

                s.subject_name,

                ay.academic_year,

                dv.division_name,

                fsa.batch_name,

                fsa.workload_hours,

                fsa.is_active

            FROM faculty_subject_assignments fsa

            INNER JOIN faculty f

                ON fsa.faculty_id = f.faculty_id

            INNER JOIN departments d

                ON fsa.department_id = d.department_id

            INNER JOIN courses c

                ON fsa.course_id = c.course_id

            INNER JOIN subjects s

                ON fsa.subject_id = s.subject_id

            INNER JOIN academic_years ay

                ON fsa.academic_year_id = ay.academic_year_id

            INNER JOIN divisions dv

                ON fsa.division_id = dv.division_id

            ORDER BY

                d.department_name,

                c.course_name,

                fsa.semester,

                faculty_name
            """
        )

        rows = cursor.fetchall()

        connection.close()

        return rows
    
    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(assignment_id):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM faculty_subject_assignments
            WHERE assignment_id=?
            """,
            (assignment_id,)
        )

        row = cursor.fetchone()

        connection.close()

        return row
        # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(assignment: FacultySubjectAssignment):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE faculty_subject_assignments
            SET
                faculty_id=?,
                department_id=?,
                course_id=?,
                semester=?,
                subject_id=?,
                academic_year_id=?,
                division_id=?,
                batch_name=?,
                workload_hours=?,
                remarks=?,
                is_active=?
            WHERE assignment_id=?
            """,
            (
                assignment.faculty_id,
                assignment.department_id,
                assignment.course_id,
                assignment.semester,
                assignment.subject_id,
                assignment.academic_year_id,
                assignment.division_id,
                assignment.batch_name,
                assignment.workload_hours,
                assignment.remarks,
                assignment.is_active,
                assignment.assignment_id
            )
        )

        connection.commit()

        connection.close()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(assignment_id):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM faculty_subject_assignments
            WHERE assignment_id=?
            """,
            (assignment_id,)
        )

        connection.commit()

        connection.close()

    # ==========================================================
    # EXISTS
    # ==========================================================

    @staticmethod
    def exists(
            faculty_id,
            subject_id,
            academic_year_id,
            division_id,
            batch_name):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT assignment_id
            FROM faculty_subject_assignments
            WHERE
                faculty_id=?
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

        exists = cursor.fetchone() is not None

        connection.close()

        return exists

    # ==========================================================
    # EXISTS EXCEPT
    # ==========================================================

    @staticmethod
    def exists_except(
            assignment_id,
            faculty_id,
            subject_id,
            academic_year_id,
            division_id,
            batch_name):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT assignment_id
            FROM faculty_subject_assignments
            WHERE
                faculty_id=?
                AND subject_id=?
                AND academic_year_id=?
                AND division_id=?
                AND batch_name=?
                AND assignment_id<>?
            """,
            (
                faculty_id,
                subject_id,
                academic_year_id,
                division_id,
                batch_name,
                assignment_id
            )
        )

        exists = cursor.fetchone() is not None

        connection.close()

        return exists

    # ==========================================================
    # GET BY FACULTY
    # ==========================================================

    @staticmethod
    def get_by_faculty(faculty_id):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM faculty_subject_assignments
            WHERE faculty_id=?
            ORDER BY semester, subject_id
            """,
            (faculty_id,)
        )

        rows = cursor.fetchall()

        connection.close()

        return rows

    # ==========================================================
    # GET BY SUBJECT
    # ==========================================================

    @staticmethod
    def get_by_subject(subject_id):

        connection = DatabaseManager.get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM faculty_subject_assignments
            WHERE subject_id=?
            ORDER BY faculty_id
            """,
            (subject_id,)
        )

        rows = cursor.fetchall()

        connection.close()

        return rows
    