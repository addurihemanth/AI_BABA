"""
AI_BABA User Role Repository

Enterprise repository for user-role assignments.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.shared.repositories.base import BaseRepository

from app.modules.iam.models.user_role import UserRole


class UserRoleRepository(BaseRepository[UserRole]):
    """
    Repository for managing user-role mappings.
    """

    def __init__(self, db: Session) -> None:
        super().__init__(
            db=db,
            model=UserRole,
        )

    def assign_role(
        self,
        user_role: UserRole,
    ) -> UserRole:
        self.db.add(user_role)
        self.db.commit()
        self.db.refresh(user_role)

        return user_role

    def remove_role(
        self,
        user_id: str,
        role_id: str,
    ) -> bool:
        statement = (
            select(UserRole)
            .where(
                UserRole.user_id == user_id,
                UserRole.role_id == role_id,
            )
            .limit(1)
        )

        record = self.db.scalar(statement)

        if record is None:
            return False

        self.db.delete(record)
        self.db.commit()

        return True

    def has_role(
        self,
        user_id: str,
        role_id: str,
    ) -> bool:
        statement = (
            select(UserRole)
            .where(
                UserRole.user_id == user_id,
                UserRole.role_id == role_id,
            )
            .limit(1)
        )

        return self.db.scalar(statement) is not None