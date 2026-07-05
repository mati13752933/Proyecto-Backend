from typing import Generic, TypeVar
from pydantic import BaseModel
T = TypeVar("T")
class IResponse(BaseModel, Generic[T]):
    ok: bool=True
    code : int
    message: str
    data: T | None = None
    offset: int | None = None
    limit: int | None = None
    