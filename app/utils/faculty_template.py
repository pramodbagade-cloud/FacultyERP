"""
FacultyERP
Faculty Excel Template
----------------------
"""

from app.utils.excel_template import ExcelTemplate


class FacultyTemplate:

    @staticmethod
    def create(filepath):

        headers = [

            "Employee Code",

            "First Name",

            "Middle Name",

            "Last Name",

            "Department",

            "Designation",

            "Mobile",

            "Email",

            "Gender",

            "Qualification",

            "Experience",

            "Joining Date",

            "Employment Type",

            "Specialization"

        ]

        mandatory_columns = [

            "Employee Code",

            "First Name",

            "Last Name",

            "Department",

            "Designation"

        ]

        sample_rows = [

            [

                "EMP001",

                "Pramod",

                "",

                "Bagade",

                "Computer Engineering",

                "Assistant Professor",

                "9876543210",

                "faculty@college.edu",

                "Male",

                "PhD",

                "12",

                "01-06-2018",

                "Permanent",

                "CFD"

            ]

        ]

        ExcelTemplate.create(

            filepath=filepath,

            headers=headers,

            mandatory_columns=mandatory_columns,

            sample_rows=sample_rows

        )