"""
FacultyERP
Faculty Subject Allocation Service
----------------------------------
"""

from app.models.faculty_subject_allocation import FacultySubjectAllocation

from app.repositories.faculty_subject_allocation_repository import (
    FacultySubjectAllocationRepository
)

from app.repositories.faculty_repository import FacultyRepository
from app.repositories.subject_repository import SubjectRepository
from app.repositories.academic_year_repository import AcademicYearRepository
from app.repositories.division_repository import DivisionRepository


class FacultySubjectAllocationService:
    """Business logic for Faculty Subject Allocation."""

    @staticmethod
    def add_allocation(
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
                # ==========================================================
        # VALIDATION
        # ==========================================================

        if not faculty_id:
            raise ValueError("Please select Faculty.")

        if not subject_id:
            raise ValueError("Please select Subject.")

        if not academic_year_id:
            raise ValueError("Please select Academic Year.")

        if not division_id:
            raise ValueError("Please select Division.")

        if theory_hours < 0:
            raise ValueError("Theory hours cannot be negative.")

        if practical_hours < 0:
            raise ValueError("Practical hours cannot be negative.")

        if tutorial_hours < 0:
            raise ValueError("Tutorial hours cannot be negative.")

        if display_order < 1:
            display_order = 1
                    # ==========================================================
        # VERIFY MASTER RECORDS
        # ==========================================================

        if FacultyRepository.get_by_id(faculty_id) is None:
            raise ValueError("Selected faculty does not exist.")

        if SubjectRepository.get_by_id(subject_id) is None:
            raise ValueError("Selected subject does not exist.")

        if AcademicYearRepository.get_by_id(academic_year_id) is None:
            raise ValueError("Selected Academic Year does not exist.")

        if DivisionRepository.get_by_id(division_id) is None:
            raise ValueError("Selected Division does not exist.")
                # ==========================================================
        # WORKLOAD CALCULATION
        # ==========================================================

        workload_hours = (
            theory_hours +
            practical_hours +
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

        return FacultySubjectAllocationRepository.add(allocation)
    