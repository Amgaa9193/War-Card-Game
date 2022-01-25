from card import Card

class Player():
  def __init__(self, name):
      self.name = name
      self.cards_in_hand = []

  def deal_one(self):
    return self.cards_in_hand.pop(0)

  def add_cards(self,new_cards):
    self.cards_in_hand.extend(new_cards)


# test
# p1 = Player('test')
# p1.cards_in_hand
# p1.add_cards(Card("♠", 2))
# p1.cards_in_hand