from Polygon import *

BLACK = "black"

class Equilateral_Triangle(Polygon):
    """
    an initializer for the class
    ;values: is a list of the values that the class get from
     the user to create an equilateral triangle,
     including start point and the side's length
    ;color: is the color that the user wants to
     fill the equilateral triangle with
    """
    def __init__(self, x=100, y=0, side=10, color=BLACK, poly=BLACK):
        hight = math.sin(math.acos((side/2) /
                        side)) * side
        dot = [x, y,
               x + side/2,
               y + hight,
               x - side/2,
               y + hight]
        self.area = hight*dot[2]/2

        super(Equilateral_Triangle, self).__init__(dot, color, poly)


    def calc_area(self):
        """
        a function that calculate the equilateral triangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass