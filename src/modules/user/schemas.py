from pydantic import BaseModel, ConfigDict, EmailStr
from src.core.enums import TypeRoles
class UserBase(BaseModel):
    email: EmailStr
    name: str
    last_name: str
    codsis: str
class UserCreate(UserBase):
    password: str
class UserResponse(UserBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
    role: TypeRoles
    area_id: int | None=None
    stage_id: int | None=None
    sigue_postulando: bool
class UserPatch(BaseModel):
    email: EmailStr | None=None
    name: str | None=None
    last_name: str | None=None
    codsis: str | None=None
    role: TypeRoles | None=None
    area_id: int | None=None
    stage_id: int | None=None
    sigue_postulando: bool | None=None
    