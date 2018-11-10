from abc import ABCMeta, abstractmethod
import math


class Shape:

    __metaclass__ = ABCMeta

    def __init__(self, color, poly):
        """
        an initializer for the class
        ;ani: bool - animation on or off
        ;color: is the color that the user wants to fill the shape with
        """
        self.ani = False
        self.color = color
        self.move = True
        self.poly = poly

    @abstractmethod
    def draw_me(self, canvas):
        pass

    @abstractmethod
    def calc_area(self):
        pass

    def move_me(self, x, y):
        if self.move:
            print m

    def animation_on(self):
        self.ani = True

    def animation_off(self):
        self.ani = False

    def set_fill_color(self, color):
        self.color = color
