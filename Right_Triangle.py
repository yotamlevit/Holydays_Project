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
        super(Right_Tri, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw a right triangle on the
        screen using the values that the user gave
        """
        temp = [self.values[0], self.values[1], self.values[0],
                self.values[2]+self.values[1], self.values[3]+self.values[0],
                self.values[2]+self.values[1]]
        canvas.create_polygon(temp, fill=self.color)

    def calc_area(self):
        """
        a function that calculate the right triangle's area
        """
        return self.values[2]*self.values[3]/2

    def move_me(self, x, y):
        pass