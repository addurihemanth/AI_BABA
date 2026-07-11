from fastapi import FastAPI

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


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }