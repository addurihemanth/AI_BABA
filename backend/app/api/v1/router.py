"""
AI_BABA API v1 Router

Central router for API version 1.
"""

from __future__ import annotations

from fastapi import APIRouter

# Health
from app.api.v1.health import router as health_router

# IAM
from app.modules.iam.api.auth import (
    router as auth_router,
)

from app.modules.iam.api.role import (
    router as role_router,
)

from app.modules.iam.api.permission import (
    router as permission_router,
)

# Authorization
from app.modules.authorization.api.authorization import (
    router as authorization_router,
)


router = APIRouter()


# Health
router.include_router(
    health_router,
)


# Authentication
router.include_router(
    auth_router,
)


# Role Management
router.include_router(
    role_router,
)


# Permission Management
router.include_router(
    permission_router,
)

 
# Authorization
router.include_router(
    authorization_router,
)