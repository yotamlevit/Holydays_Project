from abc import ABCMeta, abstractmethod
import math


class Shape:

    __metaclass__ = ABCMeta

    def __init__(self, color):
        """
        an initializer for the class
        ;ani: bool - animation on or off
        ;color: is the color that the user wants to fill the shape with
        """
        self.ani = False
        self.color = "white"

    @abstractmethod
    def draw_me(self, canvas):
        pass

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def move_me(self, x, y):
        pass

    def animation_on(self):
        self.ani = True

    def animation_on(self):
        self.ani = True

    def set_fill_color(self, color):
        self.color = color
