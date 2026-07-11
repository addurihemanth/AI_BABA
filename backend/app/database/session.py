"""
AI_BABA Database Session

Creates the SQLAlchemy engine and session factory.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency used by FastAPI endpoints.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()