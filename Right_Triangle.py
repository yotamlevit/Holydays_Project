from Polygon import *


class Right_Tri(Polygon):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from the user
        to create a right triangle, including start point, side
        1 length and side 2 length
        ;color: is the color that the user wants to fill the
        right triangle with
        """
        self.area = values[2]*values[3]/2
        dot = [values[0], values[1], values[0],
               values[2]+values[1], values[3]+values[0],
               values[2]+values[1]]
        super(Right_Tri, self).__init__(dot, color)


    def calc_area(self):
        """
        a function that calculate the right triangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass