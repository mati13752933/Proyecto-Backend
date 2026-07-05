from fastapi import HTTPException
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.user.schemas import UserCreate, UserPatch
from src.modules.user.services import UserService
class UserController:
    @staticmethod
    async def get_all(session: SessionDep):
        users=await UserService.get_all(session)
        return IResponse(code=200, message="users retrieved", data=users)
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        user=await UserService.get_by_id(id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        return IResponse(code=200, message="user retrieved", data=user)
    @staticmethod
    async def create_user(payload: UserCreate, session: SessionDep):
        user=await UserService.create_user(payload, session)
        return IResponse(code=201, message="user created", data=user)
    @staticmethod
    async def update_user(id: int, payload: UserPatch, session: SessionDep):
        user=await UserService.get_by_id(id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        user_updated=await UserService.update_user(id, payload, session)
        return IResponse(code=200, message="user updated", data=user_updated)
    @staticmethod
    async def delete_user(id: int, session: SessionDep):
        user=await UserService.get_by_id(id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        await UserService.delete_user(id, session)