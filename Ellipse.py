from ClosedCurve import *

BLACK = "black"

class Ellipse(ClosedCurve):
    def __init__(self, x=200, y=500, hor_rad=20, rad=10, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from
        the user to create an ellipse, including cernter
        semi-major axe and the emi-minor axe
        ;color: is the color that the user wants to
        fill the ellipse with
        """
        dot = [x-hor_rad,
               y-rad,
               x+hor_rad,
               y+rad]
        self.area = math.pi * hor_rad * rad
        super(Ellipse, self).__init__(dot, color, poly)

    def calc_area(self):
        """
        a function that calculate the ellipse's area
        """
        return self.area

    def move_me(self, x, y):
        pass

