"""
AI_BABA Role Service

Enterprise role management business logic.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.iam.models.role import Role
from app.modules.iam.repositories.role_repository import RoleRepository


class RoleAlreadyExistsError(Exception):
    """Raised when a role already exists."""


class RoleNotFoundError(Exception):
    """Raised when a role cannot be found."""


class RoleService:
    """
    Enterprise Role Service.

    Responsibilities:
    - Role creation
    - Role retrieval
    - Role updates
    - Role validation
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.role_repository = RoleRepository(db)

    def create_role(
        self,
        *,
        name: str,
        code: str,
        description: str | None = None,
        is_system: bool = False,
    ) -> Role:
        """
        Create a new role.
        """

        if self.role_repository.exists_by_code(code):
            raise RoleAlreadyExistsError(
                "Role code already exists."
            )

        role = Role(
            name=name,
            code=code,
            description=description,
            is_system=is_system,
        )

        return self.role_repository.create(role)

    def get_role_by_code(
        self,
        code: str,
    ) -> Role:

        role = self.role_repository.get_by_code(code)

        if role is None:
            raise RoleNotFoundError(
                "Role not found."
            )

        return role

    def update_role(
        self,
        role: Role,
    ) -> Role:

        return self.role_repository.update(role)

    def deactivate_role(
        self,
        role: Role,
    ) -> Role:

        role.is_active = False

        return self.role_repository.update(role)