from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    print("Health check endpoint is working!")
    return {"status": "ok"}