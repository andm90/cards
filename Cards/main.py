from cardsatributes.Color import Color
from cardsatributes.Figure import Figure
from Card import Card
from Deck import Deck

#create colors and figures of the cards
colors = [Color("heart"), Color("spade"), Color("club"), Color("diamond")]
figures = [Figure("2"), Figure("3"), Figure("4"), Figure("5"), Figure("6"), 
           Figure("7"), Figure("8"), Figure("9"), Figure("10"), Figure("jack"), 
           Figure("queen"), Figure("king"), Figure("as")]

#create the deck
deck = Deck()

for f in figures:
    for c in colors:
        deck.addCardOnDeck(Card(f,c))





