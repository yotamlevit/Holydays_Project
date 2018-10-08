from ClosedCurve import *


class Ellipse(ClosedCurve):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from
        the user to create an ellipse, including cernter
        semi-major axe and the emi-minor axe
        ;color: is the color that the user wants to
        fill the ellipse with
        """
        super(Ellipse, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw an ellipse on the screen
        using the values that the user gave
        """
        canvas.create_oval(self.value[0]-self.value[2],
                           self.value[1]-self.value[3],
                           self.value[0]+self.value[2],
                           self.value[1]+self.value[3],
                           fill=self.color)

    def calc_area(self):
        """
        a function that calculate the ellipse's area
        """
        return math.pi * self.value[2] * self.value[3]

    def move_me(self, x, y):
        pass