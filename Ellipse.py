from ClosedCurve import *


class Ellipse(ClosedCurve):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from
        the user to create an ellipse, including cernter
        semi-major axe and the emi-minor axe
        ;color: is the color that the user wants to
        fill the ellipse with
        """
        dot = [values[0]-values[2],
               values[1]-values[3],
               values[0]+values[2],
               values[1]+values[3]]
        self.area = math.pi * values[2] * values[3]
        super(Ellipse, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the ellipse's area
        """
        return self.area

    def move_me(self, x, y):
        pass

