"""
FacultyERP
Designation Service
-------------------
"""

from app.models.designation import Designation
from app.repositories.designation_repository import DesignationRepository


class DesignationService:
    """Business logic for Designation."""

    # ==========================================================
    # ADD DESIGNATION
    # ==========================================================

    @staticmethod
    def add_designation(

            code,

            name,

            description

    ):

        code = code.strip().upper()

        name = name.strip()

        description = description.strip()

        if code == "":

            return False, "Designation Code is required."

        if name == "":

            return False, "Designation Name is required."

        if DesignationRepository.exists(code, name):

            return False, "Designation already exists."

        designation = Designation(

            designation_code=code,

            designation_name=name,

            description=description

        )

        DesignationRepository.add(designation)

        return True, "Designation added successfully."

    # ==========================================================
    # GET ALL DESIGNATIONS
    # ==========================================================

    @staticmethod
    def get_designations():

        return DesignationRepository.get_all()

    # ==========================================================
    # GET DESIGNATION BY ID
    # ==========================================================

    @staticmethod
    def get_designation(designation_id):

        return DesignationRepository.get_by_id(designation_id)

    # ==========================================================
    # UPDATE DESIGNATION
    # ==========================================================

    @staticmethod
    def update_designation(

            designation_id,

            code,

            name,

            description

    ):

        designation = Designation(

            designation_id=designation_id,

            designation_code=code.strip().upper(),

            designation_name=name.strip(),

            description=description.strip()

        )

        DesignationRepository.update(designation)

        return True, "Designation updated successfully."

    # ==========================================================
    # DELETE DESIGNATION
    # ==========================================================

    @staticmethod
    def delete_designation(designation_id):

        DesignationRepository.delete(designation_id)

        return True, "Designation deleted successfully."

    # ==========================================================
    # GET DESIGNATION BY NAME
    # ==========================================================

    @staticmethod
    def get_designation_by_name(name):

        designations = DesignationRepository.get_all()

        for designation in designations:

            if designation.designation_name == name:

                return designation

        return None
        # ==========================================================
    # NEXT DESIGNATION CODE
    # ==========================================================

    @staticmethod
    def get_next_designation_code():

        return DesignationRepository.get_next_designation_code()