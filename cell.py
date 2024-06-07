from graphics import Point, Window, Line

class Cell:
    def __init__(self, window: Window):
        self.has_top = True
        self.has_right = True
        self.has_bottom = True
        self.has_left = True
        self._win = window

    def __repr__(self):
        # return f"Cell(t: {self.has_top}, r: {self.has_right}, b: {self.has_bottom}, l: {self.has_left})"
        return f"Cell()"

    def draw(self, top_l_pt: Point, bot_r_pt: Point):
        self._top_l_pt = top_l_pt
        self._bot_r_pt = bot_r_pt
        if self.has_top:
            tline = Line(self._top_l_pt, Point(self._bot_r_pt.x, self._top_l_pt.y))
            self._win.draw_line(tline, "black")
        if self.has_right:
            rline = Line(Point(self._bot_r_pt.x, self._top_l_pt.y), self._bot_r_pt)
            self._win.draw_line(rline, "black")
        if self.has_bottom:
            bline = Line(self._bot_r_pt, Point(self._top_l_pt.x, self._bot_r_pt.y))
            self._win.draw_line(bline, "black")
        if self.has_left:
            lline = Line(Point(self._top_l_pt.x, self._bot_r_pt.y), self._top_l_pt)
            self._win.draw_line(lline, "black")
    
    def draw_move(self, to_cell, undo: bool=False):
        if undo:
            lcolor = "gray"
        else:
            lcolor = "red"
        self_center = self._center()
        other_center = to_cell._center()
        move = Line(self_center, other_center)
        self._win.draw_line(move, lcolor)

    def _center(self):
        x = (self._top_l_pt.x + self._bot_r_pt.x) // 2
        y = (self._top_l_pt.y + self._bot_r_pt.y) // 2
        return Point(x, y)

