from Polygon import *


class Square(Polygon):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from the user
        to create a square, including start point and the side's length
        ;color: is the color that the user wants to fill the square with
        """
        super(Square, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw a square on the screen
        using the values that the user gave
        """
        canvas.create_rectangle(self.values[0], self.values[1],
                                self.values[0]+self.values[2],
                                self.values[1]+self.values[2], fill=self.color)

    def calc_area(self):
        """
        a function that calculate the square's area
        """
        return self.values[2]**2

    def move_me(self, x, y):
        pass