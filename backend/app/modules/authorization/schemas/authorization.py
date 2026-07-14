"""
AI_BABA Authorization Schemas

Enterprise authorization request and response models.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field


class AuthorizationRequest(BaseModel):
    """
    Authorization decision request.
    """

    permission_code: str = Field(
        ...,
        examples=[
            "news:create",
        ],
    )


class AuthorizationResponse(BaseModel):
    """
    Authorization decision response.
    """

    allowed: bool

    permission_code: str

    message: str