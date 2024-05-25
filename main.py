from fastapi import FastAPI
from src.routes.recipes import router as recipes_router

app = FastAPI()

app.include_router(recipes_router, prefix='/api')

@app.get("/")
async def root():
    return {"message": "Hello World"}