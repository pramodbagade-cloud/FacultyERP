"""
FacultyERP
Department Repository
---------------------
"""

from app.core.database import DatabaseManager
from app.models.department import Department


class DepartmentRepository:
    """Database operations for Department."""

    @staticmethod
    def add(department: Department):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO departments
            (
                department_code,
                department_name,
                hod_name,
                description
            )

            VALUES (?,?,?,?)
            """,
            (
                department.department_code,
                department.department_name,
                department.hod_name,
                department.description
            )
        )

        conn.commit()

    @staticmethod
    def get_all():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM departments
            ORDER BY department_name
            """
        )

        rows = cursor.fetchall()

        departments = []

        for row in rows:

            departments.append(

                Department(

                    department_id=row["department_id"],
                    department_code=row["department_code"],
                    department_name=row["department_name"],
                    hod_name=row["hod_name"],
                    description=row["description"],
                    is_active=row["is_active"],
                    created_at=row["created_at"]

                )

            )

        return departments

    @staticmethod
    def get_by_id(department_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM departments
            WHERE department_id=?
            """,
            (department_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Department(

            department_id=row["department_id"],
            department_code=row["department_code"],
            department_name=row["department_name"],
            hod_name=row["hod_name"],
            description=row["description"],
            is_active=row["is_active"],
            created_at=row["created_at"]

        )

    @staticmethod
    def update(department: Department):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE departments

            SET

                department_code=?,

                department_name=?,

                hod_name=?,

                description=?

            WHERE department_id=?
            """,

            (

                department.department_code,

                department.department_name,

                department.hod_name,

                department.description,

                department.department_id

            )

        )

        conn.commit()

    @staticmethod
    def delete(department_id):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            DELETE FROM departments
            WHERE department_id=?
            """,

            (department_id,)

        )

        conn.commit()

    @staticmethod
    def exists(code, name):

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM departments

            WHERE department_code=?

               OR department_name=?
            """,

            (

                code,

                name

            )

        )

        return cursor.fetchone()[0] > 0
    
        # ==========================================================
    # NEXT DEPARTMENT CODE
    # ==========================================================

    @staticmethod
    def get_next_department_code():

        conn = DatabaseManager.get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """

            SELECT MAX(

                CAST(department_code AS INTEGER)

            )

            FROM departments

            """

        )

        value = cursor.fetchone()[0]

        if value is None:

            return "01"

        return f"{value + 1:02d}"
    # ==========================================================
    # GET BY NAME
    # ==========================================================
    @staticmethod
    def get_by_name(department_name):
        conn=DatabaseManager.get_connection()
        cursor=conn.cursor()
        value=department_name.strip()
        cursor.execute(
            """
            SELECT *
            FROM departments
            WHERE UPPER(TRIM(department_name))=UPPER(TRIM(?))
            OR UPPER(TRIM(department_code))=UPPER(TRIM(?))
            """,
            (value,value)
        )
        row=cursor.fetchone()
        if row is None:
            return None
        return Department(
            department_id=row["department_id"],
            department_code=row["department_code"],
            department_name=row["department_name"],
            hod_name=row["hod_name"],
            description=row["description"],
            is_active=row["is_active"],
            created_at=row["created_at"]
        )
    # ==========================================================
    # GET ID BY NAME
    # ==========================================================

    @staticmethod
    def get_id_by_name(department_name):

        department = DepartmentRepository.get_by_name(department_name)

        if department is None:

            return None

        return department.department_id

    # ==========================================================
    # EXISTS BY NAME
    # ==========================================================

    @staticmethod
    def exists_by_name(department_name):

        return DepartmentRepository.get_by_name(department_name) is not None