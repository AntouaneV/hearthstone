from entity.hero import Hero
from entity.deck import Deck
from entity.hand import Hand


class User:
    def __init__(self, id, nom, hero, deck):
        self.id = id
        self.nom = nom
        self.hp = 30
        self.mana = 0
        self.armor = 0
        self.weapon = {}
        self.status = {}
        self.class_ = Hero(hero["name"],hero["power"])
        self.deck = Deck(deck)
        self.hand= Hand()

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
