from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import src.repositories.recipes as recipes_repository
import src.repositories.ingredients as ingredients_repository

from src.schemas import RecipeBaseModel, RecipeResponse
from src.database.db import get_db_connection

router = APIRouter(prefix='/recipes')

# 1) Дістаємо інгридіенти
# 2) Дивимось в базу даних, чи є такі інгридіенти
# 3) Якщо є, то просто додаємо інгридіент до рецепту
# 4) Якщо немає, то створюємо та додаємо
@router.post("/", response_model=RecipeResponse)
async def create_recipe(recipe: RecipeBaseModel, db: Session = Depends(get_db_connection)):
    # Запит чи э такий рецепт за імʼям
    current_recipe = await recipes_repository.get_recipe_by_name(recipe.name, db)
    if current_recipe:
        raise HTTPException(status_code=409, detail="Recipe already exists")
    # Запит на чи є такий інгридіент за імʼям
    ingredients = recipe.ingredients
    created_ingredients_list = []
    for ingredient in ingredients:
        current_ingredient = await ingredients_repository.get_ingredient_by_name(ingredient.name, db)
        if not current_ingredient:
            current_ingredient = await ingredients_repository.save_ingredient(ingredient, db)
        created_ingredients_list.append(current_ingredient)

    created_recipe = await recipes_repository.save_recipe(recipe, db)
    created_recipe.ingredients += created_ingredients_list
    created_recipe = await recipes_repository.update_recipe(created_recipe, db)
    # Зберігаємо рецепт
    return created_recipe

@router.get("/{id}", response_model=RecipeResponse)
async def get_ingredient_by_id(id: int, db: Session = Depends(get_db_connection)):
    return await recipes_repository.get_recipe_by_id(id, db)
