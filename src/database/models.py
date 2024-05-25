from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column

Base = declarative_base()

#Recipe (id, name, description, ingredients[])
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=False)

# Ingredient (id, name, description)
