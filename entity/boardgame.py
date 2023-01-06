from entity.card import Card

class Boardgame:

    emplacements: list

    def __init__(self):
        self.emplacements = []

    def jouer_carte(self, carte):
        emplacement = int(input("Choisissez une position entre 0 et 6"))
        while True:
            if self.emplacements[emplacement] is None and emplacement in range(0, 6):
                self.emplacements[emplacement] = carte
                print(
                    f"La carte {carte} a été jouée sur l'emplacement {emplacement}.")
            else:
                print("Emplacement déjà occupé ou valeur invalide, veuillez choisir un autre emplacement.")
    
    def __str__(self, bordgame):
        return str(bordgame.emplacements), str(self.emplacements)

    def remove_card(self, emplacement:int):
        self.emplacements.pop(emplacement)
        return None
    
        
