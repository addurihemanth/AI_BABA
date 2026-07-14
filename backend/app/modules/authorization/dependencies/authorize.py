"""
AI_BABA Authorization Dependency

Enterprise authorization dependency layer.

Connects:
FastAPI -> Current User -> Authorization Service -> Audit Service
"""

from __future__ import annotations

from collections.abc import Callable

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.authorization.services.authorization_service import (
    AuthorizationService,
)

from app.modules.iam.dependencies.current_user import (
    get_current_user,
)

from app.modules.iam.models.user import User

from app.modules.audit.services.audit_service import (
    AuditService,
)


def authorize(
    permission_code: str,
) -> Callable:
    """
    Require a permission for an API endpoint.
    """

    def dependency(
        current_user: User = Depends(
            get_current_user,
        ),
        db: Session = Depends(
            get_db,
        ),
    ) -> User:

        authorization_service = AuthorizationService(
            db,
        )

        audit_service = AuditService(
            db,
        )

        try:

            authorization_service.authorize(
                user=current_user,
                permission_code=permission_code,
            )

            audit_service.record_authorization_success(
                user_id=current_user.id,
                permission_code=permission_code,
            )

        except PermissionError as exc:

            audit_service.record_authorization_failure(
                user_id=current_user.id,
                permission_code=permission_code,
            )

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=str(exc),
            ) from exc

        return current_user

    return dependency