from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.core.config import config
engine = create_async_engine(config.database_url, echo=config.is_debug)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)
class Base(DeclarativeBase):
    pass
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
async def create_database():
    print(Base.metadata.tables)
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.create_all)
SessionDep = Annotated[AsyncSession, Depends(get_db)]