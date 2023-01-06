import random
from entity.card import Card
from typing import List


class Deck:
    card_list: List[Card] = []

    def __init__(self, deck: list):
        # Initialise la liste de cartes avec une instance de Card
        # pour chaque combinaison de valeur et de symbole
        for nb_card in deck:
            card = deck[nb_card][0]
            self.card_list.append(Card(
                card["id"],
                card["name"],
                card["type"],
                card["cost"],
                card["attack"],
                card["health"],
                card["text"],
                card["mechanics"],
                card["health"],
                card["img"],
                card["armor"]
            ))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.card_list)

    def draw_one(self):
        return self.card_list.pop(0)

    def draw_multiple(self, nb_card: int):
        card_drawn = []
        if nb_card > 0:
            while nb_card != 0:
                card_drawn.append(self.card_list.pop(0))
                nb_card -= 1
            return card_drawn
        else:
            return card_drawn
