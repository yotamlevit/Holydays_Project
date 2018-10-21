from Polygon import *


class Equilateral_Triangle(Polygon):
    """
    an initializer for the class
    ;values: is a list of the values that the class get from
     the user to create an equilateral triangle,
     including start point and the side's length
    ;color: is the color that the user wants to
     fill the equilateral triangle with
    """
    def __init__(self, values, color):
        hight = math.sin(math.acos((values[2]/2) /
                        values[2])) * values[2]
        dot = [values[0], values[1],
               values[0] + values[2]/2,
               values[1] + hight,
               values[0] - values[2]/2,
               values[1] + hight]
        self.area = hight*dot[2]/2

        super(Equilateral_Triangle, self).__init__(dot, color)


    def calc_area(self):
        """
        a function that calculate the equilateral triangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass