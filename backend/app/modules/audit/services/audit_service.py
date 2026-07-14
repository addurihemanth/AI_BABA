"""
AI_BABA Audit Service

Enterprise audit event management service.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.audit.models.audit_log import (
    AuditLog,
)

from app.modules.audit.repositories.audit_repository import (
    AuditRepository,
)


class AuditService:
    """
    Central audit event service.

    Used by:
    - Authentication
    - Authorization
    - Admin operations
    - AI workflows
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.repository = AuditRepository(
            db,
        )

    def record_event(
        self,
        *,
        event_type: str,
        action: str,
        status: str,
        user_id: str | None = None,
        resource: str | None = None,
        permission_code: str | None = None,
        ip_address: str | None = None,
        details: str | None = None,
    ) -> AuditLog:
        """
        Create an audit event.
        """

        audit_log = AuditLog(
            user_id=user_id,
            event_type=event_type,
            action=action,
            resource=resource,
            permission_code=permission_code,
            status=status,
            ip_address=ip_address,
            details=details,
        )

        return self.repository.create(
            audit_log,
        )

    def record_authorization_success(
        self,
        *,
        user_id: str,
        permission_code: str,
    ) -> AuditLog:
        """
        Record successful authorization.
        """

        return self.record_event(
            event_type="AUTHORIZATION",
            action="permission_check",
            status="SUCCESS",
            user_id=user_id,
            permission_code=permission_code,
        )

    def record_authorization_failure(
        self,
        *,
        user_id: str,
        permission_code: str,
    ) -> AuditLog:
        """
        Record failed authorization.
        """

        return self.record_event(
            event_type="AUTHORIZATION",
            action="permission_check",
            status="FAILED",
            user_id=user_id,
            permission_code=permission_code,
        )