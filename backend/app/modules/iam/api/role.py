"""
AI_BABA Role API

Enterprise Role management endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.iam.schemas.role import RoleCreate
from app.modules.iam.schemas.role import RoleResponse

from app.modules.iam.services.role_service import RoleService


router = APIRouter(
    prefix="/roles",
    tags=["IAM - Roles"],
)


@router.post(
    "",
    response_model=RoleResponse,
)
def create_role(
    payload: RoleCreate,
    db: Session = Depends(get_db),
) -> RoleResponse:
    """
    Create new role.
    """

    service = RoleService(db)

    return service.create_role(
        name=payload.name,
        code=payload.code,
        description=payload.description,
        is_system=payload.is_system,
    )


@router.get(
    "/{code}",
    response_model=RoleResponse,
)
def get_role(
    code: str,
    db: Session = Depends(get_db),
) -> RoleResponse:
    """
    Get role by code.
    """

    service = RoleService(db)

    return service.get_role_by_code(
        code
    )