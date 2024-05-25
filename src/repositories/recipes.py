from sqlalchemy import Session

from src.database.models import Recipe
from src.schemas import RecipeBaseModel

async def save_recipe(body: RecipeBaseModel, db: Session) -> Recipe:
    recipe = Recipe(name=body.name, description=body.description)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe
