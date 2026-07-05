from sqlalchemy import delete, select, update
from src.core.data_base import SessionDep
from src.modules.session.model import Session
from src.modules.session.schemas import SessionCreate, SessionPatch, SessionResponse
class SessionService:
    @staticmethod
    async def create_session(payload: SessionCreate, session: SessionDep):
        new_session=Session(**payload.model_dump())
        session.add(new_session)
        await session.commit()
        return SessionResponse.model_validate(new_session)
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        result=await session.execute(select(Session).where(Session.id == id))
        session_orm=result.scalar_one_or_none()
        if not session_orm:
            return None
        return SessionResponse.model_validate(session_orm)
    @staticmethod
    async def get_all_sessions(session: SessionDep, limit, offset):
        result=await session.execute(select(Session).limit(limit).offset(offset))
        session_list_orm=result.scalars().all()
        return [SessionResponse.model_validate(s) for s in session_list_orm]
    @staticmethod
    async def delete_session(id: int, session: SessionDep):
        await session.execute(delete(Session).where(Session.id == id))
        await session.commit()
    @staticmethod
    async def update_session(id: int, payload: SessionPatch, session: SessionDep):
        result=await session.execute(
            update(Session)
            .where(Session.id == id)
            .values(**payload.model_dump(exclude_unset=True))
            .returning(Session)
        )
        session_orm=result.scalar_one()
        await session.commit()
        return SessionResponse.model_validate(session_orm)