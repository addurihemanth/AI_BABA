"""
AI_BABA Migration Service
"""

from __future__ import annotations

from app.database.migration import MigrationManager


class MigrationService:

    def __init__(
        self,
        manager: MigrationManager | None = None,
    ) -> None:

        self.manager = manager or MigrationManager()

    def migrate(self) -> None:

        self.manager.upgrade()

    def rollback(
        self,
        revision: str,
    ) -> None:

        self.manager.downgrade(
            revision,
        )

    def create_revision(
        self,
        message: str,
    ) -> None:

        self.manager.revision(
            message,
        )