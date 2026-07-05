from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.core.data_base import Base
class Stage(Base):
    __tablename__="stages"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]=mapped_column(index=True, unique=True)
    description: Mapped[str]=mapped_column()
class StageTutor(Base):
    __tablename__ = "stage_tutors"
    stage_id: Mapped[int]=mapped_column(ForeignKey("stages.id"), primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"), primary_key=True)