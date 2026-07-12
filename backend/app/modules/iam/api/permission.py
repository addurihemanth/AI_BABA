"""
AI_BABA Permission API

Enterprise Permission management endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.iam.schemas.permission import PermissionCreate
from app.modules.iam.schemas.permission import PermissionResponse

from app.modules.iam.services.permission_service import (
    PermissionService,
)


router = APIRouter(
    prefix="/permissions",
    tags=["IAM - Permissions"],
)


@router.post(
    "",
    response_model=PermissionResponse,
)
def create_permission(
    payload: PermissionCreate,
    db: Session = Depends(get_db),
) -> PermissionResponse:
    """
    Create new permission.
    """

    service = PermissionService(db)

    return service.create_permission(
        resource=payload.resource,
        action=payload.action,
        code=payload.code,
        description=payload.description,
        is_system=payload.is_system,
    )


@router.get(
    "/{code}",
    response_model=PermissionResponse,
)
def get_permission(
    code: str,
    db: Session = Depends(get_db),
) -> PermissionResponse:
    """
    Get permission by code.
    """

    service = PermissionService(db)

    return service.get_permission_by_code(
        code
    )