from Polygon import *
import math

class Parallelogram(Polygon):
    def __init__(self, values, color):
        super(Parallelogram, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):

        locations = [self.values[0], self.values[1]]
        locations.append(self.values[0] + self.values[2])
        locations.append(self.values[1])
        locations.append(self.values[2] + self.values[0]-self.values[3]*math.sin(math.radians(self.values[4]-90)))
        locations.append((self.values[1]+self.values[3]*math.cos(math.radians(self.values[4]-90))))
        locations.append(self.values[0]-self.values[3]*math.sin(math.radians(self.values[4]-90)))
        locations.append((self.values[1]+self.values[3]*math.cos(math.radians(self.values[4]-90))))
        canvas.create_polygon(locations, fill=self.color)

    def calc_area(self):
        return self.values[2]*self.values[3]

    def move_me(self, x, y):
        pass