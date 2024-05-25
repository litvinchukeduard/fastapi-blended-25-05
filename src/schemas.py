from typing import List
from pydantic import BaseModel, Field, field_validator
# {
#     "name": "Pasta Carbonara",
#     "description": "To make pasta carbonara...",
#     "ingredients": [
#         {"name": "Pasta", "description": "Regular pasta"},
#         {"name": "Parmigiano", "description": "parmigiano cheese"}
#     ]
# }

class IngredientBaseModel(BaseModel):
    name: str
    description: str


class RecipeBaseModel(BaseModel):
    name: str = Field(max_length=100)
    description: str
    ingredients: List[IngredientBaseModel]

    @field_validator('description')
    def description_is_all_alpha(cls, value):
        if not value.isalpha():
            raise ValueError('Description should be all alpha!')
        return value
