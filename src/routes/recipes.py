from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import src.repositories.recipes as recipes_repository
import src.repositories.recipes as recipes_repository

from src.schemas import RecipeBaseModel, RecipeResponse
from src.database.db import get_db_connection

router = APIRouter(prefix='/recipes')

# 1) Дістаємо інгридіенти
# 2) Дивимось в базу даних, чи є такі інгридіенти
# 3) Якщо є, то просто додаємо інгридіент до рецепту
# 4) Якщо немає, то створюємо та додаємо
@router.post("/")
async def create_recipe(recipe: RecipeBaseModel, db: Session = Depends(get_db_connection)):
    ingredients = recipe.ingredients
    # Запит чи э такий рецепт за імʼям
    # Запит на чи є такий інгридіент за імʼям

    # Зберігаємо рецепт

@router.get("/{id}", response_model=RecipeResponse)
async def get_ingredient_by_id(id: int, db: Session = Depends(get_db_connection)):
    return await recipes_repository.get_recipe_by_id(id, db)
