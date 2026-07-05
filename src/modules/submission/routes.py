from fastapi import APIRouter, status
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.submission.controller import SubmissionController
from src.modules.submission.schemas import SubmissionCreate, SubmissionPatch
router=APIRouter()
@router.get("/", status_code=200, response_model=IResponse)
async def get_all_submissions(session: SessionDep, limit: int = 2, offset: int = 0):
    return await SubmissionController.get_all_submissions(session, limit, offset)
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def get_by_id(id: int, session: SessionDep):
    return await SubmissionController.get_by_id(id, session)
@router.post("/", status_code=201, response_model=IResponse)
async def create_submission(session: SessionDep, payload: SubmissionCreate):
    return await SubmissionController.create_submission(payload, session)
@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=IResponse)
async def patch_submission(session: SessionDep, id: int, payload: SubmissionPatch):
    return await SubmissionController.update_submission(id, payload, session)