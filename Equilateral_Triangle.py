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
    def __init__(self, dot, color):
        super(Equilateral_Triangle, self).__init__(dot, color)
        self.dot = dot
        self.color = color
        self.hight = math.sin(math.acos((self.dot[2]/2) /
                                        self.dot[2])) * self.dot[2]

    def draw_me(self, canvas):
        """
        a function that draw an equilateral triangle on the
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
        a function that calculate the equilateral triangle's area
        """
        return self.hight * self.dot[2]/2

    def move_me(self, x, y):
        pass