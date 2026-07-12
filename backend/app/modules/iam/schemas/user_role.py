"""
AI_BABA User Role Schemas

Enterprise schemas for user-role assignment.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class UserRoleAssign(BaseModel):
    """
    Assign role to user request.
    """

    user_id: str
    role_id: str


class UserRoleResponse(BaseModel):
    """
    User role response.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    user_id: str
    role_id: str