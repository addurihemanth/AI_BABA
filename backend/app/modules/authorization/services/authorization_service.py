"""
AI_BABA Authorization Service

Enterprise authorization decision engine.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.modules.authorization.policies.permission_policy import (
    PermissionPolicy,
)

from app.modules.iam.models.user import User


class AuthorizationService:
    """
    Enterprise Authorization Service.

    Central authorization decision engine.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

    def has_permission(
        self,
        *,
        user: User,
        permission_code: str,
    ) -> bool:
        """
        Check whether user has permission.
        """

        return PermissionPolicy.can_access(
            user=user,
            permission_code=permission_code,
        )

    def authorize(
        self,
        *,
        user: User,
        permission_code: str,
    ) -> None:
        """
        Authorize user access.

        Raises:
            PermissionError
        """

        allowed = self.has_permission(
            user=user,
            permission_code=permission_code,
        )

        if not allowed:
            raise PermissionError(
                f"Permission denied: {permission_code}"
            )