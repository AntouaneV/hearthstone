from fastapi import FastAPI
import os
from entity.game import Game

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def start_game():
    game= Game()
    return game.

if __name__=="__main__":
    os.system("uvicorn main:app --reload")