from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.core.data_base import Base
class Submission(Base):
    __tablename__ ="submissions"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    link: Mapped[str]=mapped_column()
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"), nullable=False)
    session_id: Mapped[int]=mapped_column(ForeignKey("sessions.id"), nullable=False)