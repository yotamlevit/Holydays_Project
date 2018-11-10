#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 10, 2018 02:31:33 PM +0200  platform: Windows NT

import sys
from Polygon import *
import ast
import Shape_Func


COLORS=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
'indian red', 'saddle brown', 'sandy brown',
'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
'pale violet red', 'maroon', 'medium violet red', 'violet red',
'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
'thistle', 'snow2', 'snow3',
'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99', 'black']


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


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Create_Polygon_ (root)
    root.mainloop()

w = None
def create_Create_Polygon_(root, data_obj, canvas, shape=None, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Create_Polygon_ (root, data_obj, canvas, shape,w)
    return (w, top)

def destroy_Create_Polygon_():
    global w
    w.destroy()
    w = None


class Create_Polygon_:
    def __init__(self, root, data_obj, canvas, shape, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("600x120+650+150")
        top.configure(background="#d9d9d9")

        if shape is None:
            top.title("Create Polygon ")
        else:
            top.title("Mode Polygon ")
            Shape_Func.create_Shape_Change(top, data_obj, canvas, shape)

        self.data = data_obj
        self.shape = shape
        self.canv = canvas

        self.txt_dot = Label(top)
        self.txt_dot.place(relx=0.05, rely=0.333, height=21, width=44)
        self.txt_dot.configure(background="#d9d9d9")
        self.txt_dot.configure(disabledforeground="#a3a3a3")
        self.txt_dot.configure(foreground="#000000")
        self.txt_dot.configure(text='''Dots  -''')

        self.txt_create = Label(top)
        self.txt_create.place(relx=0.05, rely=0.083, height=21, width=87)
        self.txt_create.configure(background="#d9d9d9")
        self.txt_create.configure(disabledforeground="#a3a3a3")
        self.txt_create.configure(foreground="#000000")
        self.txt_create.configure(text='''Create Polygon''')

        self.dot = Entry(top)
        self.dot.place(relx=0.15, rely=0.333,height=20, relwidth=0.84)
        self.dot.configure(background="white")
        self.dot.configure(disabledforeground="#a3a3a3")
        self.dot.configure(font=font10)
        self.dot.configure(foreground="#000000")
        self.dot.configure(insertbackground="black")
        self.dot.configure(width=504)

        self.txt_color = Label(top)
        self.txt_color.place(relx=0.05, rely=0.667, height=21, width=46)
        self.txt_color.configure(background="#d9d9d9")
        self.txt_color.configure(disabledforeground="#a3a3a3")
        self.txt_color.configure(foreground="#000000")
        self.txt_color.configure(text='''Color -''')

        self.color = Entry(top)
        self.color.place(relx=0.15, rely=0.667,height=20, relwidth=0.123)
        self.color.configure(background="white")
        self.color.configure(disabledforeground="#a3a3a3")
        self.color.configure(font=font10)
        self.color.configure(foreground="#000000")
        self.color.configure(insertbackground="black")
        self.color.configure(width=74)

        self.txt_line = Label(top)
        self.txt_line.place(relx=0.3, rely=0.667, height=21, width=36)
        self.txt_line.configure(background="#d9d9d9")
        self.txt_line.configure(disabledforeground="#a3a3a3")
        self.txt_line.configure(foreground="#000000")
        self.txt_line.configure(text='''Line -''')

        self.line = Entry(top)
        self.line.place(relx=0.383, rely=0.667,height=20, relwidth=0.123)
        self.line.configure(background="white")
        self.line.configure(disabledforeground="#a3a3a3")
        self.line.configure(font=font10)
        self.line.configure(foreground="#000000")
        self.line.configure(insertbackground="black")
        self.line.configure(width=74)

        self.create = Button(top)
        self.create.place(relx=0.533, rely=0.583, height=34, width=267)
        self.create.configure(activebackground="#d9d9d9")
        self.create.configure(activeforeground="#000000")
        self.create.configure(background="#d9d9d9")
        self.create.configure(disabledforeground="#a3a3a3")
        self.create.configure(foreground="#000000")
        self.create.configure(highlightbackground="#d9d9d9")
        self.create.configure(highlightcolor="black")
        self.create.configure(pady="0")
        self.create.configure(text='''Create''')
        self.create.configure(width=267)
        self.create.bind('<Button-1>',lambda e: self.button_pres())

        if shape is None:
            self.color.insert(0,"black")
            self.line.insert(0, "black")
            self.dot.insert(0, "[100, 100, 150, 200, 300, 400]")
        else:
            value = self.data.get_obj(shape)[1]
            self.color.insert(0, value[1])
            self.line.insert(0, value[2])
            self.dot.insert(0, value[0])
            self.txt_create.configure(text='''Mode Isosceles Triangle''')


    def button_pres(self):
        dot = self.dot.get()
        color = self.color.get()
        line = self.line.get()
        if self.check_poly(dot) and color is not "" and color in COLORS and line in COLORS:
            if self.shape is not None:
                self.canv.delete(self.shape)
                self.data.delete_value(self.shape)
            dots = ast.literal_eval(dot)
            obj = [Polygon(dots, color, line), [dots, color, line]]
            obj_val = obj[0].draw_me(self.canv)
            self.data.set_value(obj_val, obj)
            destroy_Create_Polygon_()

    def check_poly(self, dot):
        lis = ast.literal_eval(dot)
        for element in lis:
            if type(element) is not int and type(element) is not float:
                return False
        return True






if __name__ == '__main__':
    vp_start_gui()



