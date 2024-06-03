from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int):
        self.root = Tk()
        self.root.configure(width=width, height=height)
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.running = False

    


