import random
from Card import Card

class Deck(object):
    """
    Class: Deck od cards
    Attributes: 
        cards (List[Card]):
    """
    def __init__(self):
        self.__cards = []

    def addCardOnDeck(self, card):
        """
        Add card on the top of stack
        Args:
            card (Card):
        """
        self.__cards.append(card)

    def removeCardFromDeck(self):
        """
        Remove card from the top of deck
            Return: romoved card
        """
        return self.__cards.pop()

    def shuffleDeck(self):
        """
        shuffle the deck randomly
        """
        random.shuffle(self.__cards)

    def __str__(self):
        
        decksList = ""
        for i in range(len(self.__cards)-1, -1, -1):
            decksList += str(self.__cards[i]) + '\n'

        return decksList

    def getCards(self):
        return self.__cards

    def setCards(self, cards):
        self.__cards = cards