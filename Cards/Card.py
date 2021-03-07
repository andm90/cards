from cardsatributes.Color import Color
from cardsatributes.Figure import Figure

class Card(object):
    """
    Class: Card
    Attributes: 
        color (Color):
        figure (Figure):
    """
    def __init__(self, figure, color):
        self.__figure = figure
        self.__color = color

    def __str__(self):
        return f"C: {self.__color}, F: {self.__figure}"

    def getFigure(self):
        return self.__figure

    def setFigure(self, figure):
        self.__figure = figure

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color
