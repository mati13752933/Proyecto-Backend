from pydantic import BaseModel, ConfigDict
class AreaBase(BaseModel):
    name: str
    description: str
class AreaCreate(AreaBase):
    pass
class AreaResponse(AreaBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
class AreaPatch(BaseModel):
    name: str | None=None
    description: str | None=None