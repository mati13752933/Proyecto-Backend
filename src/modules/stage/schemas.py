from pydantic import BaseModel, ConfigDict
class StageBase(BaseModel):
    name: str
    description: str
class StageCreate(StageBase):
    pass
class StageResponse(StageBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
class StagePatch(BaseModel):
    name: str | None=None
    description: str | None=None