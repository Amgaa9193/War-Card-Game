class Card:
  def __init__(self, suite, value):
      self.suite = suite
      self.value = value 

  # show individual card value
  def show(self):
    print(self.suite, self.value)

  


# test:
# card = Card("♠", 2)
# card.show()

