"""
AI_BABA Configuration Settings

Author : AI_BABA
Python : 3.13+
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from .env
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ============================================================
    # Application
    # ============================================================

    APP_NAME: str = Field(default="AI_BABA")
    APP_VERSION: str = Field(default="1.0.0")
    APP_DESCRIPTION: str = Field(
        default="Enterprise AI Platform"
    )

    DEBUG: bool = Field(default=True)

    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    API_PREFIX: str = Field(default="/api/v1")

    # ============================================================
    # Database
    # ============================================================

    DATABASE_HOST: str = Field(default="localhost")
    DATABASE_PORT: int = Field(default=5432)
    DATABASE_NAME: str = Field(default="ai_baba")
    DATABASE_USER: str = Field(default="postgres")
    DATABASE_PASSWORD: str = Field(default="postgres")

    DATABASE_URL: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/ai_baba"
    )

    DATABASE_ECHO: bool = Field(default=False)

    # ============================================================
    # Security
    # ============================================================

    SECRET_KEY: str = Field(
        default="CHANGE_THIS_SECRET_IN_PRODUCTION"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)

    ALGORITHM: str = Field(default="HS256")

    # ============================================================
    # Redis
    # ============================================================

    REDIS_HOST: str = Field(default="localhost")
    REDIS_PORT: int = Field(default=6379)

    REDIS_URL: str = Field(
        default="redis://localhost:6379/0"
    )

    # ============================================================
    # Celery
    # ============================================================

    CELERY_BROKER_URL: str = Field(
        default="redis://localhost:6379/0"
    )

    CELERY_RESULT_BACKEND: str = Field(
        default="redis://localhost:6379/0"
    )

    # ============================================================
    # AI Providers
    # ============================================================

    OPENAI_API_KEY: str = Field(default="")

    GEMINI_API_KEY: str = Field(default="")

    ANTHROPIC_API_KEY: str = Field(default="")

    GROK_API_KEY: str = Field(default="")

    DEEPSEEK_API_KEY: str = Field(default="")

    # ============================================================
    # Logging
    # ============================================================

    LOG_LEVEL: str = Field(default="INFO")

    LOG_FILE: str = Field(default="logs/ai_baba.log")


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """
    return Settings()


settings = get_settings()
