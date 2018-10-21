from ClosedCurve import *


class Circle(ClosedCurve):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class
        get from the user to create a circle,
        including cernter and radius
        ;color: is the color that the user
        wants to fill the circle with
        """
        dot = [values[0]-values[2],
               values[1]-values[2],
               values[0]+values[2],
               values[1]+values[2]]
        self.area = math.pi * values[2]**2
        super(Circle, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the circle's area
        """
        return self.area

    def move_me(self, x, y):
        pass