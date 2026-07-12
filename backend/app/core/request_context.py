"""
AI_BABA Request Context
"""

from __future__ import annotations

from contextvars import ContextVar
from uuid import uuid4

_request_id: ContextVar[str] = ContextVar(
    "request_id",
    default="",
)


def create_request_id() -> str:
    request_id = str(uuid4())
    _request_id.set(request_id)
    return request_id


def get_request_id() -> str:
    return _request_id.get()


def set_request_id(request_id: str) -> None:
    _request_id.set(request_id)

    