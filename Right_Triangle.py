from Polygon import *

class Right_Tri(Polygon):
    def __init__(self, values, color):
        super(Right_Tri, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        temp = [self.values[0], self.values[1], self.values[0], self.values[2]+self.values[1], self.values[3]+self.values[0], self.values[2]+self.values[1]]
        print temp
        canvas.create_polygon(temp, fill= self.color)\


    def calc_area(self):
        return self.values[2]*self.values[3]/2


    def move_me(self, x, y):
        pass