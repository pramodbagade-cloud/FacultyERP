"""
FacultyERP
Student Service
---------------
"""

from app.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.repositories.department_repository import DepartmentRepository
from app.repositories.course_repository import CourseRepository


class StudentService:
    """Business logic for Student."""

    # ==========================================================
    # GENERATE COLLEGE ID
    # ==========================================================

    @staticmethod
    def generate_college_id(

            admission_year,

            department_code,

            course_code,

            division,

            roll_no

    ):

        year = str(admission_year)[-2:]

        dept = f"{int(department_code):02d}"

        course = f"{int(course_code):02d}"

        roll = f"{int(roll_no):02d}"

        return f"{year}{dept}{course}{division.upper()}{roll}"

    # ==========================================================
    # ADD STUDENT
    # ==========================================================

    @staticmethod
    def add_student(

            admission_year,

            academic_year,

            department_name,

            course_name,

            semester,

            division,

            roll_no,

            student_name,

            prn="",

            mobile="",

            email=""

    ):

        #
        # Get Department
        #

        department = DepartmentRepository.get_by_name(

            department_name

        )

        if department is None:

            return False, "Department not found."

        #
        # Get Course
        #

        course = CourseRepository.get_by_name(

            course_name,

            department.department_id

        )

        if course is None:

            return False, "Course not found."

        #
        # Generate College ID
        #

        college_id = StudentService.generate_college_id(

            admission_year,

            department.department_code,

            course.course_code,

            division,

            roll_no

        )

        #
        # Create Student Object
        #

        student = Student(

            college_id=college_id,

            prn=prn.strip(),

            roll_no=f"{int(roll_no):02d}",

            student_name=student_name.strip(),

            department_id=department.department_id,

            course_id=course.course_id,

            semester=int(semester),

            division=division,

            academic_year=academic_year,

            mobile=mobile.strip(),

            email=email.strip()

        )

        #
        # Save Student
        #

        StudentRepository.add(

            student

        )

        return True, "Student added successfully."

    # ==========================================================
    # GET ALL STUDENTS
    # ==========================================================

    @staticmethod
    def get_students():

        return StudentRepository.get_all()

    # ==========================================================
    # GET STUDENT BY ID
    # ==========================================================

    @staticmethod
    def get_student(

            student_id

    ):

        return StudentRepository.get_by_id(

            student_id

        )