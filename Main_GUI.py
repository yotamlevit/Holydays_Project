#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 03, 2018 04:20:06 PM +0200  platform: Windows NT

import sys
from Data_Shapes import *
path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]
DATABASE = path_to_tool + "/" + "data.txt"

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Main_GUI_support




def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Paint (root)
    Main_GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Paint(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Paint (w)
    Main_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Paint():
    global w
    w.destroy()
    w = None


class Paint:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1116x897+414+73")
        top.title("Paint")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        with open(DATABASE, "w") as file:
            print "file cleared"

        self.data = DataBase()


        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.right_triangle = Button(top)
        self.right_triangle.place(relx=0.0, rely=0.0, height=94, width=127)
        self.right_triangle.configure(activebackground="#d9d9d9")
        self.right_triangle.configure(activeforeground="#000000")
        self.right_triangle.configure(background="#d9d9d9")
        self.right_triangle.configure(disabledforeground="#a3a3a3")
        self.right_triangle.configure(foreground="#000000")
        self.right_triangle.configure(highlightbackground="#d9d9d9")
        self.right_triangle.configure(highlightcolor="black")
        self.right_triangle.configure(pady="0")
        self.right_triangle.configure(text='''Right Triangle''')
        self.right_triangle.bind('<Button-1>',lambda e:Main_GUI_support.creat_right_tri(top, self.data, self.shape_c))

        self.isos_triangle = Button(top)
        self.isos_triangle.place(relx=0.0, rely=0.1, height=94, width=127)
        self.isos_triangle.configure(activebackground="#d9d9d9")
        self.isos_triangle.configure(activeforeground="#000000")
        self.isos_triangle.configure(background="#d9d9d9")
        self.isos_triangle.configure(disabledforeground="#a3a3a3")
        self.isos_triangle.configure(foreground="#000000")
        self.isos_triangle.configure(highlightbackground="#d9d9d9")
        self.isos_triangle.configure(highlightcolor="black")
        self.isos_triangle.configure(pady="0")
        self.isos_triangle.configure(text='''Isosceles Triangle''')
        self.isos_triangle.bind('<Button-1>',lambda e:Main_GUI_support.creat_isos_tri(top, self.data, self.shape_c))

        self.equilateral_triangle = Button(top)
        self.equilateral_triangle.place(relx=0.0, rely=0.201, height=84
                , width=127)
        self.equilateral_triangle.configure(activebackground="#d9d9d9")
        self.equilateral_triangle.configure(activeforeground="#000000")
        self.equilateral_triangle.configure(background="#d9d9d9")
        self.equilateral_triangle.configure(disabledforeground="#a3a3a3")
        self.equilateral_triangle.configure(foreground="#000000")
        self.equilateral_triangle.configure(highlightbackground="#d9d9d9")
        self.equilateral_triangle.configure(highlightcolor="black")
        self.equilateral_triangle.configure(pady="0")
        self.equilateral_triangle.configure(text='''Equilateral Triangle''')
        self.equilateral_triangle.bind('<Button-1>',lambda e:Main_GUI_support.creat_equilateral_triangle(top, self.data, self.shape_c))

        self.square = Button(top)
        self.square.place(relx=0.0, rely=0.29, height=94, width=127)
        self.square.configure(activebackground="#d9d9d9")
        self.square.configure(activeforeground="#000000")
        self.square.configure(background="#d9d9d9")
        self.square.configure(disabledforeground="#a3a3a3")
        self.square.configure(foreground="#000000")
        self.square.configure(highlightbackground="#d9d9d9")
        self.square.configure(highlightcolor="black")
        self.square.configure(pady="0")
        self.square.configure(text='''Square''')
        self.square.bind('<Button-1>',lambda e:Main_GUI_support.creat_square(top, self.data, self.shape_c))

        self.rectangle = Button(top)
        self.rectangle.place(relx=0.0, rely=0.39, height=94, width=127)
        self.rectangle.configure(activebackground="#d9d9d9")
        self.rectangle.configure(activeforeground="#000000")
        self.rectangle.configure(background="#d9d9d9")
        self.rectangle.configure(disabledforeground="#a3a3a3")
        self.rectangle.configure(foreground="#000000")
        self.rectangle.configure(highlightbackground="#d9d9d9")
        self.rectangle.configure(highlightcolor="black")
        self.rectangle.configure(pady="0")
        self.rectangle.configure(text='''Rectangle''')
        self.rectangle.bind('<Button-1>',lambda e:Main_GUI_support.creat_rectangle(top, self.data, self.shape_c))

        self.parallelogram = Button(top)
        self.parallelogram.place(relx=0.0, rely=0.491, height=94, width=127)
        self.parallelogram.configure(activebackground="#d9d9d9")
        self.parallelogram.configure(activeforeground="#000000")
        self.parallelogram.configure(background="#d9d9d9")
        self.parallelogram.configure(disabledforeground="#a3a3a3")
        self.parallelogram.configure(foreground="#000000")
        self.parallelogram.configure(highlightbackground="#d9d9d9")
        self.parallelogram.configure(highlightcolor="black")
        self.parallelogram.configure(pady="0")
        self.parallelogram.configure(text='''Parallelogram''')
        self.parallelogram.bind('<Button-1>',lambda e:Main_GUI_support.creat_parallelogram(top, self.data, self.shape_c))

        self.circle = Button(top)
        self.circle.place(relx=0.0, rely=0.591, height=94, width=127)
        self.circle.configure(activebackground="#d9d9d9")
        self.circle.configure(activeforeground="#000000")
        self.circle.configure(background="#d9d9d9")
        self.circle.configure(disabledforeground="#a3a3a3")
        self.circle.configure(foreground="#000000")
        self.circle.configure(highlightbackground="#d9d9d9")
        self.circle.configure(highlightcolor="black")
        self.circle.configure(pady="0")
        self.circle.configure(text='''Circle''')
        self.circle.bind('<Button-1>',lambda e:Main_GUI_support.creat_circle(top, self.data, self.shape_c))

        self.ellipse = Button(top)
        self.ellipse.place(relx=0.0, rely=0.691, height=104, width=127)
        self.ellipse.configure(activebackground="#d9d9d9")
        self.ellipse.configure(activeforeground="#000000")
        self.ellipse.configure(background="#d9d9d9")
        self.ellipse.configure(disabledforeground="#a3a3a3")
        self.ellipse.configure(foreground="#000000")
        self.ellipse.configure(highlightbackground="#d9d9d9")
        self.ellipse.configure(highlightcolor="black")
        self.ellipse.configure(pady="0")
        self.ellipse.configure(text='''Ellipse''')
        self.ellipse.bind('<Button-1>',lambda e:Main_GUI_support.creat_ellipse(top, self.data, self.shape_c))

        self.polygon = Button(top)
        self.polygon.place(relx=0.0, rely=0.803, height=104, width=127)
        self.polygon.configure(activebackground="#d9d9d9")
        self.polygon.configure(activeforeground="#000000")
        self.polygon.configure(background="#d9d9d9")
        self.polygon.configure(disabledforeground="#a3a3a3")
        self.polygon.configure(foreground="#000000")
        self.polygon.configure(highlightbackground="#d9d9d9")
        self.polygon.configure(highlightcolor="black")
        self.polygon.configure(pady="0")
        self.polygon.configure(text='''Polygon''')
        self.polygon.configure(width=127)
        self.polygon.bind('<Button-1>',lambda e:Main_GUI_support.creat_poligon(root, self.data, self.shape_c))

        self.shape_c = Canvas(top)
        self.shape_c.place(relx=0.108, rely=0.0, relheight=1.003, relwidth=0.896)
        self.shape_c.configure(background="#FEFFBD")
        self.shape_c.configure(borderwidth="2")
        self.shape_c.configure(insertbackground="black")
        self.shape_c.configure(relief=RIDGE)
        self.shape_c.configure(selectbackground="#c4c4c4")
        self.shape_c.configure(selectforeground="black")
        self.shape_c.configure(width=953)
        self.shape_c.bind('<Double-1>', self.click)

    def click(self, event):
        x, y = event.x, event.y
        if self.shape_c.find_overlapping(x, y,x,y):
            Main_GUI_support.click()



if __name__ == '__main__':
    vp_start_gui()



