from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from entity.game import Game
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/game")
async def start_game(user):
    game = Game(user)
    return game.id
inp=""


@app.post('/disable/{name}')
def disable_cat(name: str):
    inp = {name}  
    return inp    
print(inp)

@app.get("/game/{id}", response_class=HTMLResponse)
async def find_game(request: Request, id):
    return templates.TemplateResponse("game.html", {
        "request": request, 
        "id": id,
        "player1": "Moi",
        "hero1": "Mage",
        "player2": "Toi",
        "hero2": "Elfe",
        })

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")