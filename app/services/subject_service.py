"""
FacultyERP
Subject Service
---------------
"""

from app.models.subject import Subject
from app.repositories.subject_repository import SubjectRepository


class SubjectService:
    """Business logic for Subject."""

    # ==========================================================
    # ADD SUBJECT
    # ==========================================================

    @staticmethod
    def add_subject(

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

    ):

        subject_name = subject_name.strip()

        subject_short_name = subject_short_name.strip().upper()
        university_subject_code = university_subject_code.strip().upper()

        description = description.strip()

        if subject_name == "":

            return False, "Subject Name is required."

        if subject_short_name == "":

            return False, "Subject Short Name is required."

        if department_id == 0:

            return False, "Please select Department."

        if course_id == 0:

            return False, "Please select Course."

        subject_code = SubjectRepository.generate_subject_code()

        if SubjectRepository.exists(

                subject_code,

                subject_name,

                department_id,

                course_id,

                int(semester_id)

        ):

            return False, "Subject already exists."

        subject = Subject(

            subject_code=subject_code,
            university_subject_code=university_subject_code,

            subject_name=subject_name,

            subject_short_name=subject_short_name,

            department_id=department_id,

            course_id=course_id,

            semester_id=int(semester_id),

            subject_type=subject_type,

            credits=int(credits),

            theory_hours=int(theory_hours),

            practical_hours=int(practical_hours),

            tutorial_hours=int(tutorial_hours),

            description=description

        )

        SubjectRepository.add(

            subject

        )

        return True, "Subject added successfully."

    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_subjects():

        return SubjectRepository.get_all()

    # ==========================================================
    # GET SUBJECTS BY COURSE & SEMESTER
    # ==========================================================

    @staticmethod
    def get_subjects_by_course_semester(
            course_id,
            semester_id
    ):

        return SubjectRepository.get_by_course_semester(
            course_id,
            semester_id
        )

    # ==========================================================
    # GET SUBJECT
    # ==========================================================

    @staticmethod
    def get_subject(

            subject_id

    ):

        return SubjectRepository.get_by_id(

            subject_id

        )

    # ==========================================================
    # UPDATE SUBJECT
    # ==========================================================

    @staticmethod
    def update_subject(

            subject_id,

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

            description,

            is_active=1

    ):

        subject = Subject(

            subject_id=subject_id,

            subject_code=subject_code,
            university_subject_code=university_subject_code,
            

            subject_name=subject_name.strip(),

            subject_short_name=subject_short_name.strip().upper(),

            department_id=department_id,

            course_id=course_id,

            semester_id=int(semester_id),

            subject_type=subject_type,

            credits=int(credits),

            theory_hours=int(theory_hours),

            practical_hours=int(practical_hours),

            tutorial_hours=int(tutorial_hours),

            description=description.strip(),

            is_active=is_active

        )

        SubjectRepository.update(

            subject

        )

        return True, "Subject updated successfully."

    # ==========================================================
    # DELETE SUBJECT
    # ==========================================================

    @staticmethod
    def delete_subject(

            subject_id

    ):

        SubjectRepository.delete(

            subject_id

        )

        return True, "Subject deleted successfully."

    # ==========================================================
    # GENERATE SUBJECT CODE
    # ==========================================================

    @staticmethod
    def generate_subject_code():

        return SubjectRepository.generate_subject_code()