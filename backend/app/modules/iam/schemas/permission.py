"""
AI_BABA Permission Schemas

Enterprise API schemas for Permission management.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class PermissionCreate(BaseModel):
    """
    Permission creation request.
    """

    resource: str
    action: str
    code: str
    description: str | None = None
    is_system: bool = False


class PermissionUpdate(BaseModel):
    """
    Permission update request.
    """

    description: str | None = None
    is_active: bool | None = None


class PermissionResponse(BaseModel):
    """
    Permission response.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    resource: str
    action: str
    code: str
    description: str | None
    is_system: bool
    is_active: bool