from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.core.data_base import Base
class Area(Base):
    __tablename__ ="areas"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]=mapped_column(index=True, unique=True)
    description: Mapped[str]=mapped_column()
class AreaTutor(Base):
    __tablename__ = "area_tutors"
    area_id: Mapped[int]=mapped_column(ForeignKey("areas.id"), primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"), primary_key=True)