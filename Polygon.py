from Shape import *
import pygame
import math
WHITE = (255, 255, 255)

class Polygon(Shape):
    def __init__(self, dot, color):
        super(Polygon, self).__init__(color)
        self.dot = dot
        self.color = color

    def draw_me(self, canvas):
        """
        index = len(self.dot) -1
        while index >= 0:
            pygame.draw.line(canvas, WHITE, [self.dot[index][0], self.dot[index][1]],
                             [self.dot[index-1][0], self.dot[index-1][1]], 4)
            pygame.display.flip()
            index -= 1
        """
        pygame.draw.polygon(canvas, self.color, self.dot, 5)
        pygame.display.flip()


    def get_tri_len(self, arr):
        """
        this function only work for right tri
        thia tunction can work only ig there is 2 points on the same line
        """
        count = 0
        side = []
        for point in arr:
            index = count
            while index < len(arr):
                if point != arr[index]:
                    if point[0] == arr[index][0]:
                        if point[1] > arr[index][1]:
                            side.append(point[1] - arr[index][1])
                        else:
                            side.append(arr[index][1] - point[1])
                    elif point[1] == arr[index][1]:
                        if point[0] > arr[index][0]:
                            side.append(point[0] - arr[index][0])
                        else:
                            side.append(arr[index][0] - point[0])
                index += 1
            count += 1
        side.append(math.sqrt(math.pow(side[0], 2) + math.pow(side[1], 2)))
        return side


    def calc_area(self):
        pass


    def move_me(self, x, y):
        pass