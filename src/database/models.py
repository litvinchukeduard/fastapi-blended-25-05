from typing import List

from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey, String, Integer, Column
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

Base = declarative_base()

recipe_ingredient_association_table = Table(
    "recipe_ingredient_association_table",
    Base.metadata,
    Column("recipe_id", ForeignKey("recipes.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
)

#Recipe (id, name, description, ingredients[])
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=False)
    ingredients: Mapped[List['Ingredient']] = relationship(secondary=recipe_ingredient_association_table)

# Ingredient (id, name, description)

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=False)