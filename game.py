# # game class will be here and will be triggered when clicked on start game btn with "/wargame" end point
# from deck import Deck 
# from player import Player 

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
#       player1_won = False
#       player2_won = False
#       round += 1
#       print(f"Round {round}")

#       if len(self.player1.cards_in_hand) == 0:
#         print(f'{self.player1.name} is out of cards {self.player2.name} Wins!')
#         player2_won = True
#         game_status = False
#         break

#       if len(self.player2.cards_in_hand) == 0:
#         print(f'{self.player2.name} is out of cards {self.player1.name} Wins!')
#         player1_won  = True
#         game_status = False
#         break
#       # game continie
#       else: 
#         dealt_cards = []

#         one_hand = self.player1.deal_one()
#         print(f" Player one first hand: {one_hand.suite, one_hand.value  }")
#         dealt_cards.append(one_hand)

#         two_hand = self.player2.deal_one()
#         print(f" Player two first hand: {two_hand.suite, two_hand.value  }")
#         dealt_cards.append(two_hand)

    
#         if one_hand.value > two_hand.value:
#           self.player1.add_cards(dealt_cards)
#           print(f"{self.player1.name}'s take")
#         elif one_hand.value < two_hand.value:
#           self.player1.add_cards(dealt_cards)
#           print(f"{self.player2.name}'s take")
#         elif one_hand.value == two_hand.value:
#           at_war = True 

#           print("WAR!!!")
#           while at_war == True: 
#             if len(self.player1.cards_in_hand) < 2:
#               print(f"{self.player2.name} has won")
#               player2_won = True
#               at_war = False
#               game_status = False
#             elif len(self.player2.cards_in_hand) < 2:
#               print(f"{self.player1.name} has won")
#               player1_won = True
#               at_war = False
#               game_status = False
#             else:
#               war_cards = []

#               hidden_hand1 = self.player1.deal_one()
#               one_hand = self.player1.deal_one()
#               print(f" Player one first hand: {one_hand.suite, one_hand.value  }")
#               war_cards.append(hidden_hand1)
#               war_cards.append(one_hand)

#               hidden_hand2 = self.player2.deal_one()
#               two_hand = self.player2.deal_one()
#               print(f" Player two first hand: {two_hand.suite, two_hand.value  }")
#               war_cards.append(hidden_hand2)
#               war_cards.append(two_hand)

#               dealt_cards.extend(war_cards)
          
#               if one_hand.value > two_hand.value:
#                 self.player1.add_cards(dealt_cards)
#                 # print(self.player1.cards_in_hand[-1])

#                 # for card in self.player1.cards_in_hand:
#                 #   card.show()

#                 print(f"{self.player1.name}'s take")
#                 at_war = False
#               elif one_hand.value < two_hand.value:
#                 self.player2.add_cards(dealt_cards)
#                 # print(self.player2.cards_in_hand[-1])

#                 # for card in self.player2.cards_in_hand:
#                 #   card.show()
#                 print(f"{self.player2.name}'s take")
#                 at_war = False
#               elif one_hand.value == two_hand.value:
#                 at_war = True
         