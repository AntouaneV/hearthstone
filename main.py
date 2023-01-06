from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from entity.game import Game
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Welcome to the Hearthstone !"}


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

@app.post('/draw-card/{id}')
def draw_card(id: int):
    inp = {id}
    return inp

@app.post('/drop-card/{id}')
def drop_card(id: int):
    inp = {id}
    return inp


@app.post('/disable/{name}')
def disable_cat(name: str):
    global inp 
    inp = {name}
    print(inp)
    return inp


# @app.get("/game/{id}", response_class=HTMLResponse)
# async def find_game(request: Request, id):
#     return templates.TemplateResponse("game.html", {
#         "request": request,
#         "id": id,
#         "player1": "Moi",
#         "hero1": "Mage",
#         "player2": "Toi",
#         "hero2": "Elfe",
#         })


@app.get("/game/{id}", response_class=HTMLResponse)
async def find_game(request: Request, id):
    return templates.TemplateResponse("index.jinja2", {
        "request": request,
        "id": id,
        "user_card_list": GAME.user.hand.cards_in_hand,
        "bot_card_list":GAME.user.hand.cards_in_hand,
        "user_bord":GAME.user.boardgame,
        "bot_board":GAME.bot.boardgame})

@app.get("/game/{id}", response_class=HTMLResponse)
async def find_game(request: Request, id):
    return templates.TemplateResponse("game.html", {
        "request": request,
        "id": id,
        "card_list": GAME.user.hand.hand,
        "player1": GAME.user.name,
        "hero1": GAME.user.hero.name,
        "hero1_power": GAME.user.hero.power["name"],
        })

@app.post("/game/{id}", response_class=HTMLResponse)
async def  game_action(request:Request,id):
    return templates.TemplateResponse("index.jinja2", {
        "request": request,
        "id": id,
        "user_card_list": GAME.user.hand.cards_in_hand,
        "bot_card_list": GAME.bot.hand.cards_in_hand
        })

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
