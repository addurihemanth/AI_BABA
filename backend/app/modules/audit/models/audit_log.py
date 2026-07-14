"""
AI_BABA Audit Log Model

Enterprise audit event storage model.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.shared.models.base import BaseModel

if TYPE_CHECKING:
    from app.modules.iam.models.user import User


class AuditLog(BaseModel):
    """
    Enterprise Audit Log Entity.

    Stores every important security and business event.

    Examples:
    - User Login
    - User Logout
    - Failed Login
    - Permission Check
    - Role Assignment
    - Authorization Denied
    - CRUD Operations
    - System Events
    """

    __tablename__ = "audit_logs"

    user_id: Mapped[str | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    action: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    resource: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    permission_code: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    user_agent: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    details: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    user: Mapped["User | None"] = relationship(
        "User",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return (
            f"AuditLog("
            f"id='{self.id}', "
            f"user_id='{self.user_id}', "
            f"event_type='{self.event_type}', "
            f"status='{self.status}')"
        )