# requirements list:
# Create a RESTful service with two endpoints:
  # An endpoint to start a game. Two simulated players will play out the game.
  # An endpoint to get lifetime wins for each player stored in a database.
# You should include some basic tests along with the application code.


from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from game import Game


# Setting up the app
app = Flask(__name__)
# config the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///war.db'
# initializing the db with our app
db = SQLAlchemy(app)


# Database Model for score table
class Score(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  winner_name = db.Column(db.String(10), nullable=False)
  # score = db.Column(db.Integer, default=0, nullable=False)
  total_win = db.Column(db.Integer, default=1, nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)

  # function that returns str everythime a Score is created 
  def __repr__(self) -> str:
      return '<Task %r>' % self.id




# ********************************************************************************
# game class combines DEck, Card, Player classes and initiate a new game!
from deck import Deck 
from player import Player 

class Game:
  def __init__(self):
      self.deck = Deck()
      self.player1 = Player("Ben")
      self.player2 = Player("Rey")
      self.display_content = []
      self.start_game()


  # saves and updates the score to the database
  def save_score(self, player_name):
  
      score = Score.query.filter_by(winner_name=player_name).order_by(Score.date_created).first()
      if score:
        # print(score)
        try:
          score.total_win += 1
          db.session.commit()
          return redirect('/scores')
        except:
          return "There was issue updating this score!"
      else:
        try:
          new_score = Score(winner_name=player_name)
          db.session.add(new_score)
          db.session.commit()
          return redirect('/scores')
        except:
          return "There was issue adding this score"




  def start_game(self):
    newdeck = Deck()
    # newdeck.show()
    newdeck.shuffle()

  #splitting the deck among the two players - alternate card from deck goes to each player respectively

    for i in range(0,len(newdeck.cards)-1):  
      if i % 2 == 0:
        self.player1.cards_in_hand.append(newdeck.cards[i])
      else:
        self.player2.cards_in_hand.append(newdeck.cards[i])


    # test
       # Test for checking the players card
      # count = 0
      # for card in self.player1.cards_in_hand:
      #   count += 1
      #   card.show()
      # print(count)
    
    game_status = True 
    round = 0
    while game_status == True:

      round += 1
      self.display_content.append(f"Round {round}")
      # print(f"Round {round}")

      if len(self.player1.cards_in_hand) == 0:
        self.display_content.append(f'{self.player1.name} is out of cards {self.player2.name} Won!')
        # print(f'{self.player1.name} is out of cards {self.player2.name} Wins!')
        self.save_score(self.player2.name)
        game_status = False
        break

      if len(self.player2.cards_in_hand) == 0:
        self.display_content.append(f'{self.player2.name} is out of cards {self.player1.name} Won!')
        # print(f'{self.player2.name} is out of cards {self.player1.name} Wins!')
        self.save_score(self.player1.name)
        game_status = False
        break
      # game continie
      else: 
        dealt_cards = []

        one_hand = self.player1.deal_one()
        self.display_content.append(f"Player one first hand: {one_hand.suite, one_hand.value  }")
        # print(f" Player one first hand: {one_hand.suite, one_hand.value  }")
        dealt_cards.append(one_hand)

        two_hand = self.player2.deal_one()
        self.display_content.append(f" Player two first hand: {two_hand.suite, two_hand.value  }")
        # print(f" Player two first hand: {two_hand.suite, two_hand.value  }")
        dealt_cards.append(two_hand)

    
        if one_hand.value > two_hand.value:
          self.player1.add_cards(dealt_cards)
          self.display_content.append(f"{self.player1.name}'s take")
          # print(f"{self.player1.name}'s take")
        elif one_hand.value < two_hand.value:
          self.player2.add_cards(dealt_cards)
          self.display_content.append(f"{self.player2.name}'s take")
          # print(f"{self.player2.name}'s take")
        elif one_hand.value == two_hand.value:
          at_war = True 
          self.display_content.append("WAR!!!")
          # print("WAR!!!")
          while at_war == True: 
            if len(self.player1.cards_in_hand) < 2:
              self.display_content.append(f"{self.player1.name} run out of card, {self.player2.name} has won!")
              # print(f"{self.player2.name} has won")
              self.save_score(self.player2.name)
              at_war = False
              game_status = False
            elif len(self.player2.cards_in_hand) < 2:
              self.display_content.append(f"{self.player2.name} run out of card, {self.player1.name} has won!")
              # print(f"{self.player1.name} has won")
              self.save_score(self.player1.name)
              at_war = False
              game_status = False
            else:
              war_cards = []

              hidden_hand1 = self.player1.deal_one()
              one_hand = self.player1.deal_one()
              self.display_content.append(f" Player one second hand: {one_hand.suite, one_hand.value  }")
              # print(f" Player one first hand: {one_hand.suite, one_hand.value  }")
              war_cards.append(hidden_hand1)
              war_cards.append(one_hand)

              hidden_hand2 = self.player2.deal_one()
              two_hand = self.player2.deal_one()
              self.display_content.append(f" Player two second hand: {two_hand.suite, two_hand.value  }")
              # print(f" Player two first hand: {two_hand.suite, two_hand.value  }")
              war_cards.append(hidden_hand2)
              war_cards.append(two_hand)

              dealt_cards.extend(war_cards)
          
              if one_hand.value > two_hand.value:
                self.player1.add_cards(dealt_cards)
                # print(self.player1.cards_in_hand[-1])

                # for card in self.player1.cards_in_hand:
                #   card.show()
                self.display_content.append(f"{self.player1.name}'s take")
                # print(f"{self.player1.name}'s take")
                at_war = False
              elif one_hand.value < two_hand.value:
                self.player2.add_cards(dealt_cards)
                # print(self.player2.cards_in_hand[-1])

                # for card in self.player2.cards_in_hand:
                #   card.show()
                self.display_content.append(f"{self.player2.name}'s take")
                # print(f"{self.player2.name}'s take")
                at_war = False
              elif one_hand.value == two_hand.value:
                at_war = True

@app.route("/")
def index():
  return render_template("index.html")

# endpoint 1 to start a game?
@app.route("/start")
def start():
  game = Game()
  return render_template("start.html", game_contents = game.display_content)

@app.route("/scores", methods=['POST', 'GET'])
def get_score():
    scores = Score.query.order_by(Score.date_created).all()
    if scores:
      return render_template("score.html", scores=scores)
    else:
      return render_template("score.html")


# main driver function 
if __name__ == "__main__":
  app.run(debug = True)