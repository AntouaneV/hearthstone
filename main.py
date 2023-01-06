from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from entity.game import Game
from fastapi.templating import Jinja2Templates
import json
import pygame
import sys

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

inp = ""

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
    # pygame.init()
    # # Créer une fenêtre de 800x600 pixels
    # fenetre = pygame.display.set_mode((800, 600))
    # # Définir la couleur de fond de la fenêtre en blanc
    # fenetre.fill((255, 255, 255))
    # # Créer une police Arial de taille 36
    # police = pygame.font.SysFont("comicsansms", 20)
    # # Parcourir la liste de cartes
    # x = 0
    # y = 0
    # for carte in GAME.user.hand.hand:
    #     x += 40
    #     y += 40
    #     # Créer une image de texte à partir du texte de la carte en utilisant la police et en spécifiant la couleur blanche
    #     image_texte = police.render(carte.text, True, (255, 255, 255))
    #     # Obtenir les dimensions de l'image de texte
    #     largeur, hauteur = image_texte.get_size()
    #     # Dessiner un rectangle noir de la taille de l'image de texte autour de cette dernière
    #     pygame.draw.rect(fenetre, (0, 0, 0), (60,60 , largeur, hauteur))
    #     # Coller l'image de texte sur la fenêtre à la position (10, 10)
    #     fenetre.blit(image_texte, (x, y))
    #     # Mettre à jour la fenêtre
    #     pygame.display.update()
    # # Attendre que l'utilisateur ferme la fenêtre
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    return templates.TemplateResponse("game.html", {
        "request": request,
        "id": id,
        "card_list": GAME.user.hand.hand,
        "player1": GAME.user.name,
        "hero1": GAME.user.hero.name,
        "hero1_power": GAME.user.hero.power["name"],
        })


if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
