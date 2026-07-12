from fastapi import FastAPI

from app.api.router import api_router
from app.config.settings import settings
from app.core.exceptions import global_exception_handler

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }