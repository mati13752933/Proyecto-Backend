from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.core.data_base import Base
class Session(Base):
    __tablename__ ="sessions"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]=mapped_column(index=True)
    description: Mapped[str]=mapped_column()
    link: Mapped[str | None]=mapped_column(nullable=True)
    stage_id: Mapped[int]=mapped_column(ForeignKey("stages.id"), nullable=False)
    area_id: Mapped[int | None]=mapped_column(ForeignKey("areas.id"), nullable=True)