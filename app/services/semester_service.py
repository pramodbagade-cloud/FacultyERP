"""
FacultyERP
Semester Service
----------------
"""

from app.models.semester import Semester
from app.repositories.semester_repository import SemesterRepository

class SemesterService:
    """Business logic for Semester."""
    # ==========================================================
    # ADD SEMESTER
    # ==========================================================

    @staticmethod
    def add_semester(semester_no, semester_name):
        semester_name = semester_name.strip()
        if semester_name == "":
            return False, "Semester Name is required."
        try:
            semester_no = int(semester_no)
        except ValueError:
            return False, "Invalid Semester Number."
        if SemesterRepository.exists(semester_no): return False, "Semester already exists."
        semester = Semester(semester_no=semester_no, semester_name=semester_name)
        SemesterRepository.add(semester)
        return True, "Semester added successfully."

    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_semesters(): return SemesterRepository.get_all()

    # ==========================================================
    # GET SEMESTER
    # ==========================================================

    @staticmethod
    def get_semester(semester_id): return SemesterRepository.get_by_id(semester_id)
    # ==========================================================
    # UPDATE SEMESTER
    # ==========================================================

    @staticmethod
    def update_semester(semester_id, semester_no, semester_name):
        semester_name = semester_name.strip()
        if semester_name == "":
            return False, "Semester Name is required."
        try:
            semester_no = int(semester_no)
        except ValueError:
            return False, "Invalid Semester Number."
        if SemesterRepository.exists_for_update(
            semester_no,
            semester_id
        ):
            return False, "Semester Number already exists."
        semester = Semester(
            semester_id=semester_id,
            semester_no=semester_no,
            semester_name=semester_name
        )
        SemesterRepository.update(semester)
        return True, "Semester updated successfully."
    # ==========================================================
    # DELETE SEMESTER
    # ==========================================================

    @staticmethod
    def delete_semester(semester_id):
        SemesterRepository.delete(semester_id)
        return True, "Semester deleted successfully."
    # ==========================================================
    # NEXT SEMESTER NUMBER
    # ==========================================================

    @staticmethod
    def get_next_semester_number():
        return SemesterRepository.get_next_semester_number()