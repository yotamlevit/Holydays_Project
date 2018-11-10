from Polygon import *

BLACK = "black"

class Square(Polygon):
    def __init__(self, x=10, y=10, side=10, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from the user
        to create a square, including start point and the side's length
        ;color: is the color that the user wants to fill the square with
        """
        dot = [x, y,
               x + side, y,
               x + side, y + side,
               x, y + side]
        self.area = side**2
        super(Square, self).__init__(dot, color, poly)

    def calc_area(self):
        """
        a function that calculate the square's area
        """
        return self.area

    def move_me(self, x, y):
        pass