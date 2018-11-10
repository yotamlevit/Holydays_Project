from Polygon import *

BLACK = "black"
class Parallelogram(Polygon):
    def __init__(self, x=10, y=10, side1=50, side2=50, angle=45, color=BLACK, poly=BLACK):
        """
        an initializer for the class
        ;x: the x value center of the circle
        ;y: the x value center of the circle
        ;color: is the color that the user
        wants to fill the shape with
        ;poly: the line color around the shape
        ;side1: a parallelogram side
        ;side2: a parallelogram side
        ;angle: the top left angle in the parallelogram
        """
        self.area = side1*side2
        dot = [x, y]
        dot.append(x + side1)
        dot.append(y)
        dot.append(side1 + x-side2 *
                   math.sin(math.radians(angle-90)))
        dot.append((y+side2 *
                    math.cos(math.radians(angle-90))))
        dot.append(x-side2 *
                   math.sin(math.radians(angle-90)))
        dot.append((y+side2 *
                    math.cos(math.radians(angle-90))))
        super(Parallelogram, self).__init__(dot, color, poly)

    def calc_area(self):
        """
        a function that calculate the parallelogram's area
        """
        return self.area

    def move_me(self, x, y):
        pass