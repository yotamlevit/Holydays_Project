# -*- coding: utf-8 -*-
import pygame
from Polygon import *
from ClosedCurve import *
from Right_Triangle import *
from Isosceles_tri import *
from Square import *
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Init screen

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shapes")

def main():
    """
    poly = Polygon(dot)
    poly.draw_me(screen)
    """
    point = [500, 100, 300, 200]
    clos = ClosedCurve(point, RED)
    clos.draw_me(screen)
    dot = [(100, 100), (150, 200), (300, 400), (500, 500)]
    poly = Polygon(dot, WHITE)
    poly.draw_me(screen)
    dot_sq = [(400, 400), (500, 500), (600, 400), (500, 300)]
    dot_sq2 = [(400, 400), (400, 500), (500, 500), (500, 400)]
    squ = Square(dot_sq2, RED)
    squ.draw_me(screen)
    print "55555555555555555555555"
    print squ.calc_area()
    dot1 = [(100, 100), (150, 100), (100, 200)]
    ri_tri = Right_Tri(dot1, BLUE)
    ri_tri.draw_me(screen)
    ri_tri.calc_area()
    dot2 = [(500,500 ), (700, 500), (600, 900)]
    iso_tri = Isosceles_Tri(dot2, GREEN)
    iso_tri.draw_me(screen)
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
    pygame.QUIT


if __name__ == '__main__':
    main()