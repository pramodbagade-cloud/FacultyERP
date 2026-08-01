"""
FacultyERP
Subject Repository
------------------
"""

from app.core.database import DatabaseManager
from app.models.subject import Subject


class SubjectRepository:
    """Database operations for Subject."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(subject: Subject):

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO subjects
            (
                subject_code,
                university_subject_code,
                subject_name,
                subject_short_name,
                department_id,
                course_id,
                semester_id,
                subject_type,
                credits,
                theory_hours,
                practical_hours,
                tutorial_hours,
                description
            )

            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,?,?,?
            )
            """,
            (
                subject.subject_code,
                subject.university_subject_code,
                subject.subject_name,
                subject.subject_short_name,
                subject.department_id,
                subject.course_id,
                subject.semester_id,
                subject.subject_type,
                subject.credits,
                subject.theory_hours,
                subject.practical_hours,
                subject.tutorial_hours,
                subject.description
            )
        )

        conn.commit()
    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_all():

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM subjects
            ORDER BY
                department_id,
                course_id,
                semester_id,
                subject_name
            """
        )

        rows = cursor.fetchall()
        

        subjects = []

        for row in rows:

            subjects.append(
                Subject(
                    subject_id=row["subject_id"],
                    subject_code=row["subject_code"],
                    university_subject_code=row["university_subject_code"],
                    subject_name=row["subject_name"],
                    subject_short_name=row["subject_short_name"],
                    department_id=row["department_id"],
                    course_id=row["course_id"],
                    semester_id=row["semester_id"],
                    subject_type=row["subject_type"],
                    credits=row["credits"],
                    theory_hours=row["theory_hours"],
                    practical_hours=row["practical_hours"],
                    tutorial_hours=row["tutorial_hours"],
                    description=row["description"],
                    is_active=row["is_active"],
                    created_at=row["created_at"],
                )
            )

        return subjects
    # ==========================================================
    # GET BY COURSE & SEMESTER
    # ==========================================================

    @staticmethod
    def get_by_course_semester(
            course_id,
            semester_id
    ):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *

            FROM subjects

            WHERE

                course_id=?

                AND

                semester_id=?

                AND

                is_active=1

            ORDER BY subject_name
            """,
            (
                course_id,
                semester_id
            )
        )

        rows = cursor.fetchall()
        print("Subjects Found :", len(rows))
        subjects = []

        for row in rows:

            subjects.append(

                Subject(

                    subject_id=row["subject_id"],

                    subject_code=row["subject_code"],
                    university_subject_code=row["university_subject_code"],

                    subject_name=row["subject_name"],

                    subject_short_name=row["subject_short_name"],

                    department_id=row["department_id"],

                    course_id=row["course_id"],

                    semester_id=row["semester_id"],

                    subject_type=row["subject_type"],

                    credits=row["credits"],

                    theory_hours=row["theory_hours"],

                    practical_hours=row["practical_hours"],

                    tutorial_hours=row["tutorial_hours"],

                    description=row["description"],

                    is_active=row["is_active"],

                    created_at=row["created_at"]

                )

            )

        return subjects

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(subject_id):

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM subjects
            WHERE subject_id=?
            """,
            (subject_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Subject(
            subject_id=row["subject_id"],
            subject_code=row["subject_code"],
            university_subject_code=row["university_subject_code"],
            subject_name=row["subject_name"],
            subject_short_name=row["subject_short_name"],
            department_id=row["department_id"],
            course_id=row["course_id"],
            semester_id=row["semester_id"],
            subject_type=row["subject_type"],
            credits=row["credits"],
            theory_hours=row["theory_hours"],
            practical_hours=row["practical_hours"],
            tutorial_hours=row["tutorial_hours"],
            description=row["description"],
            is_active=row["is_active"],
            created_at=row["created_at"],
        )
        # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(subject: Subject):

        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE subjects

            SET

                subject_code=?,
                university_subject_code=?,

                subject_name=?,

                subject_short_name=?,

                department_id=?,

                course_id=?,

                semester_id=?,

                subject_type=?,

                credits=?,

                theory_hours=?,

                practical_hours=?,

                tutorial_hours=?,

                description=?,

                is_active=?

            WHERE subject_id=?
            """,

            (

                subject.subject_code,
                subject.university_subject_code,

                subject.subject_name,

                subject.subject_short_name,

                subject.department_id,

                subject.course_id,

                subject.semester_id,

                subject.subject_type,

                subject.credits,

                subject.theory_hours,

                subject.practical_hours,

                subject.tutorial_hours,

                subject.description,

                subject.is_active,

                subject.subject_id

            )

        )

        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(subject_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            DELETE FROM subjects

            WHERE subject_id=?
            """,

            (subject_id,)

        )

        conn.commit()

    # ==========================================================
    # EXISTS
    # ==========================================================

    @staticmethod
    def exists(
            subject_code,
            subject_name,
            department_id,
            course_id,
            semester_id
    ):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT COUNT(*)

            FROM subjects

            WHERE subject_code=?

               OR
               (

                    subject_name=?

                    AND department_id=?

                    AND course_id=?

                    AND semester_id=?

               )
            """,

            (

                subject_code,

                subject_name,

                department_id,

                course_id,

                semester_id

            )

        )

        return cursor.fetchone()[0] > 0

    # ==========================================================
    # GENERATE SUBJECT CODE
    # ==========================================================

    @staticmethod
    def generate_subject_code():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT MAX(subject_id)

            FROM subjects
            """

        )

        last_id = cursor.fetchone()[0]

        if last_id is None:

            next_id = 1

        else:

            next_id = last_id + 1

        return f"SUB{next_id:04d}"
    