from src.core.data_base import SessionDep
from fastapi.security import OAuth2PasswordRequestForm
from src.modules.user.services import UserService
from fastapi import HTTPException
from src.modules.auth.services import AuthService
class AuthController:
    @staticmethod
    async def login(session: SessionDep, form_data: OAuth2PasswordRequestForm):
        password=form_data.password.strip()
        if len(password)<=7:
            raise HTTPException(status_code=400, detail="password small")
        user=await UserService.authenticate(form_data.username, password, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not founded")
        jwt_token=AuthService.login(user)
        return jwt_token