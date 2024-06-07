import time

from graphics import Point, Window
from cell import Cell

class Maze:
    def __init__(self, 
                 xpos: int, 
                 ypos:int, 
                 nrows: int, 
                 ncols: int, 
                 cell_size_x: int, 
                 cell_size_y: int, 
                 win: Window):
        self.xpos = xpos
        self.ypos = ypos
        self.nrows = nrows
        self.ncols = ncols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win 
        self._create_cells()

    def _create_cells(self):
        row = [Cell(self._win) for _ in range(self.ncols)]
        self._cells = [row for _ in range(self.nrows)]
        # print(self._cells)
        for row in range(len(self._cells)):
            for col in range(len(self._cells[row])):
                self._draw_cell(row, col)
        
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x = self.xpos + (i * self.cell_size_x)
        y = self.ypos + (j * self.cell_size_y)
        topl = Point(x, y)
        botr = Point(x + self.cell_size_x, y + self.cell_size_y)
        self._cells[i][j].draw(topl, botr)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


