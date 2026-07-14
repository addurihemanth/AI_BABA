"""
AI_BABA User Model

Enterprise User Entity
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
    from app.modules.audit.models.audit_log import AuditLog
    from app.modules.iam.models.role import Role
    from app.modules.iam.models.user_role import UserRole


class User(BaseModel):
    """
    Enterprise User Entity.
    """

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    first_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    last_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    # -----------------------------
    # IAM Relationships
    # -----------------------------

    user_roles: Mapped[list["UserRole"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    roles: Mapped[list["Role"]] = relationship(
        secondary="user_roles",
        viewonly=True,
    )

    # -----------------------------
    # Audit Relationships
    # -----------------------------

    audit_logs: Mapped[list["AuditLog"]] = relationship(
        back_populates="user",
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return (
            f"User("
            f"id='{self.id}', "
            f"username='{self.username}', "
            f"email='{self.email}')"
        )