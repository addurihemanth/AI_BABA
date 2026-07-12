"""
AI_BABA Role Schemas

Enterprise API schemas for Role management.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class RoleCreate(BaseModel):
    """
    Role creation request.
    """

    name: str
    code: str
    description: str | None = None
    is_system: bool = False


class RoleUpdate(BaseModel):
    """
    Role update request.
    """

    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class RoleResponse(BaseModel):
    """
    Role response.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    name: str
    code: str
    description: str | None
    is_system: bool
    is_active: bool