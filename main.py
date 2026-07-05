from fastapi import FastAPI
from src.core.api import api
app=FastAPI()
app.include_router(api)