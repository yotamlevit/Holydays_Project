#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Oct 29, 2018 11:39:43 AM +0200  platform: Windows NT

import sys
import Creat_Right_Tri

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

def Creat_Right_Tri(p1,p2,p3,root):
    Creat_Right_Tri.Toplevel1(root)
    print('Main_GUI_support.Creat_Right_Tri')
    print('p1 = {0}'.format(p1))
    print('p2 = {0}'.format(p2))
    print('p3 = {0}'.format(p3))
    sys.stdout.flush()

def xxx(p1):
    print('Main_GUI_support.xxx')
    print('p1 = {0}'.format(p1))
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Main_GUI.py
    Main_GUI.py.vp_start_gui()




