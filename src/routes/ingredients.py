from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import src.repositories.ingredients as ingredients_repository

from src.schemas import IngredientResponse
from src.database.db import get_db_connection

router = APIRouter(prefix='/ingredients')

@router.get("/{id}", response_model=IngredientResponse)
async def get_ingredient_by_id(id: int, db: Session = Depends(get_db_connection)):
    return await ingredients_repository.get_ingredient_by_id(id, db)
