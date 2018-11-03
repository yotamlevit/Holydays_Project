from Tkinter import *
import math
import subprocess
import Creat_Right_Tri as Right_tri
import sys

root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()


def main():
    dot = [100, 100, 150, 200, 300, 400, 500, 500]
    a = canvas.create_polygon(dot, fill="red")
    dot = [500, 500, 800, 900, 700, 500]
    b = canvas.create_polygon(dot, fill="blue")
    canvas.move(1,-100,-100)
    root.mainloop()

if __name__ == '__main__':
    main()