"""
AI_BABA Password Security

Enterprise password hashing and verification service.
"""

from __future__ import annotations

from passlib.context import CryptContext


class PasswordService:
    """
    Central password hashing service.
    """

    _context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto",
    )

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Generate a secure password hash.
        """
        return cls._context.hash(password)

    @classmethod
    def verify_password(
        cls,
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        """
        Verify a plain password against its hash.
        """
        return cls._context.verify(
            plain_password,
            hashed_password,
        )

    @classmethod
    def needs_rehash(
        cls,
        hashed_password: str,
    ) -> bool:
        """
        Check whether the stored hash should be upgraded.
        """
        return cls._context.needs_update(
            hashed_password,
        )