from fastapi import APIRouter
from src.modules.health.controllers import ControllerHealth
router = APIRouter()
@router.get("/")
def health_check():
    return ControllerHealth.health_check()