"""
AI_BABA Database Seeder
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.database.seed_data import DEFAULT_ROLES


class DatabaseSeeder:
    """
    Initial database seeder.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

    def seed(self) -> None:
        """
        Seed initial system data.

        Role seeding will be enabled
        after the RBAC models are created.
        """

        _ = DEFAULT_ROLES