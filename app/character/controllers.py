import logging

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response

from app.database import get_db
from app.character.schemas import CharacterOut, CharacterBase
from app.character.service import CharacterService


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "/getAll",
    status_code=status.HTTP_200_OK,
    response_model=list[CharacterOut],
    description="Retrieves a list of Characters",
)
async def retrieve_characters(
    db: Session = Depends(get_db), offset=0, search: str = ""
):
    logger.info("Retrieving characters.")

    characters = await CharacterService.list_characters(db, offset, search)

    if not characters:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No character found with payload: {search}",
        )

    return [
        CharacterOut(
            id=character.id,
            name=character.name,
            height=character.height,
            mass=character.mass,
            eye_color=character.eye_color,
            birth_year=character.birth_year,
        ).dict()
        for character in characters
    ]


@router.get(
    "/get/{character_id:str}",
    status_code=status.HTTP_200_OK,
    description="Retrieves a specific Character",
)
async def retrieve_character(character_id: str, db: Session = Depends(get_db)):

    logger.info("Retrieving a specific character.")

    character = await CharacterService.get_character(db, character_id)

    if not character:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No character found with id: {character_id}",
        )
    return character


@router.post(
    "/add",
    status_code=status.HTTP_201_CREATED,
    response_model=CharacterBase,
    description="Create a new Character",
)
async def create_character(
    character_data: CharacterBase, db: Session = Depends(get_db)
):
    logger.info(f"Creating a new character with data {character_data} .")
    try:
        new_character = await CharacterService.create_character(db, character_data)
        logger.info(f"New character created with id {new_character.id}.")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not create a character with payload: {character_data} with error {e}",
        )
    return new_character


@router.delete(
    "/delete/{character_id:str}",
    status_code=status.HTTP_200_OK,
    description="Deletes a specific Character",
)
async def delete_character(character_id: str, db: Session = Depends(get_db)):
    logger.info(f"Trying to delete Character with id {character_id}.")
    try:
        await CharacterService.delete_character(db, character_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not delete a character with ID: {character_id} with error {e}",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
