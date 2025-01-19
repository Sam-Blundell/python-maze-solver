import time
import random
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        cell_size_x,
        cell_size_y,
        num_rows,
        num_cols,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (self._cell_size_x * i)
        y1 = self._y1 + (self._cell_size_y * j)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        end_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        start_cell.wall_t = False
        start_cell.draw(start_cell.x1, start_cell.y1, start_cell.x2, start_cell.y2)
        end_cell.wall_b = False
        end_cell.draw(end_cell.x1, end_cell.y1, end_cell.x2, end_cell.y2)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i < (self._num_cols - 1) and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j < (self._num_rows - 1) and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))

            if not to_visit:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(to_visit))
            next_index = to_visit[direction]

            # right
            if next_index[0] == i + 1:
                self._cells[i][j].wall_r = False
                self._cells[i + 1][j].wall_l = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].wall_l = False
                self._cells[i - 1][j].wall_r = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].wall_b = False
                self._cells[i][j + 1].wall_t = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].wall_t = False
                self._cells[i][j - 1].wall_b = False

            self._break_walls_r(next_index[0], next_index[1])
