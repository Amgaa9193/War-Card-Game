from card import Card
import random
# from player import Player




class Deck:
  def __init__(self):
      self.cards = []
      self.build()

  def build(self):
    suites = ["♦", "♣", "♥", "♠"]
    for suite in suites:
      for value in range(1, 14):
        self.cards.append(Card(suite,value))


 
      
  def shuffle(self):
    return random.shuffle(self.cards)


  def show(self):
    for card in self.cards:
      card.show()



# Unit test:
# deck = Deck()
# deck.shuffle()
# deck.show()



