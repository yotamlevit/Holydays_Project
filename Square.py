from Polygon import *


class Square(Polygon):
    def __init__(self, values, color):
        super(Square, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        canvas.create_rectangle(self.values[0], self.values[1], self.values[0] + self.values[2], self.values[1] + self.values[2], fill=self.color)

    def calc_area(self):
        return self.values[2]**2

    def move_me(self, x, y):
        pass