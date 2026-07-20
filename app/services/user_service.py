"""
FacultyERP
User Service
------------
"""

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.password_service import PasswordService


class UserService:
    """Business logic for User Management."""

    # ==========================================================
    # ADD USER
    # ==========================================================
        # ==========================================================
    # ADD USER
    # ==========================================================

    @staticmethod
    def add_user(

            faculty_id,

            username,

            password,

            role,

            is_active=1

    ):

        username = username.strip()

        role = role.strip()

        if username == "":

            return False, "Username is required."

        if password == "":

            return False, "Password is required."

        if role == "":

            return False, "Role is required."

        if UserRepository.username_exists(username):

            return False, "Username already exists."

        if faculty_id is not None:

            existing = UserRepository.get_by_faculty_id(faculty_id)

            if existing is not None:

                return False, (
                    "Selected faculty already has a user account."
                )

        user = User(

            faculty_id=faculty_id,

            username=username,

            password_hash=PasswordService.hash_password(password),

            role=role,

            is_active=is_active

        )

        UserRepository.add(user)

        return True, "User created successfully."
    # ==========================================================
    # UPDATE USER
    # ==========================================================

    @staticmethod
    def update_user(

            user_id,

            faculty_id,

            username,

            role,

            is_active

    ):

        username = username.strip()

        role = role.strip()

        if username == "":

            raise ValueError("Username is required.")

        if role == "":

            raise ValueError("Role is required.")

        existing = UserRepository.get_by_username(username)

        if existing is not None:

            if existing.user_id != user_id:

                raise ValueError("Username already exists.")

        user = User(

            user_id=user_id,

            faculty_id=faculty_id,

            username=username,

            role=role,

            is_active=is_active

        )

        UserRepository.update(user)
            # ==========================================================
    # DELETE USER
    # ==========================================================

    @staticmethod
    def delete_user(user_id):

        user = UserRepository.get_by_id(user_id)

        if user is None:

            raise ValueError("User not found.")

        UserRepository.delete(user_id)

    # ==========================================================
    # RESET PASSWORD
    # ==========================================================

    @staticmethod
    def reset_password(

            user_id,

            new_password

    ):

        if new_password.strip() == "":

            raise ValueError("Password is required.")

        password_hash = PasswordService.hash_password(

            new_password

        )

        UserRepository.update_password(

            user_id,

            password_hash

        )

    # ==========================================================
    # CHANGE PASSWORD
    # ==========================================================

    @staticmethod
    def change_password(

            user_id,

            old_password,

            new_password

    ):

        user = UserRepository.get_by_id(user_id)

        if user is None:

            raise ValueError("User not found.")

        if not PasswordService.verify_password(

                old_password,

                user.password_hash

        ):

            raise ValueError("Current password is incorrect.")

        if new_password.strip() == "":

            raise ValueError("New password is required.")

        password_hash = PasswordService.hash_password(

            new_password

        )

        UserRepository.update_password(

            user_id,

            password_hash

        )

    # ==========================================================
    # ACTIVATE USER
    # ==========================================================

    @staticmethod
    def activate_user(user_id):

        user = UserRepository.get_by_id(user_id)

        if user is None:

            raise ValueError("User not found.")

        user.is_active = 1

        UserRepository.update(user)

    # ==========================================================
    # DEACTIVATE USER
    # ==========================================================

    @staticmethod
    def deactivate_user(user_id):

        user = UserRepository.get_by_id(user_id)

        if user is None:

            raise ValueError("User not found.")

        user.is_active = 0

        UserRepository.update(user)
            # ==========================================================
    # GET USER
    # ==========================================================

    @staticmethod
    def get_user(user_id):

        return UserRepository.get_by_id(user_id)

    # ==========================================================
    # GET USER BY USERNAME
    # ==========================================================

    @staticmethod
    def get_user_by_username(username):

        return UserRepository.get_by_username(

            username.strip()

        )

    # ==========================================================
    # GET ALL USERS
    # ==========================================================

    @staticmethod
    def get_all_users():

        return UserRepository.get_all()

    # ==========================================================
    # USERNAME EXISTS
    # ==========================================================

    @staticmethod
    def username_exists(username):

        return UserRepository.username_exists(

            username.strip()

        )