"""
AI_BABA Permission Repository

Enterprise repository for Permission entity.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.shared.repositories.base import BaseRepository

from app.modules.iam.models.permission import Permission


class PermissionRepository(BaseRepository[Permission]):
    """
    Enterprise repository responsible for
    Permission persistence operations.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        super().__init__(
            db=db,
            model=Permission,
        )

    def get_by_id(
        self,
        permission_id: str,
    ) -> Permission | None:
        """
        Retrieve permission by ID.
        """

        return self.db.get(
            Permission,
            permission_id,
        )

    def get_by_code(
        self,
        code: str,
    ) -> Permission | None:
        """
        Retrieve permission by code.
        """

        statement = (
            select(Permission)
            .where(
                Permission.code == code,
            )
            .limit(1)
        )

        return self.db.scalar(statement)

    def get_by_resource_action(
        self,
        resource: str,
        action: str,
    ) -> Permission | None:
        """
        Retrieve permission by
        resource and action.
        """

        statement = (
            select(Permission)
            .where(
                Permission.resource == resource,
                Permission.action == action,
            )
            .limit(1)
        )

        return self.db.scalar(statement)

    def exists_by_code(
        self,
        code: str,
    ) -> bool:
        """
        Check whether permission
        code already exists.
        """

        return (
            self.get_by_code(code)
            is not None
        )

    def create(
        self,
        permission: Permission,
    ) -> Permission:
        """
        Persist new permission.
        """

        self.db.add(permission)
        self.db.commit()
        self.db.refresh(permission)

        return permission

    def update(
        self,
        permission: Permission,
    ) -> Permission:
        """
        Update existing permission.
        """

        self.db.add(permission)
        self.db.commit()
        self.db.refresh(permission)

        return permission

    def delete(
        self,
        permission: Permission,
    ) -> None:
        """
        Delete permission.
        """

        self.db.delete(permission)
        self.db.commit()

    def list_all(
        self,
    ) -> list[Permission]:
        """
        Return all permissions.
        """

        statement = (
            select(Permission)
            .order_by(
                Permission.resource,
                Permission.action,
            )
        )

        return list(
            self.db.scalars(statement).all()
        )