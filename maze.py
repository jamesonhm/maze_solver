import random
import time

from graphics import Line, Point, Window
from cell import Cell

class Maze:
    def __init__(self, 
                 xpos: int, 
                 ypos:int, 
                 nrows: int, 
                 ncols: int, 
                 cell_size_x: int, 
                 cell_size_y: int, 
                 seed: int | None = None,
                 win: Window | None = None):
        self._cells = []
        self.xpos = xpos
        self.ypos = ypos
        self.nrows = nrows
        self.ncols = ncols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        random.seed(seed)
        self._win = win 
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.ncols):
            cells = []
            for j in range(self.nrows):
                cells.append(Cell(self._win))
            self._cells.append(cells)
        # row = [Cell(self._win) for _ in range(self.ncols)]
        # self._cells = [row for _ in range(self.nrows)]
        # print(self._cells)
        for i in range(self.ncols):
            for j in range(self.nrows):
                self._draw_cell(i, j)
        
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
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom = False
        self._draw_cell(self.ncols-1, self.nrows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            adjacent_cells = self._get_adjacent_cells(i, j)
            for cell in adjacent_cells:
                if not self._cells[cell[0]][cell[1]].visited:
                    to_visit.append(cell)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            next = random.choice(to_visit)
            self._connect_cells((i, j), next)
            self._break_walls_r(next[0], next[1])
    
    def _get_adjacent_cells(self, i, j):
        possibles = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        cells = [(c, r) for (c, r) in possibles if 0 <= c < self.ncols and 0 <= r < self.nrows]
        return cells

    def _connect_cells(self, c1, c2):
        if c2[1] > c1[1]:
            # c2 below c1
            self._cells[c1[0]][c1[1]].has_bottom = False
            self._draw_cell(c1[0], c1[1])
            self._cells[c2[0]][c2[1]].has_top = False
            self._draw_cell(c2[0], c2[1])
        elif c2[1] < c1[1]:
            #c2 above c1
            self._cells[c1[0]][c1[1]].has_top = False
            self._draw_cell(c1[0], c1[1])
            self._cells[c2[0]][c2[1]].has_bottom = False
            self._draw_cell(c2[0], c2[1])
        if c2[0] > c1[0]:
            # c2 right c1
            self._cells[c1[0]][c1[1]].has_right = False
            self._draw_cell(c1[0], c1[1])
            self._cells[c2[0]][c2[1]].has_left = False
            self._draw_cell(c2[0], c2[1])
        elif c2[0] < c1[0]:
            #c2 left c1
            self._cells[c1[0]][c1[1]].has_left = False
            self._draw_cell(c1[0], c1[1])
            self._cells[c2[0]][c2[1]].has_right = False
            self._draw_cell(c2[0], c2[1])

    def _cells_open(self, c1, c2):
        if c2[1] > c1[1]:
            # c2 below c1
            if self._cells[c1[0]][c1[1]].has_bottom == False and self._cells[c2[0]][c2[1]].has_top == False:
                return True
            return False
        elif c2[1] < c1[1]:
            #c2 above c1
            if self._cells[c1[0]][c1[1]].has_top == False and self._cells[c2[0]][c2[1]].has_bottom == False:
                return True
            return False
        elif c2[0] > c1[0]:
            # c2 right c1
            if self._cells[c1[0]][c1[1]].has_right == False and self._cells[c2[0]][c2[1]].has_left == False:
                return True
            return False
        elif c2[0] < c1[0]:
            #c2 left c1
            if self._cells[c1[0]][c1[1]].has_left == False and self._cells[c2[0]][c2[1]].has_right == False:
                return True
            return False

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.ncols-1 and j == self.nrows-1:
            return True
        adjacent_cells = self._get_adjacent_cells(i, j)
        for cell in adjacent_cells:
            if self._cells_open((i, j), cell) and self._cells[cell[0]][cell[1]].visited == False:
                # self._draw_move(self._cells[i][j], self._cells[cell[0]][cell[1]])
                self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]])
                if self._solve_r(cell[0], cell[1]):
                    return True
                else:
                    #self._draw_undo(self._cells[i][j], self._cells[cell[0]][cell[1]])
                    self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]], undo=True)
        return False

    def _draw_move(self, c1, c2):
        move = Line(c1._center(), c2._center())
        self._win.draw_line(move, "red")

    def _draw_undo(self, c1, c2):
        move = Line(c1._center(), c2._center())
        self._win.draw_line(move, self._win.bg_color)

