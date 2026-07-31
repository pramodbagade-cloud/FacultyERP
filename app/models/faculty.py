"""
FacultyERP
Faculty Model
-------------
"""

from dataclasses import dataclass


@dataclass
class Faculty:
    """Faculty Model."""
    faculty_id: int | None = None
    faculty_code: str = ""
    employee_code: str = ""
    first_name: str = ""
    middle_name: str = ""
    last_name: str = ""
    gender: str = ""
    date_of_birth: str = ""
    mobile: str = ""
    email: str = ""
    address: str = ""
    pan_card_no: str = ""
    aadhaar_number: str = ""
    blood_group: str = ""
    marital_status: str = ""
    bank_account_number: str = ""
    ifsc_code: str = ""
    uan_number: str = ""
    passport_number: str = ""
    joining_department_date: str = ""
    university_approval_number: str = ""
    university_approval_date: str = ""
    department_id: int = 0
    designation: str = ""
    joining_date: str = ""
    employment_type: str = ""
    qualification: str = ""
    specialization: str = ""
    experience: float = 0.0
    research_area: str = ""
    orcid_id: str = ""
    google_scholar_id: str = ""
    scopus_author_id: str = ""
    vidwan_id: str = ""
    aicte_id: str = ""
    university_approved: int = 1
    photo: str = ""
    remarks: str = ""
    is_active: int = 1
    created_at: str = ""

    @property
    def full_name(self) -> str:
        """Return complete faculty name."""

        return " ".join(
            part
            for part in (
                self.first_name,
                self.middle_name,
                self.last_name
            )
            if part
        )