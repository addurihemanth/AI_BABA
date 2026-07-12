"""
AI_BABA Authentication Schemas

Enterprise Pydantic v2 Authentication Schemas.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field


class RegisterRequest(BaseModel):
    """
    User Registration Request
    """

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        validate_assignment=True,
    )

    username: str = Field(
        min_length=4,
        max_length=50,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    first_name: str | None = Field(
        default=None,
        max_length=100,
    )

    last_name: str | None = Field(
        default=None,
        max_length=100,
    )


class LoginRequest(BaseModel):
    """
    User Login Request
    """

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        validate_assignment=True,
    )

    username: str = Field(
        min_length=4,
        max_length=50,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class TokenResponse(BaseModel):
    """
    Authentication Token Response
    """

    access_token: str

    refresh_token: str

    token_type: str = "bearer"


class MessageResponse(BaseModel):
    """
    Generic API Response
    """

    success: bool

    message: str