from Polygon import *

BLACK = "black"

class Right_Tri(Polygon):
    def __init__(self, x=10, y=10, side1=10, side2=10, color=BLACK):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from the user
        to create a right triangle, including start point, side
        1 length and side 2 length
        ;color: is the color that the user wants to fill the
        right triangle with
        """
        self.area = side1*side2/2
        dot = [x, y, x,
               side1+y, side2+x,
               side1+y]
        super(Right_Tri, self).__init__(dot, color)


    def calc_area(self):
        """
        a function that calculate the right triangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass