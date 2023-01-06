from fastapi import FastAPI, Request
import os
from entity.game import Game
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import pygame
import sys

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
    pygame.init()
    # Créer une fenêtre de 800x600 pixels
    fenetre = pygame.display.set_mode((800, 600))
    # Définir la couleur de fond de la fenêtre en blanc
    fenetre.fill((255, 255, 255))
    # Créer une police Arial de taille 36
    police = pygame.font.SysFont("comicsansms", 20)
    # Parcourir la liste de cartes
    x = 0
    y = 0
    for carte in GAME.user.deck.card_list:
        x += 40
        y += 40
        # Créer une image de texte à partir du texte de la carte en utilisant la police et en spécifiant la couleur blanche
        image_texte = police.render(carte.text, True, (255, 255, 255))
        # Obtenir les dimensions de l'image de texte
        largeur, hauteur = image_texte.get_size()
        # Dessiner un rectangle noir de la taille de l'image de texte autour de cette dernière
        pygame.draw.rect(fenetre, (0, 0, 0), (10, 10, largeur, hauteur))
        # Coller l'image de texte sur la fenêtre à la position (10, 10)
        fenetre.blit(image_texte, (x, y))
        # Mettre à jour la fenêtre
        pygame.display.update()
    # Attendre que l'utilisateur ferme la fenêtre
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # return templates.TemplateResponse("index.jinja2", {
    #     "request": request,
    #     "id": id,
    #     "card_list": GAME.user.deck.card_list})

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
