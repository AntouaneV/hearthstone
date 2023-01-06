from entity.user import User
import random


class Game:

    id: int
    is_in_progress: bool
    turn: int = 0

    def __init__(self, user):
        self.user = User(user["id"], user["name"], user["hero"], user["deck"])
        self.bot = User("0", "Bot test", user["hero"], user["deck"])
        self.id = random.randint(1, 99)
        self.is_in_progress = True
        self.turn += 1
        self.user.hand.add_card(self.user.deck)

    def set_up(self):
        # set up the game: user1, user2, heroe1, heroe2,
        # deck1, deck2, hand1, hand2, board1, board2, mana1,
        # mana2, mana_max1, mana_max2, turn, turn_max
        pass

    def next_turn(self):
        self.turn += 1
        if self.turn % 2 == 0:
            self.bot.hand.add_card()
        else:
            self.user.hand.add_card()
