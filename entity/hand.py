from card import Card

# methode pour ajouter des cartes
def add_card(self,card):
    if type(card) == list :
        self.cards.extend(card)
    else :
        self.cards.append(card)
    # methode pour supprimer 1 carte joué
def delete_card(self,card):
    self.cards.remove(card)
class hand:
    def __init__(self,cards):
        self.hand = []
        self.cards = add_card(cards)