from card import Card

class Boardgame:

    emplacements: list

    def __init__(self):
        self.emplacements = [None] * 7

    def jouer_carte(self, carte):
        emplacement = int(input("Choisissez une position entre 0 et 6"))
        while True:
            if self.emplacements[emplacement] is None and emplacement in range(0, 6):
                self.emplacements[emplacement] = carte
                print(
                    f"La carte {carte} a été jouée sur l'emplacement {emplacement}.")
            else:
                print("Emplacement déjà occupé ou valeur invalide, veuillez choisir un autre emplacement.")
    
    def __str__(self, bordgame:class):
        return str(bordgame.emplacements)., str(self.emplacements)

    def remove_card(self, emplacement):
        self.emplacements.pop(emplacement)
        return None
    
    #def attack_card(self, boardgame, carte_A, carte_B):
     #   boardgame.emplacements[carte_B].hp - self.emplacements[carte_B].attack
        
        
        #boardgame.attack_card(boardgame2, iteration_bgA, iteration_bgB)
        
