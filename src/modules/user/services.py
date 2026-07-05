from sqlalchemy import delete, select, update
from src.core.data_base import SessionDep
from src.modules.user.model import User
from src.modules.user.schemas import UserCreate, UserPatch, UserResponse
from pwdlib import PasswordHash
class UserService:
    @staticmethod
    async def get_all(session: SessionDep):
        users=await session.execute(select(User))
        users_orm=users.scalars().all()
        return [UserResponse.model_validate(us) for us in users_orm]
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        user=await session.execute(select(User).where(User.id == id))
        user_orm=user.scalar_one_or_none()
        return None if not user_orm else UserResponse.model_validate(user_orm)
    @staticmethod
    async def create_user(payload: UserCreate, session: SessionDep):
        try:
            hashed_password=PasswordHash.recommended().hash(payload.password)
            user= User(**payload.model_dump(exclude={"password"}), password=hashed_password)
            session.add(user)
            await session.commit()
            return UserResponse.model_validate(user)
        except:
            await session.rollback()
            raise
    @staticmethod
    async def update_user(id: int, payload: UserPatch, session: SessionDep):
        try:
            user=await session.execute(
                update(User)
                .where(User.id == id)
                .values(**payload.model_dump(exclude_unset=True))
                .returning(User)
            )
            user_orm = user.scalar_one()
            await session.commit()
            return UserResponse.model_validate(user_orm)
        except:
            await session.rollback()
            raise
    @staticmethod
    async def delete_user(id: int, session: SessionDep):
        try:
            await session.execute(delete(User).where(User.id == id))
            await session.commit()
        except:
            await session.rollback()
            raise
    @staticmethod
    async def authenticate(email: str, password: str, session: SessionDep):
        user=await session.execute(select(User).where(User.email == email))
        user_orm=user.scalar_one_or_none()
        if not user_orm:
            return None
        is_valid = PasswordHash.recommended().verify(password, user_orm.password)
        if not is_valid:
            return None
        return UserResponse.model_validate(user_orm)