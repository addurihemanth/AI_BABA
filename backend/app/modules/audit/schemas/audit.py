"""
AI_BABA Audit Schemas

Enterprise audit request and response models.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class AuditCreateRequest(BaseModel):
    """
    Audit event creation schema.
    """

    user_id: str | None = Field(
        default=None,
    )

    event_type: str = Field(
        ...,
        examples=[
            "AUTHORIZATION",
        ],
    )

    action: str = Field(
        ...,
        examples=[
            "permission_check",
        ],
    )

    resource: str | None = Field(
        default=None,
    )

    permission_code: str | None = Field(
        default=None,
        examples=[
            "news:create",
        ],
    )

    status: str = Field(
        ...,
        examples=[
            "SUCCESS",
            "FAILED",
        ],
    )

    ip_address: str | None = None

    details: str | None = None


class AuditResponse(BaseModel):
    """
    Audit event response schema.
    """

    id: str

    user_id: str | None

    event_type: str

    action: str

    resource: str | None

    permission_code: str | None

    status: str

    created_at: datetime

    model_config = {
        "from_attributes": True,
    }