"""
AI_BABA Authorization API

Authorization module endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends

from app.modules.authorization.dependencies.authorize import (
    authorize,
)

from app.modules.iam.models.user import User


router = APIRouter(
    prefix="/authorization",
    tags=["Authorization"],
)


@router.get(
    "/health",
)
def authorization_health() -> dict[str, str]:
    """
    Authorization service health check.
    """

    return {
        "service": "authorization",
        "status": "healthy",
    }


@router.get(
    "/check/{permission_code}",
)
def check_permission(
    permission_code: str,
    current_user: User = Depends(
        authorize(
            "system:authorization"
        )
    ),
) -> dict[str, str]:
    """
    Example protected authorization endpoint.
    """

    return {
        "permission": permission_code,
        "status": "allowed",
        "user": current_user.username,
    }