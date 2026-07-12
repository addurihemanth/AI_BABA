"""
AI_BABA User Role Association Model

Enterprise User-Role Mapping Entity
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.shared.models.base import BaseModel


if TYPE_CHECKING:
    from app.modules.iam.models.user import User
    from app.modules.iam.models.role import Role


class UserRole(BaseModel):
    """
    Enterprise User Role Association.

    Maps users to assigned roles.

    Example:
        User -> ADMIN Role
        User -> EDITOR Role
    """

    __tablename__ = "user_roles"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    role_id: Mapped[str] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="user_roles",
    )

    role: Mapped["Role"] = relationship(
        back_populates="user_roles",
    )

    def __repr__(self) -> str:
        return (
            f"UserRole("
            f"user_id='{self.user_id}', "
            f"role_id='{self.role_id}')"
        )