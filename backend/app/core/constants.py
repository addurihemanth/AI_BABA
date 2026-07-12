"""
AI_BABA Global Constants
"""

from __future__ import annotations

from enum import StrEnum


class TokenType(StrEnum):
    ACCESS = "access"
    REFRESH = "refresh"


class UserStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    LOCKED = "locked"
    PENDING = "pending"


class LogLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


DEFAULT_TIMEZONE = "Asia/Kolkata"

API_VERSION = "v1"

REQUEST_ID_HEADER = "X-Request-ID"

CORRELATION_ID_HEADER = "X-Correlation-ID"