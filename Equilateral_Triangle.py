from Polygon import *
import math

class Equilateral_Triangle(Polygon):
    """
    the get_tri_len function only fits the right_tri
    *****there is need to do chenges to fit it so Iso_tri
    """
    def __init__(self, dot, color):
        super(Equilateral_Triangle, self).__init__(dot, color)
        self.dot = dot
        self.color = color
        self.hight = math.sin(math.acos((self.dot[2]/2)/self.dot[2])) * self.dot[2]

    def draw_me(self, canvas):
        canvas.create_polygon(self.dot[0], self.dot[1], self.dot[0] + self.dot[2]/2, self.dot[1] + self.hight, self.dot[0] - self.dot[2]/2, self.dot[1] + self.hight, fill=self.color)

    def calc_area(self):
        return self.hight * self.dot[2]/2

    def move_me(self, x, y):
        pass