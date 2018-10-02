from abc import ABCMeta, abstractmethod


class Shape:

    __metaclass__ = ABCMeta

    def __init__(self, color):
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
