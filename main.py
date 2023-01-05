from fastapi import FastAPI
import os
from entity.game import Game

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/game")
async def start_game(user):
    game = Game(user)
    return game.id


@app.get("/game/{id}")
async def find_game(id):
    return {"id": id}

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
