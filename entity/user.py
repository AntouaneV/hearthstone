from entity.hero import Hero
from entity.deck import Deck
from entity.hand import Hand
from entity.boardgame import Boardgame


class User:
    id: str
    name: str
    hero: Hero
    deck: Deck

    def __init__(self, id, name, hero, deck):
        self.id = id
        self.name = name
        self.hp = 30
        self.mana = 0
        self.armor = 0
        self.weapon = {}
        self.status = {}
        self.hero = Hero(hero["name"],hero["power"])
        self.deck = Deck(deck)
        self.hand= Hand(self.deck)

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

    def add_mana(self, mana_to_add):
        self.mana += mana_to_add
        if self.current_mana > 10:
            self.current_mana = 10

    def refresh_mana(self):
        self.mana = 10
