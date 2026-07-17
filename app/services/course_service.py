"""
FacultyERP
Course Service
--------------
"""

from app.models.course import Course
from app.repositories.course_repository import CourseRepository


class CourseService:
    """Business logic for Course."""

    # ==========================================================
    # ADD COURSE
    # ==========================================================

    @staticmethod
    def add_course(

            course_name,

            course_short_name,

            degree,

            pattern,

            duration_years,

            intake,

            department_id,

            description

    ):

        course_name = course_name.strip()

        course_short_name = course_short_name.strip().upper()

        degree = degree.strip()

        pattern = pattern.strip()

        description = description.strip()

        if course_name == "":

            return False, "Course Name is required."

        if course_short_name == "":

            return False, "Course Short Name is required."

        if department_id == 0:

            return False, "Please select Department."

        if intake == "":

            intake = 0

        try:

            intake = int(intake)

        except ValueError:

            return False, "Invalid Intake."

        course_code = CourseRepository.generate_course_code()

        if CourseRepository.exists(

                course_code,

                course_name,

                department_id

        ):

            return False, "Course already exists."

        course = Course(

            course_code=course_code,

            course_name=course_name,

            course_short_name=course_short_name,

            degree=degree,

            pattern=pattern,

            duration_years=int(duration_years),

            intake=intake,

            department_id=department_id,

            description=description

        )

        CourseRepository.add(

            course

        )

        return True, "Course added successfully."

    # ==========================================================
    # GET ALL
    # ==========================================================

    @staticmethod
    def get_courses():

        return CourseRepository.get_all()

    # ==========================================================
    # GET COURSE
    # ==========================================================

    @staticmethod
    def get_course(

            course_id

    ):

        return CourseRepository.get_by_id(

            course_id

        )

    # ==========================================================
    # UPDATE COURSE
    # ==========================================================

    @staticmethod
    def update_course(

            course_id,

            course_code,

            course_name,

            course_short_name,

            degree,

            pattern,

            duration_years,

            intake,

            department_id,

            description,

            is_active=1

    ):

        course_name = course_name.strip()

        course_short_name = course_short_name.strip().upper()

        degree = degree.strip()

        pattern = pattern.strip()

        description = description.strip()

        if intake == "":

            intake = 0

        try:

            intake = int(intake)

        except ValueError:

            return False, "Invalid Intake."

        course = Course(

            course_id=course_id,

            course_code=course_code,

            course_name=course_name,

            course_short_name=course_short_name,

            degree=degree,

            pattern=pattern,

            duration_years=int(duration_years),

            intake=intake,

            department_id=department_id,

            description=description,

            is_active=is_active

        )

        CourseRepository.update(

            course

        )

        return True, "Course updated successfully."

    # ==========================================================
    # DELETE COURSE
    # ==========================================================

    @staticmethod
    def delete_course(

            course_id

    ):

        CourseRepository.delete(

            course_id

        )

        return True, "Course deleted successfully."

    # ==========================================================
    # GENERATE COURSE CODE
    # ==========================================================

    @staticmethod
    def generate_course_code():

        return CourseRepository.generate_course_code()
    