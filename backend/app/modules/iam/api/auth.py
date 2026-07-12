"""
AI_BABA Authentication API

Enterprise Authentication Endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.iam.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)

from app.modules.iam.services.auth_service import (
    AuthenticationError,
    AuthService,
    UserAlreadyExistsError,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    """
    Register a new user.
    """

    service = AuthService(db)

    try:

        user = service.register(
            username=request.username,
            email=request.email,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name,
        )

        return {
            "success": True,
            "message": "User registered successfully.",
            "data": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
        }

    except UserAlreadyExistsError as exc:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    """
    Authenticate a user and return JWT tokens.
    """

    service = AuthService(db)

    try:

        return service.login(
            username=request.username,
            password=request.password,
        )

    except AuthenticationError as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc


@router.get(
    "/health",
)
def auth_health():
    """
    Authentication module health endpoint.
    """

    return {
        "service": "authentication",
        "status": "healthy",
    }