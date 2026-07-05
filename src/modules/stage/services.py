from sqlalchemy import delete, select, update
from src.core.data_base import SessionDep
from src.modules.stage.model import Stage, StageTutor
from src.modules.stage.schemas import StageCreate, StagePatch, StageResponse
class StageService:
    @staticmethod
    async def create_stage(payload: StageCreate, session: SessionDep):
        stage=Stage(**payload.model_dump())
        session.add(stage)
        await session.commit()
        return StageResponse.model_validate(stage)
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        stage=await session.execute(select(Stage).where(Stage.id == id))
        stage_orm=stage.scalar_one_or_none()
        if not stage_orm:
            return None
        return StageResponse.model_validate(stage_orm)
    @staticmethod
    async def get_all_stages(session: SessionDep, limit, offset):
        stage_list=await session.execute(select(Stage).limit(limit).offset(offset))
        stage_list_orm=stage_list.scalars().all()
        return [StageResponse.model_validate(stage) for stage in stage_list_orm]
    @staticmethod
    async def delete_stage(id: int, session: SessionDep):
        await session.execute(delete(Stage).where(Stage.id == id))
        await session.commit()
    @staticmethod
    async def update_stage(id: int, payload: StagePatch, session: SessionDep):
        stage=await session.execute(
            update(Stage)
            .where(Stage.id == id)
            .values(**payload.model_dump(exclude_unset=True))
            .returning(Stage)
        )
        stage_orm=stage.scalar_one()
        await session.commit()
        return StageResponse.model_validate(stage_orm)
    @staticmethod
    async def add_tutor(stage_id: int, user_id: int, session: SessionDep):
        stage_tutor=StageTutor(stage_id=stage_id, user_id=user_id)
        session.add(stage_tutor)
        await session.commit()
    @staticmethod
    async def remove_tutor(stage_id: int, user_id: int, session: SessionDep):
        await session.execute(
            delete(StageTutor).where(
                StageTutor.stage_id == stage_id, StageTutor.user_id == user_id
            )
        )
        await session.commit()