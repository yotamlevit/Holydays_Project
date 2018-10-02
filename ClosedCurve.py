from Shape import *
import pygame

class ClosedCurve(Shape):
    def __init__(self, corners, color):
        super(ClosedCurve, self).__init__(color)
        self.corners = corners
        self.color = color

    def draw_me(self, canvas):
        pygame.draw.ellipse(canvas, self.color, self.corners, 2)
        pygame.display.flip()

    def calc_area(self):
        pass

    def move_me(self, x, y):
        pass