import tkinter


class Maze:

    def __init__(self, size, pac_dots):
        self.size = size
        self.hindrance = []
        self.pac_dots = pac_dots

    @staticmethod
    def create_maze():
        top = tkinter.Tk()
        top.title("Pacman")
        canvas = tkinter.Canvas(top, bg="black", height=500, width=650)
        canvas.pack()
        top.mainloop

    def draw_maze(self):
        pass


