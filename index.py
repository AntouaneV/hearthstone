from entity.user import User 

player = User(1, "Player", 100, 100, 0, None, None, None, None)
print(player.hp)  # affiche 100
player.take_damage(50)
print(player.hp)  # affiche 50
print(player.is_dead())  # affiche False
player.take_damage(60)
print(player.is_dead())  # affiche True
