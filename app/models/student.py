"""
FacultyERP
Student Model
-------------
"""

from dataclasses import dataclass


@dataclass
class Student:
    """Student Model."""

    student_id: int | None = None
    college_id: str = ""
    prn: str = ""
    university_registration_no: str = ""
    abc_id: str = ""
    roll_no: str = ""
    first_name: str = ""
    middle_name: str = ""
    last_name: str = ""
    gender: str = ""
    date_of_birth: str = ""
    mobile: str = ""
    email: str = ""
    photo: str = ""
    parent_name: str = ""
    parent_mobile: str = ""
    parent_email: str = ""
    permanent_address: str = ""
    local_address: str = ""
    emergency_contact_name: str = ""
    emergency_contact_number: str = ""
    admission_year: int = 0
    academic_year_id: int = 0
    department_id: int = 0
    course_id: int = 0
    semester_id: int = 0
    division_id: int = 0
    admission_type: str = ""
    admission_category: str = ""
    caste_category: str = ""
    is_active: int = 1
    created_at: str = ""