"""
AI_BABA Authentication Service

Enterprise authentication business logic.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.password import PasswordService
from app.core.token_service import TokenService

# IAM Module
from app.modules.iam.models.user import User
from app.modules.iam.repositories.user_repository import UserRepository


class AuthenticationError(Exception):
    """Raised when authentication fails."""


class UserAlreadyExistsError(Exception):
    """Raised when username or email already exists."""


class AuthService:
    """
    Enterprise Authentication Service.

    Responsibilities:
    - User Registration
    - User Authentication
    - Token Generation
    """

    def __init__(self, db: Session) -> None:
        self.user_repository = UserRepository(db)

    def register(
        self,
        *,
        username: str,
        email: str,
        password: str,
        first_name: str | None = None,
        last_name: str | None = None,
    ) -> User:

        if self.user_repository.exists_by_username(username):
            raise UserAlreadyExistsError(
                "Username already exists."
            )

        if self.user_repository.exists_by_email(email):
            raise UserAlreadyExistsError(
                "Email already exists."
            )

        user = User(
            username=username,
            email=email,
            hashed_password=PasswordService.hash_password(
                password
            ),
            first_name=first_name,
            last_name=last_name,
        )

        return self.user_repository.create(user)

    def authenticate(
        self,
        *,
        username: str,
        password: str,
    ) -> User:

        user = self.user_repository.get_by_username(
            username
        )

        if user is None:
            raise AuthenticationError(
                "Invalid username or password."
            )

        if not PasswordService.verify_password(
            password,
            user.hashed_password,
        ):
            raise AuthenticationError(
                "Invalid username or password."
            )

        return user

    def login(
        self,
        *,
        username: str,
        password: str,
    ) -> dict[str, str]:

        user = self.authenticate(
            username=username,
            password=password,
        )

        return {
            "access_token": TokenService.create_access_token(
                subject=user.id,
            ),
            "refresh_token": TokenService.create_refresh_token(
                subject=user.id,
            ),
            "token_type": "bearer",
        }