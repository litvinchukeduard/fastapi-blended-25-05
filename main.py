from fastapi import FastAPI
from src.routes.recipes import router as recipes_router
from src.routes.ingredients import router as ingredients_router

app = FastAPI()

app.include_router(recipes_router, prefix='/api')
app.include_router(ingredients_router, prefix='/api')

@app.get("/")
async def root():
    return {"message": "Hello World"}