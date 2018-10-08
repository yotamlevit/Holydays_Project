from Polygon import *


class Rectangle(Polygon):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from
        the user to create a rectangle, including start point,
        the big side length and the small side length
        ;color: is the color that the user wants to fill the rectangle with
        """
        super(Rectangle, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw a rectangle on the
        screen using the values that the user gave
        """
        canvas.create_rectangle(self.values[0], self.values[1],
                                self.values[0] + self.values[2],
                                self.values[1] + self.values[3],
                                fill=self.color)

    def calc_area(self):
        """
        a function that calculate the rectangle's area
        """
        return self.values[2] * self.values[3]

    def move_me(self, x, y):
        pass