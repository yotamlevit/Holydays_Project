import Tkinter
class GUI(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid

if __name__ == "__main__":
    app = GUI(None)
    app.title('my application')
    app.mainloop()