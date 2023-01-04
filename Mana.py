class Mana:
  def __init__(self, quantity_mana):
    self.quantity_mana = quantity_mana

  def use_mana(self, amount):
    if self.quantity_mana - amount >= 0:
      self.quantity_mana -= amount
      return True
    return False

  def add_mana(self, amount):
    self.quantity_mana += amount

  def get_mana(self):
    return self.quantity_mana

  def has_mana(self, amount):
    return self.quantity_mana - amount >= 0

  