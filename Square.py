from Polygon import *
class Square(Polygon):
    def __init__(self, dot, color):
        super(Square, self).__init__(dot, color)
        self.dot = dot
        self.color = color

    def calc_area(self):
        if self.dot[0][0] >= self.dot[1][0]:
            x = self.dot[0][0] - self.dot[1][0]
        else:
            x = self.dot[1][0] - self.dot[0][0]
        if self.dot[0][1] >= self.dot[1][1]:
            y = self.dot[0][1] - self.dot[1][1]
        else:
            y = self.dot[1][1] - self.dot[0][1]
        return math.pow(x, 2) + math.pow(y, 2)


    def move_me(self, x, y):
        pass