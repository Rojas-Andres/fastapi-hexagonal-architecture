from fastapi import FastAPI
from app.adapters.api.endpoints import users, auth
from app.adapters.database import models
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./test.db", echo=True)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])