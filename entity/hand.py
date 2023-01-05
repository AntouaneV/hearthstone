from card import Card
class hand:
    def __init__(self):
        self.hand = []
        self.cards = [Card(id, type)]

    # methode pour ajouter liste de cartes
    def add_multiple_card(self,card_list):
        self.cards.extend(card_list)
    # methode pour ajouter 1 seul carte
    def add_card(self,card):
        self.cards.append(card)
    # methode pour supprimer 1 carte joué
    def delete_card(self,card):
        self.cards.remove(card)