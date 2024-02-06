from fastapi import APIRouter
from app.character.controllers import router as character_router

router = APIRouter()


router.include_router(character_router, tags=["Character"], prefix="/api/character")
