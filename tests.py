import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols=12
        num_rows=10
        m1 = Maze(0, 0, 10, 10, num_rows, num_cols)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_break_entrance_and_exit(self):
        num_cols=12
        num_rows=10
        m1 = Maze(0, 0, 10, 10, num_rows, num_cols)
        self.assertEqual(
            m1._cells[0][0].wall_t,
            False
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].wall_b,
            False
        )

    def test_reset_visited(self):
        num_cols=12
        num_rows=10
        m1 = Maze(0, 0, 10, 10, num_rows, num_cols)
        self.assertEqual(
            m1._cells[4][4].visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()
