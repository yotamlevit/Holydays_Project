from Polygon import *


class Rectangle(Polygon):
    def __init__(self, x, y, side1, side2, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from
        the user to create a rectangle, including start point,
        the big side length and the small side length
        ;color: is the color that the user wants to fill the rectangle with
        """
        dot = [x, y,
               x + side1, y,
               x + side1, y + side2,
               x, y + side2]
        self.area = side1 * side2
        super(Rectangle, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the rectangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass