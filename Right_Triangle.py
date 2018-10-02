from Polygon import *

class Right_Tri(Polygon):
    def __init__(self, dot, color):
        super(Right_Tri, self).__init__(dot, color)
        self.dot = dot
        self.color = color

    def calc_area(self):
        arr = super(Right_Tri, self).get_tri_len(self.dot)
        arr.sort()
        return arr[0]*arr[1]/2


    def move_me(self, x, y):
        pass