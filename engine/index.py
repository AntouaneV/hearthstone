from entity.user import User 
from entity.card import Card
from entity.boardgame import check_attack_heroe

card = Card(1, "Card", "Type", "Rarity", 1, 1, 1, "Text", ["Mechanics"], 5)
player = User(1, "Player", 30, 100, 0, None, None, None, None)

print(player.hp) 
print(card.hp) 
card.take_damage(3)
print(card.hp) 
print(card.is_dead())  # affiche False
card.take_damage(2)
print(card.is_dead())  # affiche True

if check_attack_heroe:
    player.take_damage(15)
    print(player.hp) 
    print(player.is_dead())  # affiche False
    player.take_damage(20)
    print(player.is_dead())  # affiche True
