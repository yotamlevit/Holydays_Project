from Polygon import *
import math

BLACK = "black"
class Isosceles_Tri(Polygon):
    def __init__(self, x=10, y=10, base=10, side=50, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;x: the x value center of the circle
        ;y: the x value center of the circle
        ;color: is the color that the user wants to
        fill the isosceles triangle with
        ;poly: the line color around the shape
        ;side: the triangle`s side
        ;base: the triangle`s base
        """
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
        super(Isosceles_Tri, self).__init__(dot, color, poly)

    def calc_area(self):
        """
        a function that calculate the isosceles triangle's area*
        """
        return self.area

    def move_me(self, x, y):
        pass