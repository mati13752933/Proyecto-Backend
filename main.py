from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
import src.core.mapping_database
from src.core.api import api
from src.core.data_base import engine
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    yield
app = FastAPI(lifespan=lifespan)
app.include_router(api)