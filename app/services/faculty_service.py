"""
FacultyERP
Faculty Service
---------------
"""

from app.models.faculty import Faculty
from app.repositories.faculty_repository import FacultyRepository


class FacultyService:
    """Business logic for Faculty."""

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

        # ------------------------------------------------------
        # Clean Data
        # ------------------------------------------------------

        first_name = first_name.strip()

        middle_name = middle_name.strip()

        last_name = last_name.strip()

        mobile = mobile.strip()

        email = email.strip().lower()

        address = address.strip()

        qualification = qualification.strip()

        specialization = specialization.strip()

        employment_type = employment_type.strip()

        employee_code = employee_code.strip()

        research_area = research_area.strip()

        orcid_id = orcid_id.strip()

        google_scholar_id = google_scholar_id.strip()

        scopus_author_id = scopus_author_id.strip()

        vidwan_id = vidwan_id.strip()

        aicte_id = aicte_id.strip()

        remarks = remarks.strip()

        # ------------------------------------------------------
        # Validation
        # ------------------------------------------------------

        if first_name == "":

            return False, "First Name is required."

        if last_name == "":

            return False, "Last Name is required."

        if employee_code == "":

            return False, "Employee Code is required."

        if department_id == 0:

            return False, "Please select Department."

        if designation.strip() == "":

            return False, "Please select Designation."

        # ------------------------------------------------------
        # Duplicate Check
        # ------------------------------------------------------

        if FacultyRepository.exists(employee_code):

            return False, "Employee Code already exists."

        # ------------------------------------------------------
        # Generate Faculty Code
        # ------------------------------------------------------

        faculty_code = FacultyRepository.generate_faculty_code()

        # ------------------------------------------------------
        # Faculty Object
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Save
        # ------------------------------------------------------

        FacultyRepository.add(faculty)

        return True, "Faculty saved successfully."
        # ==========================================================
    # GET ALL FACULTY
    # ==========================================================

    @staticmethod
    def get_faculty():

        return FacultyRepository.get_all()

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

        # ------------------------------------------------------
        # Clean Data
        # ------------------------------------------------------

        first_name = first_name.strip()

        middle_name = middle_name.strip()

        last_name = last_name.strip()

        mobile = mobile.strip()

        email = email.strip().lower()

        address = address.strip()

        qualification = qualification.strip()

        specialization = specialization.strip()

        employment_type = employment_type.strip()

        employee_code = employee_code.strip()

        research_area = research_area.strip()

        orcid_id = orcid_id.strip()

        google_scholar_id = google_scholar_id.strip()

        scopus_author_id = scopus_author_id.strip()

        vidwan_id = vidwan_id.strip()

        aicte_id = aicte_id.strip()

        remarks = remarks.strip()

        # ------------------------------------------------------
        # Validation
        # ------------------------------------------------------

        if first_name == "":

            return False, "First Name is required."

        if last_name == "":

            return False, "Last Name is required."

        if employee_code == "":

            return False, "Employee Code is required."

        if department_id == 0:

            return False, "Please select Department."

        if designation.strip() == "":

            return False, "Please select Designation."

        # ------------------------------------------------------
        # Existing Faculty
        # ------------------------------------------------------

        existing = FacultyRepository.get_by_id(faculty_id)

        if existing is None:

            return False, "Faculty record not found."

        # ------------------------------------------------------
        # Faculty Object
        # ------------------------------------------------------

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
                # ------------------------------------------------------
        # Update
        # ------------------------------------------------------

        FacultyRepository.update(faculty)

        return True, "Faculty updated successfully."

    # ==========================================================
    # DELETE FACULTY
    # ==========================================================

    @staticmethod
    def delete_faculty(faculty_id):

        FacultyRepository.delete(faculty_id)

        return True, "Faculty deleted successfully."
    