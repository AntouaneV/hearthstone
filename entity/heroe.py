class Heroe:
    name:str
    power:str
    imgHeroe:str

    def __init__(self, name, power, imgHero):
        self.name = name
        self.power = power
        self.imgHeroe = imgHero
    
    def take_damage(self, damage):
        self.hp -= damage
    
    def is_dead(self):
        return self.hp <= 0