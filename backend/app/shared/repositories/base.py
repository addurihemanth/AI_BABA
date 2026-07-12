"""
AI_BABA Repository Base

Enterprise generic repository implementation.
"""

from __future__ import annotations

from typing import Any
from typing import Generic
from typing import TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic repository used by all entities.
    """

    def __init__(
        self,
        db: Session,
        model: type[ModelType],
    ) -> None:

        self.db = db
        self.model = model

    def get(self, entity_id: Any) -> ModelType | None:
        """
        Get entity by primary key.
        """

        return self.db.get(
            self.model,
            entity_id,
        )

    def add(
        self,
        entity: ModelType,
    ) -> ModelType:

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def delete(
        self,
        entity: ModelType,
    ) -> None:

        self.db.delete(entity)
        self.db.commit()