"""
AI_BABA Role Permission Association Model

Enterprise Role-Permission Mapping Entity
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.shared.models.base import BaseModel


if TYPE_CHECKING:
    from app.modules.iam.models.role import Role
    from app.modules.iam.models.permission import Permission


class RolePermission(BaseModel):
    """
    Enterprise Role Permission Association.

    Maps roles to permissions.
    """

    __tablename__ = "role_permissions"

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    permission_id: Mapped[str] = mapped_column(
        ForeignKey("permissions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    role: Mapped["Role"] = relationship(
        back_populates="role_permissions",
    )

    permission: Mapped["Permission"] = relationship(
        back_populates="role_permissions",
    )

    def __repr__(self) -> str:
        return (
            f"RolePermission("
            f"role_id='{self.role_id}', "
            f"permission_id='{self.permission_id}')"
        )