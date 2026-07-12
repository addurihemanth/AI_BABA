"""
AI_BABA User Role Service

Enterprise user-role assignment business logic.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.iam.models.user_role import UserRole
from app.modules.iam.repositories.user_role_repository import (
    UserRoleRepository,
)


class UserRoleAlreadyExistsError(Exception):
    """Raised when user already has role."""


class UserRoleService:
    """
    Enterprise User Role Service.

    Responsibilities:
    - Assign roles to users
    - Remove user roles
    - Validate role assignments
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.user_role_repository = UserRoleRepository(db)

    def assign_role(
        self,
        *,
        user_id: str,
        role_id: str,
    ) -> UserRole:
        """
        Assign role to user.
        """

        if self.user_role_repository.has_role(
            user_id,
            role_id,
        ):
            raise UserRoleAlreadyExistsError(
                "User already has this role."
            )

        user_role = UserRole(
            user_id=user_id,
            role_id=role_id,
        )

        return self.user_role_repository.assign_role(
            user_role
        )

    def remove_role(
        self,
        *,
        user_id: str,
        role_id: str,
    ) -> bool:
        """
        Remove role from user.
        """

        return self.user_role_repository.remove_role(
            user_id,
            role_id,
        )

    def has_role(
        self,
        *,
        user_id: str,
        role_id: str,
    ) -> bool:
        """
        Check user role assignment.
        """

        return self.user_role_repository.has_role(
            user_id,
            role_id,
        )