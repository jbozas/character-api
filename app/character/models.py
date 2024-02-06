import uuid

from sqlalchemy import Column, String, Float, Integer
from app.database import Base


class Character(Base):
    """
    Representation of a Character with various attributes such as name, height, mass, hair
    color, skin color, eye color, and birth year.
    """

    __tablename__ = "Character"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
