"""
AI_BABA IAM Dependencies
"""

from app.modules.iam.dependencies.current_user import get_current_user
from app.modules.iam.dependencies.permissions import require_permission
from app.modules.iam.dependencies.roles import require_role

__all__ = [
    "get_current_user",
    "require_permission",
    "require_role",
]