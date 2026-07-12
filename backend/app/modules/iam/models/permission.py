"""
AI_BABA Permission Model

Enterprise Permission Entity
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.shared.models.base import BaseModel


if TYPE_CHECKING:
    from app.modules.iam.models.role import Role
    from app.modules.iam.models.role_permission import RolePermission


class Permission(BaseModel):
    """
    Enterprise Permission Entity.

    Examples:

        news:create
        news:read
        news:update
        news:delete

        user:create
        role:assign
    """

    __tablename__ = "permissions"

    resource: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    code: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_system: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    # Role Permission Association

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
        cascade="all, delete-orphan",
    )

    # Convenience Relationship

    roles: Mapped[list["Role"]] = relationship(
        secondary="role_permissions",
        viewonly=True,
    )

    def __repr__(self) -> str:
        return (
            f"Permission("
            f"id='{self.id}', "
            f"code='{self.code}')"
        )