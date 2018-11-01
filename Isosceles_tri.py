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
    def __init__(self, x, y, side, base, color):
        side += 0.0
        base += 0.0
        hight = math.sin(math.acos((side/2)
                                   / base))*base
        dot = [x, y,
               x + side/2,
               y + hight,
               x - side/2,
               y + hight]
        hight = math.sin(math.acos((dot[2]/2)
                                   / dot[3]))*dot[3]
        self.area = hight * dot[2]/2
        super(Isosceles_Tri, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the isosceles triangle's area*
        """
        return self.area

    def move_me(self, x, y):
        pass