"""
AI_BABA Migration Runner
"""

from __future__ import annotations

from app.database.migration_service import MigrationService


def main() -> None:

    MigrationService().migrate()


if __name__ == "__main__":
    main()