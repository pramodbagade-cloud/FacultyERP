"""
FacultyERP
Logger
------
"""

import logging

from app.core.config import AppConfig


class AppLogger:

    @staticmethod
    def initialize():

        AppConfig.LOG_DIR.mkdir(exist_ok=True)

        logging.basicConfig(
            filename=AppConfig.LOG_DIR / "facultyerp.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

        logging.info("FacultyERP Started")