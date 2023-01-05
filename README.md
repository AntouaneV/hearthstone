# Hearthstone game engine

## Participants

Ayse YILDRIM
Ali-Haïdar ATIA
Fatima OUDAHMANE
Rudy GOULLEY
Adrien DELACROIX
Anthony STANIX
Damien SALEM

## Langages, versions et dépendances

Python 3.10
*pip install -r requirements.txt*
flask 2.2.2
requests 2.28.1
pygame 2.1.2

## Points principaux

Structure de données
BDD résultats de partie (json)
Règles du jeu (fontions faisant avancer le jeu)
Interface

## Déroulement du jeu

### Avant la partie

creation des objets decks, users, ...

### Début de partie

* choix de la personne qui commence
* random des cartes
* pioche des cartes pour chaque joueur (4 cartes)
* créé la carte pièce pour la personne adverse

### Tour de jeu

* +1 mana au joueur (entre tour)
* pioche d'une carte (entre tour)
  * Si le joueur n'a plus de carte, -1 point de vie tour 1, x2 pour chaque tour sans cartes dans le deck
* déclencher le timer (vrai début du tour)
* le joueur joue ses cartes (vérification du coup des cartes avec le mana disponible) (highlight des cartes jouables?)
* retirer le coup de la carte du mana du joueur
* placer la carte et déclencher son effet
* utilisation du pouvoir du héro (1 héro = 1 pouvoir = 1 fonction)
  * avec choix des cibles en fonction du pouvoir
* gestion des attaques des créatures:
  * choix d'une créature (highlight des créatures qui peuvent attaquer)
  * choix d'une cible (highlight des cibles possibles)
  * résolution de l'attaque et soustraction des points de vie
  * suppression des cartes détruites
* Possibilité de passer son tour

### Fin du tour

* check timer
* check points de vie
* check passage de tour

### Fin de partie

* Check points de vie des joueurs
* Send json result:

{
    "id_game":,
    "time_stamp":,
    "player_1":{
        "status":,
        "rank":,
        "quests":{
          "nb_spells":,
          "nb_beasts":
        }
    },
    "player_2":{
        "status":,
        "rank":,
        "quests":{
            "nb_spells":,
            "nb_beasts":
        }
    }
}
