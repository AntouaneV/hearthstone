from entity.card import Card


class Boardgame:

    emplacements: list

    def __init__(self):
        self.emplacements = [None, None, None, None, None, None, None]

    def jouer_carte(self, carte):
        emplacement = int(input("Choisissez une position entre 0 et 6"))
        while True:
            if ((self.emplacements[emplacement] is None) and
                    (emplacement in range(0, 6))):
                self.emplacements[emplacement] = carte
                print(
                    f"La carte {carte} a été jouée sur \
                        l'emplacement {emplacement}.")
                return True
            else:
                print(
                    "Emplacement déjà occupé ou valeur invalide, \
                        veuillez choisir un autre emplacement.")

    def __str__(self, bordgame):
        return str(bordgame.emplacements), str(self.emplacements)

    def remove_card(self, entity):
        if type(entity) is int:
            self.emplacements[entity] = None
            return True
        elif type(entity) is Card:
            for i in range(len(self.emplacements)):
                if self.emplacements[i] == entity:
                    self.emplacements[i] = None
                    return True
        return False

    def fight_between(self, boardgame2, entity1, entity2):
        """_summary_

        Args:
            boardgame2 (Boardgame): Correspond au plateau de jeu de
            l'user attaqué. De type class(BoardGame).
            entity1 (Card): Correspond à une carte de type class(Card) de
            "emplacements" du boardgame1
            entity2 (Card or User): Correspond à une carte de type Card de
            "emplacements" du boardgame2 OU à l'utilisateur de type class(User)
        Returns:
            [result1, result2] ([bool, bool]): Retourne une liste de deux
            entités de type bool. le premier bool correspond
            à survie ou non des deux entités paramètre.
        """
        result1, result2 = True, True
        entity2.hp - entity1.hit
        if type(entity2) == Card:
            entity1.hp - entity2.hit
            if entity2.hp <= 0:
                boardgame2.remove_card(entity2)
                result2 = False
            if entity1.hp <= 0:
                self.remove_card(entity1)
                result1 = False
        elif entity2.hp <= 0:
            # Si ce IF est déclenché,
            # cela signifie la victoire d'un des deux joueurs.
            result2 = False
            # Il faudra donc penser à ajouter une méthode
            # victoire peut être dirctement ici ?
        return [result1, result2]
