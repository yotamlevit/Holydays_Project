from Polygon import *


class Rectangle(Polygon):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from
        the user to create a rectangle, including start point,
        the big side length and the small side length
        ;color: is the color that the user wants to fill the rectangle with
        """
        dot = [values[0], values[1],
               values[0] + values[2], values[1],
               values[0] + values[2], values[1] + values[3],
               values[0], values[1] + values[3]]
        self.area = values[2] * values[3]
        super(Rectangle, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the rectangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass