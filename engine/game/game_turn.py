import random
from card import Card
from heroe import Heroe
from boardgame import Boardgame

def shuffle_deck(self, user):
        random.shuffle(user.deck)

def draw_card(self, user,hand):
        if len(user.deck) > 0:
            card = user.deck.pop(0)
            hand.append(card)
        else:
            user.health -= 1

def draw_starting_hand(player):
    for i in range(4):
        draw_card(player)
        
def fight_between(entity1, entity2, boardgame1, boardgame2):
    entity2.hp - entity1.hit
    if type(entity2) != Heroe:
        entity1.hp - entity2.hit
        if entity1.hp <= 0:
            boardgame1
    
    
    
