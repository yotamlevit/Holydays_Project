#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Oct 29, 2018 11:08:08 AM +0200  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Creat_Right_Tri_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Creat_Right_Tri_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Creat_Right_Tri_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
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

        top.geometry("311x183+559+180")
        top.title("Creat Right Teiangle")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.side_one = tk.Entry(top)
        self.side_one.place(relx=0.289, rely=0.273,height=20, relwidth=0.206)
        self.side_one.configure(background="white")
        self.side_one.configure(disabledforeground="#a3a3a3")
        self.side_one.configure(font=font10)
        self.side_one.configure(foreground="#000000")
        self.side_one.configure(insertbackground="black")
        self.side_one.configure(width=64)

        self.lab46 = tk.Label(top)
        self.lab46.place(relx=0.032, rely=0.273, height=31, width=62)
        self.lab46.configure(background="#d9d9d9")
        self.lab46.configure(disabledforeground="#a3a3a3")
        self.lab46.configure(foreground="#000000")
        self.lab46.configure(text='''Side One -''')
        self.lab46.configure(width=62)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.032, rely=0.437, height=21, width=62)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Side Two -''')

        self.side_two = tk.Entry(top)
        self.side_two.place(relx=0.289, rely=0.437,height=20, relwidth=0.206)
        self.side_two.configure(background="white")
        self.side_two.configure(disabledforeground="#a3a3a3")
        self.side_two.configure(font=font10)
        self.side_two.configure(foreground="#000000")
        self.side_two.configure(insertbackground="black")
        self.side_two.configure(width=64)

        self.x_start = tk.Entry(top)
        self.x_start.place(relx=0.289, rely=0.601,height=20, relwidth=0.206)
        self.x_start.configure(background="white")
        self.x_start.configure(disabledforeground="#a3a3a3")
        self.x_start.configure(font=font10)
        self.x_start.configure(foreground="#000000")
        self.x_start.configure(insertbackground="black")
        self.x_start.configure(width=64)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.032, rely=0.601, height=21, width=77)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Start Point (x)''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.032, rely=0.055, height=41, width=134)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Creat Right Triangle''')
        self.Label4.configure(width=134)

        self.Creat = tk.Button(top)
        self.Creat.place(relx=0.514, rely=0.273, height=114, width=117)
        self.Creat.configure(activebackground="#d9d9d9")
        self.Creat.configure(activeforeground="#000000")
        self.Creat.configure(background="#d9d9d9")
        self.Creat.configure(disabledforeground="#a3a3a3")
        self.Creat.configure(foreground="#000000")
        self.Creat.configure(highlightbackground="#d9d9d9")
        self.Creat.configure(highlightcolor="black")
        self.Creat.configure(pady="0")
        self.Creat.configure(text='''Creat''')
        self.Creat.configure(width=117)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.032, rely=0.765, height=21, width=74)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Start Point (y)''')
        self.Label5.configure(width=74)

        self.y_start = tk.Entry(top)
        self.y_start.place(relx=0.289, rely=0.765,height=20, relwidth=0.206)
        self.y_start.configure(background="white")
        self.y_start.configure(disabledforeground="#a3a3a3")
        self.y_start.configure(font=font10)
        self.y_start.configure(foreground="#000000")
        self.y_start.configure(insertbackground="black")
        self.y_start.configure(width=64)

if __name__ == '__main__':
    vp_start_gui()





