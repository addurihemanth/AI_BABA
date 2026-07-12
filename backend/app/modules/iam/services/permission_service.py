"""
AI_BABA Permission Service

Enterprise permission management business logic.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.iam.models.permission import Permission
from app.modules.iam.repositories.permission_repository import (
    PermissionRepository,
)


class PermissionAlreadyExistsError(Exception):
    """Raised when permission already exists."""


class PermissionNotFoundError(Exception):
    """Raised when permission is missing."""


class PermissionService:
    """
    Enterprise Permission Service.

    Responsibilities:
    - Permission creation
    - Permission lookup
    - Permission validation
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.permission_repository = PermissionRepository(db)

    def create_permission(
        self,
        *,
        resource: str,
        action: str,
        code: str,
        description: str | None = None,
        is_system: bool = False,
    ) -> Permission:
        """
        Create a permission.
        """

        if self.permission_repository.exists_by_code(code):
            raise PermissionAlreadyExistsError(
                "Permission code already exists."
            )

        permission = Permission(
            resource=resource,
            action=action,
            code=code,
            description=description,
            is_system=is_system,
        )

        return self.permission_repository.create(
            permission
        )

    def get_permission_by_code(
        self,
        code: str,
    ) -> Permission:

        permission = (
            self.permission_repository
            .get_by_code(code)
        )

        if permission is None:
            raise PermissionNotFoundError(
                "Permission not found."
            )

        return permission

    def update_permission(
        self,
        permission: Permission,
    ) -> Permission:

        return (
            self.permission_repository
            .update(permission)
        )

    def deactivate_permission(
        self,
        permission: Permission,
    ) -> Permission:

        permission.is_active = False

        return (
            self.permission_repository
            .update(permission)
        )