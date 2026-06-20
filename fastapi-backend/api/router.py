from fastapi import APIRouter

from api.endpoints import predict, health, root

api_router = APIRouter()

api_router.include_router(predict.router)
api_router.include_router(health.router)
api_router.include_router(root.router)