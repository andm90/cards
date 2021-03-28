from Card import Card
from Deck import Deck
from Player import Player
import sqlite3


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

            elif option == "2": 
                self.readListOfWinners()

                pass 

            elif option == "3" or option[0].lower() == "q":
                self.insertThePlayerOnWinnerList()
                break

            else:
                print("ERROR: THIS OPTION DOES NOT EXIST!")

    def insertThePlayerOnWinnerList(self):
        db = sqlite3.connect('Winners.db')

        nameOfPlayer = self.__player.getName()
        pointsOfPlayer = int(self.__player.getPoints())

        qry=f"insert into winners (name, points) values('{nameOfPlayer}', {pointsOfPlayer});"
        try:
            cur=db.cursor()
            cur.execute(qry)
            db.commit()
            print ("one record added successfully")
        except:
            print ("error in operation")
            db.rollback()
        #db.execute(f"insert into winners (name, points) values('{nameOfPlayer}', {pointsOfPlayer});")
        db.close()

    def readListOfWinners(self):
        db=sqlite3.connect('Winners.db')
        sql="SELECT * from winners;"
        cur=db.cursor()
        cur.execute(sql)
        
        while True:      
            record=cur.fetchone()
            if record==None:
                break

            print (record)
        db.close()
        #db = sqlite3.connect('Winners.db') 
        #record = db.execute("SELECT * from winners;")
        #for i in record:
            #print(i)
        #db.close()
        
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
        self.checkTheWinner()
        print(self.__player)
        self.backCardsFromHandsToDeck()
        

    def backCardsFromHandsToDeck(self):
        for i in range(0, len(self.__player.showHand().split("\t"))):
            self.__deck.addCardOnDeck(self.__player.removeCardFromHand())
            self.__deck.addCardOnDeck(self.__computer.removeCardFromHand())

        self.__deck.shuffleDeck()

    def defOfPoints(self, card):   
        #if card.getFigure() == "jack":
        if "jack" in card:
            return 11
        #elif card.getFigure() == "queen":
        elif "queen" in card:
            return 12
        #elif card.getFigure() == "king":
        elif "king" in card:
            return 13
        #elif card.getFigure() == "as":
        elif "as" in card:
            return 14
        else:
            index = len(card) - 1
            return int(card[index])

    def checkTheWinner(self):
        sumForComputer = 0
        sumForPlayer = 0 

        for i in self.__computer.showHand().split("\t"):
            sumForComputer += self.defOfPoints(i)
        for j in self.__player.showHand().split("\t"):
            sumForPlayer += self.defOfPoints(i)

        print(f"Computer {sumForComputer} from cards")
        print(f"Player {sumForPlayer} from cards")
        
        if(sumForComputer > sumForPlayer):
            print("Computer won")
        elif(sumForPlayer > sumForComputer):
            print("Player won, +1 point for Player!")
            self.__player.addPoint()
        else:
            print("no one win")

    def showAllHands(self):
        print("Player has: " + self.__player.showHand())
        print("Computer has: " + self.__computer.showHand())

    def moveCardsFromDeckToHand(self):
        self.__player.addCardOnHand(self.__deck.removeCardFromDeck())
        self.__computer.addCardOnHand(self.__deck.removeCardFromDeck())


