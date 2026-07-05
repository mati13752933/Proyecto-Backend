from fastapi import HTTPException
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.stage.schemas import StageCreate, StagePatch
from src.modules.stage.services import StageService
from src.modules.user.services import UserService
class StageController:
    @staticmethod
    async def create_stage(payload: StageCreate, session: SessionDep):
        stage=await StageService.create_stage(payload, session)
        return IResponse(code=201, message="Stage created", data=stage)
    @staticmethod
    async def get_all_stages(session: SessionDep, limit: int, offset: int):
        stages=await StageService.get_all_stages(session, limit, offset)
        return IResponse(
            code=200, message="Stages retrieved", data=stages, limit=limit, offset=offset
        )
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        stage=await StageService.get_by_id(id, session)
        if not stage:
            raise HTTPException(status_code=404, detail="stage not found")
        return IResponse(code=200, message="Stage retrieved", data=stage)
    @staticmethod
    async def delete_stage(id: int, session: SessionDep):
        stage=await StageService.get_by_id(id, session)
        if not stage:
            raise HTTPException(status_code=404, detail="stage not found")
        await StageService.delete_stage(id, session)
    @staticmethod
    async def update_stage(id: int, payload: StagePatch, session: SessionDep):
        stage=await StageService.get_by_id(id, session)
        if not stage:
            raise HTTPException(status_code=404, detail="stage not found")
        new_stage=await StageService.update_stage(id, payload, session)
        return IResponse(code=200, message="Stage updated", data=new_stage)
    @staticmethod
    async def add_tutor(stage_id: int, user_id: int, session: SessionDep):
        stage=await StageService.get_by_id(stage_id, session)
        if not stage:
            raise HTTPException(status_code=404, detail="stage not found")
        user=await UserService.get_by_id(user_id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        await StageService.add_tutor(stage_id, user_id, session)
    @staticmethod
    async def remove_tutor(stage_id: int, user_id: int, session: SessionDep):
        stage=await StageService.get_by_id(stage_id, session)
        if not stage:
            raise HTTPException(status_code=404, detail="stage not found")
        user=await UserService.get_by_id(user_id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        await StageService.remove_tutor(stage_id, user_id, session)