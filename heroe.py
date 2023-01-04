class Character:
    def __init__(self, hp=100):
        self.hp = hp
    
    def take_damage(self, damage):
        self.hp -= damage
    
    def is_dead(self):
        return self.hp <= 0