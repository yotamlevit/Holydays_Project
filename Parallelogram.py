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
        self.area = values[2]*values[3]
        dot = [values[0], values[1]]
        dot.append(values[0] + values[2])
        dot.append(values[1])
        dot.append(values[2] + values[0]-values[3] *
                   math.sin(math.radians(values[4]-90)))
        dot.append((values[1]+values[3] *
                    math.cos(math.radians(values[4]-90))))
        dot.append(values[0]-values[3] *
                   math.sin(math.radians(values[4]-90)))
        dot.append((values[1]+values[3] *
                    math.cos(math.radians(values[4]-90))))
        super(Parallelogram, self).__init__(dot, color)

    def calc_area(self):
        """
        a function that calculate the parallelogram's area
        """
        return self.area

    def move_me(self, x, y):
        pass