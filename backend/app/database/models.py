"""
AI_BABA Database Models Registry

Loads all SQLAlchemy models for migrations.
"""

from app.modules.iam.models.user import User
from app.modules.iam.models.role import Role
from app.modules.iam.models.permission import Permission
from app.modules.iam.models.role_permission import RolePermission
from app.modules.iam.models.user_role import UserRole

from app.modules.audit.models.audit_log import AuditLog


__all__ = [
    "User",
    "Role",
    "Permission",
    "RolePermission",
    "UserRole",
    "AuditLog",
]