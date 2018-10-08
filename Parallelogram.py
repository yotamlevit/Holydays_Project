from Polygon import *


class Parallelogram(Polygon):
    def __init__(self, values, color):
        """
        an initializer for the class
        ;values: is a list of the values that the class get from the user
        to create a parallelogram, including start point,
        the big side length and the small side length
        ;color: is the color that the user wants to fill the parallelogram with
        """
        super(Parallelogram, self).__init__(values, color)
        self.values = values
        self.color = color

    def draw_me(self, canvas):
        """
        a function that draw a parallelogram on the screen
        using the values that the user gave
        """
        locations = [self.values[0], self.values[1]]
        locations.append(self.values[0] + self.values[2])
        locations.append(self.values[1])
        locations.append(self.values[2] + self.values[0]-self.values[3] *
                         math.sin(math.radians(self.values[4]-90)))
        locations.append((self.values[1]+self.values[3] *
                          math.cos(math.radians(self.values[4]-90))))
        locations.append(self.values[0]-self.values[3] *
                         math.sin(math.radians(self.values[4]-90)))
        locations.append((self.values[1]+self.values[3] *
                          math.cos(math.radians(self.values[4]-90))))
        canvas.create_polygon(locations, fill=self.color)

    def calc_area(self):
        """
        a function that calculate the parallelogram's area
        """
        return self.values[2]*self.values[3]

    def move_me(self, x, y):
        pass