# Система для керування рецептами

# Recipe (id, name, description, ingredients[])

# Ingredient (id, name, description)

POST /api/recipes

{
    "name": "Pasta Carbonara",
    "description": "To make pasta carbonara...",
    "ingredients": [
        {"name": "Pasta", "description": "Regular pasta"},
        {"name": "Parmigiano", "description": "parmigiano cheese"}
    ]
}

1) Дістаємо інгридіенти
2) Дивимось в базу даних, чи є такі інгридіенти
3) Якщо є, то просто додаємо інгридіент до рецепту
4) Якщо немає, то створюємо та додаємо

GET /api/recipes/{id} /api/recipes/1
