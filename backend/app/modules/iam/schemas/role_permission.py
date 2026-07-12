"""
AI_BABA Role Permission Schemas

Enterprise schemas for role-permission assignment.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class RolePermissionAssign(BaseModel):
    """
    Assign permission to role request.
    """

    role_id: str
    permission_id: str


class RolePermissionResponse(BaseModel):
    """
    Role permission response.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    role_id: str
    permission_id: str