from typing import List
from pydantic import BaseModel, Field, ConfigDict, field_validator
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
    def description_length_limited_by_200(cls, value):
        if len(value) > 200:
            raise ValueError('Description should be 200 symbols long!')
        return value
    

class IngredientResponse(IngredientBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class RecipeResponse(RecipeBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int