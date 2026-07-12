
 
"""
AI_BABA Permission Authorization Dependency

Enterprise Permission-Based Access Control (PBAC).
"""

from __future__ import annotations

from collections.abc import Callable

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.iam.dependencies.current_user import get_current_user
from app.modules.iam.models.user import User
from app.modules.iam.repositories.user_repository import UserRepository


def require_permission(
    permission_code: str,
) -> Callable:
    """
    Require a user to possess a specific permission.

    Example
    -------
    Depends(require_permission("news:create"))
    """

    def dependency(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db),
    ) -> User:

        repository = UserRepository(db)

        if not repository.has_permission(
            current_user.id,
            permission_code,
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    f"Permission '{permission_code}' is required."
                ),
            )

        return current_user

    return dependency