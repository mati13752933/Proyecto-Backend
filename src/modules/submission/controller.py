from fastapi import HTTPException
from src.core.data_base import SessionDep
from src.core.response_model import IResponse
from src.modules.session.services import SessionService
from src.modules.submission.schemas import SubmissionCreate, SubmissionPatch
from src.modules.submission.services import SubmissionService
from src.modules.user.services import UserService
class SubmissionController:
    @staticmethod
    async def create_submission(payload: SubmissionCreate, session: SessionDep):
        user=await UserService.get_by_id(payload.user_id, session)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        session_data=await SessionService.get_by_id(payload.session_id, session)
        if not session_data:
            raise HTTPException(status_code=404, detail="session not found")
        existing=await SubmissionService.get_by_user_and_session(
            payload.user_id, payload.session_id, session
        )
        if existing:
            raise HTTPException(status_code=400, detail="submission already exists")
        submission=await SubmissionService.create_submission(payload, session)
        return IResponse(code=201, message="Submission created", data=submission)
    @staticmethod
    async def get_all_submissions(session: SessionDep, limit: int, offset: int):
        submissions=await SubmissionService.get_all_submissions(session, limit, offset)
        return IResponse(
            code=200, message="Submissions retrieved", data=submissions, limit=limit, offset=offset
        )
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        submission=await SubmissionService.get_by_id(id, session)
        if not submission:
            raise HTTPException(status_code=404, detail="submission not found")
        return IResponse(code=200, message="Submission retrieved", data=submission)
    @staticmethod
    async def update_submission(id: int, payload: SubmissionPatch, session: SessionDep):
        submission=await SubmissionService.get_by_id(id, session)
        if not submission:
            raise HTTPException(status_code=404, detail="submission not found")
        new_submission=await SubmissionService.update_submission(id, payload, session)
        return IResponse(code=200, message="Submission updated", data=new_submission)