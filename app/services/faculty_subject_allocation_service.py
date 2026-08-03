"""
FacultyERP
Faculty Subject Allocation Service
----------------------------------
"""

from app.models.faculty_subject_allocation import FacultySubjectAllocation
from app.repositories.faculty_subject_allocation_repository import FacultySubjectAllocationRepository


class FacultySubjectAllocationService:
    """Business logic for Faculty Subject Allocation."""

    @staticmethod
    def _calculate_workload(theory_hours, practical_hours, tutorial_hours):
        return theory_hours + practical_hours + tutorial_hours

    @staticmethod
    def _validate(
        faculty_id,
        subject_id,
        academic_year_id,
        division_id,
        batch_name,
        theory_hours,
        practical_hours,
        tutorial_hours,
        display_order
    ):
        if not faculty_id:
            raise ValueError("Please select Faculty.")
        if not subject_id:
            raise ValueError("Please select Subject.")
        if not academic_year_id:
            raise ValueError("Please select Academic Year.")
        if not division_id:
            raise ValueError("Please select Division.")
        if batch_name is None or str(batch_name).strip() == "":
            batch_name = "Full"
        if theory_hours < 0:
            raise ValueError("Theory Hours cannot be negative.")
        if practical_hours < 0:
            raise ValueError("Practical Hours cannot be negative.")
        if tutorial_hours < 0:
            raise ValueError("Tutorial Hours cannot be negative.")
        if display_order < 1:
            display_order = 1
        return batch_name, display_order

    @staticmethod
    def add(
        faculty_id,
        subject_id,
        academic_year_id,
        division_id,
        batch_name,
        theory_hours,
        practical_hours,
        tutorial_hours,
        is_class_teacher,
        display_order,
        remarks
    ):
        batch_name, display_order = FacultySubjectAllocationService._validate(
            faculty_id,
            subject_id,
            academic_year_id,
            division_id,
            batch_name,
            theory_hours,
            practical_hours,
            tutorial_hours,
            display_order
        )
        if FacultySubjectAllocationRepository.exists(
            faculty_id,
            subject_id,
            academic_year_id,
            division_id,
            batch_name
        ):
            raise ValueError(
                "This Faculty-Subject allocation already exists."
            )
        workload_hours = FacultySubjectAllocationService._calculate_workload(
            theory_hours,
            practical_hours,
            tutorial_hours
        )
        allocation = FacultySubjectAllocation(
            faculty_id=faculty_id,
            subject_id=subject_id,
            academic_year_id=academic_year_id,
            division_id=division_id,
            batch_name=batch_name,
            theory_hours=theory_hours,
            practical_hours=practical_hours,
            tutorial_hours=tutorial_hours,
            workload_hours=workload_hours,
            is_class_teacher=is_class_teacher,
            display_order=display_order,
            remarks=remarks,
            is_active=1
        )

        allocation_id=FacultySubjectAllocationRepository.add(allocation)
        if allocation_id:
            return True,"Faculty subject allocated successfully."
        return False,"Failed to allocate subject."
    @staticmethod
    def update(
        allocation_id,
        faculty_id,
        subject_id,
        academic_year_id,
        division_id,
        batch_name,
        theory_hours,
        practical_hours,
        tutorial_hours,
        is_class_teacher,
        display_order,
        remarks,
        is_active=1
    ):
        batch_name, display_order = FacultySubjectAllocationService._validate(
            faculty_id,
            subject_id,
            academic_year_id,
            division_id,
            batch_name,
            theory_hours,
            practical_hours,
            tutorial_hours,
            display_order
        )
        if FacultySubjectAllocationRepository.exists_for_update(
            allocation_id,
            faculty_id,
            subject_id,
            academic_year_id,
            division_id,
            batch_name
        ):
            raise ValueError(
                "This Faculty-Subject allocation already exists."
            )
        workload_hours = FacultySubjectAllocationService._calculate_workload(
            theory_hours,
            practical_hours,
            tutorial_hours
        )
        allocation = FacultySubjectAllocation(
            allocation_id=allocation_id,
            faculty_id=faculty_id,
            subject_id=subject_id,
            academic_year_id=academic_year_id,
            division_id=division_id,
            batch_name=batch_name,
            theory_hours=theory_hours,
            practical_hours=practical_hours,
            tutorial_hours=tutorial_hours,
            workload_hours=workload_hours,
            is_class_teacher=is_class_teacher,
            display_order=display_order,
            remarks=remarks,
            is_active=is_active
        )
        FacultySubjectAllocationRepository.update(allocation)

    @staticmethod
    def delete(allocation_id):
        FacultySubjectAllocationRepository.delete(allocation_id)

    @staticmethod
    def get_all():
        return FacultySubjectAllocationRepository.get_all()

    @staticmethod
    def get_by_id(allocation_id):
        return FacultySubjectAllocationRepository.get_details_by_id(allocation_id)

    @staticmethod
    def get_grid_data():
        return FacultySubjectAllocationRepository.get_grid_data()

    @staticmethod
    def get_by_division(academic_year_id, division_id):
        return FacultySubjectAllocationRepository.get_by_division(
            academic_year_id,
            division_id
        )

    @staticmethod
    def get_by_faculty(faculty_id):
        return FacultySubjectAllocationRepository.get_by_faculty(
            faculty_id
        )

    @staticmethod
    def get_faculty_workload(
        faculty_id,
        academic_year_id
    ):
        return FacultySubjectAllocationRepository.get_faculty_workload(
            faculty_id,
            academic_year_id
        )
    