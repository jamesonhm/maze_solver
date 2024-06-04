from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    l1 = Line(Point(10, 10), Point(200, 200))
    l2 = Line(Point(10, 50), Point(100, 500))
    win.draw_line(l1, "orange")
    win.draw_line(l2, "purple")
    win.wait_for_close()

main()

