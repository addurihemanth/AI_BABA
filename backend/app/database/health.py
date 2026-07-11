"""
AI_BABA Database Health Check

This module provides a simple database connectivity check.
"""

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.session import engine


def check_database_connection() -> tuple[bool, str]:
    """
    Verify that the database connection is working.

    Returns:
        tuple[bool, str]:
            (True, "Database connection successful")
            or
            (False, "<error message>")
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return True, "Database connection successful"

    except SQLAlchemyError as exc:
        return False, str(exc)

    except Exception as exc:
        return False, str(exc)