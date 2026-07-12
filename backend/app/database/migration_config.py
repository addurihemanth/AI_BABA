"""
AI_BABA Migration Configuration
"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ALEMBIC_INI = PROJECT_ROOT / "alembic.ini"

MIGRATIONS_DIRECTORY = PROJECT_ROOT / "migrations"