"""
AI_BABA User Repository

Enterprise repository for User entity.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.shared.repositories.base import BaseRepository

from app.modules.iam.models.permission import Permission
from app.modules.iam.models.role import Role
from app.modules.iam.models.role_permission import RolePermission
from app.modules.iam.models.user import User
from app.modules.iam.models.user_role import UserRole


class UserRepository(BaseRepository[User]):
    """
    Enterprise repository responsible for all
    User persistence operations.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        super().__init__(
            db=db,
            model=User,
        )

    def get_by_id(
        self,
        user_id: str,
    ) -> User | None:
        """
        Retrieve user by primary key.
        """

        return self.db.get(
            User,
            user_id,
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Retrieve user by email.
        """

        statement = (
            select(User)
            .where(User.email == email)
            .limit(1)
        )

        return self.db.scalar(statement)

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        """
        Retrieve user by username.
        """

        statement = (
            select(User)
            .where(User.username == username)
            .limit(1)
        )

        return self.db.scalar(statement)

    def exists_by_email(
        self,
        email: str,
    ) -> bool:
        """
        Check whether email exists.
        """

        return self.get_by_email(email) is not None

    def exists_by_username(
        self,
        username: str,
    ) -> bool:
        """
        Check whether username exists.
        """

        return self.get_by_username(username) is not None

    def get_roles(
        self,
        user_id: str,
    ) -> list[Role]:
        """
        Return all roles assigned to a user.
        """

        statement = (
            select(User)
            .options(
                selectinload(
                    User.user_roles,
                )
                .selectinload(
                    UserRole.role,
                )
                .selectinload(
                    Role.role_permissions,
                )
                .selectinload(
                    RolePermission.permission,
                )
            )
            .where(
                User.id == user_id,
            )
        )

        user = self.db.scalar(statement)

        if user is None:
            return []

        return [
            user_role.role
            for user_role in user.user_roles
        ]

    def get_permissions(
        self,
        user_id: str,
    ) -> list[Permission]:
        """
        Return every permission
        assigned to the user.
        """

        permissions: dict[str, Permission] = {}

        for role in self.get_roles(user_id):

            for role_permission in role.role_permissions:

                permission = role_permission.permission

                permissions[
                    permission.code
                ] = permission

        return list(
            permissions.values()
        )

    def has_role(
        self,
        user_id: str,
        role_code: str,
    ) -> bool:
        """
        Check whether user has a role.
        """

        return any(
            role.code == role_code
            for role in self.get_roles(user_id)
        )

    def has_permission(
        self,
        user_id: str,
        permission_code: str,
    ) -> bool:
        """
        Check whether user has a permission.
        """

        return any(
            permission.code == permission_code
            for permission in self.get_permissions(
                user_id,
            )
        )

    def create(
        self,
        user: User,
    ) -> User:
        """
        Persist new user.
        """

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def update(
        self,
        user: User,
    ) -> User:
        """
        Update existing user.
        """

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def delete(
        self,
        user: User,
    ) -> None:
        """
        Delete user.
        """

        self.db.delete(user)
        self.db.commit()

        