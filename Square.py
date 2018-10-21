from Polygon import *


class Square(Polygon):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from the user
        to create a square, including start point and the side's length
        ;color: is the color that the user wants to fill the square with
        """
        dot = [values[0], values[1],
               values[0] + values[2], values[1],
               values[0] + values[2], values[1] + values[2],
               values[0], values[1] + values[2]]
        self.area = values[2]**2
        super(Square, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the square's area
        """
        return self.area

    def move_me(self, x, y):
        pass