"""
AI_BABA Standard API Responses

Enterprise response models used across the platform.
"""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """
    Standard API response model.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="forbid",
    )

    success: bool
    message: str
    data: T | None = None
    errors: list[str] = []
    metadata: dict[str, Any] | None = None


class SuccessResponse(ApiResponse[T]):
    """
    Success response.
    """

    success: bool = True


class ErrorResponse(ApiResponse[None]):
    """
    Error response.
    """

    success: bool = False
    data: None = None