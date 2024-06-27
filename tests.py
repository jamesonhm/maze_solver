import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells2(self):
        xpos = 10
        ypos = 10
        num_cols = 5
        num_rows = 10
        m1 = Maze(xpos, ypos, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_break_entrance_exit(self):
        xpos = 10
        ypos = 10
        num_cols = 5
        num_rows = 10
        m1 = Maze(xpos, ypos, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top)
        self.assertFalse(m1._cells[num_cols-1][num_rows-1].has_bottom)

    def test_get_adjacent_cells(self):
        xpos = 10
        ypos = 10
        num_cols = 5
        num_rows = 10
        m1 = Maze(xpos, ypos, num_rows, num_cols, 10, 10)
        self.assertEqual(sorted(m1._get_adjacent_cells(0, 0)), sorted([(0, 1), (1, 0)]))
        self.assertEqual(sorted(m1._get_adjacent_cells(4, 9)), sorted([(3, 9), (4, 8)]))
        self.assertEqual(sorted(m1._get_adjacent_cells(0, 9)), sorted([(1, 9), (0, 8)]))
        self.assertEqual(sorted(m1._get_adjacent_cells(4, 0)), sorted([(3, 0), (4, 1)]))

    def test_reset_cells(self):
        xpos = 10
        ypos = 10
        num_cols = 5
        num_rows = 10
        m1 = Maze(xpos, ypos, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()


