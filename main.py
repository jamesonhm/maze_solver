from graphics import Window
from maze import Maze


def main():
    nrows = 10
    ncols = 10
    margin = 25
    screen_width = 800
    screen_height = 800
    cell_size_x = round((screen_width - 2*margin) // ncols)
    cell_size_y = round((screen_height - 2*margin) // nrows)
    win = Window(screen_width, screen_height, "gray")

    maze = Maze(margin, margin, nrows, ncols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

main()

