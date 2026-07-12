"""
AI_BABA Current User Dependency

JWT authentication dependency.
"""

from __future__ import annotations

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.core.token_service import TokenService
from app.database.session import get_db

from app.modules.iam.repositories.user_repository import (
    UserRepository,
)

from app.modules.iam.models.user import User


bearer_scheme = HTTPBearer(
    auto_error=True,
)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme,
    ),
    db: Session = Depends(get_db),
) -> User:
    """
    Return authenticated user.
    """

    try:

        payload = TokenService.decode_token(
            credentials.credentials,
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc

    user_id = payload.get("sub")

    if user_id is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )

    repository = UserRepository(db)

    user = repository.get(user_id)

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    if not user.is_active:

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled.",
        )

    return user