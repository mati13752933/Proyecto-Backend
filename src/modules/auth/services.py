from pwdlib import PasswordHash
from datetime import datetime, timedelta
import jwt
from src.core.config import config
from src.modules.user.schemas import UserResponse
class AuthService:
    @staticmethod
    def login(user: UserResponse):
        iat=datetime.now()
        exp=iat+timedelta(hours=config.hours_session)
        payload={"sub": user.email, "iat": str(iat), "exp": str(exp)}
        token=jwt.encode(
            payload=payload, algorithm=config.algorithm, key=config.secret_key
        )
        return "Bearer "+token
    @staticmethod
    def hash_password(password: str):
        return PasswordHash.recommended().hash(password)