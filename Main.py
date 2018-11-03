"""
author: Yotam Levir
project: Holyday project
"""

import sys
path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]
path_to_tool += "/" + "Shapes"
sys.path.insert(0, path_to_tool)
from Right_Triangle import *
from Isosceles_tri import *
from Square import *
from Equilateral_Triangle import *
from Rectangle import *
from Parallelogram import *
from Circle import *
from Ellipse import *
from Main_GUI import *


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
    x = 500
    y = 100
    side1 = 100
    side2 = 300
    color = "tan1"
    ri_tri = Right_Tri(x, y, side1, side2, color)
    ri_tri.draw_me(canvas)
    print "The right triangle's area is: ", ri_tri.calc_area()

    #Isosceles triangle
    x = 500
    y = 500
    base = 600
    side = 500
    color = BLACK
    is_tri = Isosceles_Tri(x, y, base, side, color)
    is_tri.draw_me(canvas)
    print "The Isosceles triangle's area is:  ", is_tri.calc_area()


    #Equilateral Triangle
    x = 500
    y = 500
    side1 = 300
    color = GREEN
    equ_tri = Equilateral_Triangle(x, y, side1, color)
    equ_tri.draw_me(canvas)
    print "The Equilateral Triangle's area is: ", equ_tri.calc_area()

    #square
    x = 500
    y = 500
    side1 = 150
    color = RED
    sqr = Square(x, y, side1, color)
    sqr.draw_me(canvas)
    print "The square's area is: ", sqr.calc_area()

    #Rectangle
    re = [300, 300, 150, 50]
    x = 300
    y = 300
    side1 = 150
    side2 = 50
    color = GREEN
    rec = Rectangle(x, y, side1, side2, color)
    rec.draw_me(canvas)
    print "The Rectangle's area is: ", rec.calc_area()

    #Parallelogram
    x = 500
    y = 400
    side1 = 100
    side2 = 50
    angle = 150
    color = RED
    para = Parallelogram(x, y, side1, side2, angle, color)
    para.draw_me(canvas)
    print "The Parallelogram area is: ", para.calc_area()

    #Circle
    x = 200
    y = 200
    radius = 200
    color = RED
    cr = Circle(x, y, radius, color)
    cr.draw_me(canvas)
    print "The Circle area is: ", cr.calc_area()

    #Ellipse
    x = 200
    y = 200
    hor_rad = 200
    rad = 100
    color = BLUE
    el = Ellipse(x, y, hor_rad, rad, color)
    el.draw_me(canvas)
    print "The Ellipse area is: ", el.calc_area()
    root.mainloop()

if __name__ == '__main__':
    main()