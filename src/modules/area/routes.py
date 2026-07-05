from fastapi import APIRouter, status
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.area.controller import AreaController
from src.modules.area.schemas import AreaCreate, AreaPatch
router=APIRouter()
@router.get("/", status_code=200, response_model=IResponse)
async def get_all_areas(session: SessionDep, limit: int = 2, offset: int = 0):
    return await AreaController.get_all_areas(session, limit, offset)
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def get_by_id(id: int, session: SessionDep):
    return await AreaController.get_by_id(id, session)
@router.post("/", status_code=201, response_model=IResponse)
async def create_area(session: SessionDep, payload: AreaCreate):
    return await AreaController.create_area(payload, session)
@router.delete("/{id}", status_code=204)
async def delete_area(session: SessionDep, id: int):
    await AreaController.delete_area(id, session)
@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def patch_area(session: SessionDep, id: int, payload: AreaPatch):
    return await AreaController.update_area(id, payload, session)
@router.post("/{area_id}/tutors/{user_id}", status_code=204)
async def add_tutor(area_id: int, user_id: int, session: SessionDep):
    await AreaController.add_tutor(area_id, user_id, session)
@router.delete("/{area_id}/tutors/{user_id}", status_code=204)
async def remove_tutor(area_id: int, user_id: int, session: SessionDep):
    await AreaController.remove_tutor(area_id, user_id, session)