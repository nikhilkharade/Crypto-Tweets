from fastapi import FastAPI
from app.api.tweets import route

app = FastAPI()

app.include_router(router=route, prefix="/api")

@app.get("/ping")
async def ping():
    return {'msg':'pong'}