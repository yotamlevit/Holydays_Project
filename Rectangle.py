from Polygon import *

BLACK = "black"

class Rectangle(Polygon):
    def __init__(self, x=100, y=100, side1=20, side2=10, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;x: the x value center of the circle
        ;y: the x value center of the circle
        ;color: is the color that the user
        wants to fill the shape with
        ;poly: the line color around the shape
        ;side1: a Rectangle side
        ;side2: a Rectangle side
        """
        dot = [x, y,
               x + side1, y,
               x + side1, y + side2,
               x, y + side2]
        self.area = side1 * side2
        super(Rectangle, self).__init__(dot, color, poly)

    def calc_area(self):
        """
        a function that calculate the rectangle's area
        """
        return self.area

    def move_me(self, x, y):
        pass