class Color(object):
    """
    Class: Color of the card
    Attributes: 
        color (str):
    """
    def __init__(self, color):
        self.__color = color

    def __str__(self):
        return f"{self.__color}"

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

