from Shape import *
WHITE = (255, 255, 255)

class Polygon(Shape):
    def __init__(self, dot, color):
        super(Polygon, self).__init__(color)
        self.dot = dot
        self.color = color

    def draw_me(self, canvas):
        canvas.create_polygon(self.dot, fill=self.color)

    def calc_area(self):
        pass

    def move_me(self, x, y):
        pass