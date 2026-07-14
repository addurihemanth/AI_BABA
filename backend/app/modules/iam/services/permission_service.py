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
    - Permission update
    - Permission deactivation
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

        return self.permission_repository.create(permission)

    def get_permission_by_code(
        self,
        code: str,
    ) -> Permission:
        """
        Retrieve a permission by its unique code.
        """

        permission = self.permission_repository.get_by_code(code)

        if permission is None:
            raise PermissionNotFoundError(
                "Permission not found."
            )

        return permission

    def update_permission(
        self,
        permission: Permission,
    ) -> Permission:
        """
        Persist changes to an existing permission.
        """

        return self.permission_repository.update(permission)

    def update_permission_by_code(
        self,
        *,
        code: str,
        resource: str | None = None,
        action: str | None = None,
        description: str | None = None,
        is_active: bool | None = None,
    ) -> Permission:
        """
        Update a permission by permission code.

        Only supplied fields are modified.
        """

        permission = self.get_permission_by_code(code)

        if resource is not None:
            permission.resource = resource

        if action is not None:
            permission.action = action

        if description is not None:
            permission.description = description

        if is_active is not None:
            permission.is_active = is_active

        return self.permission_repository.update(permission)

    def deactivate_permission(
        self,
        permission: Permission,
    ) -> Permission:
        """
        Soft deactivate a permission.
        """

        permission.is_active = False

        return self.permission_repository.update(permission)

    def deactivate_permission_by_code(
        self,
        code: str,
    ) -> Permission:
        """
        Soft deactivate a permission using its code.
        """

        permission = self.get_permission_by_code(code)

        permission.is_active = False

        return self.permission_repository.update(permission)