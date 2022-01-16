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


# class Game:
#   def __init__(self):
#       self.deck = Deck()
#       self.player1 = Player("Han")
#       self.player2 = Player("Solo")
#       self.start_game()


#   def start_game(self):
#     newdeck = Deck()
#     newdeck.shuffle()

#   #splitting the deck among the two players - alternate card from deck goes to each player respectively

#     for i in range(0,len(newdeck.cards)-1,2):  
#      self.player1.cards_in_hand.append(newdeck.cards[i])
#      self.player2.cards_in_hand.append(newdeck.cards[i+1])


#     # unit test

#        # Test for checking the players card
#        # for card in self.player1.cards_in_hand:
#        # card.show()

#     game_status = True 
#     round = 0
#     while game_status == True:
#       round += 1
#       print(f"Round {round}")

#       if len(self.player1.cards_in_hand) == 0:
#         print(f'{self.player1.name} is out of cards {self.player2.name} Wins!')
#         game_status = False
#         break

#       if len(self.player2.cards_in_hand) == 0:
#         print(f'{self.player2.name} is out of cards {self.player1.name} Wins!')
#         game_status = False
#         break
#       # game continie
#       else: 
        
#         one_hand = self.player1.deal_one()
#         print(f" Player one first hand: {one_hand.suite, one_hand.value  }")


#         two_hand = self.player2.deal_one()
#         print(f" Player two first hand: {two_hand.suite, two_hand.value  }")

    
#         if one_hand.value > two_hand.value:
#           print(f"{self.player1.name} has won")
#         elif one_hand.value < two_hand.value:
#           print(f"{self.player2.name} has won")
#         elif one_hand.value == two_hand.value:
#           at_war = True 

#           print("WAR!!!")
#           while at_war == True: 
#             print("War logic goes here")
#             break

#     # if len(self.player1.cards_in_hand) == 0:
#     #   print(f"{self.player1.name} won!")
#     # elif len(self.player2.cards_in_hand) == 0:
#     #   print(f"{self.player2.name} won!")



# game1 = Game()



