"""
AI_BABA Role Permission Service

Enterprise role-permission assignment business logic.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.iam.models.role_permission import RolePermission

from app.modules.iam.repositories.role_permission_repository import (
    RolePermissionRepository,
)


class RolePermissionAlreadyExistsError(Exception):
    """Raised when permission already assigned."""


class RolePermissionService:
    """
    Enterprise Role Permission Service.

    Responsibilities:
    - Assign permissions to roles
    - Remove permissions
    - Validate access mappings
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.role_permission_repository = (
            RolePermissionRepository(db)
        )

    def assign_permission(
        self,
        *,
        role_id: str,
        permission_id: str,
    ) -> RolePermission:
        """
        Assign permission to role.
        """

        if self.role_permission_repository.has_permission(
            role_id,
            permission_id,
        ):
            raise RolePermissionAlreadyExistsError(
                "Role already has this permission."
            )

        role_permission = RolePermission(
            role_id=role_id,
            permission_id=permission_id,
        )

        return (
            self.role_permission_repository
            .assign_permission(role_permission)
        )

    def remove_permission(
        self,
        *,
        role_id: str,
        permission_id: str,
    ) -> bool:
        """
        Remove permission from role.
        """

        return (
            self.role_permission_repository
            .remove_permission(
                role_id,
                permission_id,
            )
        )

    def has_permission(
        self,
        *,
        role_id: str,
        permission_id: str,
    ) -> bool:
        """
        Check role permission assignment.
        """

        return (
            self.role_permission_repository
            .has_permission(
                role_id,
                permission_id,
            )
        )