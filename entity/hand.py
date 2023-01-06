from entity.card import Card
from entity.deck import Deck


class Hand:
    hand:list
    def __init__(self,deck:Deck):
        self.hand = deck.draw_multiple(4)
        
    
    # methode pour ajouter des cartes
    def add_card(self,deck:Deck):
        self.hand.append(deck.draw_one())
        # methode pour supprimer 1 carte joué
    def delete_card(self,card:Card):
        self.hand.remove(card)