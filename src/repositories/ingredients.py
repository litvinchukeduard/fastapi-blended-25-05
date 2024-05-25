from sqlalchemy import Session

from src.database.models import Ingredient
from src.schemas import IngredientBaseModel

async def save_ingredient(body: IngredientBaseModel, db: Session) -> Ingredient:
    ingredient = Ingredient(name=body.name, description=body.description)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient
