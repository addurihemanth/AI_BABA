"""
AI_BABA Database Table Creator

Registers all SQLAlchemy models and creates database tables.
"""

from __future__ import annotations

import logging

from sqlalchemy.exc import SQLAlchemyError

# Import Base and Engine
from app.database.base import Base
from app.database.session import engine

# Import ALL models here
from app.models.user import User  # noqa: F401


logger = logging.getLogger(__name__)


def create_tables() -> None:
    """
    Create all database tables.
    """

    try:
        Base.metadata.create_all(bind=engine)

        logger.info("All database tables created successfully.")

        print("======================================")
        print(" AI_BABA DATABASE INITIALIZATION")
        print("======================================")
        print("Status : SUCCESS")
        print("Tables : CREATED")
        print("======================================")

    except SQLAlchemyError as exc:
        logger.exception("Database initialization failed.")

        raise RuntimeError(
            f"Unable to create database tables: {exc}"
        ) from exc


if __name__ == "__main__":
    create_tables()