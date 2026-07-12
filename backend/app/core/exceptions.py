"""
AI_BABA Enterprise Exception Framework

Centralized exception hierarchy and global exception handlers.
"""

from __future__ import annotations

import logging
import traceback
from typing import Any

from fastapi import Request, status
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


class AIBABAException(Exception):
    """
    Base exception for AI_BABA.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "AI_BABA_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:

        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}

        super().__init__(message)


class ValidationException(AIBABAException):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_code="VALIDATION_ERROR",
        )


class AuthenticationException(AIBABAException):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code="AUTHENTICATION_ERROR",
        )


class AuthorizationException(AIBABAException):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="AUTHORIZATION_ERROR",
        )


class ResourceNotFoundException(AIBABAException):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="RESOURCE_NOT_FOUND",
        )


class ConflictException(AIBABAException):
    def __init__(self, message: str) -> None:
        super().__init__(
            message=message,
            status_code=status.HTTP_409_CONFLICT,
            error_code="RESOURCE_CONFLICT",
        )


async def global_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """
    Global exception handler.
    """

    if isinstance(exc, AIBABAException):

        logger.warning(
            "%s | %s",
            exc.error_code,
            exc.message,
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.message,
                "error": {
                    "code": exc.error_code,
                    "details": exc.details,
                },
            },
        )

    logger.exception(
        "Unhandled Exception\n%s",
        traceback.format_exc(),
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "Internal Server Error",
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
            },
        },
    )