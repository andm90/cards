class Figure(object):
    """
    Class: Figure of the card
    Attributes: 
        figure (str):
    """
    def __init__(self, figure):
        self.__figure = figure

    def __str__(self):
        return f"{self.__figure}"

    def getFigure(self):
        return self.__figure

    def setFigure(self, figure):
        self.__figure = figure

