from graphics import Point, Window
from cell import Cell


def main():
    win = Window(800, 600, "teal")
    # l1 = Line(Point(10, 10), Point(200, 200))
    # l2 = Line(Point(10, 50), Point(100, 500))
    # win.draw_line(l1, "orange")
    # win.draw_line(l2, "purple")
    c1 = Cell(win)
    c1.has_left=False
    c1.draw(Point(10, 10), Point(50, 50))

    c2 = Cell(win)
    c2.has_bottom=False
    c2.draw(Point(50, 10), Point(90, 50))

    c3 = Cell(win)
    c3.has_top=False
    c3.draw(Point(90, 10), Point(130, 50))

    win.wait_for_close()

main()

