from fastapi import APIRouter, status
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.stage.controller import StageController
from src.modules.stage.schemas import StageCreate, StagePatch
router=APIRouter()
@router.get("/", status_code=200, response_model=IResponse)
async def get_all_stages(session: SessionDep, limit: int = 4, offset: int = 0):
    return await StageController.get_all_stages(session, limit, offset)
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def get_by_id(id: int, session: SessionDep):
    return await StageController.get_by_id(id, session)
@router.post("/", status_code=201, response_model=IResponse)
async def create_stage(session: SessionDep, payload: StageCreate):
    return await StageController.create_stage(payload, session)
@router.delete("/{id}", status_code=204)
async def delete_stage(session: SessionDep, id: int):
    await StageController.delete_stage(id, session)
@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def patch_stage(session: SessionDep, id: int, payload: StagePatch):
    return await StageController.update_stage(id, payload, session)
@router.post("/{stage_id}/tutors/{user_id}", status_code=204)
async def add_tutor(stage_id: int, user_id: int, session: SessionDep):
    await StageController.add_tutor(stage_id, user_id, session)
@router.delete("/{stage_id}/tutors/{user_id}", status_code=204)
async def remove_tutor(stage_id: int, user_id: int, session: SessionDep):
    await StageController.remove_tutor(stage_id, user_id, session)