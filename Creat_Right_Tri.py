#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 02, 2018 08:56:19 PM +0200  platform: Windows NT

import sys
import Shape_Func
path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]
#sys.path.insert(0, path_to_tool + "/" + "Shapes")
from Right_Triangle import *
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
'lawn green', 'green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
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
    top = Creat_Right_Teiangle (root)
    root.mainloop()

w = None
def create_Creat_Right_Teiangle(root, data_obj, canvas, shape=None, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Creat_Right_Teiangle(data_obj, canvas, shape, w)
    return (w, top)

def destroy_Creat_Right_Teiangle():
    global w
    w.destroy()
    w = None


class Creat_Right_Teiangle:
    def __init__(self, data_obj, canvas, shape, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("310x217+618+177")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        if shape is None:
            top.title("Creat Right Teiangle")
        else:
            top.title("Mode Right Teiangle")
            Shape_Func.create_Shape_Change(top, data_obj, canvas, shape)

        self.shape = shape
        self.canv = canvas
        self.data = data_obj


        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.line = Entry(top)
        self.line.place(relx=0.29, rely=0.200, height=20, relwidth=0.206)
        self.line.configure(background="white")
        self.line.configure(disabledforeground="#a3a3a3")
        self.line.configure(font=font10)
        self.line.configure(foreground="#000000")
        self.line.configure(highlightbackground="#d9d9d9")
        self.line.configure(highlightcolor="black")
        self.line.configure(insertbackground="black")
        self.line.configure(selectbackground="#c4c4c4")
        self.line.configure(selectforeground="black")

        self.txt_line = Label(top)
        self.txt_line.place(relx=0.032, rely=0.150, height=41, width=62)
        self.txt_line.configure(activebackground="#f9f9f9")
        self.txt_line.configure(activeforeground="black")
        self.txt_line.configure(background="#d9d9d9")
        self.txt_line.configure(disabledforeground="#a3a3a3")
        self.txt_line.configure(foreground="#000000")
        self.txt_line.configure(highlightbackground="#d9d9d9")
        self.txt_line.configure(highlightcolor="black")
        self.txt_line.configure(text='''Line color''')
        self.txt_line.configure(width=62)

        self.side_one = Entry(top)
        self.side_one.place(relx=0.29, rely=0.323,height=20, relwidth=0.206)
        self.side_one.configure(background="white")
        self.side_one.configure(disabledforeground="#a3a3a3")
        self.side_one.configure(font=font10)
        self.side_one.configure(foreground="#000000")
        self.side_one.configure(highlightbackground="#d9d9d9")
        self.side_one.configure(highlightcolor="black")
        self.side_one.configure(insertbackground="black")
        self.side_one.configure(selectbackground="#c4c4c4")
        self.side_one.configure(selectforeground="black")

        self.side_1 = Label(top)
        self.side_1.place(relx=0.032, rely=0.276, height=41, width=62)
        self.side_1.configure(activebackground="#f9f9f9")
        self.side_1.configure(activeforeground="black")
        self.side_1.configure(background="#d9d9d9")
        self.side_1.configure(disabledforeground="#a3a3a3")
        self.side_1.configure(foreground="#000000")
        self.side_1.configure(highlightbackground="#d9d9d9")
        self.side_1.configure(highlightcolor="black")
        self.side_1.configure(text='''Side One -''')
        self.side_1.configure(width=62)

        self.side_2 = Label(top)
        self.side_2.place(relx=0.032, rely=0.461, height=21, width=62)
        self.side_2.configure(activebackground="#f9f9f9")
        self.side_2.configure(activeforeground="black")
        self.side_2.configure(background="#d9d9d9")
        self.side_2.configure(disabledforeground="#a3a3a3")
        self.side_2.configure(foreground="#000000")
        self.side_2.configure(highlightbackground="#d9d9d9")
        self.side_2.configure(highlightcolor="black")
        self.side_2.configure(text='''Side Two -''')

        self.side_two = Entry(top)
        self.side_two.place(relx=0.29, rely=0.461,height=20, relwidth=0.206)
        self.side_two.configure(background="white")
        self.side_two.configure(disabledforeground="#a3a3a3")
        self.side_two.configure(font=font10)
        self.side_two.configure(foreground="#000000")
        self.side_two.configure(highlightbackground="#d9d9d9")
        self.side_two.configure(highlightcolor="black")
        self.side_two.configure(insertbackground="black")
        self.side_two.configure(selectbackground="#c4c4c4")
        self.side_two.configure(selectforeground="black")

        self.x_start = Entry(top)
        self.x_start.place(relx=0.29, rely=0.599,height=20, relwidth=0.206)
        self.x_start.configure(background="white")
        self.x_start.configure(disabledforeground="#a3a3a3")
        self.x_start.configure(font=font10)
        self.x_start.configure(foreground="#000000")
        self.x_start.configure(highlightbackground="#d9d9d9")
        self.x_start.configure(highlightcolor="black")
        self.x_start.configure(insertbackground="black")
        self.x_start.configure(selectbackground="#c4c4c4")
        self.x_start.configure(selectforeground="black")

        self.start_x = Label(top)
        self.start_x.place(relx=0.032, rely=0.599, height=21, width=77)
        self.start_x.configure(activebackground="#f9f9f9")
        self.start_x.configure(activeforeground="black")
        self.start_x.configure(background="#d9d9d9")
        self.start_x.configure(disabledforeground="#a3a3a3")
        self.start_x.configure(foreground="#000000")
        self.start_x.configure(highlightbackground="#d9d9d9")
        self.start_x.configure(highlightcolor="black")
        self.start_x.configure(text='''Start Point (x)''')

        self.txt_creat_right_triangle = Label(top)
        self.txt_creat_right_triangle.place(relx=0.032, rely=0.0, height=41
                , width=134)
        self.txt_creat_right_triangle.configure(activebackground="#f9f9f9")
        self.txt_creat_right_triangle.configure(activeforeground="black")
        self.txt_creat_right_triangle.configure(background="#d9d9d9")
        self.txt_creat_right_triangle.configure(disabledforeground="#a3a3a3")
        self.txt_creat_right_triangle.configure(foreground="#000000")
        self.txt_creat_right_triangle.configure(highlightbackground="#d9d9d9")
        self.txt_creat_right_triangle.configure(highlightcolor="black")
        self.txt_creat_right_triangle.configure(text='''Creat Right Triangle''')

        self.Creat = Button(top)
        self.Creat.place(relx=0.516, rely=0.184, height=164, width=137)
        self.Creat.configure(activebackground="#d9d9d9")
        self.Creat.configure(activeforeground="#000000")
        self.Creat.configure(background="#d9d9d9")
        self.Creat.configure(disabledforeground="#a3a3a3")
        self.Creat.configure(foreground="#000000")
        self.Creat.configure(highlightbackground="#d9d9d9")
        self.Creat.configure(highlightcolor="black")
        self.Creat.configure(pady="0")
        self.Creat.configure(text='''Creat''')
        self.Creat.configure(width=137)
        self.Creat.bind('<Button-1>',lambda e: self.button_pres())

        self.star_y = Label(top)
        self.star_y.place(relx=0.032, rely=0.737, height=21, width=74)
        self.star_y.configure(activebackground="#f9f9f9")
        self.star_y.configure(activeforeground="black")
        self.star_y.configure(background="#d9d9d9")
        self.star_y.configure(disabledforeground="#a3a3a3")
        self.star_y.configure(foreground="#000000")
        self.star_y.configure(highlightbackground="#d9d9d9")
        self.star_y.configure(highlightcolor="black")
        self.star_y.configure(text='''Start Point (y)''')

        self.y_start = Entry(top)
        self.y_start.place(relx=0.29, rely=0.737,height=20, relwidth=0.206)
        self.y_start.configure(background="white")
        self.y_start.configure(disabledforeground="#a3a3a3")
        self.y_start.configure(font=font10)
        self.y_start.configure(foreground="#000000")
        self.y_start.configure(highlightbackground="#d9d9d9")
        self.y_start.configure(highlightcolor="black")
        self.y_start.configure(insertbackground="black")
        self.y_start.configure(selectbackground="#c4c4c4")
        self.y_start.configure(selectforeground="black")

        self.Color = Entry(top)
        self.Color.place(relx=0.29, rely=0.876,height=20, relwidth=0.206)
        self.Color.configure(background="white")
        self.Color.configure(disabledforeground="#a3a3a3")
        self.Color.configure(font=font10)
        self.Color.configure(foreground="#000000")
        self.Color.configure(highlightbackground="#d9d9d9")
        self.Color.configure(highlightcolor="black")
        self.Color.configure(insertbackground="black")
        self.Color.configure(selectbackground="#c4c4c4")
        self.Color.configure(selectforeground="black")

        self.color = Label(top)
        self.color.place(relx=0.032, rely=0.876, height=21, width=61)
        self.color.configure(activebackground="#f9f9f9")
        self.color.configure(activeforeground="black")
        self.color.configure(background="#d9d9d9")
        self.color.configure(disabledforeground="#a3a3a3")
        self.color.configure(foreground="#000000")
        self.color.configure(highlightbackground="#d9d9d9")
        self.color.configure(highlightcolor="black")
        self.color.configure(text='''Color  ----''')

        if shape is None:
            self.Color.insert(0,"black")
            self.side_one.insert(0,"50")
            self.side_two.insert(0,"50")
            self.x_start.insert(0,"300")
            self.y_start.insert(0,"300")
            self.line.insert(0, "black")
        else:
            value = self.data.get_obj(shape)[1]
            self.Color.insert(0, value[4])
            self.side_one.insert(0, value[2])
            self.side_two.insert(0, value[3])
            self.x_start.insert(0, value[0])
            self.y_start.insert(0, value[1])
            self.line.insert(0, value[5])
            self.txt_creat_right_triangle.configure(text='''Mode Right Triangle''')


    def button_pres(self):
        """
        operating when the user clicked on the create
        button to create a shape or to change it
        if values are incorrect show msg in the screen
        """
        x = self.x_start.get()
        y = self.y_start.get()
        side1 = self.side_one.get()
        side2 = self.side_two.get()
        color = self.Color.get()
        line = self.line.get()
        if x.isdigit() and y.isdigit() and side1.isdigit() and side2.isdigit() and color is not "" and color in COLORS and line in COLORS and int(x) < 1001 and int(y) < 916:
            if self.shape is not None:
                self.canv.delete(self.shape)
                self.data.delete_value(self.shape)
            obj = [Right_Tri(int(x), int(y), int(side1), int(side2), color, line),[int(x), int(y), int(side1), int(side2), color, line]]
            obj_val = obj[0].draw_me(self.canv)
            self.data.set_value(obj_val, obj)
            destroy_Creat_Right_Teiangle()
        else:
            self.txt_creat_right_triangle.configure(text="invalid values")






if __name__ == '__main__':
    vp_start_gui()



