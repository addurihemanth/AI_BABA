from fastapi import APIRouter

from app.config.settings import settings


router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

