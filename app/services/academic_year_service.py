"""
FacultyERP
Academic Year Service
---------------------
"""

from app.models.academic_year import AcademicYear

from app.repositories.academic_year_repository import AcademicYearRepository


class AcademicYearService:
    """Business logic for Academic Years."""

    # ==========================================================
    # GET ALL ACADEMIC YEARS
    # ==========================================================

    @staticmethod
    def get_academic_years():

        return AcademicYearRepository.get_all()

    # ==========================================================
    # GET ACADEMIC YEAR BY ID
    # ==========================================================

    @staticmethod
    def get_academic_year(

            academic_year_id

    ):

        return AcademicYearRepository.get_by_id(

            academic_year_id

        )

    # ==========================================================
    # GET CURRENT ACADEMIC YEAR
    # ==========================================================

    @staticmethod
    def get_current_academic_year():

        return AcademicYearRepository.get_current()
        # ==========================================================
    # ADD ACADEMIC YEAR
    # ==========================================================

    @staticmethod
    def add_academic_year(

            academic_year,

            start_date,

            end_date,

            is_current

    ):

        if not academic_year.strip():

            return False, "Academic Year is required."

        existing = AcademicYearRepository.get_by_name(

            academic_year

        )

        if existing:

            return False, "Academic Year already exists."

        record = AcademicYear(

            academic_year=academic_year,

            start_date=start_date,

            end_date=end_date,

            is_current=is_current

        )

        AcademicYearRepository.add(

            record

        )

        return True, "Academic Year added successfully."

    # ==========================================================
    # UPDATE ACADEMIC YEAR
    # ==========================================================

    @staticmethod
    def update_academic_year(

            academic_year_id,

            academic_year,

            start_date,

            end_date,

            is_current

    ):

        if not academic_year.strip():

            return False, "Academic Year is required."

        existing = AcademicYearRepository.get_by_name(

            academic_year

        )

        if existing:

            if existing.academic_year_id != academic_year_id:

                return False, "Academic Year already exists."

        record = AcademicYear(

            academic_year_id=academic_year_id,

            academic_year=academic_year,

            start_date=start_date,

            end_date=end_date,

            is_current=is_current

        )

        AcademicYearRepository.update(

            record

        )

        return True, "Academic Year updated successfully."

    # ==========================================================
    # DELETE ACADEMIC YEAR
    # ==========================================================

    @staticmethod
    def delete_academic_year(

            academic_year_id

    ):

        AcademicYearRepository.delete(

            academic_year_id

        )

        return True, "Academic Year deleted successfully."
    