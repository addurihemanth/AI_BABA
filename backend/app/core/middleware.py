"""
AI_BABA Request Middleware
"""

from __future__ import annotations

import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.request_context import create_request_id


class RequestMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):

        request_id = create_request_id()

        start = time.perf_counter()

        response = await call_next(request)

        duration = time.perf_counter() - start

        response.headers["X-Request-ID"] = request_id

        response.headers["X-Response-Time"] = (
            f"{duration:.6f}s"
        )

        return response