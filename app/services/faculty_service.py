"""
FacultyERP
Faculty Service
---------------
"""

from xml.parsers.expat import errors

from app.models.faculty import Faculty
from app.repositories.faculty_repository import FacultyRepository
from app.repositories.department_repository import DepartmentRepository
from app.utils.validation import Validation


class FacultyService:
    """Business logic for Faculty."""

    # ==========================================================
    # VALIDATE IMPORT ROW
    # ==========================================================

    @staticmethod
    def validate_import_row(record):

        errors = []

        employee_code = str(record.get("Employee Code", "")).strip()
        first_name = str(record.get("First Name", "")).strip()
        last_name = str(record.get("Last Name", "")).strip()
        department = str(record.get("Department", "")).strip()
        designation = str(record.get("Designation", "")).strip()
        mobile = str(record.get("Mobile", "")).strip()
        email = str(record.get("Email", "")).strip()
        pan_card_no = str(record.get("PAN Card No", "")).strip()

        if first_name == "":
            errors.append("First Name is required.")

        if last_name == "":
            errors.append("Last Name is required.")

        if employee_code == "":
            errors.append("Employee Code is required.")

        if pan_card_no == "":
            errors.append("PAN Card No is required.")

        if department == "":
            errors.append("Department is required.")

        if designation == "":
            errors.append("Designation is required.")

        if employee_code != "" and FacultyRepository.exists(employee_code):
            errors.append("Employee Code already exists.")

        if pan_card_no != "" and FacultyRepository.exists_pan(pan_card_no):
            errors.append("PAN Card Number already exists.")

        if department != "" and not DepartmentRepository.exists_by_name(department):
            errors.append("Invalid Department.")

        if mobile != "" and not Validation.is_mobile(mobile):
            errors.append("Invalid Mobile Number.")

        if email != "" and not Validation.is_email(email):
            errors.append("Invalid Email Address.")

        return errors

    # ==========================================================
    # IMPORT FACULTY
    # ==========================================================

    @staticmethod
    def import_faculty(record):

        department_id = DepartmentRepository.get_id_by_name(
            record.get("Department", "")
        )

        return FacultyService.add_faculty(

            first_name=record.get("First Name", ""),
            middle_name=record.get("Middle Name", ""),
            last_name=record.get("Last Name", ""),
            gender=record.get("Gender", ""),
            date_of_birth=record.get("Date of Birth", ""),
            mobile=record.get("Mobile", ""),
            email=record.get("Email", ""),
            address=record.get("Address", ""),

            pan_card_no=record.get("PAN Card No", ""),
            aadhaar_number=record.get("Aadhaar Number", ""),
            blood_group=record.get("Blood Group", ""),
            marital_status=record.get("Marital Status", ""),
            bank_account_number=record.get("Bank Account Number", ""),
            ifsc_code=record.get("IFSC Code", ""),
            uan_number=record.get("UAN Number", ""),
            passport_number=record.get("Passport Number", ""),
            joining_department_date=record.get("Joining Department Date", ""),
            university_approval_number=record.get("University Approval Number", ""),
            university_approval_date=record.get("University Approval Date", ""),

            department_id=department_id,
            designation=record.get("Designation", ""),
            joining_date=record.get("Joining Date", ""),
            employment_type=record.get("Employment Type", ""),
            qualification=record.get("Qualification", ""),
            specialization=record.get("Specialization", ""),
            experience=record.get("Experience", ""),
            research_area=record.get("Research Area", ""),
            orcid_id=record.get("ORCID ID", ""),
            google_scholar_id=record.get("Google Scholar ID", ""),
            scopus_author_id=record.get("Scopus Author ID", ""),
            vidwan_id=record.get("Vidwan ID", ""),
            aicte_id=record.get("AICTE ID", ""),
            university_approved=record.get("University Approved", ""),
            employee_code=record.get("Employee Code", ""),
            photo="",
            remarks=record.get("Remarks", "")

        )
        # ==========================================================
    # ADD FACULTY
    # ==========================================================

    @staticmethod
    def add_faculty(
            first_name,
            middle_name,
            last_name,
            gender,
            date_of_birth,
            mobile,
            email,
            address,
            pan_card_no,
            aadhaar_number,
            blood_group,
            marital_status,
            bank_account_number,
            ifsc_code,
            uan_number,
            passport_number,
            joining_department_date,
            university_approval_number,
            university_approval_date,
            department_id,
            designation,
            joining_date,
            employment_type,
            qualification,
            specialization,
            experience,
            research_area,
            orcid_id,
            google_scholar_id,
            scopus_author_id,
            vidwan_id,
            aicte_id,
            university_approved,
            employee_code,
            photo,
            remarks=""
    ):

        first_name = first_name.strip()
        middle_name = middle_name.strip()
        last_name = last_name.strip()
        gender = gender.strip()
        date_of_birth = date_of_birth.strip()
        mobile = mobile.strip()
        email = email.strip().lower()
        address = address.strip()
        pan_card_no = pan_card_no.strip().upper()
        aadhaar_number = aadhaar_number.strip()
        blood_group = blood_group.strip()
        marital_status = marital_status.strip()
        bank_account_number = bank_account_number.strip()
        ifsc_code = ifsc_code.strip().upper()
        uan_number = uan_number.strip()
        passport_number = passport_number.strip().upper()
        joining_department_date = joining_department_date.strip()
        university_approval_number = university_approval_number.strip()
        university_approval_date = university_approval_date.strip()
        designation = designation.strip()
        joining_date = joining_date.strip()
        employment_type = employment_type.strip()
        qualification = qualification.strip()
        specialization = specialization.strip()
        experience = str(experience).strip()
        research_area = research_area.strip()
        orcid_id = orcid_id.strip()
        google_scholar_id = google_scholar_id.strip()
        scopus_author_id = scopus_author_id.strip()
        vidwan_id = vidwan_id.strip()
        aicte_id = aicte_id.strip()
        university_approved = str(university_approved).strip()
        employee_code = employee_code.strip()
        remarks = remarks.strip()

        if first_name == "":
            return False, "First Name is required."

        if last_name == "":
            return False, "Last Name is required."

        if employee_code == "":
            return False, "Employee Code is required."

        if pan_card_no == "":
            return False, "PAN Card Number is required."

        if department_id == 0:
            return False, "Please select Department."

        if designation == "":
            return False, "Please select Designation."

        if mobile != "" and not Validation.is_mobile(mobile):
            return False, "Invalid Mobile Number."

        if email != "" and not Validation.is_email(email):
            return False, "Invalid Email Address."

        if FacultyRepository.exists(employee_code):
            return False, "Employee Code already exists."
        
        if FacultyRepository.exists_pan(pan_card_no):
            return False, "PAN Card Number already exists."

        faculty_code = FacultyRepository.generate_faculty_code()

        faculty = Faculty(
            faculty_code=faculty_code,
            employee_code=employee_code,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            mobile=mobile,
            email=email,
            address=address,
            pan_card_no=pan_card_no,
            aadhaar_number=aadhaar_number,
            blood_group=blood_group,
            marital_status=marital_status,
            bank_account_number=bank_account_number,
            ifsc_code=ifsc_code,
            uan_number=uan_number,
            passport_number=passport_number,
            joining_department_date=joining_department_date,
            university_approval_number=university_approval_number,
            university_approval_date=university_approval_date,
            department_id=department_id,
            designation=designation,
            joining_date=joining_date,
            employment_type=employment_type,
            qualification=qualification,
            specialization=specialization,
            experience=experience,
            research_area=research_area,
            orcid_id=orcid_id,
            google_scholar_id=google_scholar_id,
            scopus_author_id=scopus_author_id,
            vidwan_id=vidwan_id,
            aicte_id=aicte_id,
            university_approved=university_approved,
            photo=photo,
            remarks=remarks
        )

        FacultyRepository.add(faculty)

        return True, "Faculty saved successfully."
        # ==========================================================
    # GET ALL FACULTY
    # ==========================================================

    @staticmethod
    def get_faculty():
        return FacultyRepository.get_all()
    
    @staticmethod
    def get_faculty_by_department(department_id):
        return FacultyRepository.get_by_department(department_id)

    # ==========================================================
    # GET FACULTY BY ID
    # ==========================================================

    @staticmethod
    def get_faculty_by_id(faculty_id):
        return FacultyRepository.get_by_id(faculty_id)

    # ==========================================================
    # GENERATE FACULTY CODE
    # ==========================================================

    @staticmethod
    def generate_faculty_code():
        return FacultyRepository.generate_faculty_code()
        # ==========================================================
    # UPDATE FACULTY
    # ==========================================================

    @staticmethod
    def update_faculty(
            faculty_id,
            first_name,
            middle_name,
            last_name,
            gender,
            date_of_birth,
            mobile,
            email,
            address,
            pan_card_no,
            aadhaar_number,
            blood_group,
            marital_status,
            bank_account_number,
            ifsc_code,
            uan_number,
            passport_number,
            joining_department_date,
            university_approval_number,
            university_approval_date,
            department_id,
            designation,
            joining_date,
            employment_type,
            qualification,
            specialization,
            experience,
            research_area,
            orcid_id,
            google_scholar_id,
            scopus_author_id,
            vidwan_id,
            aicte_id,
            university_approved,
            employee_code,
            photo,
            remarks="",
            is_active=1
    ):

        first_name = first_name.strip()
        middle_name = middle_name.strip()
        last_name = last_name.strip()
        gender = gender.strip()
        date_of_birth = date_of_birth.strip()
        mobile = mobile.strip()
        email = email.strip().lower()
        address = address.strip()
        pan_card_no = pan_card_no.strip().upper()
        aadhaar_number = aadhaar_number.strip()
        blood_group = blood_group.strip()
        marital_status = marital_status.strip()
        bank_account_number = bank_account_number.strip()
        ifsc_code = ifsc_code.strip().upper()
        uan_number = uan_number.strip()
        passport_number = passport_number.strip().upper()
        joining_department_date = joining_department_date.strip()
        university_approval_number = university_approval_number.strip()
        university_approval_date = university_approval_date.strip()
        designation = designation.strip()
        joining_date = joining_date.strip()
        employment_type = employment_type.strip()
        qualification = qualification.strip()
        specialization = specialization.strip()
        experience = str(experience).strip()
        research_area = research_area.strip()
        orcid_id = orcid_id.strip()
        google_scholar_id = google_scholar_id.strip()
        scopus_author_id = scopus_author_id.strip()
        vidwan_id = vidwan_id.strip()
        aicte_id = aicte_id.strip()
        university_approved = str(university_approved).strip()
        employee_code = employee_code.strip()
        remarks = remarks.strip()

        if first_name == "":
            return False, "First Name is required."

        if last_name == "":
            return False, "Last Name is required."

        if employee_code == "":
            return False, "Employee Code is required."

        if pan_card_no == "":
            return False, "PAN Card Number is required."

        if department_id == 0:
            return False, "Please select Department."

        if designation == "":
            return False, "Please select Designation."

        if mobile != "" and not Validation.is_mobile(mobile):
            return False, "Invalid Mobile Number."

        if email != "" and not Validation.is_email(email):
            return False, "Invalid Email Address."

        existing = FacultyRepository.get_by_id(faculty_id)

        if existing is None:
            return False, "Faculty record not found."

        faculty = Faculty(
            faculty_id=faculty_id,
            faculty_code=existing.faculty_code,
            employee_code=employee_code,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            mobile=mobile,
            email=email,
            address=address,
            pan_card_no=pan_card_no,
            aadhaar_number=aadhaar_number,
            blood_group=blood_group,
            marital_status=marital_status,
            bank_account_number=bank_account_number,
            ifsc_code=ifsc_code,
            uan_number=uan_number,
            passport_number=passport_number,
            joining_department_date=joining_department_date,
            university_approval_number=university_approval_number,
            university_approval_date=university_approval_date,
                        department_id=department_id,
            designation=designation,
            joining_date=joining_date,
            employment_type=employment_type,
            qualification=qualification,
            specialization=specialization,
            experience=experience,
            research_area=research_area,
            orcid_id=orcid_id,
            google_scholar_id=google_scholar_id,
            scopus_author_id=scopus_author_id,
            vidwan_id=vidwan_id,
            aicte_id=aicte_id,
            university_approved=university_approved,
            photo=photo,
            remarks=remarks,
            is_active=is_active
        )

        FacultyRepository.update(faculty)

        return True, "Faculty updated successfully."

    