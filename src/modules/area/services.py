from sqlalchemy import delete, select, update
from src.core.data_base import SessionDep
from src.modules.area.model import Area, AreaTutor
from src.modules.area.schemas import AreaCreate, AreaPatch, AreaResponse
class AreaService:
    @staticmethod
    async def create_area(payload: AreaCreate, session: SessionDep):
        area=Area(**payload.model_dump())
        session.add(area)
        await session.commit()
        return AreaResponse.model_validate(area)
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        area=await session.execute(select(Area).where(Area.id == id))
        area_orm=area.scalar_one_or_none()
        if not area_orm:
            return None
        return AreaResponse.model_validate(area_orm)
    @staticmethod
    async def get_all_areas(session: SessionDep, limit, offset):
        area_list=await session.execute(select(Area).limit(limit).offset(offset))
        area_list_orm=area_list.scalars().all()
        return [AreaResponse.model_validate(area) for area in area_list_orm]
    @staticmethod
    async def delete_area(id: int, session: SessionDep):
        await session.execute(delete(Area).where(Area.id == id))
        await session.commit()
    @staticmethod
    async def update_area(id: int, payload: AreaPatch, session: SessionDep):
        area=await session.execute(
            update(Area)
            .where(Area.id ==id)
            .values(**payload.model_dump(exclude_unset=True))
            .returning(Area)
        )
        area_orm=area.scalar_one()
        await session.commit()
        return AreaResponse.model_validate(area_orm)
    @staticmethod
    async def add_tutor(area_id: int, user_id: int, session: SessionDep):
        area_tutor=AreaTutor(area_id=area_id, user_id=user_id)
        session.add(area_tutor)
        await session.commit()
    @staticmethod
    async def remove_tutor(area_id: int, user_id: int, session: SessionDep):
        await session.execute(
            delete(AreaTutor).where(
                AreaTutor.area_id ==area_id, AreaTutor.user_id == user_id
            )
        )
        await session.commit()