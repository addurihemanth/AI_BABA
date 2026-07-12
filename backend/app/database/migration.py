"""
AI_BABA Migration Manager

Enterprise Alembic integration using the Alembic Python API.
"""

from __future__ import annotations

from pathlib import Path

from alembic import command
from alembic.config import Config


class MigrationManager:
    """
    Enterprise Alembic Migration Manager.
    """

    def __init__(self) -> None:

        project_root = Path(__file__).resolve().parents[2]

        self.config = Config(
            str(project_root / "alembic.ini")
        )

    def upgrade(
        self,
        revision: str = "head",
    ) -> None:

        command.upgrade(
            self.config,
            revision,
        )

    def downgrade(
        self,
        revision: str,
    ) -> None:

        command.downgrade(
            self.config,
            revision,
        )

    def revision(
        self,
        message: str,
        autogenerate: bool = True,
    ) -> None:

        command.revision(
            self.config,
            message=message,
            autogenerate=autogenerate,
        )

    def history(self) -> None:

        command.history(
            self.config,
        )

    def current(self) -> None:

        command.current(
            self.config,
        )