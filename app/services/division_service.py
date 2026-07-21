"""
FacultyERP
Division Service
----------------
"""

from app.models.division import Division
from app.repositories.division_repository import DivisionRepository


class DivisionService:
    """Business logic for Division."""

    # ==========================================================
    # ADD
    # ==========================================================

    @staticmethod
    def add_division(
            division_code,
            division_name,
            course_id,
            academic_year_id,
            semester_id,
            intake,
            is_active=1
    ):

        division_code = division_code.strip().upper()

        division_name = division_name.strip()

        if division_code == "":
            raise ValueError("Division Code is required.")

        if division_name == "":
            raise ValueError("Division Name is required.")

        if course_id is None:
            raise ValueError("Please select Course.")

        if academic_year_id is None:
            raise ValueError("Please select Academic Year.")

        if semester_id is None:
            raise ValueError("Please select Semester.")

        if intake <= 0:
            raise ValueError("Intake must be greater than zero.")

        if DivisionRepository.exists(
                course_id,
                academic_year_id,
                semester_id,
                division_code
        ):
            raise ValueError("Division already exists.")

        division = Division(
            division_code=division_code,
            division_name=division_name,
            course_id=course_id,
            academic_year_id=academic_year_id,
            semester_id=semester_id,
            intake=intake,
            is_active=is_active
        )

        DivisionRepository.add(division)

    # ==========================================================
    # UPDATE
    # ==========================================================

    @staticmethod
    def update_division(
            division_id,
            division_code,
            division_name,
            course_id,
            academic_year_id,
            semester_id,
            intake,
            is_active
    ):

        division_code = division_code.strip().upper()

        division_name = division_name.strip()

        if division_code == "":
            raise ValueError("Division Code is required.")

        if division_name == "":
            raise ValueError("Division Name is required.")

        if course_id is None:
            raise ValueError("Please select Course.")

        if academic_year_id is None:
            raise ValueError("Please select Academic Year.")

        if semester_id is None:
            raise ValueError("Please select Semester.")

        if intake <= 0:
            raise ValueError("Intake must be greater than zero.")

        division = Division(
            division_id=division_id,
            division_code=division_code,
            division_name=division_name,
            course_id=course_id,
            academic_year_id=academic_year_id,
            semester_id=semester_id,
            intake=intake,
            is_active=is_active
        )

        DivisionRepository.update(division)

    # ==========================================================
    # DELETE
    # ==========================================================

    @staticmethod
    def delete_division(division_id):

        DivisionRepository.delete(division_id)

    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_all_divisions():

        return DivisionRepository.get_all()

    # ==========================================================
    # GET BY ID
    # ==========================================================

    @staticmethod
    def get_division_by_id(division_id):

        return DivisionRepository.get_by_id(division_id)
    