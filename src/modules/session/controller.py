from fastapi import HTTPException
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.area.services import AreaService
from src.modules.session.schemas import SessionCreate, SessionPatch
from src.modules.session.services import SessionService
from src.modules.stage.services import StageService
class SessionController:
    @staticmethod
    async def create_session(payload: SessionCreate, session: SessionDep):
        stage=await StageService.get_by_id(payload.stage_id, session)
        if not stage:
            raise HTTPException(status_code=404, detail="stage not found")
        if payload.area_id is not None:
            area=await AreaService.get_by_id(payload.area_id, session)
            if not area:
                raise HTTPException(status_code=404, detail="area not found")
        new_session = await SessionService.create_session(payload, session)
        return IResponse(code=201, message="Session created", data=new_session)
    @staticmethod
    async def get_all_sessions(session: SessionDep, limit: int, offset: int):
        sessions=await SessionService.get_all_sessions(session, limit, offset)
        return IResponse(
            code=200, message="Sessions retrieved", data=sessions, limit=limit, offset=offset
        )
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        session_data=await SessionService.get_by_id(id, session)
        if not session_data:
            raise HTTPException(status_code=404, detail="session not found")
        return IResponse(code=200, message="Session retrieved", data=session_data)
    @staticmethod
    async def delete_session(id: int, session: SessionDep):
        session_data=await SessionService.get_by_id(id, session)
        if not session_data:
            raise HTTPException(status_code=404, detail="session not found")
        await SessionService.delete_session(id, session)
    @staticmethod
    async def update_session(id: int, payload: SessionPatch, session: SessionDep):
        session_data=await SessionService.get_by_id(id, session)
        if not session_data:
            raise HTTPException(status_code=404, detail="session not found")
        new_session=await SessionService.update_session(id, payload, session)
        return IResponse(code=200, message="Session updated", data=new_session)