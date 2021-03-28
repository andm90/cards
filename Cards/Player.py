from Card import Card

class Player(object):
    """
    Class: Player
    Attributes: 
        hand (List[Card]): cards on hand
    """

    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__points = 0

    def addCardOnHand(self, card):
        """
        Add card on the players hand
        Args:
            card (Card):
        """
        self.__hand.append(card)

    def removeCardFromHand(self):
        """
        Remove card from the top of hand
            Return: romoved card
        """
        return self.__hand.pop()
    def addPoint(self):
        """
        Add point for win
        """
        self.__points += 1

    def showHand(self):
        """
        Show hand
            Return: cards on player hand
        """
        handList = ""
        for i in range(0, len(self.__hand)):
            handList += str(self.__hand[i]) + '\t'
        
        return handList[0:len(handList)-1] #remove last '\t'

    def __str__(self):
        return f"{self.__name} has {self.__points} points."

    def getCards(self):
        return self.__hand

    def setCards(self, hand):
        self.__hand = hand

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPoints(self):
        return self.__points

    def setPoaints(self, points):
        self.__points = points