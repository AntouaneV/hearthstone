from fastapi import FastAPI, Request
import os
from entity.game import Game
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/game")
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
    global GAME
    GAME = Game(user)
    return GAME.id


@app.get("/game/{id}", response_class=HTMLResponse)
async def find_game(request: Request, id):

    return templates.TemplateResponse("index.jinja2", {
        "request": request,
        "id": id,
        "card_list": GAME.user.deck.card_list})

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
