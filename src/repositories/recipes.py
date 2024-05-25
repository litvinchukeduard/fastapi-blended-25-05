from sqlalchemy.orm import Session

from src.database.models import Recipe
from src.schemas import RecipeBaseModel

async def get_recipe_by_id(id: int, db: Session) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == id).first()

async def save_recipe(body: RecipeBaseModel, db: Session) -> Recipe:
    recipe = Recipe(name=body.name, description=body.description)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe
