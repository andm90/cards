from cardsatributes.Color import Color
from cardsatributes.Figure import Figure
from Card import Card
from Deck import Deck
from Player import Player
from Game import Game
# 1) Create colors and figures of the cards
colors = [Color("heart"), Color("spade"), Color("club"), Color("diamond")]
figures = [Figure("2"), Figure("3"), Figure("4"), Figure("5"), Figure("6"), 
           Figure("7"), Figure("8"), Figure("9"), Figure("10"), Figure("jack"), 
           Figure("queen"), Figure("king"), Figure("as")]

# 2) Create the deck
deck = Deck()

# 3) Add cards to the deck
for f in figures:
    for c in colors:
        deck.addCardOnDeck(Card(f,c))

# 4) Shufle the deck 
deck.shuffleDeck()
print(deck)

# 5) Create players
name = input("What is your name? ")
player1 = Player(str(name))
computer = Player("Computer")

# 6) PLAY!

game = Game(player1, computer, deck)
game.beginningOfTheGame()

