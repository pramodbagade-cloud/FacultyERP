"""
FacultyERP
Department Service
------------------
"""

from app.models.department import Department
from app.repositories.department_repository import DepartmentRepository


class DepartmentService:
    """Business logic for Department."""

    # ==========================================================
    # ADD DEPARTMENT
    # ==========================================================

    @staticmethod
    def add_department(

            code,

            name,

            hod,

            description

    ):

        code = code.strip().upper()

        name = name.strip()

        hod = hod.strip()

        description = description.strip()

        if code == "":
            return False, "Department Code is required."

        if name == "":
            return False, "Department Name is required."

        if DepartmentRepository.exists(code, name):

            return False, "Department already exists."

        department = Department(

            department_code=code,

            department_name=name,

            hod_name=hod,

            description=description

        )

        DepartmentRepository.add(department)

        return True, "Department added successfully."

    # ==========================================================
    # GET ALL DEPARTMENTS
    # ==========================================================

    @staticmethod
    def get_departments():

        return DepartmentRepository.get_all()

    # ==========================================================
    # GET DEPARTMENT BY ID
    # ==========================================================

    @staticmethod
    def get_department(department_id):

        return DepartmentRepository.get_by_id(department_id)

    # ==========================================================
    # UPDATE DEPARTMENT
    # ==========================================================

    @staticmethod
    def update_department(

            department_id,

            code,

            name,

            hod,

            description

    ):

        department = Department(

            department_id=department_id,

            department_code=code.strip().upper(),

            department_name=name.strip(),

            hod_name=hod.strip(),

            description=description.strip()

        )

        DepartmentRepository.update(department)

        return True, "Department updated successfully."

    # ==========================================================
    # DELETE DEPARTMENT
    # ==========================================================

    @staticmethod
    def delete_department(department_id):

        DepartmentRepository.delete(department_id)

        return True, "Department deleted successfully."

    # ==========================================================
    # GET DEPARTMENT BY NAME
    # ==========================================================

    @staticmethod
    def get_department_by_name(name):

        departments = DepartmentRepository.get_all()

        for department in departments:

            if department.department_name == name:

                return department

        return None
        # ==========================================================
    # NEXT DEPARTMENT CODE
    # ==========================================================

    @staticmethod
    def get_next_department_code():

        return DepartmentRepository.get_next_department_code()