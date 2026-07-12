"""
AI_BABA Role Model

Enterprise Role Entity
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
    from app.modules.iam.models.permission import Permission
    from app.modules.iam.models.role_permission import RolePermission
    from app.modules.iam.models.user import User
    from app.modules.iam.models.user_role import UserRole


class Role(BaseModel):
    """
    Enterprise Role Entity.

    Examples:
        SUPER_ADMIN
        ADMIN
        EDITOR
        NEWS_MANAGER
        USER
    """

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    code: Mapped[str] = mapped_column(
        String(100),
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

    # User Role Association

    user_roles: Mapped[list["UserRole"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan",
    )

    # Role Permission Association

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan",
    )

    # Convenience Relationships

    users: Mapped[list["User"]] = relationship(
        secondary="user_roles",
        viewonly=True,
    )

    permissions: Mapped[list["Permission"]] = relationship(
        secondary="role_permissions",
        viewonly=True,
    )

    def __repr__(self) -> str:
        return (
            f"Role("
            f"id='{self.id}', "
            f"code='{self.code}', "
            f"name='{self.name}')"
        )