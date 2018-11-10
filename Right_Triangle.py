from Polygon import *

BLACK = "black"

class Right_Tri(Polygon):
    def __init__(self, x=10, y=10, side1=10, side2=10, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;x: the x value center of the circle
        ;y: the x value center of the circle
        ;color: is the color that the user
        wants to fill the shape with
        ;poly: the line color around the shape
        ;side1: a triangle`s side
        ;side2: a triangle`s side
        """
        self.area = side1*side2/2
        dot = [x, y, x,
               side1+y, side2+x,
               side1+y]
        super(Right_Tri, self).__init__(dot, color, poly)


    def calc_area(self):
        """
        a function that calculate the right triangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass