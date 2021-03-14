from Card import Card
from Deck import Deck
from Player import Player


class Game(object):
    """
    Class: Game
    Attributes: 
        
    """
    def __init__(self, player, computer, deck):
        self.__player = player
        self.__computer = computer
        self.__deck = deck

    def beginningOfTheGame(self):
        while(True):
            self.showMenu()
            option = input("What is your chose? ")
            if option == "1":
                self.startGame()

            elif option == "2": #TODO
                print("HERE WILL BE DB!")
                pass 

            elif option == "3" or option[0].lower() == "q":
                break

            else:
                print("ERROR: THIS OPTION DOES NOT EXIST!")

    def showMenu(self):
        print(
            """
            1 Start game
            2 Win list
            3 Quit
            """
        )

    def startGame(self):
        while(True):
            self.moveCardsFromDeckToHand()
            print(self.__player.showHand())
            option = input("Do you want more cards? (Y/N) ")
            if option[0].lower() == "y":
                pass
            else:
                break
        self.showAllHands()

    def showAllHands(self):
        print("Player has: " + self.__player.showHand())
        print("Computer has: " + self.__computer.showHand())

    def moveCardsFromDeckToHand(self):
        self.__player.addCardOnHand(self.__deck.removeCardFromDeck())
        self.__computer.addCardOnHand(self.__deck.removeCardFromDeck())


