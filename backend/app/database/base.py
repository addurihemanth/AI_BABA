"""
AI_BABA Database Base

This module defines the SQLAlchemy Declarative Base class
used by every database model.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.
    """

    pass