class Card:
    id: str
    name: str
    type: str
    cost: int
    attack: int
    health: int
    text: str
    mechanics: list | str
    hp: int
    img: str
    armor: int

    def __init__(self, id: int, name: str, type: str, cost: int, attack: int, health: int, text: str, mechanics: list | str, hp: int, img: str, armor: int):
        """_summary_

        Args:
            id (int): id of the card
            name (str): name of the card
            type (str): type of the card
            cost (int): mana cost of the card
            attack (int): hit damage of the card
            health (int): life of the card
            text (str): description of the card
            mechanics (list | str): power description of the card
            hp (int): life of the card
        """

        self.id = id
        self.name = name
        self.type = type
        self.cost = cost
        self.attack = attack
        self.health = health
        self.text = text
        self.mechanics = mechanics
        self.hp = hp
        self.armor = armor
        self.img = img

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0
