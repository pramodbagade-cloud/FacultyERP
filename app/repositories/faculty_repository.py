"""
FacultyERP
Faculty Repository
------------------
"""

from app.core.database import DatabaseManager
from app.models.faculty import Faculty


class FacultyRepository:
    """Database operations for Faculty."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add(faculty: Faculty):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO faculty
            (
                faculty_code,
                employee_code,
                first_name,
                middle_name,
                last_name,
                gender,
                date_of_birth,
                mobile,
                email,
                address,
                department_id,
                designation,
                joining_date,
                employment_type,
                qualification,
                specialization,
                experience,
                research_area,
                orcid_id,
                google_scholar_id,
                scopus_author_id,
                vidwan_id,
                aicte_id,
                university_approved,
                photo,
                remarks
            )

            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?
            )
            """,

            (

                faculty.faculty_code,

                faculty.employee_code,

                faculty.first_name,

                faculty.middle_name,

                faculty.last_name,

                faculty.gender,

                faculty.date_of_birth,

                faculty.mobile,

                faculty.email,

                faculty.address,

                faculty.department_id,

                faculty.designation,

                faculty.joining_date,

                faculty.employment_type,

                faculty.qualification,

                faculty.specialization,

                faculty.experience,

                faculty.research_area,

                faculty.orcid_id,

                faculty.google_scholar_id,

                faculty.scopus_author_id,

                faculty.vidwan_id,

                faculty.aicte_id,

                faculty.university_approved,

                faculty.photo,

                faculty.remarks

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
            FROM faculty
            ORDER BY first_name, last_name
            """
        )

        rows = cursor.fetchall()

        faculty_list = []

        for row in rows:

            faculty_list.append(

                Faculty(

                    faculty_id=row["faculty_id"],

                    faculty_code=row["faculty_code"],

                    employee_code=row["employee_code"],

                    first_name=row["first_name"],

                    middle_name=row["middle_name"],

                    last_name=row["last_name"],

                    gender=row["gender"],

                    date_of_birth=row["date_of_birth"],

                    mobile=row["mobile"],

                    email=row["email"],

                    address=row["address"],

                    department_id=row["department_id"],

                    designation=row["designation"],

                    joining_date=row["joining_date"],

                    employment_type=row["employment_type"],

                    qualification=row["qualification"],

                    specialization=row["specialization"],

                    experience=row["experience"],

                    research_area=row["research_area"],

                    orcid_id=row["orcid_id"],

                    google_scholar_id=row["google_scholar_id"],

                    scopus_author_id=row["scopus_author_id"],

                    vidwan_id=row["vidwan_id"],

                    aicte_id=row["aicte_id"],

                    university_approved=row["university_approved"],

                    photo=row["photo"],

                    remarks=row["remarks"],

                    is_active=row["is_active"],

                    created_at=row["created_at"]

                )

            )

        return faculty_list
        # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_by_id(faculty_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM faculty
            WHERE faculty_id=?
            """,
            (faculty_id,)
        )

        row = cursor.fetchone()

        if row is None:

            return None

        return Faculty(

            faculty_id=row["faculty_id"],

            faculty_code=row["faculty_code"],

            employee_code=row["employee_code"],

            first_name=row["first_name"],

            middle_name=row["middle_name"],

            last_name=row["last_name"],

            gender=row["gender"],

            date_of_birth=row["date_of_birth"],

            mobile=row["mobile"],

            email=row["email"],

            address=row["address"],

            department_id=row["department_id"],

            designation=row["designation"],

            joining_date=row["joining_date"],

            employment_type=row["employment_type"],

            qualification=row["qualification"],

            specialization=row["specialization"],

            experience=row["experience"],

            research_area=row["research_area"],

            orcid_id=row["orcid_id"],

            google_scholar_id=row["google_scholar_id"],

            scopus_author_id=row["scopus_author_id"],

            vidwan_id=row["vidwan_id"],

            aicte_id=row["aicte_id"],

            university_approved=row["university_approved"],

            photo=row["photo"],

            remarks=row["remarks"],

            is_active=row["is_active"],

            created_at=row["created_at"]

        )
        # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update(faculty: Faculty):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE faculty
            SET
                employee_code=?,
                first_name=?,
                middle_name=?,
                last_name=?,
                gender=?,
                date_of_birth=?,
                mobile=?,
                email=?,
                address=?,
                department_id=?,
                designation=?,
                joining_date=?,
                employment_type=?,
                qualification=?,
                specialization=?,
                experience=?,
                research_area=?,
                orcid_id=?,
                google_scholar_id=?,
                scopus_author_id=?,
                vidwan_id=?,
                aicte_id=?,
                university_approved=?,
                photo=?,
                remarks=?,
                is_active=?
            WHERE faculty_id=?
            """,
            (
                faculty.employee_code,
                faculty.first_name,
                faculty.middle_name,
                faculty.last_name,
                faculty.gender,
                faculty.date_of_birth,
                faculty.mobile,
                faculty.email,
                faculty.address,
                faculty.department_id,
                faculty.designation,
                faculty.joining_date,
                faculty.employment_type,
                faculty.qualification,
                faculty.specialization,
                faculty.experience,
                faculty.research_area,
                faculty.orcid_id,
                faculty.google_scholar_id,
                faculty.scopus_author_id,
                faculty.vidwan_id,
                faculty.aicte_id,
                faculty.university_approved,
                faculty.photo,
                faculty.remarks,
                faculty.is_active,
                faculty.faculty_id
            )
        )

        conn.commit()

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete(faculty_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM faculty
            WHERE faculty_id=?
            """,
            (faculty_id,)
        )

        conn.commit()

    # ==========================================================
    # EXISTS
    # ==========================================================

    @staticmethod
    def exists(employee_code):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM faculty
            WHERE employee_code=?
            """,
            (employee_code,)
        )

        return cursor.fetchone()[0] > 0

    # ==========================================================
    # GENERATE FACULTY CODE
    # ==========================================================

    @staticmethod
    def generate_faculty_code():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT MAX(faculty_id)
            FROM faculty
            """
        )

        last_id = cursor.fetchone()[0]

        if last_id is None:

            next_id = 1

        else:

            next_id = last_id + 1

        return f"FAC{next_id:04d}"
    