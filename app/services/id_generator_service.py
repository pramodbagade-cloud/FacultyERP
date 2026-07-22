"""
FacultyERP
ID Generator Service
--------------------
"""

class IDGeneratorService:
    """Generates IDs used throughout FacultyERP."""

    @staticmethod
    def format_number(number, digits=3):
        """Return zero padded number."""
        return str(number).zfill(digits)

    @staticmethod
    def generate_student_college_id(
            admission_year,
            department_code,
            course_code,
            division_name,
            roll_no
    ):
        """
        Format:
        26MEBEA015

        26  -> Admission Year
        ME  -> Department Code
        BE  -> Course Code
        A   -> Division
        015 -> Roll Number
        """

        year = str(admission_year)[-2:]
        department = str(department_code).upper().strip()
        course = str(course_code).upper().strip()
        division = str(division_name).upper().strip()
        roll = IDGeneratorService.format_number(int(roll_no), 3)

        return f"{year}{department}{course}{division}{roll}"

    @staticmethod
    def generate_faculty_code(faculty_id):
        """
        Future Format:
        FAC00001
        """
        return f"FAC{IDGeneratorService.format_number(faculty_id,5)}"

    @staticmethod
    def generate_employee_code(employee_id):
        """
        Future Format:
        EMP00001
        """
        return f"EMP{IDGeneratorService.format_number(employee_id,5)}"

    @staticmethod
    def generate_department_code(department_id):
        """
        Reserved for future implementation.
        """
        return f"DPT{IDGeneratorService.format_number(department_id,3)}"

    @staticmethod
    def generate_course_code(course_id):
        """
        Reserved for future implementation.
        """
        return f"CRS{IDGeneratorService.format_number(course_id,3)}"

    @staticmethod
    def generate_subject_code(subject_id):
        """
        Reserved for future implementation.
        """
        return f"SUB{IDGeneratorService.format_number(subject_id,5)}"