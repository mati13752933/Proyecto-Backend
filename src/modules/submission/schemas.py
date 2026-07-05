from pydantic import BaseModel, ConfigDict
class SubmissionBase(BaseModel):
    link: str
    user_id: int
    session_id: int
class SubmissionCreate(SubmissionBase):
    pass
class SubmissionResponse(SubmissionBase):
    model_config=ConfigDict(from_attributes=True)
    id: int
class SubmissionPatch(BaseModel):
    link: str

