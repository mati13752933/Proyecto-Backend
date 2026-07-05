from sqlalchemy import select, update
from src.core.data_base import SessionDep
from src.modules.submission.model import Submission
from src.modules.submission.schemas import SubmissionCreate, SubmissionPatch, SubmissionResponse
class SubmissionService:
    @staticmethod
    async def create_submission(payload: SubmissionCreate, session: SessionDep):
        submission=Submission(**payload.model_dump())
        session.add(submission)
        await session.commit()
        return SubmissionResponse.model_validate(submission)
    @staticmethod
    async def get_by_id(id: int, session: SessionDep):
        result=await session.execute(select(Submission).where(Submission.id == id))
        submission_orm=result.scalar_one_or_none()
        if not submission_orm:
            return None
        return SubmissionResponse.model_validate(submission_orm)
    @staticmethod
    async def get_by_user_and_session(user_id: int, session_id: int, session: SessionDep):
        result=await session.execute(
            select(Submission).where(
                Submission.user_id == user_id, Submission.session_id == session_id
            )
        )
        submission_orm=result.scalar_one_or_none()
        if not submission_orm:
            return None
        return SubmissionResponse.model_validate(submission_orm)
    @staticmethod
    async def get_all_submissions(session: SessionDep, limit, offset):
        result=await session.execute(select(Submission).limit(limit).offset(offset))
        submission_list_orm = result.scalars().all()
        return [SubmissionResponse.model_validate(s) for s in submission_list_orm]
    @staticmethod
    async def update_submission(id: int, payload: SubmissionPatch, session: SessionDep):
        result=await session.execute(
            update(Submission)
            .where(Submission.id == id)
            .values(**payload.model_dump(exclude_unset=True))
            .returning(Submission)
        )
        submission_orm=result.scalar_one()
        await session.commit()
        return SubmissionResponse.model_validate(submission_orm)