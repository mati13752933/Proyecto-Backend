from fastapi import APIRouter
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.user.controller import UserController
from src.modules.user.schemas import UserCreate, UserPatch
router=APIRouter()
@router.get("/", status_code=200, response_model=IResponse)
async def get_all(session: SessionDep):
    return await UserController.get_all(session)
@router.get("/{id}", status_code=200, response_model=IResponse)
async def get_by_id(id: int, session: SessionDep):
    return await UserController.get_by_id(id, session)
@router.post("/", status_code=201, response_model=IResponse)
async def create_user(payload: UserCreate, session: SessionDep):
    return await UserController.create_user(payload, session)
@router.patch("/{id}", status_code=200, response_model=IResponse)
async def update_user(id: int, payload: UserPatch, session: SessionDep):
    return await UserController.update_user(id, payload, session)
@router.delete("/{id}", status_code=204)
async def delete_user(id: int, session: SessionDep):
    await UserController.delete_user(id, session)