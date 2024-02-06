from fastapi import FastAPI

from app.character import models
from app.character.router import router as character_router
from app.database import engine

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(character_router)


@app.get("/api/healthchecker")
def root():
    return {"message": "FastAPI SQAlchemy Character API."}
