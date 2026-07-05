from fastapi import APIRouter
from src.modules.health.routes import router as health_router
from src.modules.user.routes import router as user_router
from src.modules.area.routes import router as area_router
from src.modules.stage.routes import router as stage_router
from src.modules.session.routes import router as session_router
from src.modules.submission.routes import router as submission_router
from src.modules.auth.routes import router as auth_router
api=APIRouter()
api.include_router(health_router, prefix="/health-check", tags=["Health"])
api.include_router(user_router, prefix="/user", tags=["User"])
api.include_router(area_router, prefix="/area", tags=["Area"])
api.include_router(stage_router, prefix="/stage", tags=["Stage"])
api.include_router(session_router, prefix="/session", tags=["Session"])
api.include_router(submission_router, prefix="/submission", tags=["Submission"])
api.include_router(auth_router, prefix="", tags=["Auth"])