"""
FacultyERP
Faculty Subject Assignment Service
----------------------------------
"""

from app.models.faculty_subject_assignment import FacultySubjectAssignment
from app.repositories.faculty_subject_assignment_repository import (
    FacultySubjectAssignmentRepository
)


class FacultySubjectAssignmentService:
    """Business logic for Faculty Subject Assignments."""

    # ==========================================================
    # ADD ASSIGNMENT
    # ==========================================================

    @staticmethod
    def add_assignment(
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
            is_active):

        if faculty_id <= 0:

            return False, "Please select Faculty."

        if department_id <= 0:

            return False, "Please select Department."

        if course_id <= 0:

            return False, "Please select Course."

        if semester <= 0:

            return False, "Please select Semester."

        if subject_id <= 0:

            return False, "Please select Subject."

        if academic_year_id <= 0:

            return False, "Please select Academic Year."

        if division_id <= 0:

            return False, "Please select Division."

        batch_name = batch_name.strip()

        if batch_name == "":

            batch_name = "Full"

        if FacultySubjectAssignmentRepository.exists(
                faculty_id,
                subject_id,
                academic_year_id,
                division_id,
                batch_name):

            return False, "This faculty is already assigned to this subject."

        assignment = FacultySubjectAssignment(
            faculty_id=faculty_id,
            department_id=department_id,
            course_id=course_id,
            semester=semester,
            subject_id=subject_id,
            academic_year_id=academic_year_id,
            division_id=division_id,
            batch_name=batch_name,
            workload_hours=workload_hours,
            remarks=remarks.strip(),
            is_active=is_active
        )

        FacultySubjectAssignmentRepository.add(assignment)

        return True, "Faculty Subject Assignment added successfully."
        # ==========================================================
    # GET ALL ASSIGNMENTS
    # ==========================================================

    @staticmethod
    def get_assignments():

        return FacultySubjectAssignmentRepository.get_all()

    # ==========================================================
    # GET ASSIGNMENT
    # ==========================================================

    @staticmethod
    def get_assignment(assignment_id):

        return FacultySubjectAssignmentRepository.get_by_id(
            assignment_id
        )

    # ==========================================================
    # UPDATE ASSIGNMENT
    # ==========================================================

    @staticmethod
    def update_assignment(
            assignment_id,
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
            is_active):

        if faculty_id <= 0:

            return False, "Please select Faculty."

        if department_id <= 0:

            return False, "Please select Department."

        if course_id <= 0:

            return False, "Please select Course."

        if semester <= 0:

            return False, "Please select Semester."

        if subject_id <= 0:

            return False, "Please select Subject."

        if academic_year_id <= 0:

            return False, "Please select Academic Year."

        if division_id <= 0:

            return False, "Please select Division."

        batch_name = batch_name.strip()

        if batch_name == "":

            batch_name = "Full"

        if FacultySubjectAssignmentRepository.exists_except(
                assignment_id,
                faculty_id,
                subject_id,
                academic_year_id,
                division_id,
                batch_name):

            return (
                False,
                "This faculty subject assignment already exists."
            )

        assignment = FacultySubjectAssignment(
            assignment_id=assignment_id,
            faculty_id=faculty_id,
            department_id=department_id,
            course_id=course_id,
            semester=semester,
            subject_id=subject_id,
            academic_year_id=academic_year_id,
            division_id=division_id,
            batch_name=batch_name,
            workload_hours=workload_hours,
            remarks=remarks.strip(),
            is_active=is_active
        )

        FacultySubjectAssignmentRepository.update(
            assignment
        )

        return True, "Faculty Subject Assignment updated successfully."
        # ==========================================================
    # DELETE ASSIGNMENT
    # ==========================================================

    @staticmethod
    def delete_assignment(assignment_id):

        FacultySubjectAssignmentRepository.delete(
            assignment_id
        )

        return True, "Faculty Subject Assignment deleted successfully."

    # ==========================================================
    # GET ASSIGNMENTS BY FACULTY
    # ==========================================================

    @staticmethod
    def get_by_faculty(faculty_id):

        return FacultySubjectAssignmentRepository.get_by_faculty(
            faculty_id
        )

    # ==========================================================
    # GET ASSIGNMENTS BY SUBJECT
    # ==========================================================

    @staticmethod
    def get_by_subject(subject_id):

        return FacultySubjectAssignmentRepository.get_by_subject(
            subject_id
        )
    