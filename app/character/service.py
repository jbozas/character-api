from app.character.models import Character


class ServiceException(Exception): ...


class CharacterService:

    async def list_characters(db, offset: int = 1, search: str = ""):
        return (
            db.query(Character)
            .filter(Character.name.contains(search))
            .offset(offset)
            .all()
        )

    async def get_character(db, character_id: str) -> Character:
        return db.query(Character).filter(Character.id == character_id).first()

    async def create_character(db, character_data: dict) -> Character:
        character = Character(**character_data.dict())
        db.add(character)
        db.commit()
        db.refresh(character)
        return character

    async def delete_character(db, character_id):
        character = db.query(Character).filter(Character.id == character_id).first()
        if not character:
            raise ServiceException("Character not found.")
        db.delete(character)
        db.commit()
