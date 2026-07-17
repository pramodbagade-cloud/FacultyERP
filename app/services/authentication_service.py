"""
FacultyERP
Authentication Service
----------------------
"""

from app.repositories.user_repository import UserRepository
from app.services.password_service import PasswordService


class AuthenticationService:
    """Handles user authentication."""

    @staticmethod
    def login(username: str, password: str):

        user = UserRepository.get_by_username(username)

        if user is None:
            return None

        if user.is_active != 1:
            return None

        if not PasswordService.verify_password(
            password,
            user.password_hash
        ):
            return None

        return user