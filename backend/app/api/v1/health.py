from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "success": True,
        "message": "Success",
        "data": {
            "application": "AI_BABA",
            "version": "1.0.0",
            "status": "healthy",
        },
    }