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
    def __init__(self, dot, color):
        super(Isosceles_Tri, self).__init__(dot, color)
        self.dot = dot
        self.color = color
        self.dot[2] += 0.0
        self.dot[3] += 0.0
        self.hight = math.sin(math.acos((self.dot[2]/2)
                                        / self.dot[3]))*self.dot[3]

    def draw_me(self, canvas):
        """
        a function that draw an isosceles triangle on the
         screen using the values that the user gave
        """
        canvas.create_polygon(self.dot[0], self.dot[1],
                              self.dot[0] + self.dot[2]/2,
                              self.dot[1] + self.hight,
                              self.dot[0] - self.dot[2]/2,
                              self.dot[1] + self.hight,
                              fill=self.color)

    def calc_area(self):
        """
        a function that calculate the isosceles triangle's area
        """
        return self.hight * self.dot[2] / 2

    def move_me(self, x, y):
        pass