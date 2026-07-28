"""
FacultyERP
Validation Utility
------------------
"""

import re
from datetime import datetime


class Validation:

    @staticmethod
    def is_blank(value):
        if value is None:
            return True
        return str(value).strip() == ""

    @staticmethod
    def is_email(value):
        if Validation.is_blank(value):
            return True
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return re.fullmatch(pattern, str(value).strip()) is not None

    @staticmethod
    def is_mobile(value):
        if Validation.is_blank(value):
            return True
        value = str(value).strip()
        return value.isdigit() and len(value) == 10

    @staticmethod
    def is_integer(value):
        if Validation.is_blank(value):
            return True
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_float(value):
        if Validation.is_blank(value):
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_date(value, date_format="%d-%m-%Y"):
        if Validation.is_blank(value):
            return True
        try:
            datetime.strptime(str(value).strip(), date_format)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_in_list(value, valid_values):
        if Validation.is_blank(value):
            return False
        return str(value).strip() in valid_values

    @staticmethod
    def is_unique(value, existing_values):
        return value not in existing_values