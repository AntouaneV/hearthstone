# Hearthstone_game-engin

Fonctions:
_ Tirage de cartes (draw du début de partie + draw à chaque tour + radomisation après un draw spécifique dans le deck)
_ Gestion du mana
_ Lecture de cartes et effets
_ Gestion des points de vie des joueurs
_ Gestion du timer
_ Gestions des points de vie / attaques de cartes
_ Gestion des capacités de héros


Structure de données
Règles du jeu (fontions faisant avancer le jeu)
BDD resultats (fichier json)
Interface

Déroulement du jeu:
_ choix de la personne qui commence
_ random des cartes
_ pioche des cartes pour chaque joueur
_ créé la carte pièce pour la personne adverse
_ donner 1 mana au joueur 1
_ déclencher le timer
_ le joueur 1 joue ses cartes (vérification du coup des cartes avec le mana disponible) (highlight des cartes jouables?)
_ retirer le coup de la carte du mana du joueur
_ placer la carte et déclencher son effet
_ 