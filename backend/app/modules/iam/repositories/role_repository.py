"""
AI_BABA Role Repository

Enterprise repository for Role entity.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.shared.repositories.base import BaseRepository

from app.modules.iam.models.permission import Permission
from app.modules.iam.models.role import Role
from app.modules.iam.models.role_permission import RolePermission


class RoleRepository(BaseRepository[Role]):
    """
    Enterprise repository responsible for
    Role persistence operations.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        super().__init__(
            db=db,
            model=Role,
        )

    def get_by_id(
        self,
        role_id: str,
    ) -> Role | None:
        """
        Retrieve role by ID.
        """

        return self.db.get(
            Role,
            role_id,
        )

    def get_by_code(
        self,
        code: str,
    ) -> Role | None:
        """
        Retrieve role by code.
        """

        statement = (
            select(Role)
            .where(Role.code == code)
            .limit(1)
        )

        return self.db.scalar(statement)

    def get_by_name(
        self,
        name: str,
    ) -> Role | None:
        """
        Retrieve role by name.
        """

        statement = (
            select(Role)
            .where(Role.name == name)
            .limit(1)
        )

        return self.db.scalar(statement)

    def exists_by_code(
        self,
        code: str,
    ) -> bool:
        """
        Check whether role code exists.
        """

        return self.get_by_code(code) is not None

    def get_permissions(
        self,
        role_id: str,
    ) -> list[Permission]:
        """
        Return all permissions assigned
        to a role.
        """

        statement = (
            select(Role)
            .options(
                selectinload(
                    Role.role_permissions,
                ).selectinload(
                    RolePermission.permission,
                )
            )
            .where(
                Role.id == role_id,
            )
        )

        role = self.db.scalar(statement)

        if role is None:
            return []

        return [
            role_permission.permission
            for role_permission
            in role.role_permissions
        ]

    def create(
        self,
        role: Role,
    ) -> Role:
        """
        Persist new role.
        """

        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)

        return role

    def update(
        self,
        role: Role,
    ) -> Role:
        """
        Update existing role.
        """

        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)

        return role

    def delete(
        self,
        role: Role,
    ) -> None:
        """
        Delete role.
        """

        self.db.delete(role)
        self.db.commit()