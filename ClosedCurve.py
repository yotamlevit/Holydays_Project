from Shape import *


class ClosedCurve(Shape):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that
        the class get from the user to create an closed curve shape
        ;color: is the color that the user wants to
        fill the closed curve shape with
        """
        super(ClosedCurve, self).__init__(color)
        self.values = values

    def draw_me(self, canvas):
        canvas.create_oval(self.values,
                           fill=self.color)

    def calc_area(self):
        pass

    def move_me(self, x, y):
        pass