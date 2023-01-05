from entity.user import User


class Game:

    id: int
    is_in_progress: bool

    def __init__(self, user):
        self.user = User(user["id"],user["name"],user["hero"],user["deck"])
        self.is_in_progress = True

    def set_up(self):
        # set up the game: user1, user2, heroe1, heroe2, deck1, deck2, hand1, hand2, board1, board2, mana1, mana2, mana_max1, mana_max2, turn, turn_max
        pass
