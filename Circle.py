from ClosedCurve import *

BLACK = "black"

class Circle(ClosedCurve):
    def __init__(self, x=100, y=200, rad=10, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;x: the x value center of the circle
        ;y: the x value center of the circle
        ;rad: the radius
        ;color: is the color that the user
        wants to fill the circle with
        ;poly: the line color around the shape
        """
        dot = [x-rad,
               y-rad,
               x+rad,
               y+rad]
        self.area = math.pi * rad**2
        super(Circle, self).__init__(dot, color,poly)

    def calc_area(self):
        """
        a function that calculate the circle's area
        """
        return self.area

    def move_me(self, x, y):
        pass