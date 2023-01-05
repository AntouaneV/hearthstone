class User:
    def __init__(self, id, nom, hp, mana, armor, weapon, status, class_, deck):
        self.id = id
        self.nom = nom
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.weapon = weapon
        self.status = status
        self.class_ = class_
        self.deck = deck

    def take_damage(self, damage):
        self.hp -= damage
    
    def is_dead(self):
        return self.hp <= 0