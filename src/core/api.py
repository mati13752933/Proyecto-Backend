from fastapi import APIRouter
from src.modules.health.routes import router as health_router
api=APIRouter()
api.include_router(health_router, prefix="/health-check", tags=["Health"])