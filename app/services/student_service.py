"""
FacultyERP
Student Service
---------------
"""

from app.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.repositories.department_repository import DepartmentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.division_repository import DivisionRepository
from app.repositories.academic_year_repository import AcademicYearRepository
from app.repositories.semester_repository import SemesterRepository
from app.services.id_generator_service import IDGeneratorService


class StudentService:
    """Business logic for Student."""

    # ==========================================================
    # ADD STUDENT
    # ==========================================================

       
    @staticmethod
    def add_student(
            first_name,
            last_name,
            admission_year,
            academic_year_id,
            department_id,
            course_id,
            semester_id,
            division_id,
            prn="",
            mobile="",
            email="",
            middle_name="",
            gender="",
            date_of_birth=None,
            parent_name="",
            parent_mobile="",
            parent_email="",
            permanent_address="",
            local_address="",
            emergency_contact_name="",
            emergency_contact_number="",
            photo=None,
            is_active=True
    ):

        validation = StudentService.validate_student(
            first_name,
            last_name,
            mobile,
            admission_year,
            academic_year_id,
            department_id,
            course_id,
            semester_id,
            division_id
        )

        if validation[0] is False:
            return validation

        academic_year = AcademicYearRepository.get_by_id(academic_year_id)
        department = DepartmentRepository.get_by_id(department_id)
        course = CourseRepository.get_by_id(course_id)
        semester = SemesterRepository.get_by_id(semester_id)
        division = DivisionRepository.get_by_id(division_id)

        if academic_year is None:
            return False, "Academic Year not found."

        if department is None:
            return False, "Department not found."

        if course is None:
            return False, "Course not found."

        if semester is None:
            return False, "Semester not found."

        if division is None:
            return False, "Division not found."

        roll_no = StudentRepository.get_next_roll_no(
            academic_year_id,
            course_id,
            semester_id,
            division_id
        )

        college_id = StudentService.generate_college_id(
            admission_year,
            department,
            course,
            division,
            roll_no
        )

        if StudentRepository.exists(college_id, prn):
            return False, "Student already exists."
        prn = StudentService.normalize_optional(prn)
        student = Student(
            college_id=college_id,
            prn=prn,
            roll_no=str(roll_no),
            first_name=first_name.strip(),
            middle_name=middle_name.strip(),
            last_name=last_name.strip(),
            gender=gender,
            date_of_birth=date_of_birth,
            mobile=mobile.strip(),
            email=email.strip(),
            photo=photo,
            parent_name=parent_name.strip(),
            parent_mobile=parent_mobile.strip(),
            parent_email=parent_email.strip(),
            permanent_address=permanent_address.strip(),
            local_address=local_address.strip(),
            emergency_contact_name=emergency_contact_name.strip(),
            emergency_contact_number=emergency_contact_number.strip(),
            admission_year=admission_year,
            academic_year_id=academic_year_id,
            department_id=department_id,
            course_id=course_id,
            semester_id=semester_id,
            division_id=division_id,
            is_active=is_active
        )
        
        StudentRepository.add(student)

        return True, "Student added successfully."

    # ==========================================================
    # IMPORT STUDENT
    # ==========================================================

    @staticmethod
    def import_student(student_data,
                       admission_year,
                       academic_year_id,
                       department_id,
                       course_id,
                       semester_id,
                       division_id):

        return StudentService.add_student(
            first_name=student_data["first_name"],
            last_name=student_data["last_name"],
            admission_year=admission_year,
            academic_year_id=academic_year_id,
            department_id=department_id,
            course_id=course_id,
            semester_id=semester_id,
            division_id=division_id,
            prn=student_data["prn"],
            mobile=student_data["mobile"],
            email=student_data["email"],
            middle_name=student_data["middle_name"],
            gender=student_data["gender"],
            date_of_birth=student_data["date_of_birth"],
            parent_name=student_data["parent_name"],
            parent_mobile=student_data["parent_mobile"],
            parent_email=student_data["parent_email"],
            permanent_address=student_data["permanent_address"],
            local_address=student_data["local_address"],
            emergency_contact_name=student_data["emergency_contact_name"],
            emergency_contact_number=student_data["emergency_contact_number"],
            photo=None,
            is_active=True
        )
    # ==========================================================
    # UPDATE STUDENT
    # ==========================================================

    @staticmethod
    def update_student(
            student_id,
            first_name,
            middle_name,
            last_name,
            gender,
            date_of_birth,
            mobile,
            email,
            parent_name,
            parent_mobile,
            parent_email,
            permanent_address,
            local_address,
            emergency_contact_name,
            emergency_contact_number,
            prn,
            admission_year,
            academic_year_id,
            department_id,
            course_id,
            semester_id,
            division_id,
            photo=None,
            is_active=True
    ):

        validation = StudentService.validate_student(
            first_name,
            last_name,
            mobile,
            admission_year,
            academic_year_id,
            department_id,
            course_id,
            semester_id,
            division_id
        )

        if validation[0] is False:
            return validation

        student = StudentRepository.get_by_id(student_id)

        if student is None:
            return False, "Student not found."

        academic_year = AcademicYearRepository.get_by_id(academic_year_id)
        department = DepartmentRepository.get_by_id(department_id)
        course = CourseRepository.get_by_id(course_id)
        semester = SemesterRepository.get_by_id(semester_id)
        division = DivisionRepository.get_by_id(division_id)

        if academic_year is None:
            return False, "Academic Year not found."

        if department is None:
            return False, "Department not found."

        if course is None:
            return False, "Course not found."

        if division is None:
            return False, "Division not found."

        college_id = StudentService.generate_college_id(
            admission_year,
            department,
            course,
            division,
            student.roll_no
        )

        if StudentRepository.exists(
                college_id,
                prn,
                student_id
        ):
            return False, "Student already exists."

        student.college_id = college_id
        student.prn = StudentService.normalize_optional(prn)
        student.first_name = first_name.strip()
        student.middle_name = middle_name.strip()
        student.last_name = last_name.strip()
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.mobile = mobile.strip()
        student.email = email.strip()
        student.parent_name = parent_name.strip()
        student.parent_mobile = parent_mobile.strip()
        student.parent_email = parent_email.strip()
        student.permanent_address = permanent_address.strip()
        student.local_address = local_address.strip()
        student.emergency_contact_name = emergency_contact_name.strip()
        student.emergency_contact_number = emergency_contact_number.strip()
        student.photo = photo
        student.admission_year = admission_year
        student.academic_year_id = academic_year_id
        student.department_id = department_id
        student.course_id = course_id
        student.semester_id = semester_id
        student.division_id = division_id
        student.is_active = is_active

        StudentRepository.update(student)

        return True, "Student updated successfully."

    # ==========================================================
    # DELETE STUDENT
    # ==========================================================

    @staticmethod
    def delete_student(student_id):

        student = StudentRepository.get_by_id(student_id)

        if student is None:
            return False, "Student not found."

        StudentRepository.delete(student_id)

        return True, "Student deleted successfully."
        # ==========================================================
    # GET STUDENT
    # ==========================================================

    @staticmethod
    def get_student(student_id): return StudentRepository.get_by_id(student_id)

    # ==========================================================
    # GET ALL STUDENTS
    # ==========================================================

    @staticmethod
    def get_all_students(): return StudentRepository.get_all()

    # ==========================================================
    # GET STUDENTS BY DIVISION
    # ==========================================================

    @staticmethod
    def get_students_by_division(division_id):

        return StudentRepository.get_by_division(
            division_id
        )
    
    # ==========================================================
    # GET EXISTING IMPORT DATA
    # ==========================================================

    @staticmethod
    def get_existing_import_data(): return StudentRepository.get_existing_import_data()

    # ==========================================================
    # STUDENT EXISTS
    # ==========================================================

    @staticmethod
    def student_exists(college_id, prn, student_id=None):
        return StudentRepository.exists(college_id, prn, student_id)

    # ==========================================================
    # GET NEXT ROLL NUMBER
    # ==========================================================

    @staticmethod
    def get_next_roll_no(academic_year_id, course_id, semester_id, division_id):
        return StudentRepository.get_next_roll_no(academic_year_id, course_id, semester_id, division_id)
    # ==========================================================
    # GENERATE COLLEGE ID
    # ==========================================================

    @staticmethod
    def generate_college_id(admission_year, department, course, division, roll_no):

        department_code = getattr(department, "department_code", None)
        course_code = getattr(course, "degree", None)
        division_name = getattr(division, "division_name", "")

        if not department_code:
            raise ValueError("Department code is not available.")

        if not course_code:
            raise ValueError("Course code is not available.")

        if not division_name:
            raise ValueError("Division name is not available.")


        return IDGeneratorService.generate_student_college_id(
            admission_year=admission_year,
            department_code=department_code,
            course_code=course_code,
            division_name=division_name,
            roll_no=roll_no
        )
    # ==========================================================
    # NORMALIZE OPTIONAL VALUE
    # ==========================================================

    @staticmethod
    def normalize_optional(value):

        if value is None:
            return None

        value = str(value).strip()

        if value == "":
            return None

        return value
    # ==========================================================
    # VALIDATE STUDENT
    # ==========================================================

    @staticmethod
    def validate_student(
            first_name,
            last_name,
            mobile,
            admission_year,
            academic_year_id,
            department_id,
            course_id,
            semester_id,
            division_id
    ):

        if not first_name.strip():
            return False, "First Name is required."

        if not last_name.strip():
            return False, "Last Name is required."

        if not admission_year:
            return False, "Admission Year is required."

        if not academic_year_id:
            return False, "Academic Year is required."

        if not department_id:
            return False, "Department is required."

        if not course_id:
            return False, "Course is required."

        if not semester_id:
            return False, "Semester is required."

        if not division_id:
            return False, "Division is required."

        mobile = mobile.strip()

        if mobile:

            if not mobile.isdigit():
                return False, "Mobile number must contain digits only."

            if len(mobile) != 10:
                return False, "Mobile number must be 10 digits."

        return True, "Validation successful."
    