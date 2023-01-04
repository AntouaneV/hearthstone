class Card:
    id:str
    name:str
    type:str
    rarity:str
    cost:int
    attack:int
    health:int
    text:str
    mechanics:list
    
    def __init__(self, id:int, name:str, type:str, rarity:str, cost:int, attack:int, health:int, text:str, mechanics:list):
        """_summary_

        Args:
            id (int): id of the card
            name (str): name of the card
            type (str): type of the card
            rarity (str): rarity of the card
            cost (int): mana cost of the card
            attack (int): hit damage of the card
            health (int): life of the card
            text (str): description of the card
            mechanics (list): power description of the card
        """
        
        self.id = id
        self.name = name
        self.type = type
        self.rarity = rarity
        self.cost = cost
        self.attack = attack
        self.health = health
        self.text = text
        self.mechanics = mechanics