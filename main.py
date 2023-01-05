from fastapi import FastAPI
import os
from entity.game import Game
import jinja2
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/game")
async def start_game():
    testfile = open("data/deck.json", "r")
    user = {
        "id": 6,
        "name": "Toto",
        "hero": {
            "name": "Jaina Proudmore",
            "power": {
                "name": "fireball",
                "description": "inflige 1 point de dégâts à n'importe quelle cible."
            }
        },
        "deck": json.load(testfile)
    }
    game = Game(user)
    return game.id


@app.get("/game/{id}")
async def find_game(id):
    # affichage sur un template html de la partie
    return {"id": id}

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
