from Polygon import *

class Isosceles_Tri(Polygon):
    """
    the get_tri_len function only fits the right_tri
    *****there is need to do chenges to fit it so Iso_tri
    """
    def __init__(self, dot, color):
        super(Isosceles_Tri, self).__init__(dot, color)
        self.dot = dot
        self.color = color

    def calc_area(self):
        arr = super(Isosceles_Tri, self).get_tri_len(self.dot)
        arr.sort()
        seen = []
        index = 0
        for number in arr:
            if number in seen:
                break
            else:
                index += 1
                seen.append(number)
        if index == 0:
            index = 2
        else:
            index = 0
        return arr[0]*arr[1]/2



    def move_me(self, x, y):
        pass