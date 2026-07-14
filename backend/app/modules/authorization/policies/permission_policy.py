"""
AI_BABA Permission Policy

Enterprise authorization policy definitions.

Central place for permission rules.
"""

from __future__ import annotations

from app.modules.iam.models.user import User


class PermissionPolicy:
    """
    Enterprise permission policy engine.

    Future extensions:
    - Tenant based policies
    - Organization rules
    - Resource ownership checks
    - AI agent permissions
    """

    @staticmethod
    def can_access(
        user: User,
        permission_code: str,
    ) -> bool:
        """
        Evaluate permission access.

        Superusers bypass normal checks.
        """

        if user.is_superuser:
            return True

        return any(
            permission.code == permission_code
            for role in user.roles
            for permission in role.permissions
        )