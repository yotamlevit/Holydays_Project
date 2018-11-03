from Polygon import *
import math


class Isosceles_Tri(Polygon):
    """
    an initializer for the class
    ;values: is a list of the values that the class get from the user
     to create an isosceles triangle, including start point,
     the base length and the length of the 2 other sides
    ;color: is the color that the user wants to
     fill the isosceles triangle with
    """
    def __init__(self, x, y, base, side, color):
        side += 0.0
        base += 0.0
        hight = math.sin(math.acos((base/2)
                                   / side))*side
        dot = [x, y,
               x + base/2,
               y + hight,
               x - base/2,
               y + hight]
        self.area = hight * dot[2]/2
        super(Isosceles_Tri, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the isosceles triangle's area*
        """
        return self.area

    def move_me(self, x, y):
        pass