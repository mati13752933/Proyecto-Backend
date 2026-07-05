from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey
from src.core.data_base import Base
from src.core.enums import TypeRoles
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column(index=True)
    codsis: Mapped[str] = mapped_column(unique=True)
    role: Mapped[TypeRoles] = mapped_column(Enum(TypeRoles), default=TypeRoles.USER)
    area_id: Mapped[int | None] = mapped_column(ForeignKey("areas.id"), nullable=True)