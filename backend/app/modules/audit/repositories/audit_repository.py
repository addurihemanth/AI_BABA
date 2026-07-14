"""
AI_BABA Audit Repository

Enterprise persistence layer for audit logs.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.audit.models.audit_log import AuditLog

from app.shared.repositories.base import (
    BaseRepository,
)


class AuditRepository(
    BaseRepository[AuditLog],
):
    """
    Repository for AuditLog entity.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        super().__init__(
            db=db,
            model=AuditLog,
        )

    def create(
        self,
        audit_log: AuditLog,
    ) -> AuditLog:
        """
        Store audit event.
        """

        self.db.add(
            audit_log,
        )

        self.db.commit()

        self.db.refresh(
            audit_log,
        )

        return audit_log


    def get_by_user(
        self,
        user_id: str,
    ) -> list[AuditLog]:
        """
        Retrieve audit events by user.
        """

        statement = (
            select(AuditLog)
            .where(
                AuditLog.user_id == user_id,
            )
            .order_by(
                AuditLog.created_at.desc(),
            )
        )

        return list(
            self.db.scalars(
                statement,
            ).all()
        )