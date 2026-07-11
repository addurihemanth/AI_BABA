from fastapi import FastAPI


def register_security(app: FastAPI):

    @app.middleware("http")
    async def security_headers(request, call_next):

        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"

        return response