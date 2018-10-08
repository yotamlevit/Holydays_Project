from ClosedCurve import *


class Circle(ClosedCurve):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class
        get from the user to create a circle,
        including cernter and radius
        ;color: is the color that the user
        wants to fill the circle with
        """
        super(Circle, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw a circle on the screen
        using the values that the user gave
        """
        canvas.create_oval(self.value[0]-self.value[2],
                           self.value[1]-self.value[2],
                           self.value[0]+self.value[2],
                           self.value[1]+self.value[2],
                           fill=self.color)

    def calc_area(self):
        """
        a function that calculate the circle's area
        """
        return math.pi * self.value[2]**2

    def move_me(self, x, y):
        pass