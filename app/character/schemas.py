from pydantic import BaseModel


class CharacterBase(BaseModel):
    id: str
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int

    class Config:
        orm_mode = True


class CharacterOut(BaseModel):
    id: str
    name: str
    height: float
    mass: float
    eye_color: str
    birth_year: int
