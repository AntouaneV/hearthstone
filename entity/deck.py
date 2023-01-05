import random
import card
class Deck:
    def __init__(self):
        # Initialise la liste de cartes avec une instance de Card pour chaque combinaison de valeur et de symbole
        self.cards = [Card(id, type)]
        # values et suits sont deux listes qui contiennent les valeurs et les symboles possibles pour les cartes d'un jeu de cartes standard

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)