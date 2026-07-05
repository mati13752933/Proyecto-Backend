from fastapi import APIRouter, status
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.session.controller import SessionController
from src.modules.session.schemas import SessionCreate, SessionPatch
router=APIRouter()
@router.get("/", status_code=200, response_model=IResponse)
async def get_all_sessions(session: SessionDep, limit: int = 2, offset: int = 0):
    return await SessionController.get_all_sessions(session, limit, offset)
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def get_by_id(id: int, session: SessionDep):
    return await SessionController.get_by_id(id, session)
@router.post("/", status_code=201, response_model=IResponse)
async def create_session(session: SessionDep, payload: SessionCreate):
    return await SessionController.create_session(payload, session)
@router.delete("/{id}", status_code=204)
async def delete_session(session: SessionDep, id: int):
    await SessionController.delete_session(id, session)
@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def patch_session(session: SessionDep, id: int, payload: SessionPatch):
    return await SessionController.update_session(id, payload, session)