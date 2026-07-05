from pydantic import BaseModel, ConfigDict
class SessionBase(BaseModel):
    title: str
    description: str
    link: str | None=None
    stage_id: int
    area_id: int | None=None
class SessionCreate(SessionBase):
    pass
class SessionResponse(SessionBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
class SessionPatch(BaseModel):
    title: str | None =None
    description: str | None=None
    link: str | None=None
    stage_id: int | None=None
    area_id: int | None=None