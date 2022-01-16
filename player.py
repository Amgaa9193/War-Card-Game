class Player():
  def __init__(self, name):
      self.name = name
      self.cards_in_hand = []

  def deal_one(self):
    return self.cards_in_hand.pop(0)

  def add_cards(self,new_cards):
    self.cards_in_hand.extend(new_cards)