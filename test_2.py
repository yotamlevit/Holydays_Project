from Tkinter import *
import math
root = Tk()

canvas = Canvas(root, width = 2000, height = 2000)
canvas.pack()
dot = [100, 100, 150, 200, 300, 400, 500, 500]
temp = [100, 100, 100, 200, 300, 200]

canvas.create_oval(10, 10, 80, 80, fill="green", width=2)
canvas.create_oval(10, 10, 1000, 1000, fill="green", width=2)
#rec = canvas.create_rectangle(200, 500, 150, 150, fill = "green")
#canvas.create_polygon(dot, fill = "green")
root.mainloop()


def main():
    is_tri1 = [500, 500, 600, 500]
    print is_tri1[2]/2
    print is_tri1[3]
    print is_tri1[2]+0.0/is_tri1[3]+0.0
    print math.acos(is_tri1[2]+0.0/2/is_tri1[3]+0.0)


if __name__ == '__main__':
    main()