from pydantic import BaseModel, ConfigDict
class SessionBase(BaseModel):
    title: str
    description: str
    link: str
    area_id: int
class SessionCreate(SessionBase):
    pass
class SessionResponse(SessionBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
class SessionPatch(BaseModel):
    title: str | None =None
    description: str | None=None
    link: str | None=None
    area_id: int | None=None