from entity.heroe import Heroe 

player = Heroe()
print(player.hp)  # affiche 100
player.take_damage(50)
print(player.hp)  # affiche 50
print(player.is_dead())  # affiche False
player.take_damage(60)
print(player.is_dead())  # affiche True
