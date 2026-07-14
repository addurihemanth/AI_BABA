"""
AI_BABA Authorization Tests

Tests for authorization service and permission policies.
"""

from __future__ import annotations

import pytest

from app.modules.authorization.policies.permission_policy import (
    PermissionPolicy,
)


class MockPermission:
    """
    Mock permission entity.
    """

    def __init__(
        self,
        code: str,
    ) -> None:
        self.code = code


class MockRole:
    """
    Mock role entity.
    """

    def __init__(
        self,
        permissions: list[MockPermission],
    ) -> None:
        self.permissions = permissions


class MockUser:
    """
    Mock user entity.
    """

    def __init__(
        self,
        *,
        is_superuser: bool = False,
        roles: list[MockRole] | None = None,
    ) -> None:

        self.is_superuser = is_superuser
        self.roles = roles or []


def test_superuser_can_access_permission() -> None:
    """
    Superuser should bypass permission checks.
    """

    user = MockUser(
        is_superuser=True,
    )

    assert (
        PermissionPolicy.can_access(
            user,
            "news:create",
        )
        is True
    )


def test_user_with_permission_can_access() -> None:
    """
    User with permission should be allowed.
    """

    user = MockUser(
        roles=[
            MockRole(
                permissions=[
                    MockPermission(
                        "news:create",
                    )
                ]
            )
        ]
    )

    assert (
        PermissionPolicy.can_access(
            user,
            "news:create",
        )
        is True
    )


def test_user_without_permission_denied() -> None:
    """
    User without permission should be denied.
    """

    user = MockUser()

    assert (
        PermissionPolicy.can_access(
            user,
            "news:create",
        )
        is False
    )