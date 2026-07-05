from fastapi import HTTPException
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.area.schemas import AreaCreate, AreaPatch
from src.modules.area.services import AreaService
from src.modules.user.services import UserService
class AreaController:
    @staticmethod
    async def create_area(payload: AreaCreate, session: SessionDep):
        area=await AreaService.create_area(payload, session)
        return IResponse(code=201, message="Area created", data=area)
    @staticmethod
    async def get_all_areas(session: SessionDep, limit: int, offset: int):
        areas=await AreaService.get_all_areas(session, limit, offset)
        return IResponse(
            code=200, message="Areas retrieved", data=areas, limit=limit, offset=offset
        )
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        area=await AreaService.get_by_id(id, session)
        if not area:
            raise HTTPException(status_code=404, detail="area not found")
        return IResponse(code=200, message="Area retrieved", data=area)
    @staticmethod
    async def delete_area(id: int, session: SessionDep):
        area=await AreaService.get_by_id(id, session)
        if not area:
            raise HTTPException(status_code=404, detail="area not found")
        await AreaService.delete_area(id, session)
    @staticmethod
    async def update_area(id: int, payload: AreaPatch, session: SessionDep):
        area=await AreaService.get_by_id(id, session)
        if not area:
            raise HTTPException(status_code=404, detail="area not found")
        new_area=await AreaService.update_area(id, payload, session)
        return IResponse(code=200, message="Area updated", data=new_area)
    @staticmethod
    async def add_tutor(area_id: int, user_id: int, session: SessionDep):
        area=await AreaService.get_by_id(area_id, session)
        if not area:
            raise HTTPException(status_code=404, detail="area not found")
        user=await UserService.get_by_id(user_id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        await AreaService.add_tutor(area_id, user_id, session)
    @staticmethod
    async def remove_tutor(area_id: int, user_id: int, session: SessionDep):
        area=await AreaService.get_by_id(area_id, session)
        if not area:
            raise HTTPException(status_code=404, detail="area not found")
        user=await UserService.get_by_id(user_id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        await AreaService.remove_tutor(area_id, user_id, session)