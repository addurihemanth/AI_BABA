"""
AI_BABA Token Service

Enterprise JWT Access & Refresh Token Service.
"""

from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Any

import jwt
from jwt import ExpiredSignatureError
from jwt import InvalidTokenError

from app.config.settings import settings


class TokenService:
    """
    Enterprise JWT Token Service.
    """

    @classmethod
    def create_access_token(
        cls,
        subject: str,
        expires_minutes: int | None = None,
        extra_claims: dict[str, Any] | None = None,
    ) -> str:
        """
        Create an access token.
        """

        expires = datetime.now(timezone.utc) + timedelta(
            minutes=expires_minutes
            or settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload: dict[str, Any] = {
            "sub": subject,
            "type": "access",
            "iat": datetime.now(timezone.utc),
            "exp": expires,
        }

        if extra_claims:
            payload.update(extra_claims)

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )

    @classmethod
    def create_refresh_token(
        cls,
        subject: str,
        days: int = 30,
    ) -> str:
        """
        Create a refresh token.
        """

        expires = datetime.now(timezone.utc) + timedelta(
            days=days,
        )

        payload = {
            "sub": subject,
            "type": "refresh",
            "iat": datetime.now(timezone.utc),
            "exp": expires,
        }

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )

    @classmethod
    def decode_token(
        cls,
        token: str,
    ) -> dict[str, Any]:
        """
        Decode and validate a JWT token.
        """

        try:

            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM],
            )

            return payload

        except ExpiredSignatureError as exc:
            raise ValueError(
                "Token has expired."
            ) from exc

        except InvalidTokenError as exc:
            raise ValueError(
                "Invalid token."
            ) from exc

    @classmethod
    def get_subject(
        cls,
        token: str,
    ) -> str:
        """
        Return token subject.
        """

        payload = cls.decode_token(token)

        subject = payload.get("sub")

        if subject is None:
            raise ValueError(
                "Token subject is missing."
            )

        return str(subject)

    @classmethod
    def is_access_token(
        cls,
        token: str,
    ) -> bool:
        """
        Check whether token is an access token.
        """

        payload = cls.decode_token(token)

        return payload.get("type") == "access"

    @classmethod
    def is_refresh_token(
        cls,
        token: str,
    ) -> bool:
        """
        Check whether token is a refresh token.
        """

        payload = cls.decode_token(token)

        return payload.get("type") == "refresh"