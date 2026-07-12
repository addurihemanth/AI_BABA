"""
AI_BABA Role Permission Repository

Enterprise repository for role-permission assignments.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.shared.repositories.base import BaseRepository

from app.modules.iam.models.role_permission import RolePermission


class RolePermissionRepository(BaseRepository[RolePermission]):
    """
    Repository for managing role-permission mappings.
    """

    def __init__(self, db: Session) -> None:
        super().__init__(
            db=db,
            model=RolePermission,
        )

    def assign_permission(
        self,
        role_permission: RolePermission,
    ) -> RolePermission:
        self.db.add(role_permission)
        self.db.commit()
        self.db.refresh(role_permission)

        return role_permission

    def remove_permission(
        self,
        role_id: str,
        permission_id: str,
    ) -> bool:
        statement = (
            select(RolePermission)
            .where(
                RolePermission.role_id == role_id,
                RolePermission.permission_id == permission_id,
            )
            .limit(1)
        )

        record = self.db.scalar(statement)

        if record is None:
            return False

        self.db.delete(record)
        self.db.commit()

        return True

    def has_permission(
        self,
        role_id: str,
        permission_id: str,
    ) -> bool:
        statement = (
            select(RolePermission)
            .where(
                RolePermission.role_id == role_id,
                RolePermission.permission_id == permission_id,
            )
            .limit(1)
        )

        return self.db.scalar(statement) is not None