from sqlalchemy.orm import Session

from src.database.models import Ingredient
from src.schemas import IngredientBaseModel

async def get_ingredient_by_id(id: int, db: Session) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.id == id).first()

async def get_ingredient_by_name(name: str, db: Session) -> Ingredient:
    return db.query(Ingredient).filter(Ingredient.name == name).first()

async def save_ingredient(body: IngredientBaseModel, db: Session) -> Ingredient:
    ingredient = Ingredient(name=body.name, description=body.description)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient
