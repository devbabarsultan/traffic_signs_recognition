from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    print("Welcome to the Traffic Sign Recognition API!")
    return {"message": "root endpoint is working!"}