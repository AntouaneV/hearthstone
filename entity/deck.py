import random
from card import Card
from typing import List


class Deck:
    cardlist:List[Card]
    def __init__(self,deck:list):
        # Initialise la liste de cartes avec une instance de Card pour chaque combinaison de valeur et de symbole
        for card in deck:
            self.cardlist.append(Card(card))
        # ID et Type sont deux listes qui contiennent les valeurs et les symboles possibles pour les cartes d'un jeu de cartes standard

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)
