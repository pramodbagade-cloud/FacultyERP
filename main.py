"""
FacultyERP
==========

Application Entry Point

Author : Pramod Bagade
"""

from app.core.app import FacultyERP


def main():
    """Application Entry."""

    app = FacultyERP()
    app.run()


if __name__ == "__main__":
    main()