"""
author: Yotam Levir
project: Holyday project
"""

from Tkinter import *
from Right_Triangle import *
from Isosceles_tri import *
from Square import *
from Equilateral_Triangle import *
from Rectangle import *
from Parallelogram import *
from Circle import *
from Ellipse import *


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
BLACK = "black"
WHITE = "white"
BLUE = "blue"
GREEN = "green"
RED = "red"

#Init scree
root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()


def main():

    #polygon
    dot = [100, 100, 150, 200, 300, 400, 500, 500]
    poly = Polygon(dot, WHITE)
    poly.draw_me(canvas)

    #right triangle
    val_ri_tri = [500, 100, 100, 300]
    ri_tri = Right_Tri(val_ri_tri, BLUE)
    ri_tri.draw_me(canvas)
    print "The right triangle's area is: ", ri_tri.calc_area()

    #Isosceles triangle
    is_tri1 = [500, 500, 600, 500]
    is_tri = Isosceles_Tri(is_tri1, BLACK)
    is_tri.draw_me(canvas)
    print "The Isosceles triangle's area is:  ", is_tri.calc_area()

    #Equilateral Triangle
    equ = [500, 500, 300]
    equ_tri = Equilateral_Triangle(equ, GREEN)
    equ_tri.draw_me(canvas)
    print "The Equilateral Triangle's area is: ", equ_tri.calc_area()

    #square
    sq = [500, 500, 150]
    sqr = Square(sq, RED)
    sqr.draw_me(canvas)
    print "The square's area is: ", sqr.calc_area()

    #Rectangle
    re = [300, 300, 150, 50]
    rec = Rectangle(re, GREEN)
    rec.draw_me(canvas)
    print "The Rectangle's area is: ", rec.calc_area()

    #Parallelogram
    pa = [500, 400, 100, 50, 150]
    para = Parallelogram(pa, RED)
    para.draw_me(canvas)
    print "The Parallelogram area is: ", para.calc_area()

    #Circle
    cer = [200, 200, 200]
    cr = Circle(cer, RED)
    cr.draw_me(canvas)
    print "The Circle area is: ", cr.calc_area()

    #Ellipse
    ell = [200, 200, 200, 100]
    el = Ellipse(ell, BLUE)
    el.draw_me(canvas)
    print "The Ellipse area is: ", el.calc_area()
    root.mainloop()

if __name__ == '__main__':
    main()