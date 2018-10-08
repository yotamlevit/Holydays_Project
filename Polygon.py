from Shape import *


class Polygon(Shape):
    def __init__(self, dot, color):
        """
        an initializer for the class
        ;dot: is a list of the dot on the screen that
        the class get from the user to create an polygon
        ;color: is the color that the user wants to
        fill the polygon with
        """
        super(Polygon, self).__init__(color)
        self.dot = dot
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw a polygon on the screen
        using the dots that the user gave
        """
        canvas.create_polygon(self.dot, fill=self.color)

    def calc_area(self):
        pass

    def move_me(self, x, y):
        pass