from fastapi import APIRouter, Depends
from sqlalchemy import Session

import src.repositories.recipes as recipes_repository
import src.repositories.ingredients as ingredients_repository

from schemas import RecipeBaseModel
from src.database.db import get_db_connection

router = APIRouter(prefix='/recipes')

@router.post("/")
async def create_recipe(recipe: RecipeBaseModel, db: Session = Depends(get_db_connection)):
    pass