from .db_connect import engine, Base, SessionLocal
from fastapi import FastAPI
from .model import Users
from app.routes.user import router as user_router
from fastapi.staticfiles import StaticFiles
import os
from fastapi.openapi.utils import get_openapi


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(user_router)