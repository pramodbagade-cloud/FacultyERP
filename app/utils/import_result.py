"""
FacultyERP
Import Result
-------------
"""

from dataclasses import dataclass
from dataclasses import field


@dataclass
class ImportResult:
    success: bool = True
    total_rows: int = 0
    valid_rows: int = 0
    invalid_rows: int = 0
    imported_rows: int = 0
    records: list = field(default_factory=list)
    errors: list = field(default_factory=list)

    def add_record(self, record):
        self.records.append(record)
        self.valid_rows += 1

    def add_error(self, row_number, message):
        self.errors.append({
            "row": row_number,
            "message": message
        })
        self.invalid_rows += 1
        self.success = False

    def summary(self):
        return {
            "success": self.success,
            "total_rows": self.total_rows,
            "valid_rows": self.valid_rows,
            "invalid_rows": self.invalid_rows,
            "imported_rows": self.imported_rows
        }