from Tkinter import *
import math
root = Tk()
import subprocess
import Creat_Right_Tri as Right_tri
import sys




def main():
    path_to_tool = sys.argv[0].split("/")
    path_to_tool.pop()
    temp = ""
    for word in path_to_tool:
        temp += word + "/"
    path_to_tool = temp[:-1]
    path_to_tool += "/" + "Creat_Right_Tri"
    print path_to_tool
    value = ["pytohn", path_to_tool] + []
    a = subprocess.check_output([value, root)
    print a


if __name__ == '__main__':
    main()